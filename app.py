from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from werkzeug.utils import secure_filename
import os
from model import predict_viral

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        df = pd.read_csv(file_path)
        predictions = predict_viral(df)
        return render_template('result.html', predictions=predictions.to_html())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



