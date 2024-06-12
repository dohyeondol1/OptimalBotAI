import streamlit as st
# 현재 페이지 상태를 저장할 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# 페이지 전환 함수
def switch_page(page_name):
    st.session_state.page = page_name

# 메인 페이지 함수
def main_page():
    # CSS 적용
    st.markdown(main_page_style, unsafe_allow_html=True)
    
    # 메인 페이지 내용
    st.title('Streamlit App with Styled Main Page')
    st.write('이 예제는 메인 페이지의 배경 이미지와 컨텐츠 스타일을 지정하는 방법을 보여줍니다.')
    
    # 다음 페이지로 이동하는 버튼
    if st.button('두 번째 페이지로 이동'):
        switch_page('second_page')

# 두 번째 페이지 함수
def second_page():
    st.title('Second Page')
    st.write('이것은 두 번째 페이지입니다.')
    
    # 이전 페이지로 돌아가는 버튼
    if st.button('이전 페이지로 돌아가기'):
        switch_page('main')
    
    # 다음 페이지로 이동하는 버튼
    if st.button('세 번째 페이지로 이동'):
        switch_page('third_page')

# 세 번째 페이지 함수
def third_page():
    st.title('Third Page')
    st.write('이것은 세 번째 페이지입니다.')
    
    # 두 번째 페이지로 돌아가는 버튼
    if st.button('두 번째 페이지로 돌아가기'):
        switch_page('second_page')

# 현재 페이지에 따라 해당 페이지 함수 호출
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'second_page':
    second_page()
elif st.session_state.page == 'third_page':
    third_page()
