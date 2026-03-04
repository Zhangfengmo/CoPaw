# CoPaw Examples

Quick start examples to help you get up and running with CoPaw.

## 📚 Table of Contents

1. [Hello CoPaw](#01-hello-copaw) - Get started in 5 minutes
2. [Custom Skills](#02-custom-skills) - Extend agent capabilities
3. [Channel Integration](#03-channel-integration) - Connect to DingTalk, Telegram, etc.
4. [Advanced Scenarios](#04-advanced-scenarios) - Cron jobs, memory optimization, etc.

## 🚀 Prerequisites

- Python 3.10+
- CoPaw installed: `pip install copaw`
- Initialized: `copaw init --defaults`
- API key configured (DashScope, OpenAI, or other providers)

## 🎯 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/agentscope-ai/CoPaw.git
cd CoPaw/examples

# 2. Run your first example
cd 01_hello_copaw
python hello_copaw.py
```

## 📖 Examples Overview

### 01 Hello CoPaw

Basic usage examples to get you started:

- `hello_copaw.py` - Simplest conversation example
- `hello_with_memory.py` - Conversation with memory management
- `hello_with_tools.py` - Using built-in tools

**Learn:** Agent initialization, basic conversation, message handling

### 02 Custom Skills

Create and use custom skills:

- `weather_skill/` - Weather query skill example
- `calculator_skill/` - Calculator skill example
- `create_and_use_skill.py` - Complete workflow demonstration

**Learn:** Skill structure, SKILL.md format, skill registration

### 03 Channel Integration

Connect CoPaw to messaging platforms:

- `dingtalk_bot.py` - DingTalk bot implementation
- `telegram_bot.py` - Telegram bot implementation
- `console_bot.py` - Console channel example
- `multi_channel_bot.py` - Run multiple channels simultaneously

**Learn:** Channel configuration, message processing, multi-channel setup

### 04 Advanced Scenarios

Production-ready patterns:

- `cron_news_digest.py` - Scheduled news digest
- `memory_optimization.py` - Memory management strategies
- `mcp_integration.py` - MCP client integration
- `custom_channel.py` - Custom channel implementation

**Learn:** Cron jobs, memory compaction, MCP tools, channel development

## 🛤️ Learning Path

1. **Beginners**: Start with `01_hello_copaw`
2. **Intermediate**: Learn `02_custom_skill` to create your own skills
3. **Advanced**: Use `03_channel_integration` for real-world deployment
4. **Expert**: Optimize with `04_advanced_scenarios`

## ❓ Common Issues

### API Key Not Configured

```bash
# Method 1: Interactive setup
copaw init

# Method 2: Environment variable
export DASHSCOPE_API_KEY="your-key-here"
```

### Skills Not Loading

```bash
# Check skills directory
ls ~/.copaw/active_skills/

# Re-sync skills
copaw skills sync
```

### Import Errors

```bash
# Reinstall CoPaw
pip install --upgrade copaw

# Install optional dependencies
pip install copaw[ollama]  # For Ollama support
```

## 📚 Additional Resources

- [Official Documentation](https://copaw.agentscope.io/)
- [Skills Development Guide](https://copaw.agentscope.io/docs/skills)
- [Channel Configuration](https://copaw.agentscope.io/docs/channels)
- [Contributing Guide](../CONTRIBUTING.md)

## 💬 Get Help

- [GitHub Issues](https://github.com/agentscope-ai/CoPaw/issues)
- [GitHub Discussions](https://github.com/agentscope-ai/CoPaw/discussions)
- [Discord Community](https://discord.gg/eYMpfnkG8h)

---

Happy coding with CoPaw! 🐾
