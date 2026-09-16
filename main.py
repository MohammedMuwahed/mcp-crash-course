import asyncio
from dotenv import load_dotenv

load_dotenv()

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools

from langchain.agents import create_agent

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:\\Users\\moham\\Documents\\GitHub\\mcp-crash-course\\server\\math_server.py"],
)

async def main():
    print("Hello from mcp-crash-course")

if __name__ == "__main__":
    asyncio.run(main())
