import streamlit as st

from ui import eda
from ui import home
from ui import ml

def main() :
    st.title("자동차 가격 예측 앱")
    
    menu = ["Home", "EDA", "ML"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == menu[0] :
        home.run_home()
    elif choice == menu[1] :
        eda.run_eda()
    elif choice == menu[2] :
        ml.run_ml()

if __name__ == "__main__" :
    main()