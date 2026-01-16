import streamlit as st
import random
import datetime

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="로또 번호 생성기", page_icon="🪙")
st.title("🪙 로또 번호 생성기 🪙")

# 2. 버튼 디자인을 위한 CSS 설정
st.markdown("""
    <style>
    /* 모든 버튼 및 링크 버튼 공통 스타일 */
    .stButton > button, .stLinkButton > a {
        height: 3em !important;
        width: 100% !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        white-space: nowrap !important;
    }

    /* 첫 번째 컬럼 (로또 생성 버튼): 주황색 (#FF3300) */
    [data-testid="stHorizontalBlock"] > div:nth-of-type(1) button {
        background-color: #FF3300 !important;
        color: #FFFFFF !important;
    }
    
    /* 로또 생성 버튼 마우스 커서 올렸을 때 (#FF6600) */
    [data-testid="stHorizontalBlock"] > div:nth-of-type(1) button:hover {
        background-color: #FF6600 !important;
    }

    /* 두 번째 컬럼 (동행복권 바로가기): 검정색 (#111111) */
    [data-testid="stHorizontalBlock"] > div:nth-of-type(2) a {
        background-color: #111111 !important;
        color: #FFFFFF !important;
    }
    
    /* 바로가기 버튼 마우스 커서 올렸을 때 */
    [data-testid="stHorizontalBlock"] > div:nth-of-type(2) a:hover {
        background-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 로또 번호 생성 함수 정의
def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)
        lotto.add(number)
    return sorted(list(lotto))

# 4. 레이아웃 배치 (버튼 간격을 좁게 유지)
col1, col2, col3 = st.columns([1.1, 1.3, 2.5], gap="small")

with col1:
    button = st.button("로또 번호 생성하기")

with col2:
    # https://www.woongjinbn.com/m/board.html?code=ojm0904_board3&page=5&board_cate=&num1=999291&num2=00000&type=q&type2=u&s_id=&stext=&ssubject=&shname=&scontent=&sbrand=&sgid=&datekey=&branduid= www가 포함된 정확한 링크로 변경되었습니다.
    st.link_button("동행복권 바로가기❤️", "https://www.dhlottery.co.kr/")

with col3:
    pass

# 5. 버튼 클릭 시 실행될 로직
if button:
    st.divider() 
    for i in range(1, 6):
        numbers = generate_lotto()
        st.subheader(f"{i}번째 추천 번호 : {numbers}")
    
    st.divider()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st.write(f"✅ 생성된 시각 : {now}")