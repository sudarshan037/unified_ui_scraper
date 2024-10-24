from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Path to save the uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Available scraper names (to be populated in dropdown)
SCRAPER_NAMES = ['eventbrite_links', 'other_scraper']

@app.route('/')
def index():
    return render_template('index.html', scrapers=SCRAPER_NAMES)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        scraper_name = request.form.get('scraper_name')
        # Handle the file and scraper name selection here
        return f'File {filename} uploaded and scraper selected: {scraper_name}'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
