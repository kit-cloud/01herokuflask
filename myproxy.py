from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
app = Flask(__name__,
            static_url_path='', 
            static_folder='site/static',
            template_folder='site')

@app.route('/')
def homepage():
    return render_template("main.html")

if __name__== '__name__':
    app.run()