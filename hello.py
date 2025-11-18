# import flash module
from flask import Flask, render_template, request
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Proses data form di sini
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']

        # Tampilkan di terminal
        print(f'Nama: {nama}, Email: {email}, Pesan: {pesan}')

    title = 'Contact Page'
    return render_template('contact.html', title=title)

@app.route('/pmb')
def pmb():
    return render_template('pmb.html')

# run the application
if __name__ == '__main__':
    app.run(debug=True)