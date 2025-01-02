# **Laporan Submission 2 - Anindita Gayatri**

Proyek ini bertujuan untuk membangun sistem rekomendasi pilihan buku menggunakan data identitas buku. Sistem ini akan memberikan rekomendasi buku kepada pelanggan berdasarkan kesamaan salah satu identitas buku, dalam hal ini bahasa yang dipakai buku sebelumnya. Disamping itu proyek ini tidak hanya bermanfaat bagi perpustakaan dalam hal peminjaman buku, tetapi juga dapat digunakan pada penjualan buku online seperti amazon, tokopedia, dll. Juga dapat dikembangkan lagi untuk memberikan wawasan berharga yang dapat digunakan untuk pengambilan keputusan strategis bisnis literatur di masa depan.

**Opsional**:
- Jelaskan mengapa dan bagaimana masalah tersebut harus diselesaikan
**Rubrik/Kriteria Tambahan (Opsional)**:
- Jelaskan mengapa proyek ini penting untuk diselesaikan.
- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.

  Format Referensi: [Judul Referensi](https://scholar.google.com/) 
@@ -18,29 +18,28 @@ Bagian laporan ini mencakup:

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
        Gambar_1.jpg
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

Dengan mengikuti tahapan data preparation di atas tadi, kita dapat memastikan bahwa data yang digunakan dalam analisis dan model rekomendasi adalah data yang berkualitas dan siap digunakan. Berikut beberapa contoh analisis data nya.
- 
        




## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menyajikan top-N recommendation sebagai output.
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Opsional**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

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

