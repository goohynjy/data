import streamlit as st
import pandas as pd

st.title("📏 키와 몸무게")

df = pd.DataFrame({
    "키": [150,155,160,165,170,175,180,185],
    "몸무게": [45,50,54,58,65,70,76,82]
})

st.dataframe(df)

st.scatter_chart(df, x="키", y="몸무게")
