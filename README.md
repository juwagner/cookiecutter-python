# cookiecutter-python

Lightweight [Cookiecutter][1] template for quickly starting Python projects.

## Features

- Minimal [src layout][2]
- Dependency management with [uv][3]
- Quality checks with [pre-commit][4]
- Linting and formatting with [Ruff][5]
- Testing with [pytest][6]
- Task automation with [Task][7]
- CI starter for [GitHub Actions][8]

## Prerequisites

- [uv][3]
- [Task][7]
- Python >= 3.12

## Generate a project

### From GitHub

```bash
uv tool run cookiecutter https://github.com/juwagner/cookiecutter-python
cd <project_slug>
task setup
```

### From local path

```bash
uv tool run cookiecutter /absolute/path/to/cookiecutter-python
cd <project_slug>
task setup
```

### Variable reference

- `project_name`: Human-readable project name (e.g., "My Project")
- `project_slug`: Repository folder name, derived from project name (e.g., `my-project`)
- `package_name`: Python import package, derived from project slug (e.g., `my_project`)
- `author`: Author name

## Generated project structure

```text
<project_slug>/
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
│   └── <package_name>/
│       ├── __init__.py
│       ├── config.py
│       ├── constants.py
│       ├── logger.py
│       └── utils.py
└── tests/
    └── conftest.py
```

## Typical workflow

```bash
# First time setup
task setup

# Quality checks (linting + formatting via Ruff)
task lint

# Run tests
task test
```

## Contributing

See [Contributing](CONTRIBUTING.md).

[1]: https://github.com/cookiecutter/cookiecutter
[2]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[3]: https://docs.astral.sh/uv/
[4]: https://pre-commit.com/
[5]: https://docs.astral.sh/ruff/
[6]: https://docs.pytest.org/
[7]: https://taskfile.dev/
[8]: https://docs.github.com/en/actions
