from flask import Flask, request, render_template
import requests
import asyncio
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
        
    if request.method == 'POST':
        a = request.form
        requests.post("http://127.0.0.1:5000/", data={"name":f"{a['name']}","email":f"{a['email']}","message":f"{a['message']}"})
        
        return render_template('base.html')
    
    
    else:
        return render_template('base.html')

#changed lots of links MUST CHANGE BACK WHEN COMMITING