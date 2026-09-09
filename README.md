# AutoStudy 学习工作区

在 Claude Code / Codex 等 agent 环境中，用自然语言管理多个学期的课程资料、笔记和作业。Canvas CLI 负责访问 Canvas，AutoStudy 提供清晰的文件结构、来源调查约定和按需任务指引。已在 HKUST(GZ) Canvas 实例上使用；其他实例需核对其实际功能与权限。

[English](README.en.md) · [快速开始](README.quick.md) · [目录规范](docs/workspace-layout.md)

本分支为 [pheonix2006/autoust-dev](https://github.com/pheonix2006/autoust-dev)，基于 [Aurorra1123/autoust-dev](https://github.com/Aurorra1123/autoust-dev)。配套工具使用 [pheonix2006/canvascli](https://github.com/pheonix2006/canvascli)。

## 一个项目，两个独立仓库

在你选定的学习项目文件夹中打开 agent，直接说：

```text
请在当前学习项目中准备 https://github.com/pheonix2006/autoust-dev 和
https://github.com/pheonix2006/canvascli 两个同级独立仓库。
已有仓库先检查并复用，不要覆盖。读取 autoust-dev/skill.md，
按初始化指南配置本地环境，核对我的 Canvas 学期和课程，再建立学习工作区。
```

Agent 会检查现有目录，缺失时 clone 到 `autoust-dev/` 与 `canvascli/`，优先把同级 Canvas CLI 可编辑安装到 AutoStudy 的 `.venv/`。两个 Git 仓库独立更新；用户只需打开上层学习项目。无需把 AutoStudy 当成单个技能文件下载，也无需另做一个项目管理器。

手动准备也可以，在选定的目录运行：

```bash
git clone https://github.com/pheonix2006/autoust-dev.git
git clone https://github.com/pheonix2006/canvascli.git
```

然后让 agent 阅读 `autoust-dev/skill.md`，按 [初始化指南](sub-skills/tools/canvascli-setup.md) 配置。命令适用于 Windows 与 Unix；虚拟环境执行文件分别位于 `.venv/Scripts/` 与 `.venv/bin/`。路径只是约定，不覆盖用户已有布局。

首次使用需要确认学校的 Canvas URL 并在浏览器中完成 SSO。之后用 `canvascli version` 和 `canvascli whoami` 检查环境与会话。此 fork 的受支持 GET 请求可尝试通过已保存的 SSO 状态自动续签；只有自动续签不可用或失败时才需要交互登录。认证信息只保存在本机，不能打印到聊天或提交 Git。

## 日常使用

| 可以这样说 | 指引 | 主要位置（相对 AutoStudy 根） |
|---|---|---|
| 看看这周有什么作业 | `sync-status` | `data/semesters/<TERM>/runs/` |
| 同步这门课的资料 | `sync-course` | `data/semesters/<TERM>/courses/<COURSE>/` |
| 写这门课的课程笔记 | `write-course-notes` | 课程下 `notes/` |
| 帮我完成／继续修改这份作业 | `do-homework` | 课程下 `homework/<assignment>/` |
| 现在巡检课程／每天帮我巡检 | `daily-course-review` | 学期下 `reports/` 与课程归档 |

`<TERM>` 来自已核对的 Canvas 学期元数据，例如 `2026-27 Fall` 对应目录 `2026-27-Fall`，不能按今天日期猜测。课程保留现有名称，例如 `AIAA3201--L02`；通过元数据中的 course ID 与学期核对身份。

[完整目录规范](docs/workspace-layout.md) 是唯一结构定义：学期下面保留 `courses/`、`reports/`、`runs/`、`sync/current/`；课程里面保留 `canvas_sync/`、`materials/{lectures,readings,other}`、`notes/`，并聚合作业 `homework/`。全局 `data/workflows/` 和 `data/setup/` 不按学期拆分。

`canvas_sync/assignments.json` 是 Canvas 来源快照，`homework/` 是实际成果，两者用途不同。共享课件归档一份，作业通过路径与来源信息引用；总览集中链接各门课的作业。

## 作业流程

先完整调查 assignment/rubric、syllabus、学期公告、首页、modules/pages、全部课程文件目录、已有资料和任务相关外链，检查内容后再筛选适用信息。保存有用来源与简洁调查总结，维护一份短 `pipeline.md`，随后自主制作、运行、检查和修正成果。

继续与修复沿用同一流程，复用仍有效的调查并补充更新与缺口。不强制阶段回执、stage reviews、JSON schemas 或单独 repair pipeline。历史分阶段审计仅在用户明确要求时启用。课程的具体交付要求优先，Canvas 提交仍需明确授权。

## 每日课程巡检

[daily-course-review](sub-skills/tasks/daily-course-review.md) 检查公告、syllabus、作业正文与附件、Files、Modules/Pages 等来源，维护学期总览和每日日志，默认给新课件生成简短预习，并保留人工笔记。首次建立基线，以后检查变化；读取失败不会写成“没有更新”。

“现在巡检”只运行一次。“每天巡检”才设置定时任务，按用户选择的时间（建议 08:00）、时区、学期、范围与通知偏好保存；同对话任务优先复用，避免重复创建。运行环境不支持调度时说明限制。定时运行依赖电脑和对应应用保持可用。发布本项目不会自动创建个人任务。

## 开发与边界

`AGENTS.md` / `CLAUDE.md` 指向 `skill.md` 按需路由；`sub-skills/` 提供领域指引，`scripts/` 提供必要的稳定辅助能力。既有通用工具可直接使用，不需要为每种成果重复安装 skill。

课程资料、草稿、配置、日志与认证信息保持本地；状态扫描给建议，不自动批量执行作业。不得编造个人信息、不可达内容或验证结果。已授权的调查与制作持续推进，只在真正影响结果的缺失信息上询问。

开发请读 [DEVELOPMENT.md](docs/DEVELOPMENT.md) 与 [ROADMAP.md](docs/ROADMAP.md)。旧设计与验证记录保留历史身份；迁移需同时核对文件完整性、链接、脚本路径和定时任务配置。
