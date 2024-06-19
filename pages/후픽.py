import streamlit as st
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
        padding: 4rem 1rem 4rem 4rem;
    }
    @media (min-width: 576px) {
        .st-emotion-cache-1jicfl2 {
        padding: 4rem 1rem 4rem 4rem;
        }
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

html_ad = ""
for champion in champions_ad:
    name = champion["name"]
    image_url = champion["image_url"]
    html_ad += f'<a href="#" id="{name}"><img src="{image_url}" style="margin: 10px; border-radius: 50%;" width="100" height="100"></a>'

html_sup = ""
for champion in champions_sup:
    name = champion["name"]
    image_url = champion["image_url"]
    html_sup += f'<a href="#" id="{name}"><img src="{image_url}" style="margin: 10px; border-radius: 50%;" width="100" height="100"></a>'

# CSS 스타일 추가
st.markdown("""
    <style>
    .champion-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        justify-items: center;
    }
    .champion-image {
        margin: 10px;
        width: 50px;
        height: 50px;
        display: inline-block;
        border-radius: 50%;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# 컬럼을 사용하여 페이지 레이아웃 설정
col1, col2 = st.columns([1, 4])

# 왼쪽 컬럼 (사이드바 역할)
with col1:
    st.markdown('### Champions - AD')
    st.markdown('<div class="champion-container">', unsafe_allow_html=True)
    for champion in champions_ad:
        st.markdown(f'<a href="#" id="{champion["name"]}"><img src="{champion["image_url"]}" class="champion-image"></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('### Champions - Support')
    st.markdown('<div class="champion-container">', unsafe_allow_html=True)
    for champion in champions_sup:
        st.markdown(f'<a href="#" id="{champion["name"]}"><img src="{champion["image_url"]}" class="champion-image"></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 오른쪽 컬럼 (메인 콘텐츠)
with col2:
    st.write("여기에 메인 콘텐츠를 추가합니다.")