# 基于 Langfuse 构建 Agent 可观测与评测平台

[在线阅读](https://99like-wjj.github.io/langfuse-agent-observability/) · [Markdown 正文](article.md) · [配图画廊](https://99like-wjj.github.io/langfuse-agent-observability/diagrams/)

从平台选型、链路接入到评测集自动化，介绍一个经过匿名处理的企业 Agent 平台如何使用 Langfuse 组织观测、实验和评价。

文章内容包括平台选型、SDK/OTel 接入、Dataset/Run/Score 关系、webhook 与 BFF、可扩展的评测指标、Skill 自动化，以及会议室查询合成案例。

## 阅读与源文件

| 文件 | 内容 |
|---|---|
| [index.html](index.html) | GitHub Pages 阅读页面，含跳转目录 |
| [article.md](article.md) | 完整文章的 Markdown 正文 |
| [diagrams/](diagrams/) | 七张图的 PNG、可编辑 SVG 和 Mermaid 源文件 |
| [example/](example/) | 合成任务、工具资料、评价设计及接口示例 |
| [references.md](references.md) | 官方资料与方法参考 |

示例为人工合成设计，未执行真实业务或评分。文章已区分代码事实、配置快照、通用建议与尚未验证事项；技术资料核查基准为 2026-11-04。

站点为静态 HTML，通过 GitHub Pages 从 `main` 分支根目录发布。修改后推送至 `main` 即可触发更新。
