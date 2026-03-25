import streamlit as st
import requests

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

.card {
padding:25px;
border-radius:12px;
background:white;
box-shadow:0px 4px 15px rgba(0,0,0,0.05);
margin-bottom:20px;
}

.generate-button button{
width:100%;
height:50px;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 AI Product Manager Agent</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">输入产品名称，自动生成PRD、用户画像、竞品分析</div>', unsafe_allow_html=True)

product = st.text_input("输入产品名称", placeholder="例如：抖音")

generate = st.button("生成产品分析")

if generate and product:

    with st.spinner("AI正在分析产品..."):

        url = "https://7fv2jsrt7q.coze.site/run"

        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkMjgyYTVkLWJlMmUtNDViOS1hODFkLWM4ZGI3MTU5MmExOSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc0NDQzODQyLCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIxMTc4MjczODg3NjgyNTYwIn0.lfFXpK9UGxs1us52Uu-rq8GhjGxAeVPYGlVEYKhEYAt8HOF8nuXPonZDJRIe7fPFFRFzTpzifh-t6Tvb-lnHiF_53IGH5_rsX5jBEHVy6Ig6etUCpT68QWHVJjPVq_QqgVHRNqZoqCVSE_IH80D6qSPXCDB3Ls3jZvqtaXLElzMSX8pBsWQI0tL8jXJT8Nbt9ImjNBMOzTL20W6gOj2LDE0T1TWM2TyvlCpEXIICqNYZm_pmp1zAUkCw2lfea9bV9st0HsHOgS1lxKscnedphhf0CLUt73WdAHgYzIIQs8tQPtVS6AssdNrAzc_Q-5jcIybsGKYdFJl6-XH9IUeHig",
            "Content-Type": "application/json"
        }

        data = {
            "product_name": product
        }

        response = requests.post(url, headers=headers, json=data)

        result = response.text

    st.success("分析完成")

    st.markdown("## 📊 AI分析结果")

    st.markdown(
        f'<div class="card">{result}</div>',
        unsafe_allow_html=True
    )

    st.download_button(
        "📥 下载PRD文档",
        result,
        file_name="product_analysis.md"
    )

else:

    st.markdown("")

st.markdown("---")

st.markdown(
"""
### ✨ 功能

- 自动生成 **PRD**
- 分析 **用户画像**
- 输出 **竞品分析**
- 生成 **产品商业模式**
- 一键下载产品文档
"""
)