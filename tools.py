from agents import function_tool
from duckduckgo_search import DDGS

@function_tool
async def web_search(query: str) -> str:
    """Search the web for a query using DuckDuckGo and return a summary."""
    with DDGS() as ddgs:
        results = ddgs.text(query)
        output = ""
        for r in results[:5]:
            output += f"- {r['title']}: {r['href']}\n"
        return output or "No relevant results found."