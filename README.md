# cookiecutter-python

Lightweight [Cookiecutter][1] template for quickly starting private Python projects.

## What you get

- Minimal [src layout][2]
- Dependency management with [uv][3]
- Quality checks with [pre-commit][4]
- Linting and formatting with [Ruff][5]
- Tests with [pytest][6]
- Task automation with [Task][7]
- CI starter for [GitHub Actions][8]

## Prerequisites

- [uv][3]
- [Task][7]
- [cookiecutter][1] (`uv tool install cookiecutter`)

## Generate a project

From GitHub:

```bash
uv tool run cookiecutter https://github.com/juwagner/cookiecutter-python
cd <project_slug>
task setup
```

From local path:

```bash
uv tool run cookiecutter /absolute/path/to/cookiecutter-python
cd <project_slug>
task setup
```

`project_slug` is the repository folder name (for example `my-private-project`).
`package_name` is the Python import package (for example `my_private_project`).

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

## Project workflow

- `task setup` initializes the local dev environment
- `task lint` runs pre-commit checks on all files
- `task test` runs pytest

[1]: https://github.com/cookiecutter/cookiecutter
[2]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[3]: https://docs.astral.sh/uv/
[4]: https://pre-commit.com/
[5]: https://docs.astral.sh/ruff/
[6]: https://docs.pytest.org/
[7]: https://taskfile.dev/
[8]: https://docs.github.com/en/actions
