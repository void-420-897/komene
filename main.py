from flask import Flask, render_template
myapp=Flask(__name__)
@myapp.route("/")
def hello():
    return render_template("neng1.html")
if __name__=="__main__":
    myapp.run(debug=True)
