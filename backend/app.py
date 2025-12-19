from flask import Flask, request, send_file,jsonify,render_template
import subprocess
import os
import uuid

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "../uploads")
DOWNLOAD_DIR = os.path.join(BASE_DIR, "../downloads")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/compress", methods=["POST"])
def compress():
    file = request.files["file"]
    algo = request.form["algo"]   # huff or rle

    # clean filename
    original_filename = os.path.basename(file.filename)
    name, ext = os.path.splitext(original_filename)

    if not name:
        name = "file"

    input_path = os.path.join(UPLOAD_DIR, original_filename)

    if algo == "huff":
        output_filename = f"{name}.huff.cmp"
    else:
        output_filename = f"{name}.rle.cmp"

    output_path = os.path.join(DOWNLOAD_DIR, output_filename)

    # save uploaded file
    file.save(input_path)

    # run compressor
    subprocess.run(
        ["./compress", algo, "c", input_path, output_path],
        cwd=BASE_DIR,
        check=True
    )

    # calculate sizes
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)

    ratio = round(
        (compressed_size / original_size) * 100, 2
    ) if original_size != 0 else 0

    return jsonify({
        "original_file": original_filename,
        "compressed_file": output_filename,
        "original_size": original_size,
        "compressed_size": compressed_size,
        "compression_ratio": ratio
    })



@app.route("/decompress", methods=["POST"])
def decompress():
    file = request.files["file"]
    algo = request.form["algo"]

    filename = file.filename
    name, ext = os.path.splitext(filename)

    input_path = os.path.join(UPLOAD_DIR, filename)

    if name.endswith(".huff") or name.endswith(".rle"):
        original_name = name.rsplit(".", 1)[0]
    else:
        original_name = name

    output_name = f"{original_name}_decompressed.txt"
    output_path = os.path.join(DOWNLOAD_DIR, output_name)

    file.save(input_path)

    subprocess.run(
        ["./compress", algo, "d", input_path, output_path],
        cwd=BASE_DIR,
        check=True
    )

    return send_file(output_path, as_attachment=True)
@app.route("/download/<filename>", methods=["GET"])

def download(filename):
    path = os.path.join(DOWNLOAD_DIR, filename)
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
