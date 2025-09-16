<details>
<summary>Tugas 2</summary>

## Link Aplikasi
(https://your-pws-link.cs.ui.ac.id)

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. **Membuat Proyek Django Baru**  
   - Menjalankan `django-admin startproject football_shop` untuk membuat proyek utama.

2. **Membuat Aplikasi `main`**  
   - Menjalankan `python manage.py startapp main` untuk membuat aplikasi dalam proyek.

3. **Routing Proyek**  
   - Menambahkan `path('', include('main.urls'))` di `football_shop/urls.py`.
   - Membuat `main/urls.py` dengan path root yang mengarah ke `show_main`.

4. **Membuat Model `Product`**  
   - Membuat model `Product` dengan atribut wajib:  
     `name` (CharField), `price` (IntegerField), `description` (TextField),  
     `thumbnail` (URLField), `category` (CharField), `is_featured` (BooleanField).

5. **Membuat View `show_main`**  
   - Mengambil semua produk dari database (`Product.objects.all()`) dan mengirim context berisi data diri dan produk ke template `main.html`.

6. **Membuat Template HTML (`main.html`)**  
   - Menampilkan nama aplikasi, nama dan kelas, serta daftar featured products.

7. **Testing**  
   - Membuat `tests.py` untuk memastikan URL, template, dan model bekerja.

8. **Deployment ke PWS**  
   - Mengikuti panduan deployment PWS untuk menjalankan aplikasi agar bisa diakses secara publik.

---

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas HTML.
![Bagan](images/bagan.png)

---

## 3. Jelaskan peran settings.py dalam Proyek Django
Berkas `settings.py` berfungsi sebagai pusat konfigurasi proyek Django.  
Semua pengaturan utama didefinisikan di sini, seperti:  
- **INSTALLED_APPS** → daftar aplikasi yang digunakan dalam proyek.  
- **DATABASES** → konfigurasi database (misalnya SQLite, PostgreSQL, MySQL).  
- **MIDDLEWARE** → komponen yang memproses request dan response.  
- **TEMPLATES** → lokasi dan pengaturan template HTML.  
- **STATIC & MEDIA FILES** → pengaturan file statis (CSS, JS, gambar).  
- **DEBUG & ALLOWED_HOSTS** → mengatur mode debugging dan domain yang diizinkan.  

---

## 4. Bagaimana cara kerja migrasi database di Django?
Migrasi database di Django adalah proses untuk menyinkronkan perubahan pada **model (models.py)** dengan **struktur database**.  

Cara kerjanya:  
1. **Membuat file migrasi**  
   - Saat menjalankan `python manage.py makemigrations`, Django membaca perubahan di `models.py` dan membuat file migrasi (di folder `migrations/`) yang berisi instruksi SQL.  

2. **Menerapkan migrasi ke database**  
   - Dengan `python manage.py migrate`, Django mengeksekusi file migrasi tersebut ke database sehingga struktur tabel sesuai dengan definisi di model.  

3. **Tracking migrasi**  
   - Django menyimpan catatan migrasi yang sudah dijalankan di tabel khusus (`django_migrations`) agar tidak dijalankan ulang.  

---

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih sebagai framework awal dalam pembelajaran karena beberapa alasan:  

1. **Konsep MVC/MVT yang jelas**  
   Django menggunakan arsitektur *Model-View-Template* yang memisahkan logika bisnis, data, dan tampilan. Hal ini membantu untuk memahami bagaimana sebuah aplikasi web bekerja secara terstruktur.  

2. **Banyak fitur bawaan**  
   Django sudah menyediakan ORM, sistem autentikasi, admin panel, form handling, hingga keamanan dasar. Dengan begitu, bisa langsung fokus pada konsep inti tanpa harus membangun semuanya dari nol.  

3. **Mengajarkan praktik terbaik**  
   Django mendorong penggunaan pola desain yang rapi, DRY (*Don’t Repeat Yourself*), serta manajemen proyek yang terorganisir sehingga terbiasa menulis kode yang bersih dan terstruktur.  

4. **Relevan dengan industri**  
   Django digunakan di banyak perusahaan dan startup, dengan harapan apa yang dipelajari di PBP bisa berguna untuk dunia kerja nantinya.  

---

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Sejauh ini belum ada ^^
</details>

<details>
<summary>Tugas 3</summary>

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah proses pengiriman data dari satu pihak ke pihak lain dalam sebuah platform, baik antar komponen internal maupun eksternal. Alasan kenapa data delivery itu penting:

1. **Menghubungkan antar komponen sistem**
   Platform biasanya terdiri dari berbagai bagian. Tanpa mekanisme pengiriman data, tiap bagian ini tidak bisa saling bertukar informasi.
   
2. **Memberikan informasi yang up-to-date ke pengguna**
   Misalnya di e-commerce, data stok barang atau harga harus dikirim secara real-time agar pengguna melihat informasi terbaru.
   
3. **Mendukung interaktivitas aplikasi**
   Fitur seperti login, pencarian, transaksi, atau notifikasi hanya bisa berjalan kalau ada alur request-response data yang jelas.

4. **Menjamin konsistensi data**
   Data delivery memastikan data yang ada di server sinkron dengan yang ditampilkan di client, sehingga tidak terjadi perbedaan informasi.

5. **Membuka integrasi dengan layanan lain**
   Platform modern sering butuh komunikasi dengan layanan eksternal. Semua ini hanya bisa jalan lewat data delivery.

---

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
1. **Mana yang lebih baik antara XML dan JSON?**
   Tergantung kebutuhan. XML lebih cocok untuk data kompleks dengan hierarki, metadata, dan validasi ketat, sedangkan JSON lebih unggul untuk pertukaran data yang sederhana,    cepat, ringan, dan mudah dibaca, terutama di web dan mobile.

2. **Mengapa JSON lebih populer dibandingkan XML?**
   Beberapa alasan utama kenapa JSON lebih banyak dipakai:
   - **Lebih ringkas dan sederhana**
     JSON hanya pakai kurung kurawal dan array, sedangkan XML butuh banyak tag pembuka & penutup sehingga ukuran file JSON lebih kecil dan menyebabkan lebih cepat untuk dikirim lewat jaringan.
   - **Mudah dipahami dan dibaca**
     Struktur JSON mirip dengan objek di JavaScript, sehingga lebih cepat menggunakannya.
   - **Mudah diproses oleh program**
     Di JavaScript, data JSON bisa langsung dipakai tanpa konversi ribet.
   - **Performa lebih baik untuk API modern**
     API REST dan GraphQL umumnya mengutamakan JSON karena lebih efisien dibanding XML.
   - **Tren industri**
     JSON jadi standar de facto dalam komunikasi client–server.

---

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk memvalidasi data yang dikirimkan melalui form. Saat form menerima input, Django akan memeriksa apakah data tersebut sesuai dengan aturan yang ditentukan di form. Jika semua validasi terpenuhi, is_valid() akan mengembalikan True, dan data bersihnya bisa diakses lewat form.cleaned_data. Kalau ada yang salah, is_valid() mengembalikan False, dan form menyimpan pesan error yang bisa ditampilkan ke user. Kita membutuhkan method tsb. untuk:
- **Menjamin keakuratan data** → hanya data valid yang akan diproses atau disimpan ke database.
- **Meningkatkan keamanan** → mencegah input berbahaya masuk ke sistem.
- **Memberikan feedback ke pengguna** → jika input salah, error bisa langsung ditampilkan di form.
- **Menyederhanakan validasi** → tidak perlu menulis kode validasi manual.

---

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
1. **Mengapa kita membutuhkan csrf_token saat membuat form di Django?**
   csrf_token (Cross-Site Request Forgery token) adalah token unik yang ditambahkan ke setiap form di Django untuk memastikan bahwa request POST benar-benar berasal dari user yang sah melalui website kita, bukan dari sumber eksternal yang berbahaya. Dengan token ini, server bisa memverifikasi bahwa request datang dari browser user yang sedang login dan bukan dari serangan luar.

2. **Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?**
   Tanpa csrf_token, aplikasi jadi rentan terhadap serangan CSRF (Cross-Site Request Forgery). Artinya, penyerang bisa mengirimkan request palsu ke server atas nama user tanpa sepengetahuan user.

3. **Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
   Contoh pemanfaatan:
   1. User sedang login di aplikasi bank berbasis web.
   2. Penyerang membuat halaman berbahaya berisi form tersembunyi yang otomatis mengirimkan request POST ke server bank (misalnya transfer uang).
   3. Karena user masih login, browser akan mengirimkan cookie session valid ke server bank.
   4. Jika tidak ada proteksi csrf_token, server menganggap request itu sah, sehingga transaksi berbahaya bisa terjadi tanpa diketahui user.

---

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
1. **Siapkan `ModelForm`**  
   - Buat `main/forms.py`.

2. **Tambahkan 4 view untuk XML / JSON**
   - Menggunakan `django.core.serializers` untuk XML/JSON.

3. **Buat routing URL untuk masing-masing view**
   - Menambahkan path di `main/urls.py`

4. **Buat view untuk list, add (form) dan detail**

5. **Edit `templates/main.html` agar user bisa menambahkan porduct**

---

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Sejauh ini belum ada.

---

## Hasi akses keempat URL menggunakan Postman
