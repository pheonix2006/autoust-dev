# AutoStudy Development Guide

AutoStudy 是多学期、多课程学习工作区。首先阅读 [目录规范](workspace-layout.md) 和 [运行入口](../skill.md)。默认作业行为由 [do-homework](../sub-skills/tasks/do-homework.md) 定义。

## 仓库职责

同一学习项目中的 `canvascli/` 与 `autoust-dev/` 是独立 Git 仓库。Canvas 登录、自动续签、分页与 API 契约属于 Canvas CLI；来源调查、目录归档、状态报告和按需任务指引属于 AutoStudy。优先把同级 Canvas CLI 以 editable 方式安装到 AutoStudy 的 `.venv/`，避免开发时运行旧版本。

## 开发原则

- 先核对当前 checkout、未提交变更、相关实现及测试，不覆盖其他工作。
- 目录规范只在 `workspace-layout.md` 定义。路径解析使用显式根目录或共享定位逻辑，不从作业目录固定向上跳若干层。
- Skills 是按需领域指引，见 [skills 架构](skills-architecture-spec.md)。不要添加固定阶段、模板回执或独立 repair 流程作为普通作业前置条件。
- 继续任务时复用有效调查、补充更新与缺口，维护同一份短 `pipeline.md`。
- 用户指令和课程具体要求优先。例行实现、阅读、验证无需新增审批；Canvas 提交仍需明确授权。
- 历史 staged 协议与测试可以维护，但不得成为普通任务入口。历史文档顶部标注状态，不改写过去的验证事实。

## 修改与验证

先针对实际变更运行相关测试，再检查 README 三个版本、AGENTS/CLAUDE/skill 路由、相关任务说明及示例是否一致。涉及归档路径时检查多个学期、课程 ID 冲突、旧路径兼容读取和新路径写入；迁移还需核对内容完整性、链接与自动化配置。

检查 `git diff --check`。公开变更不要包含真实课程资料、认证状态或私人日志。只报告实际运行过的验证；不因 parser 通过就声称端到端成功。

跨仓库协作见 [COLLABORATION.md](COLLABORATION.md)。按当前用户要求和仓库分支状态工作，不强制沿用历史机器路径或某个固定开发分支。提交、推送与发布遵循当前任务授权。
