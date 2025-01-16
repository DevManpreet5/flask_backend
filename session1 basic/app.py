from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home page</h1>"

@app.route("/author/<name>")
def author(name):
    return f"<h1>welcome {name}</h1>"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    return f"<h1>welcome {num1+num2}</h1>"
    

if __name__=="__main__":
    app.run(debug=True)