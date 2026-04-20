# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [Task](https://taskfile.dev/) (optional, for shorter commands)

## Setup

```bash
task setup
```

`task setup` will:

- initialize a local Git repository (if missing)
- create `.env` from `.env.example` (if missing)
- install pre-commit hooks
- sync dependencies via `uv`

## Project structure

```text
{{cookiecutter.project_slug}}/
├── .env.example
├── .github/
│   └── workflows/
│       └── ci.yaml
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── taskfile.yml
├── data/
│   └── README.md
├── notebooks/
│   └── README.md
├── src/
│   └── {{cookiecutter.package_name}}/
│       ├── __init__.py
│       ├── config.py
│       ├── constants.py
│       ├── logger.py
│       └── utils.py
└── tests/
    └── conftest.py
```

Without Task:

```bash
git init
cp .env.example .env
uv sync --all-groups
uv tool run pre-commit install
```

## Development workflow

Run quality checks (lint + auto-fixes):

```bash
task lint
```

`task lint` runs pre-commit on all files. Import sorting is included via Ruff isort rules.

Run tests:

```bash
task test
```

Without Task:

```bash
uv run pre-commit run --all-files
uv run pytest
```
