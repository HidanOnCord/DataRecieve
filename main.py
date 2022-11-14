from flask import Flask, request, render_template
import requests
import asyncio
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    async def send_info():
        global a
        a = request.form
        print(a['name'])
        requests.post("actual-display.vercel.app", data=a)
        
    if request.method == 'POST':
        asyncio.run(send_info())
        return render_template('base.html', a=a)
    
    
    else:
        return render_template('base.html', a=None)

#changed lots of links MUST CHANGE BACK WHEN COMMITING