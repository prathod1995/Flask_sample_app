from flask import Flask, render_template
import requests
import json
app = Flask(__name__)


@app.route('/', methods= ['GET'])
def userapi():
   res = requests.get('https://jsonplaceholder.typicode.com/posts')
   data =res.content
   print(res)
   return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)

