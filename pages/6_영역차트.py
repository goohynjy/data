import streamlit as st
import pandas as pd

st.title("📈 영역 그래프 실습")

df = pd.DataFrame({
    "월": ["1월","2월","3월","4월","5월","6월"],
    "사용량": [3,5,10,16,22,27]
})

st.subheader("데이터")
st.dataframe(df)

st.subheader("영역 그래프")
st.area_chart(df.set_index("월"))
