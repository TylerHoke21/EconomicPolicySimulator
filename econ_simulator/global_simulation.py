"""Simulation utilities for global policy impact."""

from typing import Dict

from .simulation import PolicyInputs, simulate_economy

# Baseline GDP values for a few major economies (in billions of dollars)
GLOBAL_BASE_GDP = {
    "USA": 21000,
    "CHN": 14000,
    "DEU": 3800,
    "IND": 2900,
    "BRA": 1800,
}


def simulate_global(policies: PolicyInputs, years: int = 1) -> Dict[str, float]:
    """Simulate GDP outcomes for several major economies."""
    results: Dict[str, float] = {}
    for code, gdp in GLOBAL_BASE_GDP.items():
        result = simulate_economy(gdp, policies, years=years)
        results[code] = result.gdp_history[-1]
    return results
