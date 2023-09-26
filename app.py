import streamlit as st
import plotly.graph_objects as go

from data_loading import load_all_data
from data_filtering import filter_dataframe
from plotting import generate_plot

st.set_page_config(
    page_title="DataTalksClub", page_icon=":cookie:", initial_sidebar_state="expanded"
)

@st.cache_data
def load_data(selected_courses, selected_years):
    return load_all_data(selected_courses, selected_years)

def filter_dataframe(df):
    return filter_dataframe(df)

if __name__ == "__main__":
    st.title(
        'Interactive [DataTalksClub](https://github.com/DataTalksClub) Course Projects Dashboard'
    )

    course_options = ['dezoomcamp', 'mlopszoomcamp', 'mlzoomcamp']
    year_options = ['2021', '2022', '2023']

    selected_courses = st.multiselect(
        'Select course(s):', course_options, default=course_options
    )

    selected_years = st.multiselect('Select year(s):', year_options, default=year_options)

    if selected_courses and selected_years:
        data = load_data(selected_courses, selected_years)
        if data is not None:
            data = filter_dataframe(data)
            generate_plot(data)
        else:
            st.write("No data loaded.")
    else:
        st.write("Please select at least one course and one year to load data.")

    st.sidebar.write("Help Keep This Service Running")
    st.sidebar.markdown(
        "<a href='https://www.paypal.com/donate/?hosted_button_id=LR3PQYHZY4CJ4'><img src='https://www.paypalobjects.com/digitalassets/c/website/marketing/apac/C2/logos-buttons/optimize/26_Yellow_PayPal_Pill_Button.png' width='128'></a>",
        unsafe_allow_html=True,
    )

    st.sidebar.write("Connect with me")
    st.sidebar.markdown(
        "<a href='https://www.linkedin.com/in/zacharenakis'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='32'></a>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        "<a href='https://zacharenakis.super.site'><img src='https://img.icons8.com/external-vectorslab-flat-vectorslab/53/null/external-Favorite-Website-web-and-marketing-vectorslab-flat-vectorslab.png' width='32'></a>",
        unsafe_allow_html=True,
    )