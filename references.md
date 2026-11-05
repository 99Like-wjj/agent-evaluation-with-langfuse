# 参考资料：平台文档与 Agent 评测实践

资料在 2026-11-04 初核；2026-11-05 再次核对本轮涉及的取数、结果统计、脱敏、版本迁移与选型资料。平台文档用于确认产品能力和版本条件；工程文章用于理解评价方法和组织实践。它们不代表本文项目已经启用相应功能。

## Langfuse 接入、实验与评估器

- [SDK 概览](https://langfuse.com/docs/observability/sdk/overview)：SDK 的用途和服务端版本要求。
- [OpenTelemetry 接入](https://langfuse.com/integrations/native/opentelemetry)：OTLP 接收与上下文传播。
- [评测概览](https://langfuse.com/docs/evaluation/overview)：在线评价、离线实验与结果管理。
- [Dataset](https://langfuse.com/docs/evaluation/experiments/datasets)与[实验数据模型](https://langfuse.com/docs/evaluation/experiments/data-model)：样本、运行和观测的关联。
- [SDK 实验](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk)：应用 task、运行关联及从 UI 经 webhook 触发实验。
- [LLM-as-a-Judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)：模型裁判与评分规则。
- [Code Evaluator](https://langfuse.com/docs/evaluation/evaluation-methods/code-evaluators)：程序评价及自托管执行环境要求。
- [选择评价目标](https://langfuse.com/academy/evaluate/choosing-what-to-evaluate)：从实际问题决定要评价什么。
- [Dataset 入门](https://langfuse.com/academy/datasets)与[设计测试集](https://langfuse.com/academy/datasets/designing-great-datasets)：输入、参考、代表性和持续维护。

## Agent 评测方法

- Anthropic：[Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)。区分运行记录与最终状态，结合程序、模型和人工评价。
- LangChain：[Evaluating Deep Agents: Our Learnings](https://www.langchain.com/blog/evaluating-deep-agents-our-learnings)。单步、完整轮次、多轮、产物和测试环境的实践。
- LangChain：[agentevals](https://github.com/langchain-ai/agentevals)。轨迹评价、顺序/无序及部分匹配方式，帮助理解如何给合理路径留出空间。
- LangSmith：[复杂 Agent 评测教程](https://docs.langchain.com/langsmith/evaluate-complex-agent)。最终响应、执行路径和单步检查的实现示例。
- Microsoft：[Agent Evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)。工具选择、输入准确性、输出利用和执行成功等评价方向；本文没有照搬其分值或默认阈值。
- Microsoft：[Agent evaluation overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/evaluation-overview)。评价与安全测试、性能测试、用户研究等工作的关系。

## 中文工程阅读

- 美团技术团队：[Agent 评测漫谈](https://tech.meituan.com/2026/08/07/Agent-Evaluation.html)。由业务目标理解结果、过程、效率与风险。
- 美团技术团队：[Agent 评测白皮书：评测全览](https://tech.meituan.com/2026/09/10/Agent-Evaluation-White-Paper-01.html)。从实践问题逐步组织评测工作。
- 阿里云开发者社区：[基于 AgentLoop 的 Harness 评测实践](https://developer.aliyun.com/article/1758156)。以具体任务说明评价对象、记录与判断方式。

本文只参考这些文章的组织方式与可通用的方法，没有引用其项目成绩、收益数字、原图或长段原文。

## 选型、许可与版本

- Langfuse：[自托管许可](https://langfuse.com/self-hosting/license-key)、[价格](https://langfuse.com/pricing)、[自托管价格](https://langfuse.com/pricing-self-host)。
- LangSmith：[评价类型](https://docs.langchain.com/langsmith/evaluation-types)、[OTel 接入](https://docs.langchain.com/langsmith/trace-with-opentelemetry)、[自托管](https://docs.langchain.com/langsmith/self-hosted)、[价格](https://www.langchain.com/pricing)。
- Phoenix：[官方文档](https://arize.com/docs/phoenix/)、[追踪](https://arize.com/docs/phoenix/tracing/llm-traces)、[自托管](https://arize.com/docs/phoenix/self-hosting)、[ELv2 许可](https://github.com/Arize-ai/phoenix/blob/main/LICENSE)。
- Opik：[评测](https://www.comet.com/docs/opik/evaluation/overview)、[OTel](https://www.comet.com/docs/opik/integrations/opentelemetry)、[自托管](https://www.comet.com/docs/opik/self-host/overview)、[架构](https://www.comet.com/docs/opik/self-host/architecture)、[Apache-2.0 许可](https://github.com/comet-ml/opik/blob/main/LICENSE)。
- Langfuse：[兼容性说明](https://langfuse.com/docs/compatibility)、[自托管版本矩阵](https://langfuse.com/self-hosting/upgrade/versioning)、[Python v4→v5](https://langfuse.com/docs/observability/sdk/upgrade-path/python-v4-to-v5)、[legacy API 迁移](https://langfuse.com/faq/all/deprecated-api-migration)。

软件版本、许可和商业条件会变化。选择或升级时，应按目标部署重新核对；本文中的维护成本与技术栈适配建议没有作为实测排名。

## 技术核验补充

- [Trace与Observation概念](https://langfuse.com/docs/observability/data-model)：逻辑边界、上下文与后台导出。
- [Score数据模型](https://langfuse.com/docs/evaluation/scores/data-model)：API/EVAL/ANNOTATION来源及可选comment字段。
- [Python SDK v5.1.0的DatasetClient](https://github.com/langfuse/langfuse-python/blob/v5.1.0/langfuse/_client/datasets.py#L77)：固定版本源码仍定义run_experiment，不与已删除的get/delete helper混淆。
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)与[OTel Python传播](https://opentelemetry.io/docs/languages/python/propagation/)：传播上下文和采样标志，通用示例应使用propagator。

## 本轮补充：输入边界与结果完整性

- [Observation 级评估器的取数范围](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge#data-available-to-observation-level-evaluators)：不自动读取同一 Trace 的子节点与兄弟节点。
- [评估器迁移与映射](https://langfuse.com/faq/all/llm-as-a-judge-migration)：跨观测材料的组织，以及实验上下文的映射。
- [Python SDK v5.1.0 实验实现](https://github.com/langfuse/langfuse-python/blob/v5.1.0/langfuse/_client/client.py#L2725)：异常项与最终 item_results 的关系。固定版本静态分析，不代表本文项目已经部署该版本。
- [实验与 CI/CD](https://langfuse.com/docs/evaluation/experiments/experiments-ci-cd)：缺样本、重复 ID、执行失败和无效结果的处理。本文未引入自动发布门禁。
- [Masking](https://langfuse.com/docs/observability/features/masking)：客户端脱敏钩子的作用范围，其他出口需分别处理。
- [自托管 v3 到 v4](https://langfuse.com/self-hosting/upgrade/upgrade-guides/upgrade-v3-to-v4)：legacy、dual、events_only 模式与迁移步骤。

## 裁判输入复核

- 再次核对 [LLM-as-a-Judge 取数范围](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge#data-available-to-observation-level-evaluators)与[旧评估器迁移](https://langfuse.com/faq/all/llm-as-a-judge-migration)。新的目标观测取数与旧具名观测映射应区分。
- 正文实际输入表来自项目配置及既有测试裁判输入的只读抽查；内部资源 ID、模型标识、业务原文与原始响应不放入公开材料。

## 评测开销、调度范围与发布检查

- [Evaluator 与 Rule](https://langfuse.com/docs/evaluation/core-concepts#evaluators-and-rules)：评价定义、范围过滤、采样及复用；同一 Rule 挂多个评估器不等于共用一次模型调用。
- [选择评价目标](https://langfuse.com/academy/evaluate/choosing-what-to-evaluate)：将业务目标、关键约束和运行指标分开考虑。
- [评价与持续改进](https://langfuse.com/academy/evaluate)：代码、模型和人工的分工。
- [SDK 实验评价接口](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk)与[Code Evaluator](https://langfuse.com/docs/evaluation/evaluation-methods/code-evaluators)：多结果接口与运行限制，不直接证明当前 Skill 已支持联合模型裁判。
- 新章中的三张页面截图来自已有配置的只读查看。已对名称做匿名化、裁去内部导航及无关列；状态、结果数字和筛选条件含义没有更改。原始内部定位和取证过程单独保存，不随博客公开。
