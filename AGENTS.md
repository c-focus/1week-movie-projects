# AGENTS.md

## Commands
- **Build**: `docker build -t 1week-project .`
- **Lint**: `ruff check .` / `ruff check --fix .`
- **Type Check**: `mypy .`
- **Test**: `pytest` / `pytest tests/test_file.py::test_function` (single test)

## Code Style
- **Imports**: Absolute imports, grouped (stdlib/third-party/local), sorted alphabetically
- **Formatting**: ruff (88 char lines, double quotes)
- **Types**: Type hints everywhere, mypy, prefer Union over | for <3.10
- **Naming**: snake_case functions/vars, PascalCase classes, UPPER_SNAKE_CASE constants
- **Error Handling**: Specific exceptions, log with context, early returns
- **Testing**: Test public functions, descriptive names, mock dependencies