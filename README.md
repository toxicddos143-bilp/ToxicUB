# ⚡ NexusUB — The Ultimate Pyrogram UserBot

![NexusUB](https://img.shields.io/badge/NexusUB-2.0.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12%2B-green?style=for-the-badge)
![Commands](https://img.shields.io/badge/Commands-600%2B-orange?style=for-the-badge)

**A feature-packed Pyrogram UserBot with 600+ commands across 9 categories.**

---

## 🚀 Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Step-by-Step

1. **Fork this repo** to your GitHub account
2. **Get API credentials** from [https://my.telegram.org/apps](https://my.telegram.org/apps)
3. **Generate a String Session**: `pip install -r requirements.txt && python generate_session.py`
4. **Deploy on Render**: Create a Web Service, connect your repo, set env vars:

| Variable | Required | Description |
|----------|----------|-------------|
| `API_ID` | ✅ | Telegram API ID |
| `API_HASH` | ✅ | Telegram API Hash |
| `STRING_SESSION` | ✅ | Pyrogram string session |
| `PREFIX` | ❌ | Command prefix (default: `.`) |
| `LOG_GROUP` | ❌ | Chat ID for logs |

---

## 🖥️ Local Setup

```bash
git clone https://github.com/YOU/NexusUB.git && cd NexusUB
pip install -r requirements.txt
python generate_session.py
cp .env.sample .env  # Edit with your credentials
python main.py
```

---

## 📁 Project Structure

```
NexusUB/
├── main.py              # Entry point + Flask web server
├── config.py            # Environment handler
├── patches.py           # Python 3.12+ monkey patches
├── generate_session.py  # Session generator
├── plugins/
│   ├── __init__.py      # Dynamic plugin loader
│   ├── core.py          # 34 commands
│   ├── admin.py         # 46 commands
│   ├── fun.py           # 120 commands
│   ├── naughty.py       # 83 commands
│   ├── tools.py         # 119 commands
│   ├── text.py          # 134 commands
│   ├── spam.py          # 23 commands
│   ├── media.py         # 57 commands
│   └── system.py        # 56 commands
├── .env.sample
├── requirements.txt
├── render.yml
└── README.md
```

---

## 🐍 Python 3.12+ Compatibility

`patches.py` is imported first and patches: `cgi`, `audioop`, `imghdr` (removed in 3.13), and `asyncio.get_event_loop` deprecation.

---

## ⚠️ Disclaimer

For educational purposes only. Use responsibly and at your own risk. Telegram may ban accounts violating their ToS.

---

<div align="center">**NexusUB** — Made with ⚡</div>
