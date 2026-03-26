import openai
import streamlit as st
from docx import Document
from io import BytesIO

# 设置 OpenAI API Key
openai.api_key = "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"  # 请替换成你的 API Key

# 页面配置
st.set_page_config(
    page_title="AI Product Manager",
    page_icon="🚀",
    layout="wide"
)

# 页面标题
st.title("🚀 AI Product Manager Workspace")
st.subheader("输入产品信息，自动生成智能化的报告、用户画像、竞品分析、PRD与产品路线图")

# 用户输入部分：产品名称（带占位符提示）
product_name = st.text_input("请输入产品名称", placeholder="例如：抖音、Zoom等")

# 核心功能输入框（带占位符提示）
product_features = st.text_area(
    "请输入产品的核心功能",
    placeholder="例如：视频分享，社交互动，直播功能"
)

# 目标用户群体输入框（带占位符提示）
user_persona = st.text_input("请输入目标用户群体", placeholder="例如：Z世代、年轻职场")

# 动态生成产品定位的函数
def generate_product_positioning(product_name, product_features, user_persona):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
生成一份关于产品 {product_name} 的定位报告。
目标用户群体：{user_persona}
核心功能：{product_features}

请详细描述以下内容：
1. 产品定位：包括产品的市场定位、核心价值、目标用户需求等。
2. 竞争优势：描述产品与竞争对手相比的优势与独特卖点。
3. 市场机会：在当前市场环境下，产品的机会与潜力。
            """,
            max_tokens=500,
            temperature=0.7
        )
        output_text = response['choices'][0]['text'].strip()
        return output_text
    except Exception as e:
        return f"An error occurred: {e}"

# 动态生成用户画像的函数
def generate_user_persona(user_persona, product_name, product_features):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
根据产品名称 {product_name} 和核心功能 {product_features}，生成目标用户画像。
目标用户群体：{user_persona}
要求包括：用户的基本信息、需求、使用场景、偏好等。
            """,
            max_tokens=300,
            temperature=0.7
        )
        user_persona_text = response['choices'][0]['text'].strip()
        return user_persona_text
    except Exception as e:
        return f"An error occurred while generating user persona: {e}"

# 动态生成竞品分析的函数
def generate_competitor_analysis(product_name):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
生成一个关于产品 {product_name} 的竞品分析报告。

请列举并分析以下内容：
1. 主要竞品产品
2. 竞品的核心功能
3. 各竞品的市场表现和竞争优势
4. 产品与竞品的对比分析
            """,
            max_tokens=500,
            temperature=0.7
        )
        competitor_analysis_text = response['choices'][0]['text'].strip()
        return competitor_analysis_text
    except Exception as e:
        return f"An error occurred while generating competitor analysis: {e}"

# 动态生成产品路线图的函数
def generate_roadmap(product_features):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
根据以下产品功能 {product_features}，生成产品开发的 12 个月路线图，包括关键阶段和里程碑。
            """,
            max_tokens=200,
            temperature=0.6
        )
        roadmap_text = response['choices'][0]['text'].strip()
        return roadmap_text
    except Exception as e:
        return f"An error occurred while generating roadmap: {e}"

# 一键生成报告的部分
if st.button("一键生成报告", key="generate_report"):
    if product_name and product_features and user_persona:
        with st.spinner("正在生成报告，请稍候..."):
            # 生成产品定位
            product_positioning = generate_product_positioning(product_name, product_features, user_persona)
            
            # 显示产品定位报告
            st.markdown("## 📄 产品定位")
            st.write(product_positioning)

            # 生成用户画像
            user_persona_text = generate_user_persona(user_persona, product_name, product_features)
            
            # 显示用户画像
            st.markdown("## 👤 用户画像")
            st.write(user_persona_text)

            # 生成竞品分析
            competitor_analysis = generate_competitor_analysis(product_name)
            
            # 显示竞品分析
            st.markdown("## 📊 竞品分析")
            st.write(competitor_analysis)

            # 生成动态 Roadmap
            dynamic_roadmap = generate_roadmap(product_features)
            
            # 显示动态生成的 Roadmap
            st.markdown("## 🗺 产品 Roadmap")
            st.write(dynamic_roadmap)

            # 生成 Word 版本 PRD 报告
            doc = Document()
            doc.add_heading(f"{product_name} 产品分析报告", 0)
            doc.add_paragraph(product_positioning)
            doc.add_paragraph(user_persona_text)
            doc.add_paragraph(competitor_analysis)
            doc.add_paragraph(dynamic_roadmap)

            # 保存为 Word 文件
            word_file = "product_report.docx"
            doc.save(word_file)

            # 读取并展示 Word 文件内容
            with open(word_file, "rb") as file:
                file_content = file.read()

            # 读取并展示 Word 文档内容（直接显示为文本）
            doc_text = ""
            doc = Document(BytesIO(file_content))
            for para in doc.paragraphs:
                doc_text += para.text + "\n"

            # 显示文档内容
            st.markdown("## 📜 Word 报告预览")
            st.write(doc_text)

            # 下载 Word 版本报告按钮
            st.download_button(
                label="下载Word版报告",
                data=file_content,
                file_name=word_file,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="download_word"
            )
    else:
        st.warning("请输入完整的产品信息！")
