# tests/test_basic.py

def test_project_exists():
    """Basic test - project structure exists."""
    import os
    assert os.path.exists("app"), "app folder should exist"
    assert os.path.exists("data"), "data folder should exist"
    assert os.path.exists("requirements.txt"), "requirements.txt should exist"

def test_requirements_not_empty():
    """Check requirements.txt has content."""
    with open("requirements.txt") as f:
        content = f.read()
    assert len(content) > 0, "requirements.txt should not be empty"

def test_basic_math():
    """Sanity check."""
    assert 1 + 1 == 2