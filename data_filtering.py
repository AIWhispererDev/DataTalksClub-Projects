import pandas as pd
import streamlit as st
from pandas.api.types import (
    is_object_dtype,
    is_numeric_dtype,
    is_categorical_dtype,
    is_datetime64_any_dtype,
)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    filter_container = st.container()

    with filter_container:
        available_columns = [col for col in df.columns if col not in ['Course', 'Year']]
        to_filter_columns = st.multiselect(
            "Select columns to filter", available_columns, default=available_columns
        )
        col1, col2 = st.columns(2)

        hide_unknowns = col1.checkbox("Hide Unknown Titles", value=True)
        show_only_unknowns = col2.checkbox("Show only Unknown Titles")

        if hide_unknowns and show_only_unknowns:
            st.warning("You cannot select both options at the same time.")
            df_filtered = df.copy()
        elif hide_unknowns:
            df_filtered = df[df['project_title'] != 'Unknown']
        elif show_only_unknowns:
            df_filtered = df[df['project_title'] == 'Unknown']
        else:
            df_filtered = df.copy()

        for column in to_filter_columns:
            try:
                _ = {x for x in df[column]}
            except TypeError:
                continue

            left, right = st.columns((1, 20))
            left.write("↳")
            if (
                is_categorical_dtype(df_filtered[column])
                or df_filtered[column].nunique() < 10
            ):
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df_filtered[column].unique(),
                    default=list(df_filtered[column].unique()),
                )
                df_filtered = df_filtered[df_filtered[column].isin(user_cat_input)]
            elif is_numeric_dtype(df_filtered[column]):
                _min = float(df_filtered[column].min())
                _max = float(df_filtered[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df_filtered = df_filtered[df_filtered[column].between(*user_num_input)]
            else:
                user_text_input = right.text_input(f"Substring or regex in {column}")
                case_sensitive = right.checkbox(
                    'Case Sensitive', value=False, key=f"case_sensitive_{column}"
                )

                if user_text_input:
                    mask = df_filtered[column].str.contains(
                        user_text_input, case=case_sensitive, na=False
                    )
                    df_filtered = df_filtered[mask]

    return df_filtered