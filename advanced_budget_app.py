
import streamlit as st
import pandas as pd

# Initialisation des données mensuelles par défaut
months = [
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
    "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"
]

default_income_data = {month: {"Salaire_1": 0, "Salaire_2": 0, "Misc": 0} for month in months}
default_expenses_data = {month: {"Housing": 0, "Transportation": 0, "Groceries": 0} for month in months}

# Stockage des données
if "income_data" not in st.session_state:
    st.session_state.income_data = default_income_data

if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = default_expenses_data

# Fonction pour afficher et modifier les données d'un mois donné
def display_month_data(month):
    st.subheader(f"Revenus pour {month}")
    income_data = st.session_state.income_data[month]
    for category, value in income_data.items():
        income_data[category] = st.number_input(f"{category}", value=value, key=f"income_{month}_{category}")
    
    st.subheader(f"Dépenses pour {month}")
    expenses_data = st.session_state.expenses_data[month]
    for category, value in expenses_data.items():
        expenses_data[category] = st.number_input(f"{category}", value=value, key=f"expenses_{month}_{category}")
    
    st.success(f"Les données pour {month} ont été mises à jour.")

# Fonction pour afficher le résumé annuel
def display_summary():
    st.title("Résumé annuel")
    income_totals = {month: sum(st.session_state.income_data[month].values()) for month in months}
    expense_totals = {month: sum(st.session_state.expenses_data[month].values()) for month in months}
    savings = {month: income_totals[month] - expense_totals[month] for month in months}
    
    summary_df = pd.DataFrame({
        "Revenus": income_totals,
        "Dépenses": expense_totals,
        "Économies": savings
    })
    
    st.subheader("Tableau des totaux annuels")
    st.dataframe(summary_df)
    
    st.subheader("Graphiques des données annuelles")
    st.bar_chart(summary_df)

# Application principale
st.sidebar.title("Gestion de Budget")
selection = st.sidebar.radio("Navigation", ["Résumé"] + months)

if selection == "Résumé":
    display_summary()
else:
    st.title(f"Gérer le budget pour {selection}")
    display_month_data(selection)
