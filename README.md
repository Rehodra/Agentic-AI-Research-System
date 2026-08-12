# Agentic AI Research System

An agentic AI research pipeline that automates end-to-end research on any topic using multiple LLM-powered agents. It coordinates search, scraping, report writing, and critique into a single workflow.

## Tech Stack

- **Language:** Python >= 3.10
- **LLM Framework:** LangChain + Groq
- **Search:** Tavily
- **Web Scraping:** BeautifulSoup + requests + lxml
- **CLI:** Rich

## Features

- **Search Agent** — Queries the web via Tavily to fetch top results
- **Scrape Agent** — Extracts clean text from a relevant URL
- **Writer Chain** — Generates a structured research report
- **Critic Chain** — Evaluates the report with a score and feedback
- **Multi-key Load Distribution** — Distributes Groq API calls across multiple keys

## Screenshots

| | |
|---|---|
| ![Screenshot 1](assets/screenshot1.png) | ![Screenshot 2](assets/screenshot2.png) |

## Project Structure

```
Agentic-AI-Research-System/
├── .env.sample
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── app/
    ├── agents.py          # LLM instances and agent/chain builders
    ├── cli_formatter.py   # Rich terminal output utilities
    ├── pipeline.py        # End-to-end pipeline orchestration
    └── tools.py           # Web search and URL scraping tools
```

## Installation

```powershell
cd D:\GEN-AI-tutorial\Agentic-AI-Research-System
uv sync
```

## Configuration

1. Copy `.env.sample` to `.env`
2. Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Optional extra keys for load distribution:
```env
GROQ_API_KEY2=your_groq_api_key_2
GROQ_API_KEY3=your_groq_api_key_3
GROQ_API_KEY4=your_groq_api_key_4
```

Optional model override:
```env
GROQ_MODEL=llama-3.1-8b-instant
```

## Usage

```powershell
uv run python app/pipeline.py
```

Or directly:
```powershell
python app/pipeline.py
```

Enter a research topic when prompted. The pipeline will:
1. Search the web for relevant sources
2. Scrape a top result for deeper content
3. Write a structured report
4. Critique the report with a score and improvement suggestions
