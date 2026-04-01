import streamlit as st
from utils.api import call_coze_api
from utils.formatter import format_result
from utils.docx_generator import generate_docx
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
st.set_page_config(page_title="AI PRD生成器", layout="wide")

st.title("📄 AI 产品需求文档生成器（PRD）")

# 输入
product = st.text_input("请输入产品名称", "")

if st.button("生成 PRD"):

    if not product:
        st.warning("请输入产品名称")
        st.stop()

    with st.spinner("AI 生成中..."):
        result = call_coze_api(product)

    if not result:
        st.error("生成失败")
        st.stop()

    # 格式化展示
    doc_data = format_result(result)

    st.success("生成成功 🎉")

    # 展示 UI
    st.subheader("📊 PRD 预览")

    for section in doc_data:
        st.markdown(f"## {section['title']}")
        st.write(section["content"])

    # 生成 docx
    docx_file = generate_docx(doc_data, product)

    # 下载按钮
    with open(docx_file, "rb") as f:
        st.download_button(
            label="📥 下载 Word 文档",
            data=f,
            file_name=f"{product}_PRD.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
