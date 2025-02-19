import matplotlib.pyplot as plt
import seaborn as sns
import missingno as mno


def plot_missing_values (df):
    fig, ax = plt.subplots()
    mno.bar(df, ax=ax)
    return fig

def plot_missing_heatmap (df):
    fig, ax = plt.subplots()
    sns.heatmap(df.insull(), cbar=False, cmap='Viridis')
    return fig

