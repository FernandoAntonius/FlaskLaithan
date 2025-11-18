# import flash module
import os
from time import time
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

@app.route('/pmb', methods=['GET', 'POST'])
def pmb():
    if request.method == 'POST':
        # Proses data form di sini
        nama = request.form['nama']
        email = request.form['email']
        tempatlahir = request.form['tempat_lahir']
        tanggallahir = request.form['tanggal_lahir']
        asal_sma = request.form['asal_sma']
        no_hp = request.form['no_hp']
        foto = request.files['foto']

        # Upload foto ke folder 'uploads'
        foto.save(f'static/uploads/{foto.filename}')

        # Tampilkan di terminal
        print(f'Nama: {nama}, Email: {email}, Tempat Lahir: {tempatlahir}, Tanggal Lahir: {tanggallahir}, Asal SMA: {asal_sma}, No HP: {no_hp}, Foto: {foto.filename}')

    title = 'Penerimaan Mahasiswa Baru'
    return render_template('pmb.html', title=title)

    #     # Cek jika ada file yang diunggah
    #     foto = request.files['foto']
    #     if foto:
    #         # Mengambil timestamp saat ini untuk menambahkan ke nama file
    #         timestamp = str(int(time.time()))
    #          # Mengambil ekstensi file asli
    #         ext = foto.filename.split('.')[-1]

    #         # Menambahkan ekstensi ke nama file unik
    #         unique_filename = f"{timestamp}.{ext}"

    #         # Menyimpan file dengan nama unik
    #         foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    #         foto.save(foto_path)
    #         foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif dengan menggunakan '/uploads/'
    #     else:
    #         foto_path = None

    #     # Pesan konfirmasi
    #     confirmation_message = f"Thank you, {nama}. Your registration has been received!"

    #      # Tampilkan halaman dengan pesan konfirmasi
    #     return render_template('register.html', confirmation_message=confirmation_message, nama=nama, email=email, tempatlahir=tempatlahir, tanggallahir=tanggallahir, asal_sma=asal_sma, hp=no_hp, foto=foto_path)

    # title = 'PMB Page'
    #  # Render halaman form registrasi kosong untuk metode GET
    # return render_template('register.html', title=title)

# # Konfigurasi folder upload
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# run the application
if __name__ == '__main__':
    app.run(debug=True)