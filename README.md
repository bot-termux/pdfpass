# 🐧 PDF Password Tool - Termux Bot Style

## 🛠 About

- 🔓 **Unlock password-protected PDFs**
- 🔐 **Add a password to PDFs**

Built with 🐍 `pikepdf`,  Runs on **Termux**, **Linux**, **WSL**, or any Python environment.

---

## 📦 Features

- Walks all subdirectories from current folder
- Mass removes passwords if you know the correct one
- Mass adds password protection to PDFs
- Generates logs in `.log` file

---

## ⚙️ Usage

### 1. Install Requirements

```bash
pip install pikepdf coloredlogs
```

### 2. Configure Password
Edit the script and change this line:
```bash
pdf_password = "yourpassword"
```

### 3. Run the code
```bash
python pdfpassremover.py
```
or
```bash
python pdfpaddremover.py
```
