"""Simple economic simulation model."""

from dataclasses import dataclass
from typing import List

@dataclass
class PolicyInputs:
    interest_rate: float
    government_spending_pct: float  # percentage of GDP
    tax_rate: float  # percentage of GDP

@dataclass
class SimulationResult:
    gdp_history: List[float]

BASE_GROWTH = 0.02
SPENDING_MULTIPLIER = 0.5
TAX_MULTIPLIER = 0.4
INTEREST_RATE_MULTIPLIER = 0.3

def simulate_economy(
    initial_gdp: float,
    policies: PolicyInputs,
    years: int = 1,
) -> SimulationResult:
    """Run a simple economic simulation.

    Args:
        initial_gdp: Starting GDP value.
        policies: Policy inputs for the simulation.
        years: Number of years to simulate.

    Returns:
        SimulationResult containing GDP values for each year.
    """
    gdp = initial_gdp
    history = [gdp]
    for _ in range(years):
        growth_rate = (
            BASE_GROWTH
            + SPENDING_MULTIPLIER * policies.government_spending_pct
            - TAX_MULTIPLIER * policies.tax_rate
            - INTEREST_RATE_MULTIPLIER * policies.interest_rate
        )
        gdp *= 1 + growth_rate
        history.append(gdp)
    return SimulationResult(gdp_history=history)
