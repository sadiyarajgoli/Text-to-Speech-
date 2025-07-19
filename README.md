### ✅ `README.md`

```markdown
# 🎙️ Text-to-Audio Web App (Django + gTTS)

A simple Django web application that converts user-entered text into spoken audio using **Google Text-to-Speech (gTTS)**.

---

## 🚀 Features

- 🔤 Converts typed text into speech
- 🌐 Supports US English voice (`tld='com'`)
- 🐢 Slowed-down speech for better clarity
- 🔊 In-browser audio playback
- ⬇️ Downloadable `.mp3` audio file

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **TTS Engine**: `gTTS` (Google Text-to-Speech)
- **Frontend**: HTML + CSS (via Django Templates)

---

## 📁 Project Structure

```

TtoS/
├── manage.py

├── media/                       # Stores generated audio files

├── tts/                         # Django app

│   ├── views.py                 # Core TTS logic

│   ├── urls.py                  # App routing

│   └── templates/

│       └── tts/

│           └── index.html       # Main form + audio player

├── text\_to\_audio\_project/

│   └── settings.py              # Project settings

````

---

## 🧪 How to Run Locally

1. **Clone or extract** the project:
   ```bash
   cd TtoS
````

2. **(Optional)** Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   > If `requirements.txt` is not available, install manually:

   ```bash
   pip install Django gTTS
   ```

4. **Run the server**:

   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to:
   👉 `http://127.0.0.1:8000/`

---

## 🖼️ Screenshots

* Home page
* <img width="1920" height="1020" alt="Screenshot 2025-07-19 205843" src="https://github.com/user-attachments/assets/b1070961-a316-4926-83e1-17603b66c3bb" />

* Audio output + Download button
* <img width="1920" height="1020" alt="Screenshot 2025-07-19 205857" src="https://github.com/user-attachments/assets/442ad21b-826f-4a2c-9ef2-24c349e3f556" />
<img width="1915" height="911" alt="Screenshot 2025-07-19 205936" src="https://github.com/user-attachments/assets/edf5d705-970c-4dca-bddf-ad4101dba316" />
<img width="1919" height="910" alt="Screenshot 2025-07-19 210152" src="https://github.com/user-attachments/assets/1377e90a-b825-4259-b428-756181b8d503" />
<img width="1919" height="914" alt="Screenshot 2025-07-19 210224" src="https://github.com/user-attachments/assets/87e75348-06a3-4cfd-af24-20acef4e66a9" />




## 📄 License

This project is open-source and free to use for learning and personal development.

---

## 🙌 Author

**Sadiya Rajgoli.**
Made with ❤️ using Django and Python
