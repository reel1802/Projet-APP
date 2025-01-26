
import streamlit as st
import pandas as pd

# Initialisation des données mensuelles par défaut
months = [
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
    "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"
]

default_categories_income = ["Salaire_1", "Salaire_2", "Misc"]
default_categories_expenses = ["Housing", "Transportation", "Groceries"]

if "income_data" not in st.session_state:
    st.session_state.income_data = {month: {cat: 0 for cat in default_categories_income} for month in months}
if "expenses_data" not in st.session_state:
    st.session_state.expenses_data = {month: {cat: 0 for cat in default_categories_expenses} for month in months}
if "income_categories" not in st.session_state:
    st.session_state.income_categories = default_categories_income[:]
if "expense_categories" not in st.session_state:
    st.session_state.expense_categories = default_categories_expenses[:]

# Fonction pour gérer l'ajout/suppression des catégories
def manage_categories():
    st.sidebar.subheader("Gérer les catégories")
    # Ajouter une catégorie de revenus
    new_income_category = st.sidebar.text_input("Ajouter une catégorie de revenu")
    if st.sidebar.button("Ajouter revenu"):
        if new_income_category and new_income_category not in st.session_state.income_categories:
            st.session_state.income_categories.append(new_income_category)
            for month in months:
                st.session_state.income_data[month][new_income_category] = 0
            st.sidebar.success(f"Catégorie {new_income_category} ajoutée aux revenus.")

    # Ajouter une catégorie de dépenses
    new_expense_category = st.sidebar.text_input("Ajouter une catégorie de dépense")
    if st.sidebar.button("Ajouter dépense"):
        if new_expense_category and new_expense_category not in st.session_state.expense_categories:
            st.session_state.expense_categories.append(new_expense_category)
            for month in months:
                st.session_state.expenses_data[month][new_expense_category] = 0
            st.sidebar.success(f"Catégorie {new_expense_category} ajoutée aux dépenses.")

    # Supprimer une catégorie
    st.sidebar.subheader("Supprimer une catégorie")
    category_to_remove_income = st.sidebar.selectbox("Revenus", st.session_state.income_categories)
    if st.sidebar.button("Supprimer revenu"):
        st.session_state.income_categories.remove(category_to_remove_income)
        for month in months:
            del st.session_state.income_data[month][category_to_remove_income]
        st.sidebar.warning(f"Catégorie {category_to_remove_income} supprimée des revenus.")

    category_to_remove_expense = st.sidebar.selectbox("Dépenses", st.session_state.expense_categories)
    if st.sidebar.button("Supprimer dépense"):
        st.session_state.expense_categories.remove(category_to_remove_expense)
        for month in months:
            del st.session_state.expenses_data[month][category_to_remove_expense]
        st.sidebar.warning(f"Catégorie {category_to_remove_expense} supprimée des dépenses.")

# Fonction pour afficher et modifier les données d'un mois donné
def display_month_data(month, week):
    st.subheader(f"Données pour {month}, Semaine {week}")
    if week == 1:
        income_data = {k: v / 2 for k, v in st.session_state.income_data[month].items()}
        expense_data = {k: v / 2 for k, v in st.session_state.expenses_data[month].items()}
    else:
        income_data = {k: v / 2 for k, v in st.session_state.income_data[month].items()}
        expense_data = {k: v / 2 for k, v in st.session_state.expenses_data[month].items()}

    st.subheader("Revenus")
    for category, value in income_data.items():
        st.session_state.income_data[month][category] = st.number_input(
            f"{category} (Semaine {week})", value=value, key=f"income_{month}_{week}_{category}"
        )

    st.subheader("Dépenses")
    for category, value in expense_data.items():
        st.session_state.expenses_data[month][category] = st.number_input(
            f"{category} (Semaine {week})", value=value, key=f"expense_{month}_{week}_{category}"
        )

# Fonction pour afficher le résumé bihebdomadaire
def display_biweekly_summary(month):
    income_total = sum(st.session_state.income_data[month].values())
    expense_total = sum(st.session_state.expenses_data[month].values())
    savings = income_total - expense_total

    st.sidebar.subheader(f"Résumé pour {month}")
    st.sidebar.metric("Total Revenus (CAD)", f"${income_total:.2f}")
    st.sidebar.metric("Total Dépenses (CAD)", f"${expense_total:.2f}")
    st.sidebar.metric("Économies (CAD)", f"${savings:.2f}")

# Application principale
st.sidebar.title("Gestion de Budget")
selection = st.sidebar.radio("Navigation", ["Gérer les catégories"] + months)

if selection == "Gérer les catégories":
    manage_categories()
else:
    st.title(f"Budget pour {selection}")
    week = st.radio("Semaine", [1, 2], horizontal=True)
    display_month_data(selection, week)
    display_biweekly_summary(selection)
