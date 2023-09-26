import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_all_data(selected_courses, selected_years):
    dfs = []
    for course in selected_courses:
        for year in selected_years:
            path = f"./Data/{course}/{year}/data.csv"
            if os.path.exists(path):
                print(f"Loading data from {path}")
                df = pd.read_csv(path)
                df['Course'] = course
                df['Year'] = year
                dfs.append(df)
            else:
                print(f"File not found: {path}")
    return pd.concat(dfs, ignore_index=True) if dfs else None