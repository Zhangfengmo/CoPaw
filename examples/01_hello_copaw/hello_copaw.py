#!/usr/bin/env python3
"""
CoPaw 最简单的使用示例 / Simplest CoPaw Usage Example

这个示例展示如何：
1. 创建一个 CoPaw Agent
2. 发送消息并获取回复
3. 进行多轮对话

This example demonstrates how to:
1. Create a CoPaw Agent
2. Send messages and get responses
3. Have multi-turn conversations

运行前确保 / Before running:
1. pip install copaw
2. copaw init --defaults
3. 配置 API Key / Configure API Key (via copaw init or environment variable)
"""
import asyncio
import sys
from agentscope.message import Msg

try:
    from copaw.agents.react_agent import CoPawAgent
except ImportError:
    print("Error: CoPaw is not installed.")
    print("Please run: pip install copaw")
    sys.exit(1)


async def main():
    """基础对话示例 / Basic conversation example"""
    print("🐾 CoPaw Hello World Example\n")
    print("Initializing agent...")

    try:
        # 1. 创建 Agent（自动加载配置、技能、工具）
        # Create Agent (automatically loads config, skills, tools)
        agent = CoPawAgent()
        print("✓ Agent initialized successfully\n")

        # 2. 发送第一条消息
        # Send first message
        print("User: 你好！请介绍一下你自己。")
        user_msg = Msg(
            name="User",
            content="你好！请介绍一下你自己。",
            role="user"
        )
        response = await agent.reply(user_msg)

        # 3. 打印回复
        # Print response
        print(f"Agent: {response.content}\n")

        # 4. 继续对话（带上下文）
        # Continue conversation (with context)
        print("User: 你能做什么？")
        follow_up = Msg(
            name="User",
            content="你能做什么？",
            role="user"
        )
        response2 = await agent.reply(follow_up)
        print(f"Agent: {response2.content}\n")

        print("✓ Conversation completed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you've run 'copaw init'")
        print("2. Check if API key is configured")
        print("3. Verify network connection")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
