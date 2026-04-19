# cookiecutter-python

A lightweight [Cookiecutter](https://github.com/cookiecutter/cookiecutter) to setup Python projects quickly.


- Minimal `src` layout
- Dependency management with [uv](https://docs.astral.sh/uv/)
- Testing with [pytest](https://docs.pytest.org/)
- Linting and formatting via [pre-commit](https://pre-commit.com/) + [ruff](https://docs.astral.sh/ruff/)

## Quickstart

1. Install Cookiecutter:

```bash
uv tool install cookiecutter
```

2. Generate a project from this template:

```bash
uv tool run cookiecutter /path/to/cookiecutter-python
```

3. Enter the generated project and run setup:

```bash
cd <your-project-slug>
task setup
```

## Included project layout

The generated project includes only the essentials:

- `src/<package_name>/`
- `tests/`
- `pyproject.toml`
- `.pre-commit-config.yaml`
- `taskfile.yml`

## Development workflow

```bash
task setup
task lint
task test
```
