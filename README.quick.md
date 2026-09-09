# AutoStudy 快速开始

AutoStudy 是多学期、多课程学习工作区。Canvas CLI 负责访问能力，AutoStudy 负责结构、来源与按需任务指引。

在选定的学习项目中打开 Codex / Claude Code，说：

```text
请准备 https://github.com/pheonix2006/autoust-dev 和
https://github.com/pheonix2006/canvascli 两个同级独立仓库。
先检查并复用已有目录，读取 autoust-dev/skill.md，按初始化指南配置环境，
核对 Canvas 学期与课程后建立学习工作区。
```

优先本地 editable 安装 Canvas CLI。首次浏览器 SSO 登录后，用 `whoami` 检查；支持的 GET 请求会尝试自动续签，失败时再交互登录。

常用指令：看看这周作业、同步课程资料、生成课程笔记、完成或继续修改作业、现在巡检课程、设置每日巡检。定时巡检只在用户要求时建立，并确认时间、范围和通知偏好。

数据在 `data/semesters/<TERM>/`：课程下保留材料、笔记和 `homework/`，学期下保存报告与扫描；`data/workflows/`、`data/setup/` 全局共享。学期来自实际元数据，课程与作业按精确 IDs 核对。

默认作业先完整调查，再写简洁总结与一份 `pipeline.md`，自主制作和验证。无强制阶段文件；提交 Canvas 仍需明确授权。私人数据留在本地。

[完整说明](README.md) · [权威目录规范](docs/workspace-layout.md) · [初始化指南](sub-skills/tools/canvascli-setup.md)
