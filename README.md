# UK Government Debt, Bond Markets and Wealth Transfer: An Agent-Based Simulation

## Overview

This project presents an Agent-Based Simulation (ABM) developed to model the relationships between UK Government Debt, Government Bond Markets, Banks, Investors, and Households. The system integrates historical economic data, Monte Carlo Simulation, and Network Analysis to analyse debt dynamics and wealth transfer within the UK economy.

The application has been developed using Python and Flask as part of an MSc dissertation project.

---

# Project Objectives

The main objectives of this project are:

- Analyse historical UK Government Debt data.
- Investigate Government Bond Market behaviour.
- Model interactions between Government, Banks, Investors and Households.
- Simulate debt accumulation and wealth transfer using Agent-Based Modelling.
- Evaluate uncertainty through Monte Carlo Simulation.
- Visualise economic relationships using Network Analysis.

---

# Features

The web application consists of six main modules:

## Home Dashboard

- Project overview
- Navigation dashboard
- Quick access to all modules

---

## Data Analysis

- Historical dataset exploration
- Government Borrowing analysis
- Bond Yield analysis
- GDP analysis
- Inflation analysis
- Unemployment analysis
- Correlation Matrix
- Distribution plots
- Boxplots

---

## Agent-Based Simulation

Users can customise:

- Initial Government Debt
- Bond Issue Amount
- Interest Rate
- Simulation Steps
- Number of Banks
- Number of Investors
- Number of Households

Simulation outputs include:

- Government Debt
- Bond Yield
- Household Wealth
- Investor Wealth
- Bank Capital

---

## Monte Carlo Simulation

- Multiple simulation runs
- Summary statistics
- Distribution analysis
- Histogram
- Boxplot

---

## Network Analysis

Visualises interactions between:

- Government
- Banks
- Investors
- Households

Includes:

- Network Graph
- Centrality Analysis

---

## About

Provides background information regarding:

- UK Government Debt
- Government Bonds
- Wealth Transfer
- Agent-Based Modelling
- Monte Carlo Simulation
- Network Analysis

---

# Project Structure

```
UK_Debt_ABM/
│
├── app.py
├── simulation.py
├── montecarlo.py
├── network.py
├── master_dataset.csv
├── simulation_results.csv
├── MonteCarlo_Summary.csv
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── analysis.html
│   ├── simulation.html
│   ├── montecarlo.html
│   ├── network.html
│   └── about.html
│
├── static/
│   ├── css/
│   │     └── style.css
│   ├── charts/
│   └── network/
│
└── README.md
```

---

# Technologies Used

## Backend

- Python
- Flask

## Data Processing

- Pandas
- NumPy

## Agent-Based Modelling

- Mesa

## Network Analysis

- NetworkX

## Data Visualisation

- Matplotlib

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

---

# Installation

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install required packages

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# Simulation Workflow

```
Historical Data

        │

        ▼

Data Cleaning

        │

        ▼

Exploratory Data Analysis

        │

        ▼

Agent-Based Simulation

        │

        ▼

Monte Carlo Simulation

        │

        ▼

Network Analysis

        │

        ▼

Simulation Results
```

---

# Datasets

The project uses historical UK economic data from publicly available sources.

The combined master dataset includes:

- Government Borrowing
- Government Bond Yield
- Gross Domestic Product (GDP)
- Inflation
- Population
- Unemployment

---

# Outputs

The application generates:

- Historical Charts
- Simulation Results
- Monte Carlo Results
- Summary Statistics
- Network Graphs

---

# Future Improvements

Potential future enhancements include:

- Interactive dashboards
- Real-time UK economic data
- Policy scenario modelling
- Machine Learning prediction models
- Interactive Network Analysis
- Export simulation reports

---

# Author

MSc Dissertation Project

Topic:

**Modelling UK Government Debt, Bond Markets and Wealth Transfer: An Agent-Based Simulation**

---

# License

This project is intended for educational and research purposes.
