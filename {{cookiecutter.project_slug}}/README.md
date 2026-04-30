# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Prerequisites

- [uv][3]
- [Task][7]
- Python >= 3.12

## Setup development environment

```bash
task setup
```

- Initializes a local Git repository (if missing)
- Creates `.env` from `.env.example` (if missing)
- Installs and configures [pre-commit][4] hooks
- Syncs Python dependencies

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
    └── conftest.py           # Pytest fixtures
```

## Development workflow

```bash
task lint
```

- Performs linting, formatting, and import sorting with [ruff][5]
- Runs [pre-commit][4] hooks

```bash
task test
```

- Runs all tests with [pytest][7]

## Contributing

See [Contributing](CONTRIBUTING.md).


[3]: https://docs.astral.sh/uv/
[4]: https://pre-commit.com/
[5]: https://docs.astral.sh/ruff/
[6]: https://docs.pytest.org/
[7]: https://taskfile.dev/
