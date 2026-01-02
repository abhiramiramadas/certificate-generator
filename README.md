# 🎓 CertiPy

> **aka:** "Why manually type names when Python can suffer for you?"

A bulk certificate generator that saves you from:

* typing names 47 times
* misaligning text in Canva
* losing sanity at 2 AM before submissions

**Built because:** ✨ automation > suffering ✨

---

## 💡 What is this?

CertiPy started as a simple Python script and evolved into a **modular certificate generation system** with both:

- a **Command Line Interface (CLI)**  
- a **REST API (FastAPI)**  

* takes names from a CSV or a HTTP request
* gently places them on a pre-designed template
* organizes them into neat individual folders (because clutter is the enemy)
* exports everything as PNG and PDF
* can run as a local script or a fancy FastAPI web service
Basically:
- 👉 you give it names  
- 👉 it gives you certificates  
- 👉 everyone thinks you worked very hard  
---

## 🧠 What it does (no corporate jargon)

* **Organized Outputs:** Saves every person's certificate in their own folder like `certificates/Name_Surname/`.
* **CLI Mode:** Bulk generate from `names.csv` using a colorful terminal menu.
* **API Mode:** Run a local server to generate certificates on-demand via HTTP requests.
* **Print Ready PDFs:** Generates A4 sized PDFs automatically.

---

## 🗂️ Project Structure (The Glow Up)

```text
certificate-generator/
├── main.py                 # the boss: decides CLI vs API
├── api.py                  # talks HTTP, understands JSON
├── generator.py            # does the actual hard work
├── assets/                 # where the pretty lives (template, fonts)
├── data/                   # names.csv aka the guest list
├── certificates/           # finished products (git ignores these)
├──requirements.txt         # things Python needs to not cry
└── README.md


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
You’ll see a menu:
```
1. Run Local Bulk Generation
2. Start API Server
3. Exit
```

**OR use shortcuts like a pro:**

* **Bulk Local:** `python main.py --local`
* **Start API:** `python main.py --api`

---
***🌐 API Usage (Optional but Cool)***

Once the API is running, open:

http://localhost:8000/docs


Available endpoints:

POST /generate/solo → generate one certificate

POST /generate/bulk → generate for all names in CSV

GET /download/{safe_name} → download the PDF directly

Swagger UI lets you test everything without writing extra code.

## 👩‍💻 Authors

**Abhirami Ramadas**

B.Tech Information Technology

LBS Institute of Technology for Women

**Prakhar Doneria** (Added CLI menu, API integration, and organized file structure)

---

⭐ **If you star this repo, your code will compile on the first try.** *(Results may vary, but why take the risk?)*
