# First-MCP: Basic MCP Agent with Gemini

A basic Model Context Protocol (MCP) agent implementation that integrates Google's Gemini AI with custom MCP servers for mathematical calculations and weather information.

## Overview

This project demonstrates how to build an MCP-enabled AI agent using:
- **Google Gemini 2.5 Flash** as the language model
- **LangChain** for agent orchestration
- **Custom MCP servers** for specialized tools (math and weather)
- **Conversational interface** with persistent chat history

## Features

- 🤖 **AI Agent**: Powered by Google Gemini 2.5 Flash
- 🧮 **Math Operations**: Custom MCP server for mathematical calculations
- 🌤️ **Weather Information**: HTTP-based weather MCP server
- 💬 **Interactive Chat**: Command-line conversation interface
- 📝 **Conversation History**: Maintains context across interactions
- 🔧 **Extensible**: Easy to add new MCP servers and tools

## Project Structure

```
First-MCP/
├── main.py                 # Main application entry point
├── MCP-SERVERS/           # Custom MCP server implementations
│   ├── math-mcp.py        # Mathematical operations server
│   └── weather-mcp.py     # Weather information server
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
├── .env                  # Environment variables (API keys)
├── .gitignore           # Git ignore rules
└── README.md            # This documentation
```

## Prerequisites

- Python 3.12 or higher
- Google API key for Gemini access
- Internet connection for weather services

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd First-MCP
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

### Running the Agent

Start the interactive chat interface:

```bash
python main.py
```

### Example Interactions

```
You: What is 25 * 47?
Agent: The result of 25 * 47 is 1175.

You: What's the weather like in New York?
Agent: [Weather information for New York will be displayed]

You: Calculate the square root of 144
Agent: The square root of 144 is 12.

You: exit
```

### Available Commands

- Type your questions or requests naturally
- Use `exit` or `quit` to end the conversation
- The agent maintains conversation history for context

## MCP Servers

### Math MCP Server (`math-mcp.py`)
- **Transport**: stdio
- **Capabilities**: Basic mathematical operations
- **Location**: `/MCP-SERVERS/math-mcp.py`

### Weather MCP Server (`weather-mcp.py`)
- **Transport**: HTTP (streamable_http)
- **Endpoint**: `http://localhost:8000/mcp`
- **Capabilities**: Weather information retrieval
- **Location**: `/MCP-SERVERS/weather-mcp.py`

## Configuration

The MCP client configuration in `main.py`:

```python
mcp_client = MultiServerMCPClient({
    "maths-mcp": {
        "command": "python",
        "args": ["/path/to/math-mcp.py"],
        "transport": "stdio",
    },
    "weather-mcp": {
        "url": "http://localhost:8000/mcp",
        "transport": "streamable_http",
    }
})
```

## Dependencies

- **langchain-google-genai**: Google Gemini integration
- **langchain-mcp-adapters**: MCP protocol adapters for LangChain
- **langgraph**: Agent workflow orchestration
- **mcp**: Model Context Protocol implementation
- **requests**: HTTP client for API calls
- **python-dotenv**: Environment variable management

## Development

### Adding New MCP Servers

1. Create a new server file in `MCP-SERVERS/`
2. Implement the MCP protocol interface
3. Add server configuration to `main.py`
4. Update documentation

### Extending Functionality

- Modify `main.py` to add new features
- Customize the agent behavior in the `call()` function
- Add new tools and capabilities through MCP servers

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Google API key is correctly set in `.env`
2. **Server Connection**: Verify MCP servers are running and accessible
3. **Dependencies**: Run `pip install -r requirements.txt` to ensure all packages are installed
4. **Python Version**: Ensure you're using Python 3.12 or higher

### Debug Mode

For debugging, you can add logging to see MCP server interactions:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Acknowledgments

- Google Gemini AI for language model capabilities
- LangChain community for MCP adapters
- Model Context Protocol specification

## Support

For issues and questions:
- Check the troubleshooting section
- Review MCP server logs
- Ensure all dependencies are properly installed

---

**Note**: This is a basic implementation for my personal use and experimentation with MCP. 