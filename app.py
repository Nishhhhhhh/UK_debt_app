from flask import Flask, render_template, request
import pandas as pd
from simulation import run_simulation
from montecarlo import run_monte_carlo
from network import create_network

app = Flask(__name__)

# ==========================================
# LOAD DATASETS
# ==========================================

master = pd.read_csv("master_dataset.csv")
simulation = pd.read_csv("simulation_results.csv")
summary = pd.read_csv("MonteCarlo_Summary.csv")


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    latest = master.iloc[-1]

    return render_template(

        "index.html",

        debt=latest["Government_Borrowing"],

        bond=latest["Bond_Yield"],

        gdp=latest["GDP"],

        inflation=latest["Inflation"],

        unemployment=latest["Unemployment"],

        population=latest["Population"]

    )


# ==========================================
# DATA ANALYSIS
# ==========================================

@app.route("/analysis")
def analysis():

    return render_template(

        "analysis.html",

        tables=[

            master.head(20).to_html(

                classes="table table-striped table-bordered",

                index=False

            )

        ]

    )


# ==========================================
# AGENT-BASED SIMULATION
# ==========================================

@app.route("/simulation", methods=["GET", "POST"])
def simulation_page():

    results = None

    if request.method == "POST":

        government_debt = float(request.form["government_debt"])
        bond_issue = float(request.form["bond_issue"])
        interest_rate = float(request.form["interest_rate"])
        simulation_steps = int(request.form["steps"])
        number_banks = int(request.form["banks"])
        number_investors = int(request.form["investors"])
        number_households = int(request.form["households"])

        # ===== DEBUG =====
        print("Government Debt:", government_debt)
        print("Bond Issue:", bond_issue)
        print("Interest Rate:", interest_rate)
        print("Simulation Steps:", simulation_steps)
        print("Banks:", number_banks)
        print("Investors:", number_investors)
        print("Households:", number_households)
        # =================

        results = run_simulation(
            government_debt=government_debt,
            bond_yield=interest_rate,
            bond_issue=bond_issue,
            simulation_steps=simulation_steps,
            number_banks=number_banks,
            number_investors=number_investors,
            number_households=number_households
        )

    return render_template(
        "simulation.html",
        results=results
    )


# ==========================================
# MONTE CARLO SIMULATION
# ==========================================

@app.route("/montecarlo", methods=["GET", "POST"])
def montecarlo():

    table = None

    summary = None

    chart = False

    if request.method == "POST":

        iterations = int(

            request.form["iterations"]

        )

        results, stats = run_monte_carlo(

            iterations=iterations

        )

        table = results.to_html(

            classes="table table-striped table-bordered",

            index=False

        )

        summary = stats.to_html(

            classes="table table-bordered"

        )

        chart = True

    return render_template(

        "montecarlo.html",

        table=table,

        summary=summary,

        chart=chart

    )

# ==========================================
# NETWORK ANALYSIS
# ==========================================

@app.route("/network")
def network():

    create_network()

    return render_template(

        "network.html"

    )

# ==========================================
# ABOUT
# ==========================================

@app.route("/about")
def about():

    return render_template(

        "about.html"

    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True

    )