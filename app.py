from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, My name is Fong! I'm studying ISP and wanted to share my excitement about it with you." \
    "This course has been incredibly engaging and informative, and I'm thrilled to be a part of it." \
    "This course also gives me an oppotunity to simulate real world projects which is very helpful for my future career." \
    "Looking forward to learning more and collaborating with everyone!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)