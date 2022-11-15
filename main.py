from flask import Flask, request, render_template
import requests
import asyncio
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
        
    if request.method == 'POST':
        a = request.form
        requests.post("http://127.0.0.1:5000/", data=a)
        
        return render_template('base.html', a=a)
    
    
    else:
        return render_template('base.html', a=None)

#changed lots of links MUST CHANGE BACK WHEN COMMITING