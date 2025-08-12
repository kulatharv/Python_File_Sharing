# Python_File_Sharing
# 📂 Local File Sharing via Python HTTP Server & QR Code

A lightweight Python tool to **share any folder from your PC to other devices on the same network** using a built-in HTTP server.  
It automatically generates a **QR code** for quick mobile access — no cloud or third-party software needed.

---

## 🚀 Features
- 📁 **Folder Sharing** – Serve any local folder over HTTP.
- 🌐 **Local Network Access** – Works over LAN/Wi-Fi without internet.
- 📱 **QR Code Access** – Scan and open from mobile instantly.
- 💻 **Cross-Platform** – Works on Windows, Mac, and Linux.
- 🔒 **Privacy First** – Data stays within your network.

---

## 📸 How It Works
1. Select a folder you want to share.
2. The app starts an HTTP server.
3. It detects your **local IP address**.
4. Generates a **QR code** linked to your server.
5. Other devices on the same network can scan or click the link to access your files.

---

## 🛠️ Tech Stack
- **Python** – Core scripting language.
- **http.server** – Built-in HTTP server module.
- **socket** – For local IP detection.
- **pyqrcode** & **pypng** – QR code generation.
- **tkinter** – (Optional) GUI for folder selection and QR display.

---

## 📦 Installation
Make sure you have Python 3 installed.  
Install dependencies:
```bash
pip install pyqrcode pypng
