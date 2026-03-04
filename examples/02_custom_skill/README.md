# Custom Skills - Extend CoPaw Capabilities

Learn how to create and use custom skills to extend your agent's capabilities.

## 📁 Files

- `weather_skill/` - Complete weather query skill example
- `calculator_skill/` - Simple calculator skill (coming soon)
- `create_and_use_skill.py` - Workflow demonstration

## 🎯 What is a Skill?

A **skill** is a reusable capability that you can add to your CoPaw agent. Skills are defined using:

1. **SKILL.md** - Instructions for the agent (required)
2. **references/** - Reference documents (optional)
3. **scripts/** - Python scripts or tools (optional)

## 🚀 Quick Start

### 1. Explore the Weather Skill

```bash
cd examples/02_custom_skill
cat weather_skill/SKILL.md
```

### 2. Set Up API Key

```bash
# Get free API key from https://openweathermap.org/api
export WEATHER_API_KEY="your-api-key-here"
```

### 3. Test the Script

```bash
python weather_skill/scripts/weather_api.py --city "Beijing"
```

### 4. Use with CoPaw

```bash
python create_and_use_skill.py
```

## 📖 Skill Structure

### SKILL.md Format

```markdown
---
name: skill_name
description: "Clear description with trigger keywords"
metadata:
  copaw:
    emoji: "🔧"
    requires:
      ENV_VAR: "Description"
---

# Skill Instructions

When to use this skill...

How to use this skill...
```

**Key Points:**
- **name**: Unique identifier
- **description**: Include trigger keywords for better recognition
- **metadata**: Optional configuration

### Directory Layout

```
my_skill/
├── SKILL.md          # Required: Agent instructions
├── references/       # Optional: Reference docs
│   └── api_docs.md
└── scripts/          # Optional: Helper scripts
    └── helper.py
```

## 🛠️ Creating Your Own Skill

### Step 1: Create Directory

```bash
mkdir -p ~/.copaw/customized_skills/my_skill
cd ~/.copaw/customized_skills/my_skill
```

### Step 2: Write SKILL.md

```markdown
---
name: my_skill
description: "Use this skill when user wants to [functionality]. Trigger keywords: [keywords]"
---

# My Skill

Instructions for the agent...
```

### Step 3: Add Scripts (Optional)

```bash
mkdir scripts
# Add your Python scripts
```

### Step 4: Enable the Skill

```bash
copaw skills config
# Select your skill to enable it
```

## 📝 Best Practices

### 1. Clear Descriptions

✅ **Good:**
```yaml
description: "Use this skill when user wants to check weather. Trigger keywords: 'weather', 'temperature', 'forecast'"
```

❌ **Not ideal:**
```yaml
description: "Weather skill"
```

### 2. Specific Instructions

- Tell the agent **when** to use the skill
- Explain **how** to use it (commands, parameters)
- Provide **examples** of user queries

### 3. Error Handling

- Check for required environment variables
- Provide clear error messages
- Suggest fixes in error output

### 4. Documentation

- Add comments to scripts
- Include usage examples
- Document dependencies

## 🔍 Debugging Skills

### Check if Skill is Loaded

```bash
copaw skills list
ls ~/.copaw/active_skills/
```

### Test Script Independently

```bash
python ~/.copaw/active_skills/my_skill/scripts/script.py --help
```

### View Agent Logs

```bash
# Set debug logging
export COPAW_LOG_LEVEL=DEBUG
copaw app
```

## 📚 Advanced Topics

### Using External APIs

See `weather_skill/scripts/weather_api.py` for an example of:
- Making HTTP requests
- Handling API keys
- Error handling
- Output formatting

### Skill Dependencies

If your skill needs extra Python packages:

```bash
# Install in your environment
pip install requests beautifulsoup4

# Or create requirements.txt in skill directory
echo "requests>=2.28.0" > requirements.txt
```

### Multi-file Skills

```
complex_skill/
├── SKILL.md
├── references/
│   ├── guide.md
│   └── examples/
│       └── example1.md
└── scripts/
    ├── main.py
    ├── utils.py
    └── config.json
```

## ❓ Troubleshooting

### Skill Not Recognized

```bash
# Re-sync skills
copaw skills sync

# Check active skills
ls ~/.copaw/active_skills/
```

### Script Execution Fails

- Check file permissions: `chmod +x script.py`
- Verify Python path in shebang: `#!/usr/bin/env python3`
- Test script independently first

### Agent Doesn't Use Skill

- Make description more specific
- Add more trigger keywords
- Check if skill is enabled: `copaw skills list`

## 🎯 Next Steps

1. **Modify Weather Skill**: Customize it for your needs
2. **Create Your Own**: Build a skill for your use case
3. **Share**: Contribute to [Skills Hub](https://clawhub.ai/)

## 📚 Related Documentation

- [Skills Development Guide](https://copaw.agentscope.io/docs/skills)
- [SKILL.md Best Practices](https://copaw.agentscope.io/docs/skills#best-practices)
- [Skills Hub](https://clawhub.ai/)

---

Need help? [Open an issue](https://github.com/agentscope-ai/CoPaw/issues)!
