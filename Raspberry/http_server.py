from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    a = 1
    b = 2
    return "Hello from Cyril " + str(a + b)

@app.route("/html")
def html():
    return """
    <html>
        <body>
            <h1>From <i>Cyril</i></h1>
            <font color="red">En rouge</font>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run("0.0.0.0")
