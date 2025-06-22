"""Command-line interface for the economic policy simulator."""

import argparse
from .simulation import PolicyInputs, simulate_economy


def main():
    parser = argparse.ArgumentParser(description="Run a simple economic policy simulation")
    parser.add_argument("initial_gdp", type=float, help="Initial GDP value")
    parser.add_argument("--interest-rate", type=float, default=0.05, help="Interest rate (as decimal)")
    parser.add_argument(
        "--gov-spending", type=float, default=0.2, help="Government spending as percentage of GDP"
    )
    parser.add_argument("--tax-rate", type=float, default=0.2, help="Tax rate as percentage of GDP")
    parser.add_argument("--years", type=int, default=1, help="Number of years to simulate")
    args = parser.parse_args()

    policies = PolicyInputs(
        interest_rate=args.interest_rate,
        government_spending_pct=args.gov_spending,
        tax_rate=args.tax_rate,
    )

    result = simulate_economy(args.initial_gdp, policies, years=args.years)

    for year, gdp in enumerate(result.gdp_history):
        if year == 0:
            print(f"Year {year}: starting GDP = {gdp:.2f}")
        else:
            print(f"Year {year}: predicted GDP = {gdp:.2f}")


if __name__ == "__main__":
    main()
