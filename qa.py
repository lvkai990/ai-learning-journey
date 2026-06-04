from openai import OpenAI
import os

def main():
    # 获取 API 密钥
    api_key = os.getenv("OPENAI_API_KEY")
    print("API 密钥：", api_key)
    
    # 初始化客户端
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    messages = [
        {"role": "system", "content": "你是一个简洁、友好的助手，回答不超过三句话。"}
    ]

    while True:
        question = input("\n你：")
        if question.lower() == 'q':
            print("再见！")
            break
        if not question.strip():
            continue

        messages.append({"role": "user", "content": question})

        completion = client.chat.completions.create(
            model="qwen3.7-max",
            messages=messages
        )
        answer = completion.choices[0].message.content
        print(f"AI：{answer}")
        messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()






