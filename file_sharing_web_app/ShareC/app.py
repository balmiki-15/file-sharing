from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from models import db,ShareC

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///share-c.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/send',methods=['POST'])
def send():
    recieved_file = request.files['file']    
    filename = secure_filename(recieved_file.filename)
    recieved_file.save(os.path.join(f"{os.getcwd()}/static/media",filename))
    print(f" -> File with filename : {filename} uploaded.")
    try:
        newFile = ShareC(filename=filename, recieved_file=f"{url_for('static',filename='media/')}{filename}")
        db.session.add(newFile)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue while adding your task.'
    

@app.route('/recieve')
def recieve():
    recieved = ShareC.query.all()
    print(recieved)
    return render_template('recieve.html', recieved=recieved)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = ShareC.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return e
        
@app.route('/download/<int:id>', methods=['GET', 'POST'])
def download(id):
    recieved = ShareC.query.get_or_404(id)
    return "download page"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
