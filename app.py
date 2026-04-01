import streamlit as st
import json
import os

from utils.api import call_coze_api
from utils.formatter import format_result
from utils.docx_generator import generate_docx

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="AI PRD Generator",
    page_icon="📄",
    layout="wide"
)

# ======================
# 样式（优化）
# ======================
st.markdown("""
<style>
.main-title {
    font-size: 34px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 8px;
}

.sub-title {
    text-align: center;
    color: gray;
    margin-bottom: 25px;
}

.block {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #eee;
    margin-bottom: 20px;
}

.card {
    padding: 14px;
    border-radius: 8px;
    background-color: #ffffff;
    border-left: 4px solid #000;
    margin-bottom: 8px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ======================
# 标题
# ======================
st.markdown('<div class="main-title">📄 AI 产品需求文档生成器</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">输入产品名称，一键生成结构化 PRD（可导出）</div>', unsafe_allow_html=True)

# ======================
# ⭐ 新增：内容结构化渲染函数（核心）
# ======================
def render_content(content: str):
    if not content:
        st.markdown('<div class="card">暂无内容</div>', unsafe_allow_html=True)
        return

    lines = content.split("\n")

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # 小标题（###）
        if line.startswith("###"):
            st.markdown(f"**{line.replace('###', '').strip()}**")

        # 列表（-）
        elif line.startswith("-"):
            st.markdown(f"- {line[1:].strip()}")

        # 普通段落
        else:
            st.markdown(f"<div class='card'>{line}</div>", unsafe_allow_html=True)

# ======================
# 输入区域（居中）
# ======================
with st.container():
    st.markdown('<div class="block">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        product = st.text_input("📦 产品名称", placeholder="例如：小红书 / 抖音 / Keep / ChatGPT")
        generate = st.button("✨ 生成 PRD", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ======================
# 主逻辑
# ======================
if generate:

    if not product.strip():
        st.warning("请输入产品名称")
        st.stop()

    # 调用 Coze
    with st.spinner("AI 生成中，请稍候..."):
        result = call_coze_api(product.strip())

    if not result:
        st.error("生成失败，请检查 API 或工作流")
        st.stop()

    # 格式化
    doc_data = format_result(result)

    st.success("生成成功 🎉")

    # ======================
    # ⭐ PRD展示（重点优化）
    # ======================
    st.markdown("## 📊 PRD 预览")

    for section in doc_data:
        with st.expander(f"📌 {section['title']}", expanded=True):
            render_content(section["content"])

    # ======================
    # Word 导出
    # ======================
    docx_file = generate_docx(doc_data, product)

    with open(docx_file, "rb") as f:
        st.download_button(
            label="📥 下载 Word 文档",
            data=f,
            file_name=f"{product}_PRD.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )

# ======================
# 默认提示
# ======================
else:
    st.info("👆 输入产品名称并点击【生成 PRD】开始")
