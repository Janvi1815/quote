from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('quote.html')

@app.route('/get-quote')
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()[0]
        return jsonify({
            "content": data['q'],
            "author": data['a']
        })
    except Exception as e:
        return jsonify({
            "content": str(e),
            "author": "API Error"
        })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ this makes it work on Render
    app.run(debug=True, host="0.0.0.0", port=port)
