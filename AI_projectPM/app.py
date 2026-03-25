import streamlit as st
import requests
import pandas as pd
from docx import Document
from fpdf import FPDF

# 设置页面配置
st.set_page_config(
    page_title="AI Product Manager Workspace",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Product Manager Workspace")
st.write("输入产品名称，自动生成 PRD / 用户画像 / 竞品分析 / Roadmap")

product = st.text_input("输入产品名称")

# Word生成函数
def generate_word(text):
    doc = Document()
    doc.add_heading("AI 产品分析报告", 0)
    doc.add_paragraph(text)
    file = "prd_report.docx"
    doc.save(file)
    return file

# PDF生成函数
def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # 支持多行文本
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)

    file = "prd_report.pdf"
    pdf.output(file)

    return file


if st.button("生成分析"):

    with st.spinner("AI分析中..."):

        url = "https://7fv2jsrt7q.coze.site/run"  # Coze API 地址，根据实际修改

        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjgyYTVkLWJlMmUtNDViOS1hODFkLWM4ZGI3MTU5MmExOSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NDQ4NzcwLCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxMTk5NDM5NjIwNzM1MDE2In0.d0RdRYlh0K7THRNuZXYUeCj2p0E-3D4LGMj4VBofLRB2UP-a9hDfEBoemeoC_HOduUv_UsGYpy0T2lzHrUV6Rd8vvf7JuxkhNVbTc2u3W_8tEuehSVussAHPEIxYa-2cWvOvzvz1J7wXEhcwLMp4fjj3-mb-wx1Wu1dsBoZoOsymeiLTcnhfl33Kp9b7Vf45S4r9Le8QPNTAeCcP9xS5BSVXerIx0MqSHJKgDZiFUXu_hxS5k78kI7sVuoZdD3TCRqm07MmwXTXSh4oIbmVqOw9hmVLrcyKY5_GemTD_XCtL1o-5Q-N2RB6er01IwisNg3CzTnmAgMBi1yHiz1heHA",  # 替换为你的 API Token
            "Content-Type": "application/json"
        }

        prompt = f"""
你是一名有10年经验的互联网产品经理。

请分析产品：{product}

输出内容：

1. 产品定位分析：包括产品背景、用户画像、核心功能、用户痛点等
2. 竞品分析：识别 3 个主要竞品，分析功能差异和用户选择原因
3. PRD 文档：生成简化版产品需求文档，包含背景、需求、目标、功能设计等
4. 产品机会分析：提出新功能创新、用户体验优化和商业化方向
"""

        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            # 发送请求并确保返回的状态码是200
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # 如果状态码不是200，会抛出异常

            # 获取返回数据并调试输出
            response_data = response.json()
            print(response_data)  # 打印调试信息，查看返回数据结构

            # 确保返回数据包含choices字段
            if "choices" in response_data and len(response_data["choices"]) > 0:
                result = response_data["choices"][0].get("text", "No text returned.")
            else:
                result = "未返回有效内容"

        except requests.exceptions.RequestException as e:
            result = f"请求失败，错误信息: {e}"

        except KeyError:
            result = "API 返回数据格式错误，无法解析。"

        except Exception as e:
            result = f"发生了一个意外错误: {e}"

    st.success("分析完成")

    st.markdown("## 📄 产品分析报告")
    st.write(result)

    # 用户画像卡片
    st.markdown("## 👤 用户画像")
    col1, col2 = st.columns(2)

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

    # 竞品分析（从API返回的数据中提取）
    st.markdown("## 📊 竞品分析")

    try:
        competitive_analysis = result  # 假设result中包含竞品分析部分
        st.write(competitive_analysis)
    except Exception as e:
        st.error(f"竞品数据解析出错：{e}")

    # PRD文档
    st.markdown("## 📄 PRD 文档")
    st.write(result)

    # 产品机会分析
    st.markdown("## 🚀 产品机会分析")
    st.write(result)

    # 生成Word和PDF报告
    word_file = generate_word(result)
    pdf_file = generate_pdf(result)

    # 创建下载按钮
    col1, col2 = st.columns(2)

    with col1:
        with open(word_file, "rb") as f:
            st.download_button(
                "📄 下载Word报告",
                f,
                file_name="prd_report.docx"
            )

    with col2:
        with open(pdf_file, "rb") as f:
            st.download_button(
                "📄 下载PDF报告",
                f,
                file_name="prd_report.pdf"
            )
