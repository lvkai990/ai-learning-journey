import streamlit as st

st.title("自我介绍生成器")
with st.sidebar:
    st.header("设置")
    style = st.selectbox("选择风格", ["正式", "幽默", "简洁"])
    st.divider ()
    st.write("选择不同的风格生成不同风格的自我介绍")

name = st.text_input("请输入你的名字")
job = st.text_input("请输入你的职位")

if st.button("生成自我介绍"):
    if name and job:
        if style == "正式":
            st.write(f"大家好,我叫{name}，是一个{job}。")
        elif style == "幽默":
            st.write(f"{name}，一个靠{job}吃饭的有趣灵魂。")
        elif style == "简洁":
            st.write(f"{name}，{job}。")
    else:
        st.warning("请填写完整的信息")