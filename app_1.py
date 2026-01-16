import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# pip install -r requiremnet.txt를 하면 한번에 install 가능

st.title("📊 국세청 근로소득 데이터 분석기")


# 데이터 불러오기
file_path = "/data/국세청_근로소득 백분위(천분위) 자료_20241231.csv"
# ./ 현재 내가 있는 위치에서 data 방으로 가서 그 안의 파일을 불러들여라, "."은 사용안해도 괜찮음
# "." 현재 디렉토리, ".." 한 단계 밖에 나가고 싶을 때,
# path=../images/"a.jpg" 방을 먼저 나가서, 다음 방을 나간 다음, 원하는 파일명을 쓰기!


# 엑셀의 iferror처럼 혹시나 발생할 오류에 대비하는 함수
# 오류기 나면 except 함수가 예외로 실행됨

try :
    # 자료 읽기
    df=pd.read_csv(file_path)
    st.success("✅ 데이터를 성공적으로 불러 왔습니다!")

    # 데이터 미리 보기
    st.subheader("✔️ 데이터를 확인하기")
    st.dataframe(df.head()) # ()안에 아무것도 없으면 표 상단 5줄 보여주기, 추가하고 싶으면 괄호 넣기


    # 데이터 분석 그래프 그리기
    st.subheader("📉 항목별 분포 그래프")

    # 분석하고 싶은 열 이름을 선택
    # 급여,인원 같은 숫자 데이터가 있는 칸을 골라야 한다
    columns_names=df.columns.tolist()  # 컬럼의 첫번째 덩어리를 갖고오겠음
    selected_col=st.selectbox("분석할 항목을 선택하세요 : ", columns_names)


    # 그래프 그리기 (seaborn 사용)
    # fig(그래프의 전체사이즈), ax(그래프가 그려질 공간)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(df[selected_col], ax=ax, color="#F3F33D")

   
    plt.title(f"[{selected_col}] 분포 확인")  # 그래프 맨 위 제목
    plt.xlabel(selected_col) # 가로축(x) 제목
    plt.ylabel("빈도수")  # 세로축(y) 제목 얼마나 자주 나오는지


    # 스트림릿 웹 화면에 그래프 표시
    st.pyplot(fig)



except FileNotFoundError :
    st.error(f"🚨 '{file_path}' 파일을 찾을 수 없습니다. 파일명이 정확한지 확인해주세요.")
except Exception as e :
    st.error(f"🚨 에러가 발생했습니다{e}")