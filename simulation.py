# ==========================================
# IMPORT LIBRARIES
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mesa import Model
from mesa.agent import Agent
from mesa.datacollection import DataCollector

# ==========================================
# GOVERNMENT AGENT
# ==========================================

class GovernmentAgent(Agent):

    def __init__(

        self,

        model,

        initial_debt,

        bond_yield,

        bond_issue

    ):

        super().__init__(model)

        self.debt = initial_debt

        self.bond_yield = bond_yield

        self.bond_issue = bond_issue

        self.total_interest_paid = 0


    def issue_bonds(

        self,

        amount

    ):

        self.debt += amount


    def pay_interest(

        self

    ):

        interest = self.debt * (

            self.bond_yield / 100

        )

        self.total_interest_paid += interest

        return interest


    def update_bond_yield(

        self,

        inflation

    ):

        self.bond_yield += (

            0.02 * inflation

        )

        self.bond_yield = max(

            0.5,

            min(

                self.bond_yield,

                15

            )

        )
# ==========================================
# BANK AGENT
# ==========================================

class BankAgent(Agent):

    def __init__(

        self,

        model,

        capital=1000000

    ):

        super().__init__(model)

        self.capital = capital

        self.bonds = 0


    def buy_bonds(

        self,

        government,

        amount

    ):

        amount = min(

            amount,

            self.capital

        )

        self.capital -= amount

        self.bonds += amount

        government.issue_bonds(amount)


    def receive_interest(

        self,

        government

    ):

        interest = self.bonds * (

            government.bond_yield / 100

        )

        self.capital += interest


# ==========================================
# INVESTOR AGENT
# ==========================================

class InvestorAgent(Agent):

    def __init__(

        self,

        model,

        wealth=500000

    ):

        super().__init__(model)

        self.wealth = wealth

        self.bonds = 0


    def buy_bonds(

        self,

        government,

        amount

    ):

        amount = min(

            amount,

            self.wealth

        )

        self.wealth -= amount

        self.bonds += amount

        government.issue_bonds(amount)


    def receive_interest(

        self,

        government

    ):

        interest = self.bonds * (

            government.bond_yield / 100

        )

        self.wealth += interest


    def sell_bonds(

        self,

        amount

    ):

        amount = min(

            amount,

            self.bonds

        )

        self.bonds -= amount

        self.wealth += amount


# ==========================================
# HOUSEHOLD AGENT
# ==========================================

class HouseholdAgent(Agent):

    def __init__(

        self,

        model,

        wealth=100000

    ):

        super().__init__(model)

        self.wealth = wealth

        self.income = 30000

        self.consumption = 0


    def receive_income(self):

        self.wealth += self.income


    def consume(self):

        self.consumption = self.wealth * 0.20

        self.wealth -= self.consumption


    def receive_interest(

        self,

        amount

    ):

        self.wealth += amount

# ==========================================
# UK DEBT MODEL
# ==========================================

class UKDebtModel(Model):

    def __init__(

    self,

    initial_debt,

    bond_yield,

    bond_issue,

    num_banks,

    num_investors,

    num_households
    ):

        super().__init__()

        self.running = True

        # -------------------------------
        # Government
        # -------------------------------

        self.government = GovernmentAgent(

           self,

           initial_debt,

           bond_yield,

          bond_issue

          )
        # -------------------------------
        # Banks
        # -------------------------------

        self.banks = [

            BankAgent(self)

            for _ in range(num_banks)

        ]

        # -------------------------------
        # Investors
        # -------------------------------

        self.investors = [

            InvestorAgent(self)

            for _ in range(num_investors)

        ]

        # -------------------------------
        # Households
        # -------------------------------

        self.households = [

            HouseholdAgent(self)

            for _ in range(num_households)

        ]

        # -------------------------------
        # Data Collector
        # -------------------------------

        self.datacollector = DataCollector(

            model_reporters={

                "Government Debt":

                    lambda m: m.government.debt,

                "Bond Yield":

                    lambda m: m.government.bond_yield,

                "Average Bank Capital":

                    lambda m: np.mean(

                        [b.capital for b in m.banks]

                    ),

                "Average Investor Wealth":

                    lambda m: np.mean(

                        [i.wealth for i in m.investors]

                    ),

                "Average Household Wealth":

                    lambda m: np.mean(

                        [h.wealth for h in m.households]

                    )

            }

        )
            # ==========================================
    # ONE SIMULATION STEP
    # ==========================================

    def step(self):

        # --------------------------------------
        # Government issues new bonds
        # --------------------------------------

        self.government.issue_bonds(

           self.government.bond_issue

          )

        # --------------------------------------
        # Banks buy government bonds
        # --------------------------------------

        for bank in self.banks:

            bank.buy_bonds(

                self.government,

                np.random.randint(

                    500,

                    3000

                )

            )

        # --------------------------------------
        # Investors buy government bonds
        # --------------------------------------

        for investor in self.investors:

            investor.buy_bonds(

                self.government,

                np.random.randint(

                    200,

                    1500

                )

            )

        # --------------------------------------
        # Government pays interest
        # --------------------------------------

        self.government.pay_interest()

        # --------------------------------------
        # Banks receive interest
        # --------------------------------------

        for bank in self.banks:

            bank.receive_interest(

                self.government

            )

        # --------------------------------------
        # Investors receive interest
        # --------------------------------------

        for investor in self.investors:

            investor.receive_interest(

                self.government

            )

        # --------------------------------------
        # Households receive income
        # --------------------------------------

        for household in self.households:

            household.receive_income()

            household.consume()

        # --------------------------------------
        # Update Bond Yield
        # --------------------------------------

        inflation = np.random.uniform(

            1,

            5

        )

        self.government.update_bond_yield(

            inflation

        )

        # --------------------------------------
        # Store results
        # --------------------------------------

        self.datacollector.collect(

            self
        )

# ==========================================
# RUN SIMULATION FUNCTION
# ==========================================

def run_simulation(

    government_debt,

    bond_yield,

    bond_issue,

    simulation_steps,

    number_banks,

    number_investors,

    number_households

):

    # --------------------------------------
    # Create Model
    # --------------------------------------

    model = UKDebtModel(

    initial_debt=government_debt,

    bond_yield=bond_yield,

    bond_issue=bond_issue,

    num_banks=number_banks,

    num_investors=number_investors,

    num_households=number_households

      )

    # --------------------------------------
    # Run Simulation
    # --------------------------------------

    for _ in range(simulation_steps):

        model.step()

    # --------------------------------------
    # Get Results
    # --------------------------------------

    results = model.datacollector.get_model_vars_dataframe()

    # --------------------------------------
    # Save Results
    # --------------------------------------

    results.to_csv(

        "simulation_results.csv",

        index=False

    )

    # --------------------------------------
    # Final Values
    # --------------------------------------

    final = results.iloc[-1]

    return {

        "Government Debt":

            float(final["Government Debt"]),

        "Bond Yield":

            float(final["Bond Yield"]),

        "Bank Capital":

            float(final["Average Bank Capital"]),

        "Investor Wealth":

            float(final["Average Investor Wealth"]),

        "Household Wealth":

            float(final["Average Household Wealth"])

    }