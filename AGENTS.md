# AGENTS.md

This file contains commands for linting, type checking, and testing the project.

## Commands

### Build
```bash
docker build -t 1week-project .
```

### Lint
```bash
ruff check .
ruff check --fix .  # Auto-fix issues
```

### Type Check
```bash
mypy .
```

### Test
```bash
pytest                          # Run all tests
pytest tests/test_file.py       # Run specific test file
pytest tests/test_file.py::test_function  # Run single test
pytest -v                      # Verbose output
```

## Code Style Guidelines

### Imports
- Use absolute imports
- Group: standard library, third-party, local modules
- Sort imports alphabetically within groups

### Formatting
- Use ruff for consistent formatting (replaces black/isort)
- Line length: 88 characters (default)
- Use double quotes for strings

### Types
- Use type hints for all function parameters and return values
- Use mypy for static type checking
- Prefer `Union` over `|` for Python <3.10 compatibility

### Naming
- Functions/variables: snake_case
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE
- Private methods: _leading_underscore

### Error Handling
- Use specific exceptions over generic Exception
- Log errors with context
- Prefer early returns over nested if statements

### Testing
- Write tests for all public functions
- Use descriptive test names: test_function_name_condition_expected
- Mock external dependencies