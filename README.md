# Crypto News Analysis Agent 

This project is a Python-based agent that automatically fetches the latest news for top cryptocurrencies and uses a locally-run Large Language Model (Llama 3 via Ollama) to perform a quick analysis of each news headline.

The agent provides a summary, relevant keywords, and the overall sentiment (Positive, Negative, Neutral) for each news item, delivering a concise daily report directly in your terminal.


---

## Features

- **Multi-Coin Support**: Fetches news for Bitcoin, Ethereum, Ripple, Litecoin, and Cardano.
- **Automated Analysis**: Uses a local LLM (via Ollama) to analyze headlines, ensuring privacy and no API costs for analysis.
- **In-depth Insights**: Extracts a summary, keywords, and sentiment for each news title.
- **Clean Reporting**: Generates a clean, readable report in Markdown format in the terminal.
- **Modular Code**: Well-structured and easy-to-understand codebase.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-222222?style=for-the-badge&logo=ollama&logoColor=white)
![GNews API](https://img.shields.io/badge/GNews-API-orange?style=for-the-badge)

---

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/crypto-news-agent.git](https://github.com/YOUR_USERNAME/crypto-news-agent.git)
cd crypto-news-agent
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

The project requires the `requests` and `python-dotenv` libraries.

```bash
pip install -r requirements.txt
```

### 4. Set up Local LLM with Ollama

You need to have Ollama installed and running.

- **Install Ollama**: Follow the instructions on [ollama.com](https://ollama.com/).
- **Pull the Llama 3 Model**: Run the following command in your terminal.
  ```bash
  ollama pull llama3
  ```
  *(Note: The code is set to use `llama3.2:latest`, you can change this in `config.py` to `llama3` or any other model you have available).*

### 5. Configure Environment Variables

For security, API keys should not be hard-coded. This project uses a `.env` file to manage secrets.

- **Create a `.env` file** in the root directory of the project.
- **Add your GNews API key** to the file:
  ```env
  GNEWS_API_KEY="YOUR_GNEWS_API_KEY_HERE"
  ```
- The project is already configured to read from this file.

---

## Usage

Once the setup is complete, simply run the main script:

```bash
python main.py
```

The script will fetch the latest news, analyze it, and print the report directly to your console.

## Project Structure

```
crypto-news-agent/
├── .env              # Stores your secret API key (MUST NOT be on GitHub)
├── .gitignore        # Tells Git to ignore files like .env and venv/
├── config.py         # Reads configuration and API keys
├── llama_api.py      # Handles communication with the Ollama API
├── llama_processor.py# Creates prompts for the LLM and processes responses
├── main.py           # The main entry point of the application
├── news_fetcher.py   # Fetches news from the GNews API
└── requirements.txt  # Lists the Python dependencies
```
