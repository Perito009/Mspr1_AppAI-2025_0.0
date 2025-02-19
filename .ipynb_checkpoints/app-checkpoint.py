import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import missingno as mno
import seaborn as sns
from scripts.data_processing import load_datasets
from scripts.visualization import plot_missing_values, plot_missing_heatmap

# Charger les datasets
datasets = load_datasets()
df_clean_complete = datasets["df_clean_complete"]
df_daily_data = datasets["df_daily_data"]
df_summary_data = datasets["df_summary_data"]
df_wise_latest = datasets["df_wise_latest"]
df_full_grouped = datasets["df_full_grouped"]
df_worldometer_data = datasets["df_worldometer_data"]
df_usa_county_wise = datasets["df_usa_county_wise"]

def main():
    st.title("Analyse des Données Covid-19")

    st.subheader("Aperçu des datasets")
    for name, df in datasets.items():
        st.write(f"**{name.replace('_', ' ').title()}**")
        st.write(df.head())

    st.subheader("Valeurs manquantes dans Summary Data après nettoyage")
    st.write(df_summary_data.isna().sum())

    st.subheader("Valeurs manquantes dans Full Grouped Data")
    st.write(df_full_grouped.isna().sum())

    # Upload d'un fichier CSV pour analyse
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :")
        st.write(df.head())

        # Visualisation des valeurs manquantes
        st.subheader("Visualisation des valeurs manquantes")
        st.pyplot(plot_missing_values(df))

        st.subheader("Heatmap des valeurs manquantes")
        st.pyplot(plot_missing_heatmap(df))

if __name__ == "__main__":
    main()
