import streamlit as st

st.header('다중선택')

options = st.multiselect(
     '가장 좋아하는 색상은 무엇인가요',
     ['초록', '노랑', '빨강', '파랑'],
     ['노랑', '빨강'])

st.write('당신이 선택한 색상:', options)
#위에 이어서 붙여넣기 하기
st.header('체크박스')

st.write ('주문하고 싶은 것이 무엇인가요?')

icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')

if icecream:
     st.write("좋아요! 여기 더 많은 🍦")

if coffee: 
     st.write("알겠습니다, 여기 커피 있어요 ☕")

if cola:
     st.write("여기 있어요 🥤")
