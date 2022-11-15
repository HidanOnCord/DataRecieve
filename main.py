from flask import Flask, request, render_template
import requests
import asyncio
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
        
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        #requests.post("http://127.0.0.1:5000/", data={"name":f"{a['name']}","email":f"{a['email']}","message":f"{a['message']}"})
        requests.post("https://discord.com/api/webhooks/1038012726305366076/sr1YKbFZsi2t20YiuPubRFDFk3uHVyqeQ_zmIGiMxcZBKQc2pY5PDsN0LHufeI7dHUnM", data={
            "content":{
            'name':name,
            'email':email,
            'message':message
            }
        })
        
        return render_template('base.html')
    
    
    else:
        return render_template('base.html')

#changed lots of links MUST CHANGE BACK WHEN COMMITING