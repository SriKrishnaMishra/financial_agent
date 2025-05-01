# Financial AI Agent

This project is a Financial AI Agent that leverages advanced AI models and tools to provide financial insights, such as stock prices, analyst recommendations, stock fundamentals, and company news. The agent is built using the `phi` library and integrates with APIs like YFinance and Groq.

## Features

- **Stock Price Analysis**: Fetch real-time stock prices.
- **Analyst Recommendations**: Summarize analyst recommendations for a given stock.
- **Stock Fundamentals**: Provide key financial metrics and fundamentals.
- **Company News**: Display the latest news for a specific company.
- **Web Search Integration** (optional): Search the web for additional information using DuckDuckGo.

## Requirements

- Python 3.8 or higher
- `phi` library
- `dotenv` for environment variable management
- API keys for Groq and optional OpenAI integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-ai-agent.git
   cd financial-ai-agent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key  # Optional
   ```

## Usage

1. Run the `financial_agent.py` script:
   ```bash
   python financial_agent.py
   ```

2. The agent will process the query and display the results in a tabular format.

### Example Query

The agent is pre-configured to handle the following query:
```
Summarize analyst recommendation and share the latest news for NVDA
```

You can modify the query in the `finance_agent.print_response()` method in `financial_agent.py`.

## Project Structure

```
financial-ai-agent/
├── financial_agent.py       # Main script for the financial AI agent
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not included in the repo)
├── README.md                # Project documentation
└── other_files/             # Placeholder for additional scripts or data
```

## Extending the Project

### Adding a Web Search Agent

To include a web search agent, uncomment the relevant sections in `financial_agent.py` and ensure the `DuckDuckGo` tool is imported.

### Combining Agents

You can use the `multi_ai_agent` to combine the financial agent and web search agent for more comprehensive responses.

## Dependencies

- `phi`: Core library for building AI agents
- `dotenv`: Manage environment variables
- `yfinance`: Fetch financial data
- `duckduckgo-search`: Optional for web search integration

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or support, please contact [your-email@example.com].
