# 🎓 CertiPy

> **aka:** "Why manually type names when Python can suffer for you?"

A bulk certificate generator that saves you from:

* typing names 47 times
* misaligning text in Canva
* losing sanity at 2 AM before submissions

**Built because:** ✨ automation > suffering ✨

---

## 💡 What is this?

CertiPy is a modular Python powerhouse that:

* takes names from a CSV or a web request
* gently places them on a pre-designed template
* organizes them into neat individual folders (because clutter is the enemy)
* exports everything as PNG and PDF
* can run as a local script or a fancy FastAPI web service

---

## 🧠 What it does (no corporate jargon)

* **Organized Outputs:** Saves every person's certificate in their own folder like `certificates/Name_Surname/`.
* **CLI Mode:** Bulk generate from `names.csv` using a colorful terminal menu.
* **API Mode:** Run a local server to generate certificates on-demand via web requests.
* **Print Ready:** Generates A4 sized PDFs automatically.

---

## 🗂️ Project Structure (The Glow Up)

```text
certificate-generator/
├── main.py                 # The master switch (CLI + Menu)
├── api.py                  # The web brain (FastAPI)
├── generator.py            # The heavy lifter (Core logic)
├── assets/                 # Pretty things (template.png, fonts)
├── data/                   # The list of victims (names.csv)
├── certificates/           # The output (neatly filed away)
└── requirements.txt        # The shopping list

```

---

## ▶️ How to Run (Low Effort Edition)

### 1️⃣ Setup (Do this once)

```bash
python setup.py

```

### 2️⃣ Run the Magic

Just run the main file and follow the colored menu:

```bash
python main.py

```

**OR use shortcuts like a pro:**

* **Bulk Local:** `python main.py --local`
* **Start API:** `python main.py --api`

---

## 👩‍💻 Authors

**Abhirami Ramadas**

B.Tech Information Technology

LBS Institute of Technology for Women

**Prakhar Doneria** (Added CLI menu, API integration, and organized file structure)

---

⭐ **If you star this repo, your code will compile on the first try.** *(Results may vary, but why take the risk?)*