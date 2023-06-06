import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/admin')
def admin():
    return '<p><b>Go</b> to hell</p>'

@app.route('/html')
def html():
    return '''
        <!DOCTYPE html>
        <html>
            <body>
                <h2>HTML Forms</h2>
                <form action="/action_page.php">
                    <label for="fname">First name:</label><br>
                    <input type="text" id="fname" name="fname" value="John"><br>
                    <label for="lname">Last name:</label><br>
                    <input type="text" id="lname" name="lname" value="Doe"><br><br>
                    <input type="submit" value="Submit">
                </form> 
                <p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>
            </body>
        </html>
    '''

@app.route('/photo')
def photo():
    # List of image URLs
    images = [
        'https://picsum.photos/200/300',
        'https://picsum.photos/300/200',
        'https://picsum.photos/250/250',
        'https://picsum.photos/400/400',
        'https://picsum.photos/500/300'
    ]

    # Select a random image URL from the list
    image_url = random.choice(images)

    # HTML code for displaying the image
    html = f'''
        <!DOCTYPE html>
        <html>
            <body>
                <h2>Random Image</h2>
                <img src="{image_url}" alt="random image">
            </body>
        </html>
    '''

    return html

if __name__ == '__main__':
    app.run()
