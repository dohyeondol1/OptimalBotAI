import streamlit as st
import openai
from st_click_detector import click_detector

# Streamlit 페이지 구성
st.set_page_config(layout="wide")

# 사이드바에 들어가는 타이틀
st.sidebar.title('OptimalBotAI')

# Streamlit 페이지 스타일링 설정 수정하기
st.markdown("""
    <style>
    /*페이지 padding값 수정*/
    .st-emotion-cache-1jicfl2 {
        padding: 4rem 1rem 4rem 1rem;
    }
    @media (min-width: 576px) {
        .st-emotion-cache-1jicfl2 {
        padding: 4rem 1rem 4rem 4rem;
        }
    }
    /*streamlit 자체 css 수정*/
    .st-emotion-cache-1wmy9hl >div{
        gap: 0;
    }
    .st-emotion-cache-13k62yr >header {
        heigth: 0;
    }
    </style>
    """, unsafe_allow_html=True)

champions_ad=[
    {"name":"애쉬","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ashe.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"카이사","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kaisa.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"케이틀린","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Caitlyn.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"징크스","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jinx.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"진","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jhin.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"자야","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Xayah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"바루스","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Varus.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"이즈리얼","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ezreal.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"사미라","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Samira.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"베인","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Vayne.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"스몰더","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Smolder.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"제리","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zeri.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"드레이븐","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Draven.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"루시안","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lucian.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"미스포츈","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/MissFortune.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"닐라","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nilah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"시비르","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Sivir.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"코그모","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/KogMaw.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"코르키","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Corki.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"트리스타나","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Tristana.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"트위치","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Twitch.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"아펠리오스","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Aphelios.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"직스","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ziggs.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"칼리스타","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kalista.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
]

champions_sup=[
    {"name":"노틸러스","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nautilus.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"럭스","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lux.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"블리츠크랭크","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Blitzcrank.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"마오카이","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Maokai.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"레오나","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Leona.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"쓰레쉬","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Thresh.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"유미","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Yuumi.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"브라움","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Braum.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"모르가나","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Morgana.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"소나","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Sona.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"소라카","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Soraka.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"스웨인","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Swain.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"자크","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zac.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"룰루","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lulu.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"니코","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Neeko.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"뽀삐","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Poppy.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"알리스타","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Alistar.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"세라핀","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Seraphine.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"렐","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Rell.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"라칸","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Rakan.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"자이라","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zyra.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"파이크","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Pyke.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"흐웨이","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Hwei.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name":"나미","image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nami.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},           
]

# CSS 스타일 추가
st.markdown("""
    <style>
    .champion-image {
        margin: 10px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        cursor: pointer;
        float: left;
    }
    </style>
    """, unsafe_allow_html=True)

# 컬럼을 사용하여 페이지 레이아웃 설정
side_col, main_col = st.columns([1, 5])

# 선택된 챔피언 리스트
if 'selected_champions' not in st.session_state:
    st.session_state['selected_champions'] = []

selected_champions = st.session_state['selected_champions']

# GPT-3 API 키 입력
with main_col:
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    st.write("### 후픽 챔피언 조합")

    if st.button("선택 초기화"):
        selected_champions.clear()
        st.session_state['selected_champions'] = selected_champions

# 왼쪽 컬럼 (사이드바 역할)
with side_col:
    st.markdown('### 원딜 챔피언')
    for i in range(0, len(champions_ad), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(champions_ad):
                champion = champions_ad[i + j]
                with cols[j]:
                    if st.button(champion["name"], key=f"ad_{champion['name']}"):
                        if len(selected_champions) < 2 and champion["name"] not in selected_champions:
                            selected_champions.append(champion["name"])
                            st.session_state['selected_champions'] = selected_champions

    st.markdown('### 서폿 챔피언')
    for i in range(0, len(champions_sup), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(champions_sup):
                champion = champions_sup[i + j]
                with cols[j]:
                    if st.button(champion["name"], key=f"sup_{champion['name']}"):
                        if len(selected_champions) < 2 and champion["name"] not in selected_champions:
                            selected_champions.append(champion["name"])
                            st.session_state['selected_champions'] = selected_champions

# 오른쪽 컬럼 (메인 콘텐츠)
with main_col:
    if len(selected_champions) == 2:
        st.write(f"선택된 챔피언: {selected_champions[0]}, {selected_champions[1]}")
        
        if api_key:
            openai.api_key = api_key
            if st.button("응답 보기"):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",  # Example model, replace with appropriate model
                        messages=[
                            {"role": "system", "content": f"{selected_champions[0]}, {selected_champions[1]}의 조합에 대해 설명해주세요."},
                            {"role": "user", "content": "설명 보기"}
                        ]
                    )
                    explanation = response['choices'][0]['message']['content'].strip()
                    st.write("### 챔피언 조합 설명")
                    st.write(explanation)

                    # 가로선 추가
                    st.markdown("---")

                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",  # Example model, replace with appropriate model
                        messages=[
                            {"role": "system", "content": f"{selected_champions[0]}, {selected_champions[1]}의 조합에 대응할 조합을 하나 설명해주세요."},
                            {"role": "user", "content": "설명 보기"}
                        ]
                    )
                    explanation = response['choices'][0]['message']['content'].strip()
                    st.write("### 대응 조합 설명")
                    st.write(explanation)

                except Exception as e:
                    st.write("오류가 발생했습니다: ", e)
        else:
            st.write("API 키를 입력하세요.")
    elif len(selected_champions) < 2:
        st.write("두 챔피언을 선택하세요.")
