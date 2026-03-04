# CoPaw 示例代码

帮助你快速上手 CoPaw 的完整示例集合。

## 📚 目录

1. [Hello CoPaw](#01-hello-copaw) - 5 分钟快速开始
2. [自定义技能](#02-自定义技能) - 扩展 Agent 能力
3. [渠道集成](#03-渠道集成) - 接入钉钉、Telegram 等
4. [高级场景](#04-高级场景) - 定时任务、内存优化等

## 🚀 前置条件

- Python 3.10+
- 已安装 CoPaw：`pip install copaw`
- 已初始化：`copaw init --defaults`
- 已配置 API 密钥（DashScope、OpenAI 或其他提供商）

## 🎯 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/agentscope-ai/CoPaw.git
cd CoPaw/examples

# 2. 运行第一个示例
cd 01_hello_copaw
python hello_copaw.py
```

## 📖 示例概览

### 01 Hello CoPaw

基础使用示例，帮助你快速上手：

- `hello_copaw.py` - 最简单的对话示例
- `hello_with_memory.py` - 带记忆管理的对话
- `hello_with_tools.py` - 使用内置工具

**学习内容：** Agent 初始化、基础对话、消息处理

### 02 自定义技能

创建和使用自定义技能：

- `weather_skill/` - 天气查询技能示例
- `calculator_skill/` - 计算器技能示例
- `create_and_use_skill.py` - 完整流程演示

**学习内容：** 技能结构、SKILL.md 格式、技能注册

### 03 渠道集成

将 CoPaw 接入消息平台：

- `dingtalk_bot.py` - 钉钉机器人实现
- `telegram_bot.py` - Telegram 机器人实现
- `console_bot.py` - Console 渠道示例
- `multi_channel_bot.py` - 多渠道同时运行

**学习内容：** 渠道配置、消息处理、多渠道设置

### 04 高级场景

生产环境模式：

- `cron_news_digest.py` - 定时新闻摘要
- `memory_optimization.py` - 内存管理策略
- `mcp_integration.py` - MCP 客户端集成
- `custom_channel.py` - 自定义渠道实现

**学习内容：** 定时任务、内存压缩、MCP 工具、渠道开发

## 🛤️ 学习路径

1. **新手**：从 `01_hello_copaw` 开始
2. **进阶**：学习 `02_custom_skill` 创建自己的技能
3. **实战**：通过 `03_channel_integration` 接入实际应用
4. **优化**：使用 `04_advanced_scenarios` 优化生产环境

## ❓ 常见问题

### API 密钥未配置

```bash
# 方式 1：交互式设置
copaw init

# 方式 2：环境变量
export DASHSCOPE_API_KEY="your-key-here"
```

### 技能未加载

```bash
# 检查技能目录
ls ~/.copaw/active_skills/

# 重新同步技能
copaw skills sync
```

### 导入错误

```bash
# 重新安装 CoPaw
pip install --upgrade copaw

# 安装可选依赖
pip install copaw[ollama]  # Ollama 支持
```

## 📚 更多资源

- [官方文档](https://copaw.agentscope.io/)
- [技能开发指南](https://copaw.agentscope.io/docs/skills)
- [渠道配置文档](https://copaw.agentscope.io/docs/channels)
- [贡献指南](../CONTRIBUTING.md)

## 💬 获取帮助

- [GitHub Issues](https://github.com/agentscope-ai/CoPaw/issues)
- [GitHub Discussions](https://github.com/agentscope-ai/CoPaw/discussions)
- [Discord 社区](https://discord.gg/eYMpfnkG8h)

---

祝你使用 CoPaw 愉快！🐾
