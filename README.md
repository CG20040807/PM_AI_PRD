````markdown
### 🎉 AI 产品需求文档生成器 (AI PRD Generator) 🎉

## 📝 项目概述

AI 产品需求文档生成器（AI PRD Generator）是一款创新的产品需求文档自动化生成工具，专为产品经理、团队和从业人员设计。通过简单的产品名称输入，系统能够自动生成结构化的 PRD（产品需求文档），涵盖产品定位、竞品分析、功能需求和用户故事等内容。您只需提供产品名称，系统会通过强大的 API 功能，生成全面的产品文档，并支持导出 Word 文档，轻松分享与存档。

---

## 🚀 功能特点

- **🔮 自动化生成 PRD**  
   输入产品名称，一键生成包含产品定位、竞品分析、功能需求等的结构化 PRD 文档。

- **💡 详细的产品分析**  
   深入分析产品的市场机会、潜在风险及竞品优劣势，提供全面的产品视角。

- **📥 支持文档导出**  
   自动生成并导出 Word 文档，方便保存、打印或共享给团队。

- **💻 直观的界面**  
   采用 Streamlit 构建的清晰、易操作界面，轻松展示和查看产品需求文档。

- **⏱ 提高生产力**  
   减少手动撰写 PRD 的时间，帮助团队快速生成高质量的产品需求文档。

---

## 🔧 技术栈

- **🌐 Streamlit**：构建 Web 应用，展示生成的产品需求文档。
- **🧠 Coze API**：生成结构化产品分析内容。
- **🐍 Python**：后端语言，处理 API 调用和数据格式化。
- **📄 docx**：导出产品需求文档为 Word 格式。

---

## 📥 安装指南

### 1. 克隆项目

```bash
git clone https://github.com/your-username/ai-prd-generator.git
cd ai-prd-generator
````

### 2. 创建虚拟环境并安装依赖

```bash
python3 -m venv venv
source venv/bin/activate  # 对于 Mac/Linux
venv\Scripts\activate  # 对于 Windows
pip install -r requirements.txt
```

### 3. 配置 Coze API Token

在 Streamlit 的 Secrets 配置中添加 Coze API Token：

```toml
COZE_API_TOKEN = "your_coze_api_token_here"
```

### 4. 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中启动，访问 `http://localhost:8501` 即可开始使用。

---

## 🎯 使用指南

1. **输入产品名称**：在文本框中输入要分析的产品名称（例如：小红书、抖音、Keep、ChatGPT）。
2. **生成 PRD**：点击“生成 PRD”按钮，系统将自动生成详细的产品需求文档。
3. **查看文档**：通过交互式界面，查看各部分详细内容，如产品定位、竞品分析等。
4. **下载 Word 文档**：点击“下载 Word 文档”按钮，系统将自动生成并下载完整的 PRD 文档，方便分享或存档。

---

## 🏅 示例

### 输入示例：

```txt
小红书
```

### 输出示例：

* **📍 产品定位分析**：分析产品的核心功能、目标用户群体等。
* **📊 竞品分析**：列举并对比主要竞品，展示各自优劣势。
* **🔧 PRD 文档**：包含功能需求、用户故事、验收标准等详细内容。
* **🌟 市场机会分析**：总结产品的创新机会和市场潜力。
### 使用截图：
<img width="1893" height="941" alt="屏幕截图 2026-04-01 225146" src="https://github.com/user-attachments/assets/89e00f56-8929-421a-bd40-c2c92dc78ba7" />

<img width="1916" height="993" alt="屏幕截图 2026-04-01 225134" src="https://github.com/user-attachments/assets/64e7e16b-f470-4e3a-848c-f18915912351" />

<img width="1897" height="1033" alt="屏幕截图 2026-04-01 225116" src="https://github.com/user-attachments/assets/f26d1410-d52d-452c-a748-7dbd29d7110e" />

### 下载：

用户可以一键下载生成的完整报告，报告为 Word 文档格式，方便存档和共享。

---

## 💡 贡献指南

我们欢迎大家为该项目贡献代码、报告 bug 或提出新功能建议。如果你想参与贡献，请按以下步骤进行：

### 贡献步骤：

1. Fork 本仓库
2. 创建新的分支 (`git checkout -b feature-branch`)
3. 提交修改 (`git commit -am 'Add new feature'`)
4. 推送到分支 (`git push origin feature-branch`)
5. 创建 Pull Request

---

## 📜 许可证

该项目采用 [MIT 许可证](LICENSE)，你可以自由使用、修改或分发代码。

---

## 🎉 支持与致谢

感谢你对 AI PRD Generator 的关注和支持！如果你喜欢这个项目，请给我们一个 ⭐️ 星标支持，帮助更多人发现这个工具！

---

## 🏆 关注我们

* [GitHub](https://github.com/your-username/ai-prd-generator)
* [Twitter](https://twitter.com/your-username)
* [LinkedIn](https://www.linkedin.com/in/your-profile)

---

感谢使用！🚀

```
