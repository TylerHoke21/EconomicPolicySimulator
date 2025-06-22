"""Simulation utilities for global policy impact."""

from typing import Dict
from datetime import date

from .simulation import PolicyInputs, simulate_economy

# The simulation begins on this date
START_DATE = date(2025, 1, 1)

# Baseline GDP values (in billions of dollars) are based on 2019 data.
# Missing 2025 figures are extrapolated from post-COVID recovery trends.
_GDP_2019 = {
    "USA": 21521.395,
    "CHN": 14279.969,
    "JPN": 5117.994,
    "DEU": 3889.178,
    "IND": 2835.606,
    "BRA": 1873.288,
    "RUS": 1693.115,
    "GBR": 2851.407,
    "FRA": 2728.870,
    "CAN": 1743.725,
    "AUS": 1394.671,
    "ITA": 2001.244,
    "KOR": 1642.383,
    "ESP": 1394.116,
    "MEX": 1269.648,
    "IDN": 1119.190,
    "TUR": 761.425,
    "NLD": 909.887,
    "SAU": 792.967,
    "CHE": 715.360,
    "ZAF": 351.432,
}

# Approximate global growth factors for 2020-2024
_COVID_RECOVERY_FACTORS = [0.97, 1.05, 1.03, 1.025, 1.023]
_RECOVERY_MULTIPLIER = 1.0
for _factor in _COVID_RECOVERY_FACTORS:
    _RECOVERY_MULTIPLIER *= _factor

GLOBAL_BASE_GDP = {
    code: gdp * _RECOVERY_MULTIPLIER for code, gdp in _GDP_2019.items()
}


def simulate_global(policies: PolicyInputs, years: int = 1) -> Dict[str, float]:
    """Simulate GDP outcomes for several major economies."""
    results: Dict[str, float] = {}
    for code, gdp in GLOBAL_BASE_GDP.items():
        result = simulate_economy(gdp, policies, years=years)
        results[code] = result.gdp_history[-1]
    return results
