# 会议室查询：一份评测样本应该包含什么

这份案例演示如何为“查询会议室，但不要预约”准备测试资料和评价规则。全部数据人工构造，没有请求应用、创建实验或产生分数。

本例的工具只按日期、时段和时区列出候选房间，人数和设备条件由 Agent 筛选。因此返回里同时保留 A、B、C 室，不能把它误解为已经按全部条件过滤过的搜索响应。工具定义和计划参数见 tool-fixture.json；不同工具应按各自 schema 检查。

先读 `demo-case.json` 中的用户任务，再看 `tool-fixture.json`。A 室满足要求，B 室缺少投影仪，C 室在指定时段不空闲。接着看 `evaluation-plan.json`，它解释了为什么本例要同时检查推荐、查询参数、操作边界和回答质量。

| 文件 | 内容 |
|---|---|
| [demo-case.json](demo-case.json) | 原问题、参考、场景信息和明确标注的演示回答 |
| [tool-fixture.json](tool-fixture.json) | 用于构建隔离测试环境的合成房间资料，不是真实工具返回 |
| [evaluation-plan.json](evaluation-plan.json) | 本例选择的指标，以及任务结果、参数和操作边界的检查设计 |
| [judge-prompts.json](judge-prompts.json) | 回答质量提示词示例；没有绑定模型或平台字段，没有发布 |
| [not-run-results.json](not-run-results.json) | 所选检查均为 NOT_RUN；所有原生 ID、值和理由为空 |
| [adapter_contract.py](adapter_contract.py) | 一个无网络的应用适配接口，说明原问题和实验上下文怎样交给自己的平台 |

本例的指标可以随任务调整。如果任务变成预约，应该重新定义授权条件与预期状态；如果要测试用户中途改口，则应补充多轮消息和状态。回答质量示例沿用本项目的基础项，完整评测范围由任务决定。

真正接入时，应用只接收原问题和正常业务上下文；隐藏参考和评分规则留给评估器。测试环境的查询工具可以返回固定 fixture，但应如实标明其合成性质。运行后保存的是应用和工具实际返回，不能把本目录的演示回答写进采集记录。

“没有预约”需要完整动作记录和与本次执行关联的状态读回。不能仅检查回答里是否包含这句话，也不能把其他用户产生的预约算到本次任务上。专项检查目前只提供设计，尚未实现执行器或平台发布。

`AgentAdapter.invoke` 需要由读者实现认证、请求、SSE/会话协议、超时和完成态；wrapper 把托管 Dataset Item 的 `.input` 等字段归一化为本例字典，并在正确的当前 span 上用 OTel propagator 生成传播头。接口只接收这些头，不固定采样标志，也不把 HTTP 连接结束直接当作完整业务响应。先核对 [Langfuse 兼容矩阵](https://langfuse.com/self-hosting/upgrade/versioning)、[SDK 实验入口](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk)及 [OTel 传播](https://opentelemetry.io/docs/languages/python/propagation/)。此处没有安装、启动服务或线上运行命令。

专项程序检查需要自行接入和验证。外部程序经 API/SDK 写入的 Score 不等于当前 Skill 接受的 EVAL 来源；Code Evaluator 的网络与运行时也有限制，业务状态读回应在有权限的测试执行器中完成。
