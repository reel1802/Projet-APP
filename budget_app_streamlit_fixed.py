
import streamlit as st
import pandas as pd

# Initialisation des données
# Données des revenus
income_data = pd.DataFrame({
    "Category": ["Salaire_1", "Salaire_2", "Misc", "Total"],
    "JAN": [0, 0, 0, 0],
    "FEB": [0, 0, 0, 0],
    "MAR": [2500, 0, 0, 2500],
    "APR": [2500, 1200, 0, 3700],
    "MAY": [2500, 1200, 0, 3700],
    "JUN": [2500, 1200, 0, 3700],
    "JUL": [2500, 0, 0, 2500],
    "AUG": [2500, 0, 0, 2500],
    "SEPT": [2500, 0, 0, 2500],
    "OCT": [2500, 0, 0, 2500],
    "NOV": [2500, 0, 0, 2500],
    "DEC": [2500, 0, 0, 2500]
})

# Données des dépenses
expenses_data = pd.DataFrame({
    "Category": ["Housing", "Transportation", "Groceries", "Total"],
    "JAN": [0, 0, 0, 0],
    "FEB": [0, 0, 0, 0],
    "MAR": [2500, 0, 0, 2500],
    "APR": [3700, 0, 0, 3700],
    "MAY": [3700, 0, 0, 3700],
    "JUN": [3700, 0, 0, 3700],
    "JUL": [2500, 0, 0, 2500],
    "AUG": [2500, 0, 0, 2500],
    "SEPT": [2500, 0, 0, 2500],
    "OCT": [2500, 0, 0, 2500],
    "NOV": [2500, 0, 0, 2500],
    "DEC": [2500, 0, 0, 2500]
})

# Fonction pour calculer les économies potentielles
def calculate_savings(income, expenses):
    savings = income.iloc[:-1, 1:].sum().sum() - expenses.iloc[:-1, 1:].sum().sum()
    return savings

# Titre de l'application
st.title("Gestion de Budget Personnel")

# Section pour afficher les revenus (tableau non éditable pour éviter les erreurs)
st.header("Revenus")
st.dataframe(income_data)

# Section pour afficher les dépenses (tableau non éditable pour éviter les erreurs)
st.header("Dépenses")
st.dataframe(expenses_data)

# Résumé des économies potentielles
st.header("Résumé")
savings = calculate_savings(income_data, expenses_data)
st.subheader(f"Économies potentielles: {savings:.2f} €")

# Graphiques interactifs
st.header("Visualisations")
chart_data = pd.DataFrame({
    "Revenus": income_data.iloc[:-1, 1:].sum(axis=0),
    "Dépenses": expenses_data.iloc[:-1, 1:].sum(axis=0)
}, index=income_data.columns[1:])
st.line_chart(chart_data)
