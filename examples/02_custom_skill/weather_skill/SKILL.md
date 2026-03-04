---
name: weather
description: "Use this skill whenever user wants to check weather information. Trigger especially when user mentions: 'weather', 'temperature', 'forecast', or asks about weather conditions in a city."
metadata:
  copaw:
    emoji: "🌤️"
    requires:
      WEATHER_API_KEY: "Get from openweathermap.org (free tier available)"
---

# Weather Query Skill

This skill allows the agent to query real-time weather information for cities worldwide.

## When to Use

Use this skill when the user:
- Asks about current weather ("What's the weather in Beijing?")
- Wants to know temperature ("How hot is it in Shanghai?")
- Inquires about weather conditions ("Is it raining in Tokyo?")

## How to Use

When the user asks about weather, use the `execute_shell_command` tool to run:

```bash
python {SKILL_DIR}/scripts/weather_api.py --city "CityName"
```

Replace `{SKILL_DIR}` with the actual skill directory path, and `CityName` with the city the user asked about.

## Supported Cities

- **Chinese cities**: Beijing (北京), Shanghai (上海), Shenzhen (深圳), Guangzhou (广州), etc.
- **International cities**: New York, London, Tokyo, Paris, Sydney, etc.

## Response Format

The script returns weather information in this format:

```
City: Beijing
Temperature: 25°C
Weather: Clear sky
Humidity: 60%
Wind Speed: 3.5 m/s
```

## Setup

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Set the environment variable:
   ```bash
   export WEATHER_API_KEY="your-api-key-here"
   ```
3. Or add it to `~/.copaw/.secret/envs.json`:
   ```json
   {
     "WEATHER_API_KEY": "your-api-key-here"
   }
   ```

## Example Queries

- "What's the weather like in Beijing today?"
- "Tell me the temperature in New York"
- "Is it raining in London?"
- "How's the weather in Tokyo?"

## Error Handling

If the API key is not set, the script will return:
```
Error: WEATHER_API_KEY environment variable not set
```

If the city is not found:
```
Error: City not found. Please check the city name.
```

## Notes

- Weather data is updated every 10 minutes
- Free tier allows 60 calls per minute
- Temperature is in Celsius by default
