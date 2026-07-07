from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Returning a basic HTML string that includes a title tag to satisfy future pipeline tests
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Jenkins CI/CD Pipeline Demo</title>
    </head>
    <body>
        <h1>Jamie Reid - DevOps Assignment 5</h1>
        <p>If you are seeing this webpage, the automated Jenkins Docker deployment was successful!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    # host='0.0.0.0' exposes the server outside of the container so Jenkins/Docker can access it
    app.run(host='0.0.0.0', port=5000)