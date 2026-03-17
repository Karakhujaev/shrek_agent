# ShrekAgent

CLI coding agent powered by Claude with RAG-enabled documentation search.

## Setup

```bash
# Install dependencies
pip install anthropic termcolor pydantic weaviate-client

# Start Weaviate
docker compose up -d

# Index documentation
python index_docs.py

# Set API key and run
export ANTHROPIC_API_KEY="your-key"
python main.py
```

Exit with `Ctrl+D`.

## Project Structure

```
main.py         # Agent core and conversation loop
tools.py        # Tool definitions (read, edit, list, search)
rag.py          # Weaviate RAG implementation
index_docs.py   # Document indexer
docs/           # Documentation for RAG
```

## Tools

| Tool | Purpose |
|------|---------|
| `read_file` | Read file contents |
| `edit_file` | Create or modify files |
| `list_files` | List directory contents |
| `search_documentation` | Search indexed docs via RAG |
