from pathlib import Path

from cookiecutter.main import cookiecutter

ROOT_PATH = Path(__file__).parent.parent
PROJECT_NAME = "Test Project"
PROJECT_SLUG = "test-project"
PACKAGE_NAME = "test_project"
AUTHOR = "Test Author"


def test_generate_project(tmp_path: Path):
    cookiecutter(
        template=ROOT_PATH.as_posix(),
        no_input=True,
        extra_context={
            "project_name": PROJECT_NAME,
            "author": AUTHOR,
        },
        output_dir=tmp_path.as_posix(),
    )

    generated_project = tmp_path / PROJECT_SLUG
    assert generated_project.exists()
    assert (generated_project / f"src/{PACKAGE_NAME}").exists()
    assert (generated_project / "pyproject.toml").exists()

    pyproject_content = (generated_project / "pyproject.toml").read_text(encoding="utf-8")
    assert f'name = "{PROJECT_SLUG}"' in pyproject_content
    assert f'name = "{AUTHOR}"' in pyproject_content
