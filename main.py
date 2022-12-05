import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly



st.title('2022년 10월 서울역 지하철🚉')
st.subheader('시간별 승차 인원\n시간: 04~24시')

df = pd.read_csv('C:/123/Hi/fix.csv')


if st.checkbox('알아보기'):
    df.set_index = df['월']
    selectbox = st.sidebar.selectbox("몇 호선?", ("1호선","4호선","경의선","공항철도"))

    st.subheader('호선별 승차 인원')
    line_data = df.loc[(df['호선명'] == selectbox)]
    line_data = line_data[line_data.columns.difference(['월', '호선명', '승하차'])]
    s_index = line_data.index.tolist()
    st.area_chart(line_data.loc[s_index[0]], use_container_width=True)
    st.bar_chart(line_data.loc[s_index[0]], use_container_width=True)

    st.subheader('비교하기')
    time = df[['호선명','04-05시', '05-06시', '06-07시', '07-08시','08-09시','09-10시','10-11시','11-12시','12-13시','13-14시',
     '14-15시','15-16시','16-17시','17-18시','18-19시','19-20시','20-21시','21-22시','22-23시','23-24시']].transpose()
    time.rename(columns=time.iloc[0], inplace=True)
    time = time.drop(time.index[0])
    st.line_chart(time)
    st.bar_chart(time)

    if st.checkbox('가장 많이 타는 시간:18-19시 비율보기'):
        values = df['18-19시']
        names = df['호선명']
        fig=px.pie(df,
                    values=values,
                    names=names,
                    title = '18-19시'
                    )
        fig.update_traces(
                    textposition = 'inside',
                    textinfo='percent+label'
                    )
        fig.update_layout(
                    title_font_size=20
                    )
        plotly.offline.plot(fig)
