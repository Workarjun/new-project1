from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLD'
    return 'i am a new user '

if __name__ == '__main__':
    app.run(debug=True)
