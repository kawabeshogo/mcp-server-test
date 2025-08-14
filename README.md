# MCP Server Test Repository

This repository is for testing Model Context Protocol (MCP) servers. Based on Python best-practice template featuring:

- `uv` for fast, reproducible dependency management
- **Ruff** (lint + format) for Python
- **Prettier** for non-Python files (JS/TS/JSON/YAML/MD/HTML/CSS)
- `pytest` (tests), `pre-commit` (quality gates)
- VS Code workspace config & tasks
- Dev Container (Codespaces-ready)
- GitHub Actions CI (pre-commit: Ruff + Prettier, then tests, then build)
- Opinionated project structure (`src/` layout, type hints, 100-line limit)

## Purpose

This repository is specifically designed for:
- Testing MCP (Model Context Protocol) server implementations
- Experimenting with MCP client-server communication
- Developing and validating MCP tools and capabilities

## Quickstart

```bash
# 1) Clone this repository
# 2) Initialize the project:
scripts/bootstrap.sh mcp_server_test
# or on Windows PowerShell:
# scripts/New-Project.ps1 -ProjectName mcp_server_test

# 3) Run dev tasks
uv run pytest -q
uv run ruff check --fix && uv run ruff format
# Optional (if Node installed): npx prettier --write .
```

## MCP Server Development

### Directory Structure
- `src/mcp_server_test/` - Main MCP server implementation
- `tests/` - Test cases for MCP server functionality
- `scripts/` - Development and deployment scripts

### Development Workflow
1. Implement MCP server tools in `src/mcp_server_test/`
2. Add corresponding tests in `tests/`
3. Run tests with `uv run pytest`
4. Format code with `uv run ruff format`

**Formatting policy**
- Python: Ruff (formatter + lint)
- Others: Prettier (VS Code format-on-save + pre-commit)