from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'My Devops Project  '

if __name__ == '__main__':
    app.run()




