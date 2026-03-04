# Hello CoPaw - Basic Usage Examples

Get started with CoPaw in 5 minutes!

## 📁 Files

- `hello_copaw.py` - Simplest conversation example
- `hello_with_memory.py` - Conversation with memory management (coming soon)
- `hello_with_tools.py` - Using built-in tools (coming soon)

## 🚀 Quick Start

### 1. Prerequisites

```bash
# Install CoPaw
pip install copaw

# Initialize configuration
copaw init --defaults
```

### 2. Configure API Key

Choose one method:

**Method 1: Interactive setup**
```bash
copaw init
# Follow the prompts to configure your API key
```

**Method 2: Environment variable**
```bash
export DASHSCOPE_API_KEY="your-api-key-here"
```

**Method 3: Edit config directly**
```bash
# Edit ~/.copaw/providers.json
# Add your API key for the provider you're using
```

### 3. Run the Example

```bash
cd examples/01_hello_copaw
python hello_copaw.py
```

## 📖 What You'll Learn

### hello_copaw.py

This example demonstrates:

1. **Agent Initialization**: How to create a CoPawAgent instance
2. **Message Handling**: How to create and send messages
3. **Multi-turn Conversation**: How context is maintained across turns
4. **Error Handling**: Basic error handling patterns

**Key Code:**

```python
from copaw.agents.react_agent import CoPawAgent
from agentscope.message import Msg

# Create agent
agent = CoPawAgent()

# Send message
msg = Msg(name="User", content="Hello!", role="user")
response = await agent.reply(msg)
```

## ❓ Troubleshooting

### Error: "CoPaw is not installed"

```bash
pip install copaw
```

### Error: "No active LLM configured"

```bash
# Run interactive setup
copaw init

# Or set environment variable
export DASHSCOPE_API_KEY="your-key"
```

### Error: "Failed to load config.json"

```bash
# Reinitialize configuration
copaw init --force
```

### Agent responds in wrong language

Edit `~/.copaw/config.json`:

```json
{
  "agents": {
    "language": "zh"  // or "en"
  }
}
```

## 🎯 Next Steps

After completing this example:

1. **Explore Skills**: Check out `../02_custom_skill/` to learn how to extend agent capabilities
2. **Add Channels**: See `../03_channel_integration/` to connect to messaging platforms
3. **Advanced Features**: Dive into `../04_advanced_scenarios/` for production patterns

## 📚 Related Documentation

- [CoPaw Documentation](https://copaw.agentscope.io/)
- [Agent Configuration](https://copaw.agentscope.io/docs/configuration)
- [Model Providers](https://copaw.agentscope.io/docs/models)

---

Need help? [Open an issue](https://github.com/agentscope-ai/CoPaw/issues) or join our [Discord](https://discord.gg/eYMpfnkG8h)!
