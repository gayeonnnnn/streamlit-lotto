import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎲", layout="centered")

st.title("🎲 로또 번호 생성기")

# 세션 상태 초기화 (생성된 로또 번호 세트 저장용)
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []

# 공 번호에 따른 색상 반환 함수
def get_ball_color(num):
    if num <= 10:
        return "#fbc400"  # 노란색 (1~10)
    elif num <= 20:
        return "#69c6f0"  # 파란색 (11~20)
    elif num <= 30:
        return "#ff6056"  # 빨간색 (21~30)
    elif num <= 40:
        return "#a6a6a6"  # 회색 (31~40)
    else:
        return "#b0d840"  # 초록색 (41~45)

# 로또 번호 세트 추가 함수
def generate_lotto_set():
    if len(st.session_state.lotto_sets) < 5:
        # 1~45 중복 없는 6개 숫자 뽑기 후 정렬
        numbers = sorted(random.sample(range(1, 46), 6))
        st.session_state.lotto_sets.append(numbers)

# 5세트 미만일 때만 버튼 활성화
is_max = len(st.session_state.lotto_sets) >= 5

if st.button("로또번호 생성", disabled=is_max, use_container_width=True):
    generate_lotto_set()

if is_max:
    st.info("최대 5개 세트 생성이 완료되었습니다.")

st.divider()

# 생성된 번호 세트 화면에 표시
for idx, lotto_numbers in enumerate(st.session_state.lotto_sets, start=1):
    st.subheader(f"Set {idx}")
    
    # 6개의 공을 가로로 배치하기 위한 컬럼 생성
    cols = st.columns(6)
    
    for i, num in enumerate(lotto_numbers):
        color = get_ball_color(num)
        # HTML/CSS를 활용해 실제 로또 공 형태 시각화
        html_code = f"""
        <div style="
            background-color: {color};
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 18px;
            margin: auto;
            box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.2);
        ">
            {num}
        </div>
        """
        cols[i].markdown(html_code, unsafe_allow_html=True)