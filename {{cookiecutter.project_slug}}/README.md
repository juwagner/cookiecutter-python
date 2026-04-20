# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [Task](https://taskfile.dev/) (optional)

## Setup development environment

```bash
task setup
```

This command:
- Initializes a local Git repository (if not already done)
- Creates `.env` from `.env.example` (if missing)
- Installs and configures pre-commit hooks
- Syncs Python dependencies

### Without Task

```bash
git init
cp .env.example .env
uv sync --all-groups
uv tool install pre-commit
uv tool run pre-commit install
```

## Project structure

```text
{{cookiecutter.project_slug}}/
├── .env.example              # Environment variables template
├── .github/
│   └── workflows/
│       └── ci.yaml           # GitHub Actions CI/CD
├── .pre-commit-config.yaml   # Pre-commit hooks
├── pyproject.toml            # Dependencies and config
├── README.md
├── taskfile.yml              # Task automation
├── data/                     # Data files
│   └── README.md
├── notebooks/                # Jupyter notebooks
│   └── README.md
├── src/
│   └── {{cookiecutter.package_name}}/
│       ├── __init__.py
│       ├── config.py         # Configuration
│       ├── constants.py      # Constants
│       ├── logger.py         # Logging setup
│       └── utils.py          # Utilities
└── tests/
    └── conftest.py           # Pytest configuration
```

## Development workflow

### Run linters and formatters

```bash
task lint
```

This runs pre-commit on all files:
- Ruff: Linting, formatting, import sorting
- Pre-commit hooks

### Run tests

```bash
task test
```

### Without Task

```bash
uv run pre-commit run --all-files
uv run pytest
```
