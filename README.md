# 基于 Langfuse 构建 Agent 可观测与评测平台

[在线阅读](https://99like-wjj.github.io/langfuse-agent-observability/) · [Markdown 正文](article.md) · [配图画廊](https://99like-wjj.github.io/langfuse-agent-observability/diagrams/)

介绍一个经过匿名处理的企业 Agent 平台如何接入 Langfuse、组织评测，并用 AI 和专项 Skill 自动构建评测集。

文章围绕平台选型、观测接入、评测设计、实验执行与结果核验、Skill 自动化五条主线展开。四项回答质量指标是项目初期优先采用的范围，后续按业务任务扩展。

## 阅读与源文件

| 文件 | 内容 |
|---|---|
| [index.html](index.html) | 完整阅读页与跳转目录 |
| [article.md](article.md) | Markdown 正文 |
| [diagrams/](diagrams/) | 七张配图的 PNG、SVG 与 Mermaid 源文件 |
| [example/](example/) | 会议室查询的合成场景资料、评价设计与接口契约 |
| [references.md](references.md) | 官方文档及方法参考 |

会议室场景为人工合成设计，未执行或评分。正文中的实际裁判输入说明来自已有评测记录的只读抽查，仅展示数据类别；不代表所有实验的完整验收。

站点采用静态 HTML，通过 GitHub Pages 从 `main` 分支根目录发布。
