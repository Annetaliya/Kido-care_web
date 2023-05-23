#!/usr/bin/python3
'''Running our web flask '''

from flask import Flask, render_template
"""from web_flask import views"""

app = Flask(__name__)
"""app.register_blueprint(views)"""
@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')