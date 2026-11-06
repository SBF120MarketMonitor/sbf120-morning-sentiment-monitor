# SBF120 Morning Sentiment Monitor — Reddit API access request

This repository is a **minimal, public-facing demonstration** for a request to use Reddit's Data API. It is **not** the full SBF120 trading/news agent and does **not** claim to have working Reddit access.

## Purpose

A personal, read-only Python research application running on Windows. The planned integration would retrieve authorized public Reddit posts mentioning Euronext Paris companies (initially Airbus, LVMH, L'Oréal, Schneider Electric, TotalEnergies, Sanofi, BNP Paribas, AXA, Vinci, and Safran). It would examine posts published after the previous Euronext Paris closing session and before 08:55 Europe/Paris, aggregate sentiment at company level, and compare it with separately sourced financial news.

## Proposed API access

- Read-only searches of public posts across relevant communities, subject to permissions Reddit grants.
- Only post IDs, titles, timestamps, subreddit names, and text necessary for sentiment analysis.
- No posting, voting, messaging, moderation, user profiling, or AI model training.
- No redistribution of raw Reddit datasets.
- Rate limits, retention, deletions, and other Reddit conditions will be respected.
- If access is denied or results are unavailable, sentiment is `N/D` (not zero).

## Status

**Awaiting Reddit Data API approval.** The `reddit_oauth_demo.py` script demonstrates a token request and one read-only API call; it does not bypass access restrictions and is not a production collector. The actual SBF120 application is maintained separately and is not included in this repository.

## Setup (after Reddit approval)

Python 3.10+ is required. The script uses only the Python standard library. In PowerShell, set credentials for an OAuth client permitted to use the `client_credentials` grant:

```powershell
$env:REDDIT_CLIENT_ID = Read-Host 'Reddit client ID'
$env:REDDIT_CLIENT_SECRET = Read-Host 'Reddit client secret'
$env:REDDIT_USER_AGENT = 'windows:sbf120-sentiment-monitor:demo (contact: your-reddit-username)'
python .\reddit_oauth_demo.py
```

**Important:** The OAuth grant type and endpoints must match the permissions and application type approved by Reddit. A token does not itself grant access to restricted endpoints. Never commit credentials or token values.

## Example output

```text
OAuth token obtained: True
API status: 200
```

This is an **illustrative** response, not a claim of successful Reddit API access. If Reddit returns 401/403/429, the script reports the status and does not retry or circumvent the restriction.

## Security

No real API credentials, personal data, financial databases, or collected Reddit data are included. See `.gitignore`.
