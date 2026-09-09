# Skills Architecture

AutoStudy 以[学习工作区结构](workspace-layout.md)为基础。Skills 提供项目特有的领域指引，不规定模型必须经过哪些执行阶段。

## 按需加载

`AGENTS.md` / `CLAUDE.md` 指向 `skill.md`；入口只选择当前任务。任务按需要读取 `sub-skills/tools/_index.md` 中的相关领域指南及其附录，不预加载整套任务或工具。

运行环境已有的代码、图表、PDF、文档等工具可以直接使用。项目指南只补充来源覆盖、文件位置、实际要求和质量核验，不要求安装重复的通用技能。

## 默认作业契约

[do-homework.md](../sub-skills/tasks/do-homework.md) 是默认作业入口：全面调查课程来源及内容，再筛选相关信息，保存简洁调查总结与一份短 `pipeline.md`，自主制作、验证和修改成果。继续与修复沿用同一流程。

不得要求 `spec.md`、`pipeline_design.md`、stage briefs/reviews、dispatch ledgers 或 repair pipelines。已有旧文件可以作为历史证据阅读，不能因为它们存在就切换历史模式。成果路径由课程要求和实际项目结构决定，不机械创建 `src/`、`draft/` 或 JSON 报告。

## 指南编写

每个指南说明适用条件、需要的真实输入、关键领域要求及如何验证。篇幅和章节按需要决定；附录只在语言或成果类型确有差异时添加。`_index.md` 保持简短、链接有效，用户具体要求优先于默认建议。

领域指南读取原始要求、调查总结、当前计划和已有成果；跨工具通过实际文件与清晰路径协作。不将某个 skill 的产物 schema 强制传播给所有任务。不为了简单可逆编辑增加测试或审批。

## 历史模式

只有用户明确要求分阶段审计才加载 `do-homework-staged.md` 和相应 runtime 协议。该模式保留其详细契约，路径遵循当前目录规范。`docs/superpowers/`、轨迹审计与过去验证记录是设计历史，不是当前默认规则。
