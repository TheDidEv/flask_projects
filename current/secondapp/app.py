from flask import Flask, render_template, request, Response, send_from_directory
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # username = request.form['username']
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "u" and password == "p":
            return "Success"
        else:
            return "Failure"


@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    # .txt    
    if file.content_type == 'text/plain':
        return file.read().decode()
    # .xlsx, xls
    elif file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
        df = pd.read_excel(file)
        return df.to_html()
    else:
        return "Unsiported file type", 400
    
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    
    if file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
        df = pd.read_excel(file)
            
        response = Response(
            df.to_csv(),
            mimetype='text/csv',
            headers={
                'Content-Desposition': 'attachment; filename=result.csv'
            }
        )

        return response
    else: 
        return "Unsiported file type", 400
    
@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    
    df = pd.read_excel(file)
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))
    
    return render_template('download.html', filename=filename)
        
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('download', filename, download_name='result.csv')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)