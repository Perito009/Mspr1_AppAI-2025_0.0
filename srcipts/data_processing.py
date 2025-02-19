import pandas as pd


def load_datasets():
    datasets = {
       "df_clean_complete": pd.read_csv(cheamin.csv)
       "df_daily_data": pd.read_csv(cheamin.csv)
       "df_summary_data": pd.read_csv(cheamin.csv)
       "df_wise_latest": pd.read_csv(cheamin.csv)
       "df_full_grouped": pd.read_csv(cheamin.csv)
       "df_worldometer_data": pd.read_csv(cheamin.csv)
       "df_usa_country_wise": pd.read_csv(cheamin.csv)
    }

# Nettoyage des NaN
    cols_zero = ["total_deaths", "total_recovered", "active_cases", "total_deaths_per_1m_population"]
    datasets["df_summary_data"][cols_zero] = datasets["df_summary_data"][cols_zero].fillna(0)

    cols_median = ["serious_or_critical", "total_tests", "total_tests_per_1m_population"]
    datasets["df_summary_data"][cols_median] = datasets["df_summary_data"][cols_median].fillna(datasets["df_summary_data"][cols_median].median())

    # Standardiser les noms des pays
    datasets["df_full_grouped"]["Country/Region"] = datasets["df_full_grouped"]["Country/Region"].str.strip().str.lower()
    datasets["df_summary_data"]["country"] = datasets["df_summary_data"]["country"].str.strip().str.lower()

    # Harmoniser les noms de colonnes pour la fusion
    datasets["df_summary_data"].rename(columns={"country": "Country/Region"}, inplace=True)





return(datasets)




            