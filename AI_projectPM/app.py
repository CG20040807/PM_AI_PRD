import streamlit as st
import requests
from docx import Document
import openai

# 设置你的 OpenAI API Key
openai.api_key = "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"

# 页面配置
st.set_page_config(
    page_title="AI Product Manager",
    page_icon="🚀",
    layout="wide"
)

# 页面标题
st.title("🚀 AI Product Manager Workspace")
st.subheader("输入产品名称，自动生成智能化的 PRD、用户画像、竞品分析与产品路线图")

# 用户输入部分：产品名称
product_name = st.text_input("请输入产品名称", "")

# 产品领域选择
product_category = st.selectbox(
    "选择产品领域",
    ["选择领域", "互联网产品", "教育科技", "金融科技", "娱乐", "医疗健康", "其他"]
)

# 用户画像选择
user_persona = st.radio(
    "选择目标用户群体",
    ("Z世代", "年轻职场", "教育需求用户", "娱乐爱好者", "家庭用户", "其他")
)

# 产品功能输入框
product_features = st.text_area(
    "请输入产品的核心功能",
    "例如：视频分享，社交互动，直播功能"
)

# 调用OpenAI API并生成报告的函数
def generate_dynamic_report(product_name, product_category, user_persona, product_features):
    try:
        # 生成Haiku报告，调用OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",  # GPT-3 模型，可以改为你想用的其他模型
            prompt=f"Write a detailed product analysis report for the product named {product_name} in the field of {product_category} targeting {user_persona} users. Core features: {product_features}. Include product positioning, user persona, competitive analysis, and roadmap.",
            max_tokens=500,  # 根据需求调整返回长度
            temperature=0.7
        )
        
        # 获取返回的文本
        output_text = response.choices[0].text.strip()
        
        return output_text
    except Exception as e:
        # 错误处理
        return f"An error occurred: {e}"

# 生成报告的部分
if st.button("生成动态报告", key="generate_report"):
    if product_name and product_category != "选择领域" and user_persona != "其他" and product_features:
        with st.spinner("正在生成报告，请稍候..."):
            # 生成动态报告
            dynamic_report = generate_dynamic_report(product_name, product_category, user_persona, product_features)
            
            # 显示动态生成的报告
            st.markdown("## 📄 生成的产品报告")
            st.write(dynamic_report)

            # 下载按钮（文本版）
            st.download_button(
                label="下载动态报告 (文本版)",
                data=dynamic_report,
                file_name="dynamic_product_report.txt",
                mime="text/plain",
                key="download_txt"
            )
            
            # 生成Word版本PRD报告
            doc = Document()
            doc.add_heading(f"{product_name} 产品分析报告", 0)
            doc.add_paragraph(dynamic_report)

            # 保存为 Word 文件
            word_file = "product_report.docx"
            doc.save(word_file)

            # 下载Word版本报告按钮
            st.download_button(
                label="下载Word版报告",
                data=open(word_file, "rb").read(),
                file_name=word_file,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="download_word"
            )
    else:
        st.warning("请输入完整的产品信息！")

# 竞品对比：动态生成表格
st.markdown("## 📊 动态竞品分析")

# 示例竞品数据（动态生成）
competitors_data = {
    "产品": ["抖音", "快手", "B站", "优酷"],
    "核心功能": ["短视频", "短视频", "视频社区", "视频播放"],
    "用户群体": ["大众", "下沉市场", "年轻人", "家庭用户"],
    "优势": ["推荐算法强", "社交关系强", "内容质量高", "视频质量好"],
    "劣势": ["内容重复", "UI较旧", "增长慢", "广告较多"]
}

import pandas as pd
df = pd.DataFrame(competitors_data)
st.dataframe(df)

# 产品 Roadmap：简易列表展示
st.markdown("## 🗺 产品 Roadmap")

roadmap = """
- **V1**：产品原型设计，用户调研
- **V2**：核心功能开发，测试与优化
- **V3**：商业化模块，付费功能
- **V4**：用户扩展，营销与推广
"""

st.write(roadmap)
