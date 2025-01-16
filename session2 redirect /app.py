from flask import Flask, redirect ,url_for
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> welcome </h1>"

#dynamic routing 
@app.route("/users/<username>")
def dynamic(username):
    return f"<h1> welcome {username} </h1>"


@app.route("/success/<sname>")
def suc(sname):
    return f"<h1> success {sname}  </h1>"

#redirect
@app.route("/redirect/<name>")
def redir(name):
    return redirect(url_for("suc",sname=name))


if __name__== "__main__":
    app.run(debug=True)
