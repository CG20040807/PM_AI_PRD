from docx import Document
from docx.shared import Pt

def clean_text(text: str):
    """
    清理 markdown 符号
    """
    if not text:
        return ""

    text = text.replace("*", "")
    text = text.replace("-", "")
    text = text.replace("#", "")
    return text.strip()


def generate_docx(doc_data, product_name):
    doc = Document()

    # 标题
    title = doc.add_heading(f"{product_name} - PRD 文档", 0)

    for section in doc_data:

        # 一级标题
        doc.add_heading(section["title"], level=1)

        content = section.get("content", "")

        if not content:
            doc.add_paragraph("暂无内容")
            continue

        # 按行拆分
        lines = content.split("\n")

        for line in lines:
            line = clean_text(line.strip())

            if not line:
                continue

            # 子标题（###）
            if line.startswith("###"):
                doc.add_heading(line.replace("###", "").strip(), level=2)

            # 列表
            elif line.startswith("-"):
                p = doc.add_paragraph(line.replace("-", "").strip())
                p.style = "List Bullet"

            else:
                doc.add_paragraph(line)

    file_path = f"{product_name}_PRD.docx"
    doc.save(file_path)

    return file_path
