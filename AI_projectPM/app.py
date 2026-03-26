import streamlit as st
import requests
import json
from docx import Document
from io import BytesIO

# 页面配置
st.set_page_config(
    page_title="AI Product Manager Agent",
    page_icon="🚀",
    layout="wide"
)

# 页面标题
st.markdown('<div class="title">🚀 AI Product Manager Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">输入产品名称，自动生成PRD和竞品分析</div>', unsafe_allow_html=True)

# 产品名称输入框
product = st.text_input("输入产品名称", placeholder="例如：抖音")

# Word生成
def generate_word(text):
    doc = Document()
    doc.add_heading("AI 产品分析报告", 0)
    doc.add_paragraph(text)
    file = "prd_report.docx"
    doc.save(file)
    return file

# 请求API并生成分析报告
def fetch_product_analysis(product):
    url = "https://7fv2jsrt7q.coze.site/run"  # 你的API地址
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImFlNGZkZTBhLWUzZWItNGRkYi1iYWEzLTg0MzY3MzcyZmQ2ZSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NTAyOTU5LCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxNDMyMTc2OTIzMzc3NzAyIn0.FAxF_gfZivpOKuBWCwr6Rc9LvdptUoChcrKfHB_RRUOaz9OSlvPBTpa-LZW3HSPPLl9ipRWnuSceYWbjXL9CiU8jje9SyaxEN76N79MkTufL39nIseP4korE-R_sEGy71XzTtbKuqcZPwxIVqVKNmlk5V_oxk9RnxF3l77PU2EMT11hx9gjoyPXZblcRq45-oJSvccFttCR818kKVi9wv6kYaWATCJZ0CPfwV0DaCKldRJ0K2WVj0VmRS3u0cJsKBvjqPItUR2tQGPSpzW7ITDZjdO5DFOEKkSfjL9wWEih_t9Qvqagf-8vaKa8wFP-f8VT2uwMdjntcQ87TTWxq2Q",  # 使用你自己的API key
        "Content-Type": "application/json"
    }

    data = {
        "product_name": product
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # 返回JSON格式的报告数据
    else:
        st.error("请求失败，请重试。")
        return None

# 一键生成分析报告
if st.button("生成分析"):
    if product:
        with st.spinner("正在生成分析报告..."):
            # 调用API获取分析结果
            result = fetch_product_analysis(product)

            if result:
                st.success("分析完成")

                # 输出报告
                st.markdown("## 📊 AI分析结果")
                st.markdown(f'<div class="card">{json.dumps(result, ensure_ascii=False, indent=2)}</div>', unsafe_allow_html=True)

                # 产品定位分析展示
                with st.expander("🎯 产品定位分析", expanded=True):
                    st.write(result["positioning_analysis"])

                # 竞品分析展示
                with st.expander("⚔️ 竞品分析", expanded=True):
                    st.write(result["competitive_analysis"])

                # PRD文档展示
                with st.expander("📄 PRD文档", expanded=True):
                    st.write(result["prd_document"])

                # 产品机会分析展示
                with st.expander("💡 产品机会分析", expanded=True):
                    st.write(result["opportunity_analysis"])

                # Word文件下载按钮
                word_file = generate_word(result["prd_document"])  # 生成Word文件
                with open(word_file, "rb") as file:
                    st.download_button(
                        label="下载Word版本报告",
                        data=file,
                        file_name="product_analysis_report.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                # JSON下载按钮
                st.download_button(
                    label="下载PRD JSON版本",
                    data=json.dumps(result, ensure_ascii=False, indent=2),
                    file_name="prd_analysis.json",
                    mime="application/json"
                )

            else:
                st.error("无法生成报告，请检查输入或API设置。")
    else:
        st.warning("请输入产品名称！")
