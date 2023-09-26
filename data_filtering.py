import pandas as pd
import streamlit as st
from pandas.api.types import (
    is_object_dtype,
    is_numeric_dtype,
    is_categorical_dtype,
    is_datetime64_any_dtype,
)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    ...rest of the code...