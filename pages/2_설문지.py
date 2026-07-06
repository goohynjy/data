import streamlit as st

# 페이지 설정
st.set_page_config(page_title="2026 갓생 지수 측정기", page_icon="🌱", layout="centered")

# 세션 상태(Session State) 초기화: 사용자 답변 및 현재 페이지 저장
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# 전체 문항 정의 (점수 합산이 가능하도록 선택지에 점수를 배정)
questions = {
    1: {"q": "1. 하루 평균 수면 시간은 어떻게 되나요?", "type": "slider", "min": 3, "max": 12, "default": 7, "unit": "시간"},
    2: {"q": "2. 일주일에 운동(산책, 헬스 등)은 몇 번 하시나요?", "type": "radio", "options": {"안 함 (0점)": 0, "1~2회 (1점)": 1, "3~4회 (2점)": 2, "5회 이상 (3점)": 3}},
    3: {"q": "3. 스마트폰 하루 평균 스크린 타임은?", "type": "selectbox", "options": {"2시간 미만 (3점)": 3, "2시간~4시간 (2점)": 2, "4시간~6시간 (1점)": 1, "6시간 이상 (0점)": 0}},
    4: {"q": "4. 아침에 알람을 들었을 때 당신의 행동은?", "type": "radio", "options": {"바로 일어난다 (3점)": 3, "5분만 조작을 반복하다 겨우 일어난다 (2점)": 2, "지각할 때까지 잔다 (0점)": 0}},
    5: {"q": "5. 올해 혹은 이번 달에 세운 계획을 얼마나 실천하고 계시나요?", "type": "radio", "options": {"꾸준히 실천 중 (3점)": 3, "생각날 때만 가끔 함 (2점)": 2, "이미 작심삼일로 끝남 (0점)": 0}},
    6: {"q": "6. 독서나 공부 등 자기계발에 투자하는 하루 시간은?", "type": "selectbox", "options": {"없음 (0점)": 0, "1시간 미만 (1점)": 1, "1시간~2시간 (2점)": 2, "2시간 이상 (3점)": 3}},
    7: {"q": "7. 스트레스를 받았을 때 주로 어떻게 해소하시나요?", "type": "radio", "options": {"운동, 취미 등 생산적인 활동 (3점)": 3, "친구와 수다 또는 매운 음식 먹기 (2점)": 2, "폭식하거나 유튜브 쇼츠 무한 시청 (0점)": 0}},
    8: {"q": "8. 하루 동안 마시는 물의 양은 얼마나 되나요?", "type": "radio", "options": {"1L 미만 (커피/음료 위주) (0점)": 0, "1L ~ 1.5L (1점)": 1, "1.5L 이상 충분히 (3점)": 3}},
    9: {"q": "9. 주말이나 공휴일을 보통 어떻게 보내시나요?", "type": "radio", "options": {"계획대로 알차게 취미/학업 병행 (3점)": 3, "밀린 잠을 자고 누워서 휴식 (2점)": 2, "하루 종일 밤낮이 바뀌어 게임/SNS (0점)": 0}},
    10: {"q": "10. 오늘 하루를 돌아보며 일기를 쓰거나 회고하는 습관이 있나요?", "type": "radio", "options": {"자주 기록한다 (3점)": 3, "가끔 생각날 때만 한다 (1점)": 1, "전혀 안 한다 (0점)": 0}},
}

# --- 설문 조사 진행 페이지 (1~5페이지) ---
if st.session_state.page <= 5:
    current_page = st.session_state.page
    
    # 상단 제목 및 진행률 바
    st.title("🌱 2026 갓생 지수 & 라이프스타일 측정기")
    st.progress((current_page - 1) / 5)
    st.subheader(f"Step {current_page} / 5")
    st.write("---")

    # 한 페이지에 2문항씩 배치
    q1_idx = (current_page - 1) * 2 + 1
    q2_idx = (current_page - 1) * 2 + 2

    # 첫 번째 문항 렌더링
    q1 = questions[q1_idx]
    st.markdown(f"#### {q1['q']}")
    if q1['type'] == 'slider':
        ans1 = st.slider("시간을 선택하세요", q1['min'], q1['max'], q1['default'], key=f"q_{q1_idx}")
        # 수면 시간 점수 계산 환산 (7~8시간: 3점, 5~6 또는 9~10시간: 2점, 그 외: 1점)
        score1 = 3 if 7 <= ans1 <= 8 else (2 if 5 <= ans1 <= 10 else 1)
    elif q1['type'] == 'radio':
        ans1 = st.radio("선택해 주세요", list(q1['options'].keys()), key=f"q_{q1_idx}")
        score1 = q1['options'][ans1]
    elif q1['type'] == 'selectbox':
        ans1 = st.selectbox("선택해 주세요", list(q1['options'].keys()), key=f"q_{q1_idx}")
        score1 = q1['options'][ans1]

    st.write("") # 간격 띄우기

    # 두 번째 문항 렌더링
    q2 = questions[q2_idx]
    st.markdown(f"#### {q2['q']}")
    if q2['type'] == 'radio':
        ans2 = st.radio("선택해 주세요", list(q2['options'].keys()), key=f"q_{q2_idx}")
        score2 = q2['options'][ans2]
    elif q2['type'] == 'selectbox':
        ans2 = st.selectbox("선택해 주세요", list(q2['options'].keys()), key=f"q_{q2_idx}")
        score2 = q2['options'][ans2]

    st.write("---")

    # 네비게이션 버튼 배치 (이전 / 다음)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if current_page > 1:
            if st.button("⬅️ 이전 페이지"):
                st.session_state.page -= 1
                st.rerun()

    with col2:
        button_text = "결과 보러가기 ➡️" if current_page == 5 else "다음 페이지 ➡️"
        if st.button(button_text):
            # 답변 결과와 계산된 점수를 세션에 저장
            st.session_state.answers[q1_idx] = score1
            st.session_state.answers[q2_idx] = score2
            st.session_state.page += 1
            st.rerun()

# --- 결과 페이지 (6페이지) ---
else:
    st.title("📊 당신의 갓생 지수 결과")
    st.write("---")
    
    # 점수 총합 계산 (만점: 30점)
    total_score = sum(st.session_state.answers.values())
    
    # 결과 시각화 지표 (Metric)
    st.metric(label="나의 갓생 점수", value=f"{total_score} / 30 점")
    
    # 점수대별 유형 분석 및 피드백
    if total_score >= 24:
        st.success("### 👑 트렌디한 갓생 마스터")
        st.write("당신은 완벽한 시간 관리와 철저한 자기계발로 2026년을 주도하고 있습니다! 루틴이 매우 건강하며, 신체적·정신적 밸런스가 아주 뛰어난 상태입니다. 지금 페이스를 유지하되, 가끔은 스스로에게 휴식을 선물해 번아웃을 예방하세요.")
    elif total_score >= 15:
        st.info("### 🌱 성장 중인 갓생 유망주")
        st.write("균형 잡힌 라이프스타일을 유지하기 위해 노력하고 계시는군요! 좋은 습관들을 잘 정착시키고 있지만, 가끔 스마트폰이나 불규칙한 주말 루틴에 무너질 때가 있습니다. 조금만 더 의식적으로 나쁜 습관을 줄이면 마스터 단계로 올라설 수 있어요.")
    else:
        st.warning("### 🛌 안락함을 사랑하는 침대 요정")
        st.write("지금은 생산적인 활동보다는 휴식과 스마트폰, 자극적인 도파민에 조금 더 치우쳐 있는 상태입니다. 밤낮이 바뀌거나 신체 활동이 부족하면 무기력해지기 쉽습니다. 내일부터 '물 한 잔 마시기', '아침에 바로 일어나기' 같은 작은 루틴 하나부터 시작해 보는 건 어떨까요?")

    st.write("---")
    
    # 다시 하기 버튼
    if st.button("🔄 테스트 다시 하기"):
        st.session_state.page = 1
        st.session_state.answers = {}
        st.rerun()
