from flask import Flask, render_template, send_from_directory
import os


template_dir = os.path.abspath('/app/')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def render_static():
    return render_template('index.html')

@app.route("/<path:path>")
def static_dir(path):
    return send_from_directory("/app/", path)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
