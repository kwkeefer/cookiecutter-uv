"""Example tests for core module."""

import pytest

{%- if cookiecutter.include_example_code == 'yes' %}
from {{ cookiecutter.package_name }}.core.example import process_data


class TestProcessData:
    """Test suite for process_data function."""

    @pytest.mark.unit
    def test_process_data_valid(self, sample_data):
        """Test process_data with valid input."""
        result = process_data(sample_data)
        assert result is not None
        assert "processed" in result
        assert result["processed"] is True

    @pytest.mark.unit
    def test_process_data_empty(self):
        """Test process_data with empty input."""
        result = process_data({})
        assert result == {"processed": False, "reason": "empty_data"}

    @pytest.mark.unit
    def test_process_data_invalid_type(self):
        """Test process_data with invalid input type."""
        with pytest.raises(TypeError):
            process_data("invalid")

{%- else %}


@pytest.mark.unit
def test_placeholder():
    """Placeholder test - replace with your actual tests."""
    assert True
{%- endif %}