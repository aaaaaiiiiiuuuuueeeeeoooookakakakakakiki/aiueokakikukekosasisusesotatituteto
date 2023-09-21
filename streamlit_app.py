import streamlit as sｔ

st.title('おみくじ')

user_input = st.text_input('あいうえお')


if st.button('おみくじを引く'):
    sesults=["大吉","中吉","小吉","吉","凶","大凶"]
    result=random.choice(results)

st.write