"""Interactive map-based interface for the economic simulator."""

import argparse
from typing import Dict

import plotly.express as px

from .simulation import PolicyInputs
from .state_simulation import simulate_states
from .global_simulation import simulate_global


def show_map(state_gdp: Dict[str, float]) -> None:
    """Display an interactive map of the U.S. with GDP data."""
    fig = px.choropleth(
        locations=list(state_gdp.keys()),
        locationmode="USA-states",
        color=list(state_gdp.values()),
        scope="usa",
        color_continuous_scale="Blues",
        labels={"color": "GDP"},
    )
    fig.update_layout(title_text="Projected GDP by State")
    fig.show()


def show_global_map(global_gdp: Dict[str, float]) -> None:
    """Display a simple world map showing GDP results."""
    fig = px.choropleth(
        locations=list(global_gdp.keys()),
        locationmode="ISO-3",
        color=list(global_gdp.values()),
        scope="world",
        color_continuous_scale="Greens",
        labels={"color": "GDP"},
    )
    fig.update_layout(title_text="Projected Global GDP Impact")
    fig.show()


def main() -> None:
    parser = argparse.ArgumentParser(description="Interactive US map for policy simulation")
    parser.add_argument("--interest-rate", type=float, default=0.05, help="Interest rate")
    parser.add_argument("--gov-spending", type=float, default=0.2, help="Government spending as pct of GDP")
    parser.add_argument("--tax-rate", type=float, default=0.2, help="Tax rate as pct of GDP")
    parser.add_argument("--years", type=int, default=1, help="Number of years to simulate")
    args = parser.parse_args()

    policies = PolicyInputs(
        interest_rate=args.interest_rate,
        government_spending_pct=args.gov_spending,
        tax_rate=args.tax_rate,
    )

    while True:
        state_gdp = simulate_states(policies, years=args.years)
        show_map(state_gdp)
        print("\nCurrent policy settings:")
        print(f"  Interest rate: {policies.interest_rate}")
        print(f"  Government spending (% GDP): {policies.government_spending_pct}")
        print(f"  Tax rate (% GDP): {policies.tax_rate}")
        print("\nMenu:")
        print("  1. Change interest rate")
        print("  2. Change government spending")
        print("  3. Change tax rate")
        print("  4. View global impact")
        print("  5. Quit")
        choice = input("Select an option: ")
        if choice == "1":
            policies.interest_rate = float(input("Enter new interest rate: "))
        elif choice == "2":
            policies.government_spending_pct = float(input("Enter new government spending (% GDP): "))
        elif choice == "3":
            policies.tax_rate = float(input("Enter new tax rate (% GDP): "))
        elif choice == "4":
            global_gdp = simulate_global(policies, years=args.years)
            show_global_map(global_gdp)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
