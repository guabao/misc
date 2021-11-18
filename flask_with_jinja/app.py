from flask import Flask,request,render_template,redirect,session,url_for,Markup

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/demo")
def demo():
    contents = []
    if request.method == 'GET':
        pass
    return render_template('demo.html', content=contents)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
