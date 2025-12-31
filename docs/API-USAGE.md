# 🌐 CertiPy API Usage

So you want to use the API? Great choice. No more CLI, just pure HTTP vibes.

## 🚀 Getting Started

1. **Start the server**: Run `python main.py --api`.
2. **Endpoint Base**: The server lives at `http://localhost:8000`.

---

## 🛠️ Endpoints

### 1. Solo Generation

Generate a certificate for one specific person.

* **Method**: `POST`
* **Path**: `/generate/solo`
* **Body**:

```json
{
  "name": "Bruce Wayne"
}

```

* **Response**: You'll get paths to the files and a `download_url` to grab the PDF immediately.

### 2. Direct PDF Download

Download the generated PDF file directly to your machine.

* **Method**: `GET`
* **Path**: `/download/{safe_name}`
* **Example**: `http://localhost:8000/download/Bruce_Wayne`

### 3. Bulk Generate

Triggers the generator to process everyone currently listed in `data/names.csv`.

* **Method**: `POST`
* **Path**: `/generate/bulk`
* **Response**: Returns the total count of folders created.

---

## 🐍 Python Example (Requests)

```python
import requests

# Generate a certificate
response = requests.post("http://localhost:8000/generate/solo", json={"name": "Tony Stark"})
data = response.json()

# Grab the PDF
if data["status"] == "success":
    pdf_url = f"http://localhost:8000{data['data']['download_url']}"
    print(f"Download your PDF here: {pdf_url}")

```

## ⚠️ Pro Tips

* **Naming**: Spaces in names are automatically converted to underscores for filenames (e.g., `Prakhar Doneria` -> `Prakhar_Doneria`).
* **Errors**: If you get a 404 on download, make sure you actually generated the certificate first!