from fastmcp import FastMCP
import feedparser

mcp = FastMCP()

@mcp.tool(name="FreeCodeCamp News Fetcher", description="Fetches the latest news articles from FreeCodeCamp's news feed.")
def fetch_freecodecamp_news(query: str, max_results: int = 5) -> list:
    """
    Fetches the latest news articles from FreeCodeCamp's news RSS feed.

    Args:
        query (str): The search query to filter articles.
        max_results (int): The maximum number of articles to return.

    Returns:
        list: A list of dictionaries containing article titles and links.
    """
    feed_url = "https://www.freecodecamp.org/news/rss/"
    feed = feedparser.parse(feed_url)
    results = []
    query = query.strip().lower()
    for entry in feed.entries:
        if query in entry.title.lower() or query in entry.description.lower():
            results.append({
                "title": entry.title,
                "URL": entry.link
            })
        if len(results) >= max_results:
            break

    return results or [{"message": "No articles found matching the query."}]

@mcp.tool()
def fetch_freecodecamp_youtube_videos(query: str, max_results: int = 5) -> list:
    """
    Fetches the latest YouTube videos from FreeCodeCamp's YouTube channel.

    Args:
        query (str): The search query to filter videos.
        max_results (int): The maximum number of videos to return.

    Returns:
        list: A list of dictionaries containing video titles and links.
    """
    feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    feed = feedparser.parse(feed_url)
    results = []
    query = query.strip().lower()
    for entry in feed.entries:
        if query in entry.title.lower() or query in entry.summary.lower():
            results.append({
                "title": entry.title,
                "URL": entry.link
            })
        if len(results) >= max_results:
            break

    return results or [{"message": "No videos found matching the query."}]

if __name__ == "__main__":
    mcp.run() # STDIO