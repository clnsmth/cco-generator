from cco_core import __name__ as package_name


def test_environment_is_ready():
    """Ensure the package is installed and importable."""
    assert package_name == "cco_core"
