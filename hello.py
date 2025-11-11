# import flash module
from flask import Flask, render_template
# create an instance of the Flask class
app = Flask(__name__, template_folder='views')
# define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# define a route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pmb')
def pmb():
    return render_template('pmb.html')

# run the application
if __name__ == '__main__':
    app.run(debug=True)