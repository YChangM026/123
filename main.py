from datetime import datetime
import streamlit as st
import numpy as np
import pandas as pd

st.title("Diploma PDF Generator")
st.write('# Web test :sunglasses:')

date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.write(date)

grade = st.slider("Grade", 1, 100, 60)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

