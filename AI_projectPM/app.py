import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI Product Manager Agent",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

body {
background-color:#f5f7fb;
}

.title {
font-size:48px;
font-weight:700;
text-align:center;
}

.subtitle {
text-align:center;
color:gray;
margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 AI Product Manager Agent</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">输入产品名称，自动生成PRD和竞品分析</div>', unsafe_allow_html=True)

product = st.text_input("输入产品名称", placeholder="例如：抖音")

generate = st.button("生成产品分析")

if generate and product:

    with st.spinner("AI正在分析产品..."):

        url = "https://7fv2jsrt7q.coze.site/run"

        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjgyYTVkLWJlMmUtNDViOS1hODFkLWM4ZGI3MTU5MmExOSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NDQ1MjMxLCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxMTg0MjM3Mzg2ODU4NTQyIn0.pSr_emMr3DmyZBp1Ly2ckrzO-4_Ta_UFoGrPIrrMJGsZEY1KHVtByBzSh0jnoxSGeWuxplUNxQ4T35k81HF4meDxipFUSp3kWVifNoGJZIuv3_ZqKiN4gMZvtArtMWa8YdlWe8I_e5H0EDSc3sLQ_JMvG61OsVLWX6Ppv_8ANCRoErYUMD8GPa4z96Z_vmATKO16IdcR5MDbdc9ReF-S6NdDnYOfP-GCFIR14vDuiApW1rmgk-awGHhRv--gyE2DFrdQnRNJLqm9GIn8jTm9HXE6vg86m8zty3obf3RQlYjI0MfoKC0syTWUyaWxVRbyiMqfyq2mkb5oJQjjL-jPkA",
            "Content-Type": "application/json"
        }

        data = {
            "product_name": product
        }

        response = requests.post(url, headers=headers, json=data)

        result = response.json()

    st.success("分析完成")

    st.markdown("## 📊 AI分析结果")

    with st.expander("🎯 产品定位分析", expanded=True):
        st.write(result["positioning_analysis"])

    with st.expander("⚔️ 竞品分析"):
        st.write(result["competitive_analysis"])

    with st.expander("📄 PRD文档"):
        st.write(result["prd_document"])

    with st.expander("💡 产品机会分析"):
        st.write(result["opportunity_analysis"])

    st.download_button(
        "📥 下载PRD",
        json.dumps(result, ensure_ascii=False, indent=2),
        file_name="prd_analysis.json"
    )
