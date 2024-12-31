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
Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Opsional**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 
**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Approach” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).
Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

@@ -49,33 +48,29 @@ Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Opsional**:
**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Opsional**: 
**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

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

