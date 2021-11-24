# app.py
from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template('index.html')

if __name__=="__main__":
  #app.run(host="34.64.224.99", port="80", debug=True)
  app.run(host='0.0.0.0', port="5000", debug=True)
  #app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
