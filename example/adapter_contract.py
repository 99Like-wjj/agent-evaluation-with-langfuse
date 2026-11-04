"""应用适配接口示例：把原问题和本次实验上下文交给自己的 Agent。

本文件没有 SDK、认证、网络请求或评分调用。读者实现 AgentAdapter.invoke
后，再用与部署兼容的 SDK wrapper 提供样本和当前观测上下文。
"""
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Mapping, Protocol


@dataclass(frozen=True)
class ExperimentContext:
    # wrapper 在正确的当前 span 上调用 OTel propagator，生成传播头。
    # 保留其 traceparent / tracestate 和采样决定，不手工固定 sampled=1。
    # 这里只承载观测上下文；认证由应用适配器另行处理。
    propagation_headers: Mapping[str, str]


@dataclass(frozen=True)
class ApplicationResult:
    answer: Any
    # 按应用协议检查结束标志与完整性；仅收到 HTTP EOF 不足以置为 True。
    stream_complete: bool
    execution_status: str
    error_code: str | None = None


class AgentAdapter(Protocol):
    async def invoke(self, *, question: str,
                     context: ExperimentContext) -> ApplicationResult:
        """接入自己的 HTTP/SSE/会话接口，返回实际结果和完成状态。

        认证由适配器管理。隐藏参考、评分规则和预期输出不随问题发送。
        """
        ...


def bind_task(adapter: AgentAdapter) -> Callable[..., Awaitable[dict[str, Any]]]:
    async def task(*, item: dict[str, Any],
                   context: ExperimentContext) -> dict[str, Any]:
        # SDK wrapper 将托管 Dataset Item 等对象归一化为字典，并提供当前上下文。
        question = item["input"]["message"]
        if not isinstance(question, str) or not question.strip():
            raise ValueError("A nonempty original question is required")
        result = await adapter.invoke(question=question, context=context)
        if not result.stream_complete:
            raise RuntimeError("APPLICATION_RESPONSE_INCOMPLETE")
        # 请求完成后，业务仍可能失败；保留适配器返回的原始执行状态。
        return {
            "answer": result.answer,
            "status": result.execution_status,
            "error_code": result.error_code,
            "done": result.stream_complete,
        }

    return task
