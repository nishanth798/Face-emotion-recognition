from flask import Flask, render_template, request
import os
from realtime import starter;
from picture import imz;

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'image' in request.files:
        image = request.files['image']
        img_name = image.filename
        
        # Save the image file to the uploads folder
        image.save(os.path.join(UPLOAD_FOLDER, img_name))
        
        imz(img_name);
        
        return "Image uploaded successfully!"
    else:
        return "No image file found."
    
@app.route('/video')
def video():
    starter();
# @app.route('/image')
# def image():

if __name__ == '__main__': 
    app.run(debug=True)
