import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI 聊天助手", page_icon=":robot:")
st.title(":robot: AI 聊天助手")

api_key = os.getenv("OPENAI_API_KEY")
print("API 密钥：", api_key)


client = OpenAI(api_key=api_key,
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

with st.sidebar:
    st.header("⚙️ 设置")
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    model = st.selectbox("模型", ["qwen-plus", "qwen3.7-max"])
    st.divider()
    if st.button("🗑️ 清空对话"):
        st.session_state.messages = [
            {"role": "system", "content": "你是一个简洁、友好的助手，回答不超过三句话。"}
        ]
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system","content": "你是一个简洁、友好的助手，回答不超过三句话。"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("请输入你的问题"):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            message_placeholder = st.empty()
            full_response = ""
            completion = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                stream = True,
                temperature=temperature
            )
            for chunk in completion:
                if chunk.choices and len(chunk.choices) > 0:
                    delta_content = chunk.choices[0].delta.content
                    if delta_content is not None:
                        full_response += delta_content
                        message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})