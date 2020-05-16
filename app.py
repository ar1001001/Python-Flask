
#import statements
from flask import Flask, render_template, redirect, url_for

# Flask app variable
app = Flask(__name__)

# static route
@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/<name>")
def myBio(name):
    return f"Hello {name}!"


# start the server
if __name__ == "__main__":
    app.run(debug='True')
