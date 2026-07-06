import streamlit as st
import pandas as pd

st.title("📈 라인차트 실습")

# 데이터 만들기
df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "판매량": [3, 5, 10, 16, 22, 27]
})

# 데이터 보기
st.subheader("① 데이터")
st.dataframe(df)

# 라인차트 그리기
st.subheader("② 라인차트")
st.line_chart(df.set_index("월"))
import streamlit as st
import pandas as pd

st.title("📈 라인차트 실습")

# 데이터 만들기
df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "판매량": [5, 7, 12, 17, 21, 25]
})

# 데이터 보기
st.subheader("① 데이터")
st.dataframe(df)

# 라인차트 그리기
st.subheader("② 라인차트")
st.line_chart(df.set_index("월"))
