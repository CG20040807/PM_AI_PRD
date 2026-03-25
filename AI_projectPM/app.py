import streamlit as st
import requests
import pandas as pd
from docx import Document
from fpdf import FPDF

st.set_page_config(
    page_title="AI Product Manager Workspace",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Product Manager Workspace")
st.write("输入产品名称，自动生成 PRD / 用户画像 / 竞品分析 / Roadmap")

product = st.text_input("输入产品名称")

# Word生成
def generate_word(text):

    doc = Document()

    doc.add_heading("AI 产品分析报告", 0)

    doc.add_paragraph(text)

    file = "prd_report.docx"

    doc.save(file)

    return file


# PDF生成
def generate_pdf(text):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0,10,text)

    file = "prd_report.pdf"

    pdf.output(file)

    return file


if st.button("生成分析"):

    with st.spinner("AI分析中..."):

        url = "https://7fv2jsrt7q.coze.site/run"

        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjgyYTVkLWJlMmUtNDViOS1hODFkLWM4ZGI3MTU5MmExOSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NDQ3MzAzLCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxMTkzMTM0OTQ4ODEwODA0In0.d9ORVnCAqSyhzmne1gFATy9gQrAvNsS3MU6HaK4APQVZuJnYntBHZ7KEqNAi5Krp-vGfDQtQkSaEOICMAgDNOShUd048c5yQRF7N7G8GzYpUHgD9ybROnvViTHRQHRNJsgRkaQyU-aKGETib8cSEQHHN220ZoBTfUOziyjEKFSqHAqghiE88R3tkq-LJFdybmQP2l6NZEPIt2h2VFslOVV08P0vT5uPtWGziTRfTWhxwkYvGCGNaKzBowd2ZUm-zbp8DBUj9UaEkI5P5mWL5donOHzLuNDd0AzMyx08wEPZEZBPcJXxiLuyOYeaCb6aZttiHUv85QPsCJuHatqZi2g",
            "Content-Type": "application/json"
        }

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
            "model":"gpt-4",
            "messages":[
                {"role":"user","content":prompt}
            ]
        }

        response = requests.post(url,headers=headers,json=data)

        result = response.json()["choices"][0]["text"]

    st.success("分析完成")

    st.markdown("## 📄 AI分析报告")

    st.write(result)

    # 用户画像卡片
    st.markdown("## 👤 用户画像")

    col1,col2 = st.columns(2)

    with col1:
        st.info("""
用户1  
年龄：18-25  
职业：学生  
需求：娱乐、社交
""")

    with col2:
        st.info("""
用户2  
年龄：25-35  
职业：白领  
需求：资讯、学习
""")

    # 竞品对比表
    st.markdown("## 📊 竞品对比")

    data = {
        "产品":["抖音","快手","B站"],
        "核心功能":["短视频","短视频","视频社区"],
        "用户群体":["大众","下沉市场","年轻人"],
        "优势":["推荐算法强","社交关系强","内容质量高"],
        "劣势":["内容重复","UI较旧","增长慢"]
    }

    df = pd.DataFrame(data)

    st.table(df)

    # Roadmap
    st.markdown("## 🗺 产品Roadmap")

    st.markdown("""
V1：核心内容浏览  
V2：社交互动功能  
V3：商业化模块  
""")

    # 生成下载文件
    word_file = generate_word(result)

    pdf_file = generate_pdf(result)

    col1,col2 = st.columns(2)

    with col1:
        with open(word_file,"rb") as f:
            st.download_button(
                "📄 下载Word报告",
                f,
                file_name="prd_report.docx"
            )

    with col2:
        with open(pdf_file,"rb") as f:
            st.download_button(
                "📄 下载PDF报告",
                f,
                file_name="prd_report.pdf"
            )
