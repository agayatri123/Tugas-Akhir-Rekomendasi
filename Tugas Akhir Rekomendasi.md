# **Laporan Submission 2 - Anindita Gayatri**

Proyek ini bertujuan untuk membangun sistem rekomendasi pilihan buku menggunakan data identitas buku. Sistem ini akan memberikan rekomendasi buku kepada pelanggan berdasarkan kesamaan salah satu identitas buku, dalam hal ini bahasa yang dipakai buku sebelumnya. Disamping itu proyek ini tidak hanya bermanfaat bagi perpustakaan dalam hal peminjaman buku, tetapi juga dapat digunakan pada penjualan buku online seperti amazon, tokopedia, dll. Juga dapat dikembangkan lagi untuk memberikan wawasan berharga yang dapat digunakan untuk pengambilan keputusan strategis bisnis literatur di masa depan.

Pentingnya Proyek Sistem Rekomendasi Produk: Proyek sistem rekomendasi produk ini sangat penting untuk diselesaikan karena beberapa alasan berikut:
1. Menaikkan penyewaan/pembelian buku. Penelitian menemukan bahwa sistem rekomendasi secara signifikan dapat menaikkan penjualan dengan memanfaatkan data pelanggan untuk menghasilkan rekomendasi yang relevan. Penelitian menggarisbawahi dampak personalisasi pada peningkatan penjualan produk dalam e-commerce (Zhang et al., 2011).
2. Di Pasar Personalization terjadi persaingan dalam pemberian rekomendasi dimana menjadi alat yang efektif untuk membangun loyalitas pelanggan dan memberi perusahaan keunggulan kompetitif di red ocean market (Ball et al., 2006).

### Problem Statements

1. Rekomendasi judul buku yang tidak akurat dapat menyebabkan pelanggan merasa tidak puas, dimana berpotensi mengurangi tingkat peminjaman buku.
2. Pengelolaan data yang besar dan beragam dapat menyulitkan analisis dan pengambilan keputusan yang tepat, salah satunya menangani keragaman buku yang seharusnya tersedia sesuai minat pembeli/peminjam buku.

### Goals

Menjelaskan tujuan dari pernyataan masalah:
1. Meningkatkan peminjaman/penjualan dan kepuasan pelanggan melalui rekomendasi judul buku yang relevan dengan preferensi pelanggan.
2. Mengoptimalkan pengelolaan inventaris dengan memastikan buku-buku yang rekomendasikan tersedia dan beragam.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Solution statements**

Pendekatan Algoritma Rekomendasi Berbasis Kesamaan: Menggunakan algoritma cosine similarity untuk menghitung kesamaan antar produk berdasarkan fitur yang ada, seperti judul dan bahasa yang digunakan. Ini akan membantu dalam memberikan rekomendasi yang lebih relevan kepada pelanggan. 

## Data Understanding
1. Informasi Dataset Dataset yang digunakan dalam proyek ini terdiri dari 52,478 entri dengan 25 kolom yang berbeda. Data ini diambil dari transaksi rekomendasi buku terbaik dan mencakup informasi mengenai identitas buku yang dinilai memiliki kualitas terbaik oleh pelanggan yang bersumber dari dataset public kaggle. (https://www.kaggle.com/datasets/thedevastator/comprehensive-literary-greats-dataset) 
2. Kondisi Data
  - Total Baris Data: 52,478 entries
  - Memori yang Digunakan: 10.0+ MB
  - Status Missing Values:
      - series: 29,008 missing values (23470 non-null dari 52,478)
      - description: 1,338 missing values (51,140 non-null dari 52,478)
      - language: 3,806 missing values (48,672 non-null dari 52,478)
      - bookFormat: 1,473 missing values (51,005 non-null dari 52,478)
      - edition: 47,523 missing values (4,955 non-null dari 52,478)
      - pages: 2,347 missing values (50,131 non-null dari 52,478)
      - publisher: 3,696 missing values (48,782 non-null dari 52,478)
      - publishDate: 880 missing values (51,598 non-null dari 52,478)
      - firstPublishDate: 21,326 missing values (31,152 non-null dari 52,478)
      - likedPercent: 622 missing values (51,856 non-null dari 52,478)
      - coverImg: 605 missing values (51,873 non-null dari 52,478)
      - price: 14,365 missing values (38,113 non-null dari 52,478)
      - Kolom lainnya terisi lengkap

Variabel atau Fitur pada Dataset (dari 20 column yang tersisa setelah data "dibersihkan" diambil fitur data yang penting sbb:
    
        - bookId: Nomor buku di perpustakaan (type: object)
        - title: Judul Buku  (type: object)
        - series: Serial dari buku, bila ada  (type: object)
        - author: Pengarang Buku  (type: object)
        - rating: penilaian pembaca tentang kualitas buku antara 1-5  (type: int64)
        - descriptian: penjelasan singkat isi buku  (type: object)
        - language: Bahasa yang dipakai oleh penulis  (type: object)
        - dst

## Data Preparation
Pada bagian ini, kami menerapkan beberapa teknik data preparation yang penting untuk memastikan bahwa data siap digunakan dalam analisis dan model rekomendasi. Proses yang dilakukan adalah sebagai berikut :
1. Data Cleaning

  - Deskripsi: Proses ini bertujuan untuk menghapus data yang kosong dan memastikan bahwa data dalam format yang konsisten. Data yang bersih sangat penting untuk analisis yang akurat dan model yang efektif.
  - Langkah-langkah:
      - Melihat summary dari dataset awal untuk mengetahui :
              - jumlah kolom
              - jenis data apa saja yang ada
              - jenis data dari tiap kolom
              - berapa entries/baris data yang ada
              - besar memory yanng digunakan dataset
              - berapa banyak kolom yang null
    ![Gambar_1](https://github.com/user-attachments/assets/c96d1122-0ef3-4785-a65b-5c1e9f74d2eb)


        - Setelah mengetahui kolom mana saja yang null (karena di bagian "non-null count" kurang dari jumlah entries), maka dicheck ulang melihat sample isian 5 data dari tiap kolom untuk meyakiknkan isinya apa saja.
        - Juga di-check ulang mana saja kolom yang termasuk kelompok Numerical dan mana yang categorical.
        Gambar_2.jpg
        Gambar_3.jpg 
        - Setelahnya di-delete baris yang ada nilai null nya dimana terdapat di kolom-kolom sbb:
                - series, description, language, bookFormat, edition, pages, publisher, publishDate, firstPublishDate, likedPercent, coverImg dan price
        - Dilakukan pemeriksaan ulang setelah delete null untuk meyakinkan bahwa sudah tidak ada nilai null yang masih tersisa.
        - Setelah nya dilihat lagi berapa entries yang tersisa. Ternyata berkurang karena cukup banyak kolom yang ada nilai null nya tadi.

2. Handling Outliers

Deskripsi: Mengidentifikasi dan menangani outliers yang dapat mempengaruhi analisis. Outliers dapat menyebabkan distorsi dalam hasil analisis dan model.

Metode:

Menggunakan metode statistik seperti IQR (Interquartile Range) atau Z-score untuk mendeteksi outliers.
Menghapus transaksi dengan Quantity atau UnitPrice yang sangat tinggi atau rendah dibandingkan dengan rata-rata untuk meningkatkan kualitas data (bila ada). Namun di data ini tidak dilakukan karena sebaran nya sudah cukup baik. 
Gambar_4.jpg

3. Exploratory Data Analysis
   
- Dengan mengikuti tahapan data preparation ini, kami dapat memastikan bahwa data yang digunakan dalam analisis dan model rekomendasi adalah data yang berkualitas dan siap digunakan.

- Jumlah Judul Buku vs Bahasa
  Gambar_5.jpg

  Berdasar grafik di atas diketahui ternyata perpustakaan didominasi oleh buku berbahasa Inggris, diikuti Italia dan Spanish, dll. Namun secara kuantitas Italia, dst memiliki jumlah yang tidak jauh berbeda.

- Jumlah Buku vs Penerbit
  Gambar_6.jpg

  Berdasar grafik di atas diketahui ternyata perpustakaan mengoleksi buku dari penerbit yang beragam dan jumlah nya tidak jauh berbeda. Karena TOP 5 penerbit yang dipimpin oleh Marvel lalu Oxford hanya berbeda 5 pcs. Demikian pula untuk penerbit-penerbit di bawah nya.  

## Modeling

- Metode yang dipakai adalah Content Based Filtering
  
Cosine Similarity Cosine Similarity adalah metrik yang digunakan untuk mengukur seberapa mirip dua vektor dalam ruang multidimensi. Dalam konteks sistem rekomendasi, cosine similarity sering digunakan untuk menentukan kesamaan antara item (seperti produk) berdasarkan fitur-fitur yang dimiliki. Metrik ini sangat berguna dalam pendekatan Collaborative Filtering dan Content-Based Filtering.

- Cosine similarity dihitung dengan rumus berikut:

Screenshot 2024-11-24 at 16 55 55
Di mana:

( A ) dan ( B ) adalah dua vektor yang mewakili item yang dibandingkan.
( A \cdot B ) adalah hasil kali dot antara dua vektor.
( |A| ) dan ( |B| ) adalah norma (panjang) dari vektor ( A ) dan ( B ).
- Nilai cosine similarity berkisar antara -1 hingga 1:

1 menunjukkan bahwa dua vektor identik (sama arah).
0 menunjukkan bahwa dua vektor tidak memiliki kesamaan (tegak lurus).
-1 menunjukkan bahwa dua vektor berlawanan arah.

- Berdasarkan perhitungan tf-idf matrix didapatkan hasil pasangan tile (Judul Buku) terhadap language (Bahasa) yang digunakan sbb:
Gambar_7.jpeg

- Lalu kita menghitung cosine similarity dataframe tfidf_matrix yang kita peroleh pada tahapan sebelumnya sehingga menghasilkan kesamaan (similarity) antar title (Judul Buku) sbb:
Gambar_8,jpeg


## Evaluation


Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.
Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Opsional**: 
**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

