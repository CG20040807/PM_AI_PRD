import streamlit as st
import requests
from docx import Document

# 设置页面配置
st.set_page_config(
    page_title="AI Product Manager Workspace",
    page_icon="🚀",
    layout="wide"
)

# 页面标题和说明
st.title("🚀 AI Product Manager Workspace")
st.write("输入产品名称，自动生成 PRD / 用户画像 / 竞品分析 / Roadmap")

# 输入产品名称
product = st.text_input("输入产品名称")

# 生成 Word 文件的函数
def generate_word(text):
    doc = Document()
    doc.add_heading("AI 产品分析报告", 0)  # 添加标题
    doc.add_paragraph(text)  # 添加报告内容

    file = "prd_report.docx"
    doc.save(file)  # 保存文件

    return file

# 按钮点击事件
if st.button("生成分析"):

    with st.spinner("AI分析中..."):

        # Coze API URL
        url = "https://7fv2jsrt7q.coze.site/run"

        # 请求头
        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjgyYTVkLWJlMmUtNDViOS1hODFkLWM4ZGI3MTU5MmExOSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NDUyMTUwLCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxMjEzOTU1ODU5NDE1MDc0In0.VFBnKHgqK9TU28Xbh1I3_ADmj8BgKueXbhTSa1YH9C7267Esn6fdNhDh4FA77S2IH6E9b_9CJnzmHVQ1YXUZmnajKIKCJ5Svx-e80ir_lIhOBV6zJCGn_EbVbeQ17W6nOHZKU-8WzFbNwQ1FFq4l8krIijv-H3sWiliPtE-BR7IR6Cz3uce_4SWpLjMxQoyaCGxKnH9OM56pmwOSiXsnC9HhgGrXXIYcjzKCQn5eg6bYn9qmnoDBkmHf6HPhdmq-dl-HgHUJM7BxtYXGXkxWtiNuMht8JNeMWf6UGp18wAeZ0kQ7ZThGV-A0Wo3hnQZSn5xkiHthG1OGhz9nPq5Vhw",  # 替换为你的 API Token
            "Content-Type": "application/json"
        }

        # 请求内容
        prompt = f"""
你是一名有10年经验的互联网产品经理。

请分析产品：{product}

输出内容：

1 产品定位
2 用户画像
3 竞品分析
4 产品功能设计
5 PRD文档
6 产品机会
7 产品Roadmap
"""

        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        # 向 Coze 发送请求
        response = requests.post(url, headers=headers, json=data)

        # 解析返回的结果
        result = response.json()["choices"][0]["text"]

    # 显示分析完成信息
    st.success("分析完成")

    # 展示分析结果
    st.markdown("## 📄 AI分析报告")
    st.write(result)

    # 生成 Word 文件
    word_file = generate_word(result)

    # 创建下载按钮
    with open(word_file, "rb") as f:
        st.download_button(
            "📄 下载Word报告",
            f,
            file_name="prd_report.docx"
        )
