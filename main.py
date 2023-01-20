import os, subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=os.environ['PORT'])
    app.run(host="0.0.0.0", port=8080)
    Popen(['python', '-m', 'ComplexHTTPServer', '<port_number>'], cwd="static/music")
