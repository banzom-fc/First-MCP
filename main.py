from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()


mcp_client = MultiServerMCPClient(
    {
        "maths-mcp": {
            "command": "python",
            "args": [os.path.join(os.getcwd(), "MCP-SERVERS", "math-mcp.py")],
            "transport": "stdio",
        },
        "weather-mcp": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        },
        "execute-shell-mcp": {
            "command": "python",
            "args": [os.path.join(os.getcwd(), "MCP-SERVERS", "execute-shell-mcp.py")],
            "transport": "stdio",
        }
    } # type: ignore
)

async def call():
    """
    Call the MCP servers and print the results, maintaining conversation history.
    """
    tools = await mcp_client.get_tools()
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    agent = create_react_agent(
        model=model,
        tools=tools    
    )

    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        conversation_history.append(HumanMessage(content=user_input))
        # Pass the full conversation history to the agent
        response = await agent.ainvoke(
            {"messages": [msg.model_dump() for msg in conversation_history]},
        )

        # Add the agent's response to the conversation history
        agent_message = response['messages'][-1]
        conversation_history.append(agent_message)

        print("Agent:", end=" ")
        print(agent_message.content)
        print("\n---\n")

if __name__ == "__main__":
    asyncio.run(call())
    """
    Run the MCP client and start the conversation.
    This will connect to the MCP servers and allow interaction with the tools.
    """