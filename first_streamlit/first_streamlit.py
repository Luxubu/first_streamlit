import streamlit as st
from numpy import random
import pandas as pd

st.write("Get your lucky number")


def get_random_number(beginNumber, endNumber, sizeNumber) -> random:
    rn = random.randint(beginNumber, endNumber, sizeNumber)
    return rn

def get_power_ball():
    fiveNum = get_random_number(1,69,5)
    powerBall = get_random_number(1,27,1)

    columns = ['num1', 'num2','num3','num4','num5']
    df = pd.DataFrame(fiveNum.reshape(-1,len(fiveNum)), columns=columns)
    df.insert(5, "Powerball", powerBall, True)
    st.dataframe(df,hide_index=True)

if st.button("Generate PowerBall"):
    get_power_ball()

