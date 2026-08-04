# ==========================================
# IMPORT LIBRARIES
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from simulation import run_simulation


# ==========================================
# MONTE CARLO FUNCTION
# ==========================================

def run_monte_carlo(

    iterations,

    government_debt=100000000,

    bond_yield=4,

    bond_issue=10000,

    simulation_steps=100,

    number_banks=5,

    number_investors=20,

    number_households=100

):

    results = []

    # --------------------------------------
    # RUN MANY SIMULATIONS
    # --------------------------------------

    for i in range(iterations):

        debt = government_debt * np.random.uniform(0.95, 1.05)

        rate = bond_yield * np.random.uniform(0.90, 1.10)

        issue = bond_issue * np.random.uniform(0.80, 1.20)

        output = run_simulation(

            government_debt=debt,

            bond_yield=rate,

            bond_issue=issue,

            simulation_steps=simulation_steps,

            number_banks=number_banks,

            number_investors=number_investors,

            number_households=number_households

        )

        results.append(output)

    # --------------------------------------
    # CREATE DATAFRAME
    # --------------------------------------

    df = pd.DataFrame(results)

    # --------------------------------------
    # SAVE RESULTS
    # --------------------------------------

    df.to_csv(

        "MonteCarlo_Results.csv",

        index=False

    )

    summary = df.describe()

    summary.to_csv(

        "MonteCarlo_Summary.csv"

    )

    # --------------------------------------
    # HISTOGRAM
    # --------------------------------------

    plt.figure(figsize=(8,5))

    plt.hist(

        df["Government Debt"],

        bins=20,

        edgecolor="black"

    )

    plt.title("Government Debt Distribution")

    plt.xlabel("Government Debt")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(

        "static/charts/montecarlo_debt.png"

    )

    plt.close()

    # --------------------------------------
    # BOXPLOT
    # --------------------------------------

    plt.figure(figsize=(10,6))

    df.boxplot()

    plt.tight_layout()

    plt.savefig(

        "static/charts/montecarlo_boxplot.png"

    )

    plt.close()

    return df, summary