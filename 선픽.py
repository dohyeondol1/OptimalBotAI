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
col1, col2 = st.columns(2)
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
        #st.write(result)
        # call openai
        st.subheader("Team")
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

col1, col2 = st.columns(2)
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
        # call openai

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
