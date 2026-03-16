# ShrekAgent

A CLI-based coding agent powered by Claude that performs filesystem operations through natural language.

## Quick Start

```bash
pip install anthropic termcolor pydantic
export ANTHROPIC_API_KEY="your-api-key"
python main.py
```

Exit with `Ctrl+D`.

## Architecture

The agent implements a tool-use loop:
1. User input is sent to Claude API
2. Claude responds with tool calls (read/edit/list)
3. Tool results are fed back to Claude
4. Loop continues until task completion

## Project Structure

```
main.py    # Agent core and conversation loop
tools.py   # File operation tools (read, edit, list)
```

## Available Tools

| Tool | Purpose |
|------|---------|
| `read_file` | Read file contents |
| `edit_file` | Create or modify files |
| `list_files` | List directory contents |
