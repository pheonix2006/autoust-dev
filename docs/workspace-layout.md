# 学习工作区目录规范

本文是 AutoStudy 当前数据布局的唯一权威规范。README 和任务指引引用此文件；历史设计、验证记录中的旧路径只用于解释当时结果。

## 项目定位与边界

在用户选择的一个学习项目中放两个独立 Git 仓库：`autoust-dev/` 保存领域指引、辅助脚本和本地学习数据，`canvascli/` 提供 Canvas 登录、API、分页、下载等数据能力。用户打开上层学习项目即可使用两者，不需要安装一个新的项目管理器，也不需要将两个 Git 历史合并。

`skill.md` 是兼容不同 agent 环境的按需路由入口，不是唯一需要下载的文件。必须取得完整 AutoStudy 仓库。运行环境已有的代码、文档、PDF 等能力优先复用；`sub-skills/` 补充项目特有的来源、归档、验证与交付约定。

```text
学习工作区/
├── canvascli/                         # 独立工具仓库
└── autoust-dev/                       # 独立学习工作区实现仓库
    ├── README.md
    ├── AGENTS.md / CLAUDE.md / skill.md
    ├── scripts/ / sub-skills/ / docs/
    ├── .venv/
    └── data/                         # 私人数据，不提交 Git
        ├── semesters/
        │   └── <TERM>/               # 例如 2026-27-Fall
        │       ├── index.md          # 学期入口、课程与作业链接
        │       ├── courses/
        │       │   └── <COURSE>/     # 保留 AIAA3201--L02 等可读名称
        │       │       ├── meta.json
        │       │       ├── index.md
        │       │       ├── canvas_sync/
        │       │       ├── materials/
        │       │       │   ├── lectures/
        │       │       │   ├── readings/
        │       │       │   └── other/
        │       │       ├── notes/
        │       │       └── homework/
        │       │           └── <assignment>/
        │       ├── reports/          # 总览、每日记录与来源覆盖报告
        │       ├── runs/             # 每次状态扫描和使用过的快照
        │       └── sync/current/     # 当前学期最近一次状态快照
        ├── workflows/                # 跨学期任务配置
        └── setup/                    # 工作区初始化记录
```

## 学期、课程与作业身份

先读取 Canvas 返回的实际学期元数据，核对课程范围，再规范化为路径段，例如 `2026-27 Fall` → `2026-27-Fall`。不要通过今天日期猜测学期，也不要将示例 `<TERM>` 原样创建成文件夹。无法唯一确定学期时明确选择，不能默默混合多个学期。API 的 `--term` 参数使用其接受的实际学期名称；目录使用规范化名称。

课程保留已有可读 slug，例如 `AIAA3201--L02`。`meta.json` 应保存并核对 Canvas 实例、原始学期名称及可用的 term ID、course ID。写入现有目录前验证身份，禁止仅凭课程标题合并。只有同学期重名冲突时才添加 course ID 区分。作业同样保存并核对 assignment ID 与所属 course ID；编号选择结果中的精确 IDs 不得重新按标题猜测。

`canvas_sync/assignments.json` 是来源快照；`homework/<assignment>/` 是制作作业成果的位置。二者用途不同，不另建一套并行 `assignments/` 成果目录。跨课程的截止日期和进度放在学期总览或状态报告中，通过链接指向实际作业目录。

## 内容与路径约定

- 保留 `canvas_sync`、`materials/{lectures,readings,other}`、`notes`、`homework` 的现有命名。
- 共享课件原件保存在课程材料目录。作业调查引用其路径与来源信息；只有版本固定、独立运行或提交要求确有需要时才复制，并说明版本。
- 作业目录按实际成果组织。默认完整调查、简洁调查总结、一份短 `pipeline.md`，然后自主执行与验证；不强制空子目录、JSON 回执或阶段文件。
- 原始快照、个人配置、课程与作业内容、日志留在本地忽略目录。公开仓库只保存通用指引、脚本和脱敏示例。
- 从 AutoStudy 仓库根执行脚本。已知根目录用显式参数传递；从嵌套作业目录定位时，使用明确根路径或验证 `skill.md`、`scripts/` 等仓库标记。禁止依赖 `../../../..` 或固定 `parents[N]` 推算根目录。
- Windows 虚拟环境命令在 `.venv/Scripts/`，macOS/Linux 在 `.venv/bin/`。执行时替换模板参数并按所在 shell 引用路径。

## 迁移与历史兼容

旧课程树移入对应学期的 `courses/`，旧作业树按核对后的课程身份并入该课程 `homework/`；报告、扫描运行、当前快照归入实际对应学期。全局 `workflows/` 与 `setup/` 保留。迁移必须同时更新链接、脚本参数、任务配置与活动文档，检查数量、内容完整性和身份冲突后再结束。

历史过程文件不因迁移被删除，也不让默认任务恢复分阶段流程。旧路径只在历史记录或明确的兼容读取中存在；所有新写入使用本规范。显式历史审计模式仍可调用旧任务协议，但也使用新的数据布局。
