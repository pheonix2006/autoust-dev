---
name: canvascli-setup
description: Initialize the learning workspace and its local Canvas CLI environment; use interactive SSO only when necessary.
---

# Canvas CLI 初始化

遵循 [学习工作区规范](../../docs/workspace-layout.md)。两个同级独立仓库使用 [pheonix2006/autoust-dev](https://github.com/pheonix2006/autoust-dev) 与 [pheonix2006/canvascli](https://github.com/pheonix2006/canvascli)。先检查并复用已有路径与虚拟环境，不覆盖用户文件，不把示例主目录当成默认位置。

## 环境与安装

从 AutoStudy 仓库根运行。先检查 Python、`.venv/`、CLI 版本及 `whoami`，只补缺失步骤。Python 版本要求以当前 Canvas CLI `pyproject.toml` 为准。支持使用已验证的工作区虚拟环境；下列以仓库内 `.venv/` 为例。

Windows PowerShell：

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e ../canvascli
.venv/Scripts/python.exe -m playwright install chromium
.venv/Scripts/canvascli.exe version
.venv/Scripts/canvascli.exe whoami
```

macOS/Linux：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e ../canvascli
.venv/bin/python -m playwright install chromium
.venv/bin/canvascli version
.venv/bin/canvascli whoami
```

优先本地同级 editable 安装，保证使用当前 checkout。若用户只需要发布版、不保留 CLI 仓库，可以在对应环境执行 `python -m pip install "git+https://github.com/pheonix2006/canvascli.git"`。不要同时保留来源不明的不同 CLI 版本；用实际环境的 `version` 验证。

下载失败时检查实际网络与用户已有代理，不自行设定代理节点或端口。Playwright 缺少浏览器时安装完整 Chromium；系统依赖按当前平台报错处理，不假定所有机器都已安装 Python。

## 会话检查与登录

`canvascli whoami` 检查保存的会话。`init` 是明确的交互登录命令，不是健康检查。已有有效会话时不重复询问学校或打开登录窗口。

首次未配置实例时取得用户的 Canvas 根 URL；学校名不足以唯一确定实例时再询问 URL。用对应平台的 CLI 执行：

```text
canvascli init --canvas-url "https://canvas.example.edu"
```

告诉用户将在浏览器中完成 SSO。若学校提供“记住登录 / 信任此浏览器”，建议选择，以便保存的 SSO 状态日后能续签。CLI 会检测登录成功并保存状态。已有配置只需重新登录时使用 `canvascli init`，无需再问学校。

当前 fork 对受支持的 GET 请求遇到 401 时，会尝试使用保存的 SSO 状态续签并重试。续签是否成功取决于学校策略、SSO 状态和运行环境；不要承诺永久免登录。CLI 明确报告自动续签不可用或失败后再运行 `init`。不要自动重放提交等写请求。

网络、代理、SSL 或权限错误不等于会话过期；保留错误类别并针对原因处理。404 也不能笼统解释为功能关闭或来源不存在，需核对命令语义、权限和对象。

## 验证与归档入口

运行 `canvascli whoami` 后，核对实际 Canvas 学期、课程列表和 IDs。目录学期规范化例如 `2026-27 Fall` → `2026-27-Fall`。按目录规范开始状态扫描或课程同步，不创建旧的全局课程／作业／扫描树。

认证状态保存在 CLI 的平台配置位置，具体路径以当前实现为准。禁止打印、复制到聊天或成果、加入 Git；保存位置在仓库外也不代表绝无泄漏风险。`.venv/`、`data/` 保持忽略。完成后返回原任务，无需再次批准已授权的读取和初始化。
