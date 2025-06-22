import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from econ_simulator.simulation import PolicyInputs, simulate_economy


def test_simulation_basic():
    policies = PolicyInputs(interest_rate=0.05, government_spending_pct=0.2, tax_rate=0.2)
    result = simulate_economy(1000, policies, years=1)
    assert len(result.gdp_history) == 2
    assert result.gdp_history[0] == 1000
    assert result.gdp_history[1] > 0
from econ_simulator.state_simulation import simulate_states
from econ_simulator.us_states import STATE_ABBREVIATIONS
from econ_simulator.global_simulation import simulate_global, GLOBAL_BASE_GDP


def test_simulate_states_returns_all_states():
    policies = PolicyInputs(interest_rate=0.05, government_spending_pct=0.2, tax_rate=0.2)
    state_results = simulate_states(policies, years=1)
    assert set(state_results.keys()) == set(STATE_ABBREVIATIONS)
    for value in state_results.values():
        assert value > 0


def test_simulate_global_returns_all_regions():
    policies = PolicyInputs(interest_rate=0.05, government_spending_pct=0.2, tax_rate=0.2)
    global_results = simulate_global(policies, years=1)
    assert set(global_results.keys()) == set(GLOBAL_BASE_GDP.keys())
    assert len(GLOBAL_BASE_GDP) > 170
    for value in global_results.values():
        assert value > 0
