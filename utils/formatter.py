import json

def format_result(result):

    # 如果是字符串先转json
    if isinstance(result, str):
        try:
            result = json.loads(result)
        except:
            return [{"title": "结果", "content": result}]

    data = result.get("data") or result.get("output") or result

    def get_val(keys):
        for k in keys:
            if isinstance(data, dict) and k in data:
                val = data[k]

                if isinstance(val, (dict, list)):
                    return json.dumps(val, ensure_ascii=False, indent=2)

                return str(val)

        return "暂无数据"

    return [
        {"title": "一、产品定位", "content": get_val(["positioning_analysis"])},
        {"title": "二、竞品分析", "content": get_val(["competitive_analysis"])},
        {"title": "三、产品机会", "content": get_val(["opportunity_analysis"])},
        {"title": "四、PRD设计", "content": get_val(["prd_document"])}
    ]
