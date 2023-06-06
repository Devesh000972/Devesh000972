import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>My Flask App</title>
            <style>
                /* CSS for animation */
                .animate {
                  animation: pulse 2s infinite;
                }

                @keyframes pulse {
                  0% {
                    transform: scale(0.95);
                  }
                  50% {
                    transform: scale(1);
                  }
                  100% {
                    transform: scale(0.95);
                  }
                }
            </style>
          </head>
          <body>
            <h2 class="visually-hidden">Title for screen readers</h2>
            <a class="visually-hidden-focusable" href="#content">Skip to main content</a>
            <div class="visually-hidden-focusable">A container with a <a href="#">focusable element</a>.</div>

            <h1 class="animate">Hello, world!</h1>

            <p><a href="/admin">Go to admin page</a></p>

            <p><a href="/html">Go to HTML page</a></p>
          </body>
        </html>
    '''

@app.route('/admin')
def admin():
    return '<p><b>Go</b> to hell</p>'

@app.route('/html')
def html():
    return '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Bootstrap demo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
          </head>
          <body>
            <h1>Hello, world!</h1>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
          </body>
        </html>
    '''

if __name__ == '__main__':
    app.run()
