from api.AI import AIAPI
import streamlit as st  

def bwrite():
    st.write('그냥 신기해서 만들어 봤어요')
    button2 = st.button('그냥 만들어본 버튼2에요')
    if button2:
        st.balloons()
        st.text("짱 신기해요")
    
@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")



def main():

    api = get_api()

    st.title(":sparkles: 2023 HAI 여름방학 Web APP 개발 과제 :sparkles:")
   
    button1 = st.button('그냥 만들어본 버튼이에요')

    if button1:
        bwrite()


    st.divider()

    st.subheader("1. OCR API를 이용한 이미지 파일 인식시켜 :blue[텍스트]로 만들기")
    st.markdown(":blue[jpg,png,jpeg]등 그림 파일을 넣어주세요.")
    query = st.file_uploader('input image')
    if query is not None:
        st.image(query)
        response1 = api.query_image2text(query, key='image2text')
        with st.expander("**:blue[text] 보기**"):
            st.code(f"{response1}", language="python")
        

    st.divider()

    st.subheader("2. Text to Text API 활용한 :green[요약본] 만들기")
    if query is not None:
        response2 = api.query_text2text(response1, key='text2text')
        with st.expander("**:green[요약본] 보기**"):
            st.code(f"{response2}", language="csv")



if __name__ == '__main__' :
    main()
