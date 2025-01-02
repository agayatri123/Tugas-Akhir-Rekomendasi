# -*- coding: utf-8 -*-
"""Recommendation Books.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k-avYrGmJ9o6ZXJoQQZX1PiY8c9J-EbX

**Nama: Anindita Gayatri
**Email:agayatri123@yahoo.co.id
**ID Dicoding:anindita_gayatri_ukA6

# **System Recommendation: Recommendation Books**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

# load the dataset
data_book= pd.read_csv('sample_data/best_books_ever.csv')

"""# **Data Understanding**"""

# Melihat summary dari struktur data_goodreads
data_book.info()

# Data dimension
print("Best Books Ever:", data_book)

# Melihat kolom mana saja yang Numeric
num_col=[]
for col in data_book.columns:
    if(data_book[col].dtypes!='object'):
        num_col.append(col)
        #print(f"There are total {len(num_col)} numerical columns in dataset")
print(num_col)

# Melihat kolom mana saja yang Categorical
cat_col=[]
for col in data_book.columns:
    if(data_book[col].dtypes=='object'):
        cat_col.append(col)
print(f"There are total {len(cat_col)} categorical columns in dataset")
print(cat_col)

"""# **Data Cleaning & Preprocessing**"""

# Cek missing value dengan fungsi isnull()
data_book.isnull().sum()

# Membersihkan missing value dengan fungsi dropna()
data_book1 = data_book.dropna()
data_book1

# Mengecek kembali missing value pada variabel all_resto_clean
data_book1.isnull().sum()

# Mengecek Language yang unik
data_book1.language.unique()

# Mengecek kesesuaian format judul buku dengan huruf latin
data_book1[data_book1['language'] == 'Dutch']

# Mengecek kesesuaian format judul buku dengan huruf latin
data_book1[data_book1['language'] == 'Arabic']

# Mengecek kesesuaian format judul buku dengan huruf latin
data_book1[data_book1['language'] == 'Greek']

# Mengecek kesesuaian format judul buku dengan huruf latin
data_book1[data_book1['language'] == 'Tamil']

# Mengecek kesesuaian format judul buku dengan huruf latin
data_book1[data_book1['language'] == 'Japanese']

# Mengecek kesesuaian format judul buku dengan huruf latin
data_book1[data_book1['language'] == 'Bengali']

word_to_delete = 'Arabic'
data_book1 = data_book1[~data_book1.apply(lambda row: row.astype(str).str.contains(word_to_delete, case=False).any(), axis=1)]
word_to_delete1 = 'Greek'
data_book1 = data_book1[~data_book1.apply(lambda row: row.astype(str).str.contains(word_to_delete1, case=False).any(), axis=1)]
word_to_delete1 = 'Tamil'
data_book1 = data_book1[~data_book1.apply(lambda row: row.astype(str).str.contains(word_to_delete1, case=False).any(), axis=1)]
word_to_delete1 = 'Japanese'
data_book1 = data_book1[~data_book1.apply(lambda row: row.astype(str).str.contains(word_to_delete1, case=False).any(), axis=1)]
word_to_delete1 = 'Bengali'
data_book1 = data_book1[~data_book1.apply(lambda row: row.astype(str).str.contains(word_to_delete1, case=False).any(), axis=1)]
word_to_delete1 = 'Ð'
data_book2 = data_book1[~data_book1.apply(lambda row: row.astype(str).str.contains(word_to_delete1, case=False).any(), axis=1)]

data_book1.groupby('language').count()

data_book1.describe()

"""# **Explorasi data**"""

# Menghitung jumlah buku, dsb berdasarkan Bahasa yang dipakai Penulis
data_book1.groupby('language').count()

# Melihat Sebaran Jumlah Buku berdasar Bahasa nya
import matplotlib.pyplot as plt
import seaborn as sns

# Set style seaborn
sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
language1 = data_book1.groupby('language')['bookId'].count()
sns.barplot(x=language1.index, y=language1.values)
plt.title('Jumlah Judul Buku vs Bahasa')
plt.xlabel('Jumlah Judul Buku')
plt.ylabel('Bahasa')
plt.xticks(range(1, 10))
plt.show()

# Melihat sebaran Jumlah Buku berdasar TOP 5 Penerbit nya
import matplotlib.pyplot as plt
import seaborn as sns

# Set style seaborn
sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
jumlah_buku = data_book1.groupby('publisher')['bookId'].count().nlargest(5)
sns.barplot(y=jumlah_buku.index, x=jumlah_buku.values)
plt.title('Jumlah Buku vs Penerbit')
plt.xlabel('Jumlah Buku')
plt.ylabel('Penerbit')
plt.xticks(range(1, 20))
plt.show()

# Mengecek Judul-judul Buku berdasar Bahasa nya
data_book1[data_book1['language'] == 'German']

"""# **MODEL DEVELOPMENT**

# **Content Based Filtering**
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan 'Author'
tf.fit(data_book1['language'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data_book1['language'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama resto

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data_book1.title
).sample(9, axis=1).sample(8, axis=0)

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=data_book1['title'], columns=data_book1['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

def book_recommendations(title_mirip, similarity_data=cosine_sim_df, items=data_book2[['title','language']], k=5):

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,title_mirip].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title_mirip, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

data_book1[data_book1.title.eq('Eugénie Grandet')]

"""# **EVALUATION**"""

# Mendapatkan rekomendasi title yang mirip dengan title tsb
book_recommendations("Eugénie Grandet", cosine_sim_df, data_book1[['title', 'language']], k=5)