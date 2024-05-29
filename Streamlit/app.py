import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import base64

from sklearn.datasets import load_iris
from PIL import Image

# df = pd.read_csv(r'C:\Users\USER\Desktop\Workspace\streamlit\streamlit-tutorial-main\streamlit-tutorial-main\car.csv')
# df.set_index('model')
# df.style.hide()

# print(df.head())
# with open(r"C:\Users\USER\Desktop\FFA500.png", "rb") as file:
#     encoded_string = base64.b64encode(file.read()).decode()
# background_css = f"""
# <style>
# body {{
#     background-image: url("data:image/png;base64,{encoded_string}");
#     background-size: cover;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }}
# </style>
# """
# st.markdown(background_css, unsafe_allow_html=True)
st.set_page_config(layout="wide")
img = Image.open(r"C:\Users\USER\Desktop\pngegg.png")
st.image(img)
st.title("전기차 종합 DB 조회 포털:mag:")
# 터미널에서 streatmlit run <.py 파일명> 으로 실행.

# 탭 생성: 첫 번째 탭의 이름은 Tab A로, Tab B로 표시.
tab1, tab2, tab3 = st.tabs(
    ["차량 정보 조회", "전기차 등록 대수 현황", "업체 별 전기차 충전 요금"]
)

with tab1:
    st.sidebar.title("Filter")
    select_multi = st.sidebar.multiselect(
        "확인하고자 하는 차량 정보을 선택해주세요.",
        [
            "모델",
            "요약",
            "주행가능거리(km)",
            "충전시간(분)",
            "출력",
            "전장",
            "전폭",
            "전고",
            "축거",
        ],
    )
    # tab A를 누르면 표시될 내용
    st.header("전체 데이터 예시")
    # car.csv를 데이터프레임으로 가져와서 표로 표시해주기
    df_A = pd.read_csv(
        r"C:\Users\USER\Desktop\Workspace\streamlit\streamlit-tutorial-main\streamlit-tutorial-main\car.csv"
    )
    tmp_df_A = df_A
    st.table(tmp_df_A.head(5))

    start_button = st.sidebar.button("차량 정보 조회")
    if start_button:
        st.header("조회된 차량 정보")
        selected_df_A = df_A[select_multi]
        df_A.set_index(select_multi)
        # df.style.hide()
        st.table(selected_df_A)
        st.sidebar.success("차량 정보 조회 탭을 확인해주세요.")

with tab2:
    st.header("지역별 전기차 등록 대수 현황")
    # tab B를 누르면 표시될 내용
    select_region = st.sidebar.selectbox(
        "확인하고 싶은 지역을 선택하세요",
        [
            "서울",
            "부산",
            "대구",
            "인천",
            "광주",
            "대전",
            "울산",
            "세종",
            "경기",
            "강원",
            "충북",
            "충남",
            "전북",
            "전남",
            "경북",
            "경남",
            "제주",
        ],
    )
    df_B = pd.read_excel(
        r"C:\Users\USER\Desktop\Workspace\streamlit\streamlit-tutorial-main\streamlit-tutorial-main\dea8a8454ed22cf0.xlsx"
    )
    df_B.to_csv(
        r"C:\Users\USER\Desktop\Workspace\streamlit\streamlit-tutorial-main\streamlit-tutorial-main\dea8a8454ed22cf0.csv",
        index=False,
    )
    col1, col2 = st.columns([2, 3])
    with col1:
        st.table(df_B.head(10))
    with col2:
        fig1 = px.pie(
            df_B, names="지역", values="비율", hole=0.3  # title="지역별 현황",
        )  # hole을 주면 donut 차트

        fig1.update_traces(textposition="inside", textinfo="percent+label")
        # fig1.update_layout(font=dict(size=18))

        st.plotly_chart(fig1)
    st.header("특정 지역 현황")
    tmp_df_B = df_B[df_B["지역"] == select_region]
    st.table(tmp_df_B.head(5))


with tab3:

    select_multi = st.sidebar.multiselect(
        "확인하고자 하는 요금 정보를 선택해주세요.",
        ["사업자", "로밍평균요금", "회원평균요금", "비회원평균요금"],
    )
    # tab A를 누르면 표시될 내용
    st.header("업체 별 전기차 충전 요금")
    # car.csv를 데이터프레임으로 가져와서 표로 표시해주기
    df_C = pd.read_excel(
        r"C:\Users\USER\Desktop\Workspace\streamlit\streamlit-tutorial-main\streamlit-tutorial-main\944ac0abec560811.xlsx"
    )
    df_C.to_csv(
        r"C:\Users\USER\Desktop\Workspace\streamlit\streamlit-tutorial-main\streamlit-tutorial-main\944ac0abec560811.csv",
        index=False,
    )
    tmp_df_C = df_C
    st.table(tmp_df_C.head(5))

    start_button = st.sidebar.button("요금 조회")
    if start_button:
        st.header("유형별 요금 현황")
        selected_df_C = df_C[select_multi]
        df_C.set_index(select_multi)
        # df.style.hide()
        st.table(selected_df_C)
        st.sidebar.success("전기차 충전 요금 탭을 확인해주세요.")
