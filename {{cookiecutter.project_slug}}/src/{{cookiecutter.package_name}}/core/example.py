{%- if cookiecutter.include_example_code == 'yes' %}
"""Example module demonstrating project structure."""

from typing import Any, Dict


def process_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Process input data and return results.
    
    Args:
        data: Input data dictionary
        
    Returns:
        Processed data with added metadata
        
    Raises:
        TypeError: If data is not a dictionary
    """
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    
    if not data:
        return {"processed": False, "reason": "empty_data"}
    
    return {
        **data,
        "processed": True,
        "item_count": len(data),
    }
{%- endif %}