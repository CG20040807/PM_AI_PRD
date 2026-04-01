import requests

COZE_URL = "https://7fv2jsrt7q.coze.site/run"
TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjY0MmFmZTQ3LTA0NTYtNDlmNi1hNTliLWU5OTY3ZTliOWFlMiJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc1MDUzMTE3LCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIzNzk1MDg5NTQxNjkzNDUwIn0.V2V5hLo2X1fr2G_hUiku1XX52KhcvtO7-U2pgEcqhAl_1730rHiNWm29ZkoAAo2FV7ZabTu59JaZkv8oqCZ7DA3RMjLrpZ4nHY_F2uGjUllOpHDRqrlZ18N2ZuhZXMQ1lya_75X0jcC9fKEk3ye2ZyD333VGlmHxlq4FEtc9GczqDBCIi0sBgtygQRDu2lBDOUYWLaayS81XbEQCIEW2yt9R3VM5peO9EoJ0do_5He7IiZSf4CFmgtqIg7oUuH_33Dg9kLBQj-lDHMp5lw66KwwJybTuMK3e1LW5AfA_eBGtQaeilifpzBmpz3AHwiSPxvos3dzKz4gf4YdbB01syw"  # 🔴 这里填你的 token

def call_coze_api(product_name):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "product_name": product_name
    }

    try:
        res = requests.post(
            COZE_URL,
            headers=headers,
            json=payload,
            timeout=300
        )

        res.raise_for_status()
        return res.json()

    except Exception as e:
        print("API ERROR:", e)
        return None
