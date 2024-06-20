import streamlit as st
from bs4 import BeautifulSoup
import requests
import openai
from st_click_detector import click_detector
import os

# Streamlit 페이지 구성
st.set_page_config(layout="wide")
# 사이드바에 들어가는 타이틀
st.sidebar.title('OptimalBotAI')

champions_ad = [
    {"name": "애쉬", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ashe.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "카이사", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kaisa.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "케이틀린", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Caitlyn.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "징크스", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jinx.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "진", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jhin.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "자야", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Xayah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "바루스", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Varus.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "이즈리얼", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ezreal.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "사미라", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Samira.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "베인", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Vayne.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "스몰더", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Smolder.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "제리", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zeri.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "드레이븐", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Draven.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "루시안", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lucian.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "미스포츈", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/MissFortune.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "닐라", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nilah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "시비르", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Sivir.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "코그모", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/KogMaw.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "코르키", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Corki.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "트리스타나", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Tristana.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "트위치", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Twitch.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "아펠리오스", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Aphelios.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "직스", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ziggs.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "칼리스타", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kalista.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
]

champions_sup = [
    {"name": "노틸러스", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nautilus.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "쓰레쉬", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Thresh.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "파이크", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Pyke.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "모르가나", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Morgana.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "유미", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Yuumi.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "카르마", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Karma.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "파이크", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Pyke.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "세라핀", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Seraphine.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "레오나", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Leona.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "자이라", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zyra.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "알리스타", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Alistar.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "바드", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Bard.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "브라움", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Braum.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "룰루", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lulu.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "잔나", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Janna.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "소라카", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Soraka.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "나미", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nami.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "타릭", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Taric.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "질리언", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zilean.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "레나타 글라스크", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Renata.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "블리츠크랭크", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Blitzcrank.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "룰루", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lulu.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "샤코", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Shaco.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "마오카이", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Maokai.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
    {"name": "럭스", "image_url": "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lux.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"},
]


def call_example(query):
    examples={
        "징크스": {
            "counter": ["트위치", "애쉬", "드레이븐", "트리스타나", "칼리스타", "바루스", "아펠리오스"],
            "team": ["쓰레쉬", "룰루", "밀리오", "브라움", "탐켄치"]
        },
        "진": {
            "counter": ["트위치","제리","칼리스타"],
            "team": ["제라스", "자이라", "애쉬", "벨코즈", "노틸러스", "파이크", "샤코"]
        },
        "트위치": {
            "counter": ["바루스", "칼리스타", "드레이븐", "닐라"],
            "team": ["룰루", "유미", "라칸", "브라움", "질리언", "타릭"]
        },
        "루시안": {
            "counter": ["애쉬", "케이틀린", "드레이븐", "칼리스타", "바루스"],
            "team": ["밀리오", "나미", "타릭", "브라움", "레오나", "노틸러스", "마오카이", "소나"]
        },
        "코그모": {
            "counter": ["케이틀린", "바루스", "드레이븐"],
            "team": ["룰루", "유미", "밀리오", "탐켄치", "브라움", "노틸러스", "쓰레쉬", "타릭"]
        },
        "닐라": {
            "counter": ["카이사","바루스","자야","이즈리얼","애쉬"],
            "team": ["소라카", "라칸", "타릭", "유미"]
        },
        "애쉬": {
            "counter": ["바루스", "닐라", "드레이븐", "칼리스타", "사미라", "트위치"],
            "team": ["룰루", "쓰레쉬", "밀리오", "탐켄치", "브라움", "노틸러스", "자이라", "세라핀", "레오나", "바드"]
        },
        "케이틀린": {
            "counter": ["진", "애쉬", "바루스", "칼리스타", "드레이븐"],
            "team": ["럭스", "모르가나", "바드", "밀리오", "쓰레쉬", "브라움", "룰루", "나미", "소나", "잔나", "세라핀"]
        },
        "사미라": {
            "counter": ["카이사","베인","미스포츈","진","애쉬"],
            "team": ["노틸러스", "알리스타", "렐", "마오카이", "라칸", "스웨인", "파이크"]
        },
        "이즈리얼": {
            "counter": ["바루스", "칼리스타", "드레이븐", "케이틀린", "애쉬", "베인", "카이사", "루시안", "사미라", "트위치"],
            "team": ["카르마", "레오나", "노틸러스", "브라움", "파이크", "소라카", "제라스", "럭스"]
        },
            "시비르": {
            "counter": ["진", "제리", "징크스", "이즈리얼"],
            "team": ["카르마", "탐켄치", "브라움", "쓰레쉬", "룰루", "밀리오", "유미", "세라핀", "마오카이", "벨코즈"]
        },
        "제리": {
            "counter": ["드레이븐", "칼리스타", "바루스", "트위치", "징크스", "트리스타나"],
            "team": ["유미", "룰루", "밀리오", "브라움", "잔나", "노틸러스", "레오나", "라칸"]
        },
        "미스 포츈": {
            "counter": ["드레이븐", "칼리스타", "사미라", "트리스타나", "트위치", "루시안"],
            "team": ["레오나", "노틸러스", "라칸", "세라핀", "타릭", "니코", "알리스타", "렐"]
        },
        "스몰더": {
            "counter": ["제리", "베인", "이즈리얼"],
            "team": ["라칸", "밀리오", "유미", "탐켄치"]
        },
        "카이사": {
            "counter": ["바루스", "케이틀린", "칼리스타", "아펠리오스", "드레이븐", "코그모", "루시안"],
            "team": ["노틸러스", "마오카이", "타릭", "렐", "알리스타", "레오나", "파이크", "라칸", "블리츠크랭크"]
        },
        "베인": {
            "counter": ["진", "이즈리얼", "사미라"],
            "team": ["쓰레쉬", "브라움", "룰루", "밀리오", "알리스타", "마오카이", "타릭", "라칸"]
        },
        "트리스타나": {
            "counter": ["바루스", "칼리스타", "드레이븐", "케이틀린"],
            "team": ["라칸", "룰루", "유미", "레오나", "노틸러스", "타릭", "알리스타", "밀리오"]
        },
        "아펠리오스": {
            "counter": ["바루스", "칼리스타", "트위치", "루시안", "닐라", "애쉬"],
            "team": ["쓰레쉬", "룰루", "밀리오", "마오카이", "세라핀", "노틸러스", "질리언", "잔나", "레나타 글라스크"]
        },
        "드레이븐": {
            "counter": ["아펠리오스", "바루스", "칼리스타", "루시안"],
            "team": ["잔나", "노틸러스", "쓰레쉬", "밀리오", "타릭", "렐", "블리츠크랭크", "파이크", "레나타 글라스크"]
        },
        "자야": {
            "counter": ["바루스", "칼리스타", "케이틀린", "드레이븐", "애쉬"],
            "team": ["라칸", "블리츠크랭크", "노틸러스", "쓰레쉬", "브라움", "탐켄치", "바드", "알리스타", "나미", "렐", "레나타 글라스크", "레오나"]
        },
        "칼리스타": {
            "counter": ["바루스", "드레이븐", "케이틀린"],
            "team": ["쓰레쉬", "노틸러스", "블리츠크랭크", "파이크", "마오카이", "타릭", "렐"]
        },
        "바루스": {
            "counter": ["베인","스몰더","시비르"],
            "team": ["룰루","브라움"]
        },
        "애니": {
            "counter": ["파이크", "레오나"]
        },
        "블리츠크랭크": {
            "counter": ["브라움", "아무무", "라칸", "노틸러스", "타릭"]
        },
        "마오카이": {
            "counter": ["브라움"]
        },
        "아무무": {
            "counter": ["렐", "브라움"]
        },
        "하이머딩거": {
            "counter": ["애쉬", "진", "케이틀린", "럭스", "바드", "소라카"]
        },
        "렐": {
            "counter": ["알리스타", "레나타 글라스크"]
        },
       
        "노틸러스": {
            "counter": ["세트", "레오나", "레나타 글라스크"]
        },
        "파이크": {
            "counter": ["라칸", "하이머딩거"]
        },
        "쓰레쉬": {
            "counter": ["하이머딩거", "블리츠크랭크"]
        },
        "라칸": {
            "counter": ["케이틀린", "럭스", "쓰레쉬", "바드", "모르가나"]
        },
        "레오나": {
            "counter": ["모르가나", "쓰레쉬", "알리스타", "레나타 글라스크"]
        },
        "카르마": {
            "counter": ["시비르", "유미", "애쉬", "아무무", "블리츠크랭크", "노틸러스"]
        },
        "럭스": {
            "counter": ["블리츠크랭크", "파이크", "카르마", "이즈리얼"]
        },
        "나미": {
            "counter": ["케이틀린", "럭스", "애쉬", "카르마"]
        },
        "바드": {
            "counter": ["블리츠크랭크","럭스", "룰루", "카르마", "세나"]
        },
        "알리스타": {
            "counter": ["사일러스", "모르가나", "룰루", "뽀삐"]
        },
        "제라스": {
            "counter": ["블리츠크랭크","파이크","알리스타"]
        },
        "스웨인": {
            "counter": ["애쉬", "카르마"]
        },
        "자크": {
            "counter": ["세트", "잔나", "레나타 글라스크", "뽀삐"]
        },
        "룰루": {
            "counter": ["애쉬", "세나", "카르마", "제라스", "파이크", "블리츠크랭크"]
        },
        "소라카": {
            "counter": ["카르마", "유미", "나미", "애쉬", "노틸러스", "아무무"]
        },
        "샤코": {
            "counter": ["니코", "자이라", "하이머딩거"]
        },
        "모르가나": {
            "counter": ["카르마", "애쉬"]
        },
        "질리언": {
            "counter": ["블리츠크랭크", "카르마", "애니"]
        },
        "타릭": {
            "counter": ["바드", "모르가나"]
        },
        "자이라": {
            "counter": ["제라스", "바드", "레오나"]
        },
        "레나타 글라스크": {
            "counter": ["애쉬", "제라스", "케이틀린", "럭스", "자이라", "블리츠크랭크"]
        },
        "소나": {
            "counter": ["블리츠크랭크", "파이크", "애쉬", "카르마"]
        },
        "벨코즈": {
            "counter": ["블리츠크랭크","파이크","알리스타", "브랜드"]
        },
        "유미": {
            "counter": ["쓰레쉬", "노틸러스"]
        },
        "브라움": {
            "counter": ["라칸"]
        },
        "세라핀": {
            "counter": ["블리츠크랭크", "파이크", "애쉬", "카르마"]
        },
        "세나": {
            "counter": ["블리츠크랭크", "파이크", "애쉬", "카르마"]
        },
        
        "잔나": {
            "counter": ["블리츠크랭크"]
        },
        "피들스틱": {
            "counter": ["카르마", "애쉬", "케이틀린", "럭스", "블리츠크랭크"]
        },
        "판테온": {
            "counter": ["레오나", "타릭", "애쉬"]
        },
        "세트": {
            "counter": ["판테온", "블리츠크랭크", "렐"]
        },
        "미스 포츈": {
            "counter": ["블리츠크랭크", "파이크", "애쉬", "카르마"]
        },
        "탐켄치": {
            "counter": ["블리츠크랭크", "렐", "파이크"]
        },
        "직스": {
            "counter":["칼리스타","루시안","트리스타나"],
            "team":["레오나","파이크","세나"]

        },
        "미스포츈": {
            "counter":["칼리스타","루시안","트리스타나","사미라"],
            "team":["레오나","노틸러스","블리츠크랭크"]

        },
        "코르키": {
            "counter":["드레이븐","케이틀린","트리스타나"],
            "team":["쓰레쉬","블리츠크랭크","노틸러스"]

        }
    }
    return examples.get(query, {"team": [], "counter": []})




def get_openai_response(user_input):
    try:
        client = OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{user_input}의 상성과 조합에 관해 설명해 주세요."}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error occurred: {e}"


html_ad = ""
for item in champions_ad:
    name=item["name"]
    src = item["image_url"]
    html_ad += f"<a href='#' id='{name}'><img src='{src}'></a>"

html_sup = ""
for item in champions_sup:
    name=item["name"]
    src = item["image_url"]
    html_sup += f"<a href='#' id='{name}'><img src='{src}'></a>"
    
# 중앙 정렬을 위한 컨테이너
col1, col2 = st.columns([1, 5])
clicked=None
with col1:
    with st.container():
        clicked = click_detector(html_ad)
        #cols = st.columns(6)
        #for i in range(len(champions_ad)):
        #    with cols[i % 6]:
        #        champion_ad = champions_ad[i]
        #        st.image(champion_ad["image_url"], caption=champion_ad["name"])
with col2:
    with st.container():
        #placeholder = st.empty()
        st.write(clicked)
        # call openai
        result = call_example(clicked)
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        openai.api_key = api_key
        
        if st.button("상성과 조합 보기"):
            if not api_key:
                st.error("Please enter your API key.")
            else:
                response = openai.ChatCompletion.create(
                    model="gpt-4o",  # Example model, replace with appropriate model
                    messages=[
                        {"role": "system", "content": "you are lol bot"},
                        {"role": "user", "content": f"{result}의 조합과 카운터에 대해 설명해주세요."}
                    ]
                )
                explanation = response['choices'][0]['message']['content'].strip()
                st.write("### 챔피언 조합 설명")
                st.write(explanation)
                for item in result['team']:
                    for i in champions_ad:
                        if i["name"] == item:
                            st.image(i['image_url'])
                    for i in champions_sup:
                        if i["name"] == item:
                            st.image(i['image_url'])
                st.subheader("Counter")
                for item in result['counter']:
                    for i in champions_ad:
                        if i["name"] == item:
                            st.image(i['image_url'])
                    for i in champions_sup:
                        if i["name"] == item:
                            st.image(i['image_url'])
                         

st.divider()

col1, col2 = st.columns([1, 5])
clicked=None
with col1:
    with st.container():
        clicked = click_detector(html_sup)
        #cols = st.columns(6)
        #for i in range(len(champions_ad)):
        #    with cols[i % 6]:
        #        champion_ad = champions_ad[i]
        #        st.image(champion_ad["image_url"], caption=champion_ad["name"])
with col2:
    with st.container():
        #placeholder = st.empty()
        st.write(clicked)
        # call openai
        result = call_example(clicked)
        #st.write(result)

        #서폿 조합 코드
        #L_____
        
        st.subheader("Counter")
        for item in result['counter']:
            for i in champions_ad:
                if i["name"] == item:
                    st.image(i['image_url'])
            for i in champions_sup:
                if i["name"] == item:
                    st.image(i['image_url'])
