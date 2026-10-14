# 🎲 Streamlit 로또 번호 생성기 (Lotto Number Generator)

Streamlit을 활용하여 제작한 웹 기반의 로또 번호 자동 생성 프로그램입니다.

## 📌 주요 기능
- **로또 번호 자동 생성**: 1부터 45까지 중복 없는 6개 숫자 추천 및 정렬
- **로또 공 시각화**: 실제 로또 공 색상 규격에 맞춘 HTML/CSS 구형 스타일 디자인
  - `1 ~ 10`: 노란색 🟡
  - `11 ~ 20`: 파란색 🔵
  - `21 ~ 30`: 빨간색 🔴
  - `31 ~ 40`: 회색 ⚪
  - `41 ~ 45`: 초록색 🟢
- **최대 5세트 제한**: 한 화면에 최대 5세트까지 생성 및 세션 상태 유지

## 🛠️ 기술 스택 (Tech Stack)
- **Language:** Python 3
- **Framework:** Streamlit
- **Deployment:** Streamlit Community Cloud

## 🚀 실행 방법 (Local Execution)
```bash
pip install -r requirements.txt
streamlit run app.py