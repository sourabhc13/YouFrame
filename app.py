from flask import Flask,render_template,request,send_file,session
import requests
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/gallery/", methods = ["GET","POST"])
def gallery_page():
    f = request.files.get('file')
    UPLOAD_FOLDER = './static/gallery'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
    gallery=os.listdir('./static/gallery/')
    return render_template("index.html",gallery=gallery)
    






if __name__ == '__main__':
    app.run()