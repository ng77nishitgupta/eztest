import os
from flask import Flask, request, flash, redirect, url_for

upload_folder=" c:/up"
allowed_exten={'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app=Flask(__name__)
app.config["upload_folder"]= upload_folder

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in allowed_exten
@app.route('/', methods=[ "get" , "post"])
def upload_file():
    if request.method== "post":
        if 'file ' not in request.files:
            flash("no file part ")
            return redirect(request.url)
        files= request.files["file"]
        if file.filename=="":
            flash("no selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['upload_folder'], filename))
            return redirect (url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>uplaod new file </title>
    <h1> upload new file </h1>
    <form method = post enctype=multipart/form-data>
    <input type=file name= file>
    <input type=submit value=upload>
    </forms>
    '''

@app.route('/upload/<name>')
def download_file(name):
    return send_from_directory(app.config["upload_folder"], name)