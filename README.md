# Web Compressor (C++ + Flask)

A simple web application that compresses and decompresses files using:
- Huffman Coding
- Run Length Encoding (RLE)

Built with:
- C++ (compression engine)
- Python Flask (backend)
- HTML/CSS (frontend)
## Features
- Compress and decompress files
- Shows compression and decompression ratios
- Manual download option (no auto-download)
- Clean web UI
- Supports binary and text files

## Project Structure

web_compressor/
├── file_compressor/
│ ├── src/
│ └── include/
│
├── web_compressor/
│ └── backend/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ └── compress (generated after build)
│
├── README.md
└── .gitignore
## Requirements

- Linux
- C++ compiler (`g++`)
- Python 3.8+
- Flask

---

## Quick Start

### 1.Clone the repository
```bash
git clone https://github.com/akhil022007/web_compressor.git
cd web_compressor
### 2.Build the C++ compressor
g++ src/*.cpp -Iinclude -o compress
### 3.Copy the compressor to the backend
cp compress backend/
chmod +x backend/compress

### 4.Create Python virtual environment
cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask
### 5.Run the server
python app.py
open-http://127.0.0.1:5000

