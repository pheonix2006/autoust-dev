# AutoStudy

> 本地 Canvas LMS 学业助手 skill，已在 HKUST(GZ) 的 Canvas 实例上验证。
> 同步 Canvas、规划 ddl、侦查作业要求、生成可审核草稿、归档课件、生成课程笔记。

其他版本：

- [English README](./README.en.md)
- [快速版中文 README](./README.quick.md)

本分支维护于 [pheonix2006/autoust-dev](https://github.com/pheonix2006/autoust-dev)，
基于 [Aurorra1123/autoust-dev](https://github.com/Aurorra1123/autoust-dev)。

AutoStudy 是一个跑在 Claude Code / Codex 这类 agentic coding 环境里的
**本地 Canvas LMS skill 包**，已在 HKUST(GZ) 的 Canvas 实例上验证。你用自然语言提出需求，agent 读取 `skill.md`，调用本地
`canvascli` 数据层，把证据和产物写回这个仓库，并在关键节点询问你。

它先收集 Canvas 上的真实上下文，解释发现，再生成可以检查、修改和决定是否
提交的本地产物。你也可以设置当前 Codex 对话中的定时课程巡检，在同一对话
看到启动、扫描进度和结果。

---

## 你可以让它做什么

```text
"看看这周有什么作业"
"同步课程状态"
"每天帮我巡检课程，维护学期总览和每日记录"
"帮我完成 DSAA2011 Project，先生成本地草稿，不提交"
"继续改上次那个 report，让实验讨论更深入"
"同步 DSAA2011 的课件"
"把 DSAA2011 的 lecture notes 写出来"
```

当前用户侧任务：

| 任务 | 能力 | 产物位置 |
|---|---|---|
| `sync-status` | 同步 Canvas 课程、作业、公告，并生成建议计划。只规划，不自动执行作业。 | `data/runs/<date>/REPORT.md`, `plan.json`, `pending_assignments.json` |
| `daily-course-review` | 单次或定时巡检课程变化，维护学期总览、每日日志，默认为新课件生成简短预习。 | `data/reports/<term>/`，复用现有报告与课程归档 |
| `do-homework` | 创建或复用一个作业目录，按实际要求自主完成和验证本地产物。 | `data/homework/<COURSE>/<HWID>/` |
| `sync-course` | 按课程归档课件、公告、module 结构，供后续复习和笔记复用。 | `data/courses/<COURSE>/` |
| `write-course-notes` | 从已同步的 lecture PDFs 生成 Obsidian 风格 Markdown 笔记。 | `data/courses/<COURSE>/notes/` |

旧 M3 阶段已经验证过 paper / slides / math / lab 四类真实作业产出。现在的主线是
默认采用简洁作业流程：完整调查与简短计划，之后自主制作和验证；旧 M3.5 分阶段流程仅保留为显式选项。

---

## 每日课程巡检

说“每天帮我巡检课程”即可进入 [daily-course-review](sub-skills/tasks/daily-course-review.md)。
首次设置会主动询问运行时间，默认 **08:00**，并明确显示时区、学期、课程范围和
预习开关。使用 **当前 Codex 对话中的定时巡检**：开始、快速扫描和最终结果都在
本对话显示，包括无更新的日子。电脑与桌面应用需要保持运行；如果当前环境不支持
同对话调度，会说明限制，仍可手动巡检。已有相同任务会更新，不重复创建。

每轮检查公告、syllabus、作业正文及附件、Files、Modules/Pages 等入口，不能只看
Files 列表。首次建立完整基线，以后检查各入口变化，深入阅读新内容和未解决的来源。
持续维护当前学期的课程与 syllabus 总览，以及每天的变化、检查结果和缺口记录。
新课件默认生成简短预习，用户可关闭；已有人工笔记会保留。读取失败不会写成“无更新”。

说“现在巡检一下课程”只运行一次；说“把每日巡检改到九点”更新已有设置。
课程原件、个人配置、总览、日志和笔记都留在本地忽略目录，不上传到 GitHub。
发布本 task 不会自动创建定时任务或迁移已有个人自动化。

## 快速开始

### 1. 让 agent 加载这个 skill

AutoStudy 是一个完整的本地仓库，不是单独一个 `skill.md` 文件。第一次使用时，最稳的方式是在 Claude Code / Codex 里先打开一个你准备用来放 AutoStudy 的空白项目文件夹，然后让 agent 直接 clone 到当前目录：

```text
请把 https://github.com/pheonix2006/autoust-dev clone 到当前空白文件夹，
读取里面的 skill.md，并按步骤帮我完成初始化。
```

agent 应该先确认当前目录是空目录，再执行等价于下面的命令：

```bash
git clone https://github.com/pheonix2006/autoust-dev.git .
```

如果当前目录不是空的，或者你还没有打开一个明确的项目文件夹，agent 应该先问你要放到哪里，而不是默认放进 `~/workspace`、桌面、下载目录或其他隐式位置。

你也可以明确指定一个路径：

```text
请把 https://github.com/pheonix2006/autoust-dev clone 到 ~/workspace/autoust-dev，
然后进入这个文件夹，读取里面的 skill.md，并按步骤帮我完成初始化。
```

如果你想自己先 clone，也可以这样做：

```bash
mkdir -p ~/workspace
git clone https://github.com/pheonix2006/autoust-dev.git ~/workspace/autoust-dev
cd ~/workspace/autoust-dev
```

然后在这个目录里告诉 agent：

```text
请使用当前目录里的 AutoStudy skill，阅读 skill.md，然后帮我初始化。
```

`~/workspace/autoust-dev` 只是一个示例位置，不是默认位置。关键是 AutoStudy 要作为一个独立仓库存在，因为 `.venv/`、`data/`、`scripts/` 和 `sub-skills/` 都会在这个仓库目录下使用。agent 应该读取 `skill.md`，检查环境，并把缺失依赖安装到本地 `.venv/`。

### 2. 完成一次 Canvas 登录

AutoStudy 使用独立的 [`canvascli`](https://github.com/Aurorra1123/canvascli)
作为 Canvas 数据层。第一次使用时，agent 会先确认你的 Canvas 学校/域名或登录页，然后打开浏览器让你完成对应的 Canvas SSO：

```bash
.venv/bin/canvascli init --canvas-url "https://canvas.example.edu"
```

Canvas 登录态保存在本机：

```text
~/Library/Application Support/canvascli/state.json
```

这个文件是 credential。agent 不应该打印、复制到聊天、或提交到 git。检查登录态是否仍可用时，应该运行：

```bash
.venv/bin/canvascli whoami
```

`canvascli init` 是登录/刷新命令，不是健康检查。

### 3. 从同步状态开始

最安全的第一句是：

```text
看看这周有什么作业
```

AutoStudy 会：

1. 拉取 Canvas courses / assignments / announcements；
2. 保存当前 sync 快照到 `data/sync/current/`；
3. 写入当天运行目录 `data/runs/<date>/`；
4. 给出编号的下一步建议；
5. 等你选择是否进入某个作业。

如果你选择某个编号，AutoStudy 会用 `scripts/select_plan_item.py` 解析出准确的
Canvas IDs 和建议 workbench。选中编号后，不应该再靠标题模糊匹配。

---

## 作业流程现在是怎样的

每项作业创建或复用 `data/homework/<COURSE>/<assignment>/`，采用同一套流程：

1. **完整调查**：覆盖 assignment/rubric、syllabus、学期 announcements、课程首页、
   modules/pages、全部课程文件目录与现有课件，以及发现的相关外链。先检查来源及
   内容，再筛选当前任务有用的信息，不能事先凭标题判断“应该不相关”就跳过。
2. **整理要求**：保留有用原始资料与一份简洁调查总结，说明来源覆盖、要求、日期、
   评分点和缺口。读取失败不等于没有要求。
3. **简短计划**：保留一份 `pipeline.md`，说明目标、交付物、做法和验证方式。
4. **自主完成**：模型自行执行、检查与修正，不强制 stage brief/review、JSON 回执、
   dispatch ledger 或逐阶段审批。

继续和修改作业也使用这套流程：复用调查、核实更新与缺口，必要时更新同一份计划，
直接修改成果。不再生成 repair plan 或 repair pipeline。已完成且仍有效的调查不用
在同一会话的小修改中重复抓取。只有用户明确要求历史审计模式时才使用旧分阶段系统。

提交 Canvas 仍需明确授权。旧 `result.json` 可选兼容状态扫描，新作业不要求生成；
没有状态记录时，继续作业应直接检查文件夹。已有作业文件不会自动清理。

---

## 课程资料和笔记

同步课程资料：

```text
同步 DSAA2011 的资料
```

会进入 `sync-course`，确认范围后归档到：

```text
data/courses/<COURSE>/
├── materials/
├── canvas_sync/
├── notes/
├── meta.json
└── index.md
```

然后你可以说：

```text
写 DSAA2011 的课程笔记
```

这会进入 `write-course-notes`，从课程归档里的 lecture PDFs 生成结构化 Markdown notes。

---

## 仓库结构

```text
AutoStudy/
├── skill.md                         # 用户侧 skill 入口和路由
├── README.md                        # 中文默认 README
├── README.en.md                     # 英文完整版
├── README.quick.md                  # 中文快速版
├── scripts/
│   ├── write_scan_plan.py           # Canvas snapshot -> plan/report
│   ├── select_plan_item.py          # 编号计划项 -> 精确 handoff
│   └── write_homework_result.py     # 稳定 result.json writer
├── sub-skills/
│   ├── tasks/
│   │   ├── sync-status.md
│   │   ├── do-homework.md             # investigate, plan, execute freely
│   │   ├── do-homework-staged.md      # legacy opt-in router
│   │   ├── background-recon.md        # legacy mode
│   │   ├── existing-work-recon.md     # legacy mode
│   │   ├── alignment-planning.md      # legacy mode
│   │   ├── task-orchestrator.md
│   │   ├── sync-course.md
│   │   ├── daily-course-review.md
│   │   └── write-course-notes.md
│   └── tools/
│       ├── canvascli-setup.md
│       ├── canvascli-api.md
│       ├── assignment-recon.md
│       ├── code-writer.md
│       ├── writing-helper.md
│       ├── pdf-renderer.md
│       ├── slide-maker.md
│       └── ...
├── docs/
│   ├── DEVELOPMENT.md
│   ├── ROADMAP.md
│   ├── COLLABORATION.md
│   ├── runtime-agent-protocol.md
│   ├── skills-architecture-spec.md
│   ├── PITFALLS.md
│   ├── plans/feature-list.json
│   └── progress/agent-progress.md
└── data/                            # 本地 Canvas 快照和产物，gitignored
```

`data/` 是本地工作区，可能包含课程文件、作业草稿、verification logs 和 result receipts。
当前 Canvas sync 快照固定放在 `data/sync/current/`，每次 scan-plan 使用过的副本会放在
`data/runs/<date>/raw/`。

---

## 当前状态

已经可用：

- `canvascli` Canvas 数据层。
- `sync-status` scan-plan 流程。
- `do-homework`：一个作业目录，自主制作、继续修改和验证。
- 旧 `task-orchestrator` 仅供显式选择的分阶段模式使用。
- M3 工具：prose、code、figures、tests、slides、PDF rendering、humanizer。
- 课程资料同步和课程笔记生成。
- 可选 `result.json` 兼容旧状态扫描，新作业不要求生成。

仍在 hardening：

- 统一 executor/reviewer runtime 的 clean process validation。
- 保留已有草稿的 repair / continue 体验。
- course-level 和 user-level preference memory。
- 在安全的未过期/sandbox 作业上做一次真实 Canvas submission E2E。
- Claude Code 之外的多 runtime 支持。

详细状态见：

- [docs/ROADMAP.md](./docs/ROADMAP.md)
- [docs/plans/feature-list.json](./docs/plans/feature-list.json)

---

## 安全和学术诚信

- AutoStudy 不会自动提交 Canvas。
- `sync-status` 只给计划，不会自动执行计划项。
- 大范围下载、生成作业草稿、提交文件前都应该有用户确认点。
- AutoStudy 不应该编造 group details、datasets、personal experience、partner names、instructor oral instructions 或不可达来源。
- 草稿是本地 artifacts，必须由你检查、修改、决定是否提交。
- 目标是减少重复劳动、提升可追溯性，而不是替学生隐藏责任。

拿不准时，AutoStudy 应该停下来解释不确定性，而不是猜。

---

## 贡献开发

如果你是开发者，先读 [docs/DEVELOPMENT.md](./docs/DEVELOPMENT.md)。它解释
AutoStudy 与 `canvascli` 的边界、Canvas Copilot 参考项目、当前分支策略、
progress/backlog 更新规则和验证要求。
