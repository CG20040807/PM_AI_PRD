def format_result(result_json):
    """
    把 Coze 返回的 JSON 转换为结构化文档
    """

    # 这里根据你的 Coze 输出结构调整
    # 假设返回类似：
    # {
    #   "title": "...",
    #   "sections": [...]
    # }

    doc = []

    if "title" in result_json:
        doc.append({
            "title": "标题",
            "content": result_json["title"]
        })

    if "sections" in result_json:
        for sec in result_json["sections"]:
            doc.append({
                "title": sec.get("name", "模块"),
                "content": sec.get("content", "")
            })

    # fallback（防止结构不一致）
    if not doc:
        doc.append({
            "title": "原始输出",
            "content": str(result_json)
        })

    return doc
