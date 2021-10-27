import pandas as pd

import altair as alt
import streamlit as st

df = pd.DataFrame(
    [
        {"topic": "Basic Python", "votes": 22, "cat": "Programming"},
        {
            "topic": "Developing and using functions and modules in Python",
            "votes": 26,
            "cat": "Programming",
        },
        {
            "topic": "Version control (i.e. Git)",
            "votes": 24,
            "cat": "Reproducibility & Collaboration",
        },
        {"topic": "Xarray usage", "votes": 20, "cat": "Programming"},
        {"topic": "Parallel processing in Python", "votes": 14, "cat": "Programming"},
        {
            "topic": "Plotting 2D and 3D, graphics and animations",
            "votes": 15,
            "cat": "Visualisation",
        },
        {
            "topic": "Using Docker",
            "votes": 12,
            "cat": "Reproducibility & Collaboration",
        },
        {
            "topic": "Testing Code",
            "votes": 8,
            "cat": "Reproducibility & Collaboration",
        },
        {"topic": "Numpy and Pandas", "votes": 10, "cat": "Programming"},
        {
            "topic": "Creating and managing environments",
            "votes": 11,
            "cat": "Reproducibility & Collaboration",
        },
        {"topic": "Jupyter notebooks", "votes": 7, "cat": "Visualisation"},
        {
            "topic": "Project directory structure",
            "votes": 6,
            "cat": "Reproducibility & Collaboration",
        },
        {"topic": "Explore scikit-learn tools", "votes": 1, "cat": "Analysis"},
    ]
)
fs = 18
rawResults = (
    (
        alt.Chart(df, title="Survey results", width=1200, height=600)
        .mark_bar()
        .encode(
            y=alt.Y("topic", sort="-x", title="Topic"),
            x=alt.X("votes:Q", title="Number of votes"),
            color=alt.Color("cat:N", title="Category"),
        )
    )
    .configure_axis(labelLimit=0, labelFontSize=fs - 4, titleFontSize=fs)
    .configure_title(fontSize=fs)
)

st.write(rawResults)

df = pd.DataFrame(
    [
        {"topic": "Basic Python", "votes": 19},
        {"topic": "Developing and using functions and modules in Python", "votes": 19},
        {"topic": "Version control (i.e. Git)", "votes": 17},
        {"topic": "Xarray usage", "votes": 16},
        {"topic": "Parallel processing in Python", "votes": 12},
        {"topic": "2D and 3D plotting, graphics and animations", "votes": 11},
        {"topic": "Using Docker", "votes": 11},
        {"topic": "Testing Code", "votes": 11},
        {"topic": "Numpy and Pandas", "votes": 11},
        {"topic": "Creating and managing environments", "votes": 11},
        {"topic": "Jupyter notebooks", "votes": 11},
        {"topic": "Project directory structure", "votes": 11},
        {"topic": "Explore scikit-learn tools", "votes": 11},
    ]
)
