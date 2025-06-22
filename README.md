# EconomicPolicySimulator

A simple Python simulator to estimate the economic returns of social, fiscal and monetary policies.

## Features
- Basic model of GDP growth influenced by interest rates, government spending and taxes.
- Command line interface for running simulations over multiple years.
- Interactive map showing projected GDP for each U.S. state with a menu to adjust policies. The menu also includes an option to view the global impact of current settings across more than 170 countries.
- Simulations now begin on **January 1, 2025**, with missing data extrapolated from post-COVID trends.

## Usage

Install dependencies (plotly is required for the map interface) and run the CLI:

```bash
pip install plotly
python -m econ_simulator.cli 1000 --interest-rate 0.05 --gov-spending 0.2 --tax-rate 0.2 --years 3
```

This command simulates an economy starting with a GDP of 1000 units for three years.

### Map Interface

Launch the interactive map with:

```bash
python -m econ_simulator.gui --interest-rate 0.05 --gov-spending 0.2 --tax-rate 0.2 --years 1
```

A map of the United States will open in your browser. Hover over any state to see its projected GDP. Use the on-screen menu in the terminal to change policy parameters and refresh the map. You can also select the global impact option to view projected GDP for over 170 countries.
