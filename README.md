# 🎓 CertiPy

> **aka:** "Why manually type names when Python can suffer for you?"

A bulk certificate generator that saves you from:
- typing names 47 times
- misaligning text in Canva
- losing sanity at 2 AM before submissions

**Built because:**  
✨ automation > suffering ✨

---

## 💡 What is this?

CertiPy is a Python script that:
- takes names from a CSV file
- gently places them on a pre-designed certificate
- exports everything as PNG and PDF
- does not judge spelling mistakes (unlike professors)

**Basically:**
> 👉 you give it names  
> 👉 it gives you certificates  
> 👉 everyone thinks you worked very hard

---

## 🧠 What it does (no corporate jargon)

- Reads names from `names.csv`
- Uses a Canva-made certificate template (because design is hard)
- Centers names perfectly (after emotional debugging)
- Uses a fancy script font so it looks ✨official✨
- Exports:
  - **PNG** (for sharing)
  - **PDF** (for printing & authority vibes)

---

## 🧪 Tech Stack (for GitHub credibility)

| Thing | Why it exists |
|-------|---------------|
| **Python** | personality choice |
| **Pillow** | writes text without complaining |
| **Pandas** | reads CSV like a champ |
| **ReportLab** | converts images to PDFs like magic |
| **Canva** | because I'm not designing borders in CSS |

---

## 🗂️ Project Structure (organized, surprisingly)

```
certificate-generator/
├── generate.py                 # the brain
├── template.png                # the pretty background
├── names.csv                   # where the victims are listed
├── GreatVibes-Regular.ttf      # fancy font, very important
├── certificates/               # output (ignored by git)
└── README.md                   # you're reading this
```

---

## ▶️ How to Run (low effort edition)

### 1️⃣ Install dependencies

```bash
pip install pillow pandas reportlab
```

### 2️⃣ Add names to `names.csv`

```csv
name
Abhirami Ramadas
Meera K
Anu S
```

### 3️⃣ Run the script

```bash
python generate.py
```

### 4️⃣ Look inside `certificates/`

Feel accomplished.

---

## 🎨 Customization (because control issues)

- **Change name position** → edit `name_y` in `generate.py`
- **Change font size** → tweak the number (trial & error + vibes)
- **Change template** → replace `template.png`
- **Want chaos?** → try Comic Sans (not recommended)

---

## 📉 Known Issues (aka realism)

- Long names may stretch the universe
- Script fonts are dramatic
- If the name disappears, it's probably off-canvas (been there)

---

## 🤡 Why this project exists

Because:
- typing names is boring
- Canva alignment is deceptive
- automation feels powerful
- I wanted a clean GitHub repo for once

---

## 👩‍💻 Author

**Abhirami Ramadas**  
B.Tech Information Technology  
LBS Institute of Technology for Women

Built with:
- curiosity
- mild panic
- several Git mistakes (now resolved)

---

## ⭐ 

**If you star this repo, future certificates will align on the first run.**

No promises, but the odds improve.

---

> If you want, I can:
> - Rewrite it **even more chaotic**
> - Tone it down slightly for recruiters
> - Make a **LinkedIn post** announcing this project in the same vibe
> 
> Just tell me 😌✨
