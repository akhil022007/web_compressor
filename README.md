# Web File Compressor

A web-based file compression project using **C++ (Huffman & RLE)** with a  
**Python (Flask)** backend.

The web interface is handled by Python, while the actual compression logic
is implemented in C++ and executed as a backend binary.

---

## Features
- Compress text files using Huffman Coding and RLE
- Simple web interface for upload and download
- C++ used for core compression logic
- Python (Flask) used as backend
- Linux-based project

---

## Tech Stack
- C++
- Huffman Coding
- Run-Length Encoding (RLE)
- Python (Flask)
- HTML

---

## Project Structure
web_compressor/
├── backend/
│ ├── app.py
│ ├── compress
│ └── templates/index.html
├── uploads/
├── downloads/


---

## How to Run

### 1. Activate virtual environment
```bash
source backend/venv/bin/activate

###2. Run in web app
python backend/app.py

###3. Open in browser
http://127.0.0.1:5000

