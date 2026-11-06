"""Minimal read-only Reddit OAuth demonstration; requires Reddit approval.

Uses the client_credentials flow ONLY if authorized for the registered client.
Never prints tokens or secrets. Does not scrape or bypass API restrictions.
"""
import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request


def request(url, *, data=None, headers=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # Do not print response bodies: they could contain sensitive information.
        return exc.code, None


def main():
    client_id = os.getenv("REDDIT_CLIENT_ID", "")
    secret = os.getenv("REDDIT_CLIENT_SECRET", "")
    agent = os.getenv("REDDIT_USER_AGENT", "")
    if not (client_id and secret and agent):
        raise SystemExit("Set REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET and REDDIT_USER_AGENT.")
    basic = base64.b64encode(f"{client_id}:{secret}".encode()).decode()
    status, payload = request(
        "https://www.reddit.com/api/v1/access_token",
        data=urllib.parse.urlencode({"grant_type": "client_credentials"}).encode(),
        headers={
            "Authorization": f"Basic {basic}",
            "User-Agent": agent,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )
    if status != 200 or not isinstance(payload, dict) or not payload.get("access_token"):
        print(f"OAuth token request failed: HTTP {status}. Check approved API access and OAuth client type.")
        return
    print("OAuth token obtained: True")
    # Example public listing, subject to permissions; not a bulk search.
    api_status, _ = request(
        "https://oauth.reddit.com/r/stocks/new?limit=1",
        headers={
            "Authorization": f"Bearer {payload['access_token']}",
            "User-Agent": agent,
        },
    )
    print(f"API status: {api_status}")
    if api_status != 200:
        print("API access not confirmed; do not retry automatically or bypass restrictions.")


if __name__ == "__main__":
    main()
