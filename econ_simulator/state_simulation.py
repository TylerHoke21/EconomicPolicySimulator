"""Utilities for running simulations across U.S. states."""

from typing import Dict

from .simulation import PolicyInputs, simulate_economy
from .us_states import STATE_BASE_GDP


def simulate_states(policies: PolicyInputs, years: int = 1) -> Dict[str, float]:
    """Run the economic simulation for each U.S. state.

    Args:
        policies: Policy inputs shared by all states.
        years: Number of years to simulate.

    Returns:
        Mapping of state abbreviation to predicted GDP after the final year.
    """
    results: Dict[str, float] = {}
    for abbr, gdp in STATE_BASE_GDP.items():
        result = simulate_economy(gdp, policies, years=years)
        results[abbr] = result.gdp_history[-1]
    return results
