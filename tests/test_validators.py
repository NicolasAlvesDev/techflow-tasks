import pytest

from src.validators import validate_title, validate_status, ValidationError


def test_title_is_trimmed():
    assert validate_title("  Fazer deploy  ") == "Fazer deploy"


@pytest.mark.parametrize("bad", ["", "   ", None, 123])
def test_title_required(bad):
    with pytest.raises(ValidationError):
        validate_title(bad)


def test_title_too_long():
    with pytest.raises(ValidationError):
        validate_title("x" * 101)


def test_status_valid_and_invalid():
    assert validate_status("doing") == "doing"
    with pytest.raises(ValidationError):
        validate_status("pronto")


def test_priority_valid_and_invalid():
    from src.validators import validate_priority
    assert validate_priority("critical") == "critical"
    with pytest.raises(ValidationError):
        validate_priority("urgentissima")
