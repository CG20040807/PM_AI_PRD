import streamlit as st
import requests
import json
import os
from docx import Document

# ===== 页面配置 =====
st.set_page_config(
    page_title="AI Product Manager Agent",
    page_icon="🚀",
    layout="wide"
)

# ===== UI =====
st.markdown("""
<style>
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f5f7fa;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 AI Product Manager Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">输入产品名称，一键生成PRD & 竞品分析</div>', unsafe_allow_html=True)

# ===== 输入 =====
product = st.text_input("📦 产品名称", placeholder="例如：小红书 / 抖音 / Keep")

# ===== Word生成 =====
def generate_word(text):
    doc = Document()
    doc.add_heading("AI 产品分析报告", 0)
    doc.add_paragraph(text)
    file = "prd_report.docx"
    doc.save(file)
    return file

# ===== API =====
def fetch_product_analysis(product):
    url = "https://api.minimax.chat/v1/text/chatcompletion_v2"

    api_key = os.getenv("MINIMAX_API_KEY")  # 从环境变量读取

    if not api_key:
        st.error("❗ 请先设置 MINIMAX_API_KEY 环境变量")
        return None

    headers = {
        "Authorization": f"Bearer sk-NjA2LTExNzAzMDI3Mjg0LTE3NzQ1MDY5NDAzNjY=",
        "Content-Type": "application/json"
    }

    prompt = f"""
你是一个10年经验的互联网产品专家，请对产品「{product}」做系统分析。

输出必须是JSON格式，包含字段：
positioning_analysis
competitive_analysis
prd_document
opportunity_analysis

要求：
- 逻辑清晰
- 结构化输出
- 可执行
"""

    data = {
        "model": "abab6.5s-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)

        if response.status_code == 200:
            res = response.json()
            content = res["choices"][0]["message"]["content"]

            try:
                return json.loads(content)
            except:
                return {
                    "positioning_analysis": content,
                    "competitive_analysis": content,
                    "prd_document": content,
                    "opportunity_analysis": content
                }
        else:
            st.error(f"请求失败: {response.text}")
            return None

    except Exception as e:
        st.error(f"请求异常: {str(e)}")
        return None

# ===== 按钮 =====
if st.button("✨ 一键生成分析"):
    if product:
        with st.spinner("AI 正在分析中... ⏳"):
            result = fetch_product_analysis(product)

        if result:
            st.success("分析完成 ✅")

            st.markdown("## 📊 分析结果")

            with st.expander("🎯 产品定位分析", expanded=True):
                st.markdown(f'<div class="card">{result["positioning_analysis"]}</div>', unsafe_allow_html=True)

            with st.expander("⚔️ 竞品分析", expanded=True):
                st.markdown(f'<div class="card">{result["competitive_analysis"]}</div>', unsafe_allow_html=True)

            with st.expander("📄 PRD文档", expanded=True):
                st.markdown(f'<div class="card">{result["prd_document"]}</div>', unsafe_allow_html=True)

            with st.expander("💡 产品机会分析", expanded=True):
                st.markdown(f'<div class="card">{result["opportunity_analysis"]}</div>', unsafe_allow_html=True)

            # 下载 Word
            word_file = generate_word(result["prd_document"])
            with open(word_file, "rb") as file:
                st.download_button(
                    label="📥 下载Word报告",
                    data=file,
                    file_name="product_analysis.docx"
                )

            # 下载 JSON
            st.download_button(
                label="📥 下载JSON",
                data=json.dumps(result, ensure_ascii=False, indent=2),
                file_name="analysis.json"
            )
    else:
        st.warning("请输入产品名称 ❗")
