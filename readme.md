
---

# 🔍 SNI Checker Tool

A Python-based tool to check working **SNI (Server Name Indication)** domains from JSON lists. It verifies SSL handshake success and measures latency for valid SNIs.

---

## ✅ Features

* Check if SNI domains are valid via **SSL connection**.
* Measure latency for each valid SNI.
* Load domains from JSON files.
* Save working SNIs with latency to `working_sni.txt`.
* Simple CLI interface with color-coded output.

---

## 📂 Project Structure

```
├── dns_repo/
│   ├── facebook_data.json
│   ├── linkedin_data.json
│   ├── netflix_data.json
│   ├── whatsapp_data.json
│   ├── youtube_data.json
│   ├── zoom_data.json
│   ├── garena_data.json
│   ├── steampowered_data.json
├── working_sni.txt
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

1. **Clone the repository**

```bash
https://github.com/ravindudil5han/V2ray_SNI_checker-.git
cd V2ray_SNI_checker-
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

Run the tool:

```bash
python main.py
```

Select from the menu:

* Check a specific provider (Facebook, Netflix, etc.).
* Check all providers.
* Exit.

---

## 📝 JSON File Format

Each JSON file should contain an array of objects with the `domain` field:

```json
[
  {
    "domain": "echannelling.com.",
    "ipv4": "194.140.201.44",
    "ipv6": [],
    "mx": [
      "mail.echannelling.com.",
      "relay.lankacom.net."
    ]
  },
  {
    "domain": "mobitel.lk.",
    "ipv4": "202.129.235.14",
    "ipv6": [
      "2407:c00:0:3001::21"
    ],
    "mx": [
      "mailgw3.mobitel.lk.",
      "mailgw4.mobitel.lk.",
      "mailgw5.mobitel.lk.",
      "mailgw6.mobitel.lk."
    ]
  }
]
```

The script automatically removes the trailing dot (`.`) from domains.

---

## 📦 Output

Working SNIs are saved to `working_sni.txt` in this format:

```
example.com - 54.32ms
another.com - 76.89ms
```

---

## 🛠 Requirements

* Python 3.7+
* `colorama` (for colored CLI)

Install with:

```bash
pip install colorama
```

---

## 🔮 Future Improvements

* Add **parallel checking** for faster results.
* Add **HTTP/HTTPS content verification**.
* Improve **UI with rich or tqdm**.

---

### 👨‍💻 Author

**Dilshan**
Feel free to fork and contribute!

---
