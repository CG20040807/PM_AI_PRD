import streamlit as st
import requests
import json
import os
import datetime
from io import BytesIO
from docx import Document

# ======================
# 页面配置
# ======================
st.set_page_config(page_title="AI PM Agent", layout="wide")

# ======================
# 数据文件
# ======================
DATA_FILE = "history.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

# ======================
# Token 获取
# ======================
def get_token():
    return st.secrets.get("COZE_API_TOKEN", os.getenv("COZE_API_TOKEN", ""))

# ======================
# 历史记录
# ======================
def save_history(user, product, result):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if user not in data:
        data[user] = []

    data[user].append({
        "product": product,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "result": result
    })

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_history(user):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data.get(user, [])

# ======================
# API 调用（关键修复点）
# ======================
def call_api(product, workflow_url):
    token = get_token()

    if not token:
        st.error("❌ 未配置 COZE_API_TOKEN")
        st.stop()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # ✅ 修复点：字段必须是 product_name
    payload = {
        "product_name": product
    }

    with st.spinner("AI 分析中..."):
        res = requests.post(workflow_url, headers=headers, json=payload, timeout=600)

    if res.status_code == 200:
        try:
            return res.json()
        except:
            return {"output": res.text}
    else:
        st.error(f"请求失败: {res.text}")
        return None

# ======================
# 用户登录系统
# ======================
if "user" not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    st.title("AI Product Manager Agent")

    username = st.text_input("请输入用户名")

    if st.button("登录"):
        if username:
            st.session_state.user = username
            st.rerun()
        else:
            st.warning("请输入用户名")

    st.stop()

# ======================
# 主界面
# ======================
st.title("AI Product Manager Agent")
st.write(f"👤 当前用户：{st.session_state.user}")

# ======================
# Sidebar
# ======================
with st.sidebar:
    st.markdown("## ⚙️ 设置")

    workflow_url = st.text_input(
        "Coze 工作流地址",
        value="https://7fv2jsrt7q.coze.site/run"
    )

    if st.button("退出登录"):
        st.session_state.user = None
        st.rerun()

    st.markdown("## 📜 历史记录")

    history = load_history(st.session_state.user)

    if not history:
        st.write("暂无记录")
    else:
        for i, item in enumerate(reversed(history)):
            if st.button(f"{item['product']} - {item['time']}", key=i):
                st.session_state.selected = item

# ======================
# 输入区
# ======================
product = st.text_input("📦 输入产品名称", value="Keep")

if st.button("🚀 生成分析"):
    result = call_api(product, workflow_url)

    if result:
        save_history(st.session_state.user, product, result)

        st.success("✅ 分析完成")

        st.markdown("## 📊 分析结果")
        st.json(result)

        # 下载 JSON
        st.download_button(
            "⬇️ 下载 JSON",
            data=json.dumps(result, ensure_ascii=False, indent=2),
            file_name=f"{product}.json"
        )

# ======================
# 历史详情展示
# ======================
if "selected" in st.session_state:
    st.markdown("## 📂 历史详情")

    item = st.session_state.selected

    st.write("📦 产品：", item["product"])
    st.write("🕒 时间：", item["time"])

    st.json(item["result"])
