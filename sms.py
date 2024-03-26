from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

def send_sms(number, message):
    url = "https://textbelt.com/text"
    data = {"phone": number, "message": message, "key": "textbelt"}
    r = requests.post(url, data=data)
    return r.json()

@app.route('/', methods=['GET', 'POST'])
def send_sms_page():
    if request.method == 'POST':
        number = request.form['phoneNumber']
        message = request.form['message']
        response = send_sms(number, message)
        return jsonify(response)
    return render_template('sms.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)