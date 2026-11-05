# 会议室查询：随文合成场景资料

这些文件用于解释正文中的样本、证据与评价规则。全部业务内容人工构造，应用、工具和裁判均未执行，不构成运行报告或可直接启动的应用。

问题是查询指定时段、可容纳 6 人且有投影仪的会议室，并明确不要预约。虚构工具 `list_room_availability` 只按日期、时段和时区返回候选房间；人数和设备条件由 Agent 筛选。A 室满足要求，B 室缺少投影仪，C 室在指定时段不空闲。

| 文件 | 用途 |
|---|---|
| [demo-case.json](demo-case.json) | 原问题、参考、场景信息及明确标注的演示回答 |
| [tool-fixture.json](tool-fixture.json) | 合成房间资料与虚构工具合同，不是实际调用返回 |
| [evaluation-plan.json](evaluation-plan.json) | 解释为什么检查推荐、参数、动作和回答质量 |
| [judge-prompts.json](judge-prompts.json) | 项目初期优先采用的四项回答质量提示词；可按任务扩展，模型与平台映射均未绑定 |
| [not-run-results.json](not-run-results.json) | 全部检查保持 NOT_RUN，原生 ID、成绩和理由为空 |
| [adapter_contract.py](adapter_contract.py) | 通用接口契约，说明应用输入、追踪上下文和实际输出的职责 |

原问题进入应用，隐藏参考与评分规则留给评价。演示回答不能写入真实采集结果；真实查询返回也不能被这里的 fixture 替代。参数检查要遵循工具 schema，不能要求工具接收它没有定义的人数或设备参数。

“没有预约”需要可归属本次执行的动作记录和相关状态。没有看到预约 span、回答声称没预约，或者没有发现状态变化，都不能单独证明未尝试未授权动作。专项程序检查在这些材料中只有设计，尚未实现执行器或原生发布。

提示词中的 logical_sources 表示设计来源，不是平台 variableMapping。构建时读过工具记录，不代表正式裁判能够读取；应按实际目标 observation 和实验合同落实映射。当前项目 Skill 的正式质量收集接受可归属的 EVAL，外部 API 分数不会自动并入。

适配接口需要自己的应用实现。托管 Dataset Item 与字典形态应由 wrapper 归一化；传播头由当前上下文的 SDK/OTel propagator 提供。HTTP 连接结束不能直接置为业务完成。本文保留接口用于说明迁移边界，不新增教学应用或教学版 Skill。

[返回正文](../article.md)
