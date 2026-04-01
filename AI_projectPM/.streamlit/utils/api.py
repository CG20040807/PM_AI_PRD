import requests

COZE_URL = "https://7fv2jsrt7q.coze.site/run"
TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjY0MmFmZTQ3LTA0NTYtNDlmNi1hNTliLWU5OTY3ZTliOWFlMiJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb3plLmNuIiwiYXVkIjpbInhEUHIydXZyQ053SGlobmU3WWdqNmF4Y09xTWd3RUxIIl0sImV4cCI6ODIxMDI2Njg3Njc5OSwiaWF0IjoxNzc1MDE2NTg1LCJzdWIiOiJzcGlmZmU6Ly9hcGkuY296ZS5jbi93b3JrbG9hZF9pZGVudGl0eS9pZDo3NjIxMTI5OTQ4MTAyNjU2MDM0Iiwic3JjIjoiaW5ib3VuZF9hdXRoX2FjY2Vzc190b2tlbl9pZDo3NjIzNjM4MTg0ODA2NTgwMjY2In0.A4t2z9uDoQElzP_fJfAeSDSfxNJHlIsjr2ztsWM8tEaIbS3gG6-ziek-Z__QIgqd6pCfT4oZ0exdvzxshZ-2p4iWhzycxwztK_Kr43dR8JvBGOMP5baj1xgC5Hyrx336ZE0zz9vgcnfAdpz9WtxOfIZ-AZKYZbdZkvUgIR2yeoIi9cjFfVC9Ihj1GP0i_VgojjhWmZxqtkxR4V6A171YICQzFykXX3p6qYBAZEJ7nJb3BThk9iAdDCjhk9tx9uT_h7cwYXxy9taMbxTZ5BlO1LO07hNHogRDnhtgp6PlEJ_Et0Ldf2beVMCz1t9uWDiUtvg6nD9gD0j3TIcApUrU9g"  # 🔴 这里填你的 token

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
