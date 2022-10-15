import torch
import os
from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5/best.pt')  # local model

@app.route('/upload', methods=['POST']
def result():
    imagefile = flask.request.files('imagefile', '')
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        results = model(imagefile)
        results.save(results.save(save_dir='images/')
        return send_file(results, mimetype='image')
