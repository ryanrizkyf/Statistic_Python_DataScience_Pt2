# Kita dapat melakukan pemodelan regresi linier sederhana dengan menggunakan statsmodels.
# statsmodels merupakan satu dari banyak package pada bahasa pemrograman python yang bisa digunakan
# untuk membantu melakukan pemodelan regresi linier sederhana.

# Rumus yang digunakan seperti berikut :
# Lihat gambar pada file Rumus_RegresiLinierSederhana_Menggunakan_Statsmodels.png

# Jika dicontohkan ke dalam bahasa pemrograman, ada beberapa tahapan yang perlu dilakukan.

# 1. Membuat dataset dari file dengan format .csv.
# Menampilkan dataset (https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv)

# Load beberapa library
import pandas as pd
import statsmodels.api as sm

# Load data
raw_data = pd.read_csv("dataset_statistic.csv", sep";")

# Lihat data
print(raw_data)
# Lalu akan muncul isi dari dataset yang dipanggil.

# 2. Kita akan mengambil variabel 'Total' sebagai variabel tak bebas
# dan variabel 'Pendapatan' sebagai variabel bebas.
# Untuk menambahkan membentuk model yang disertai dengan intercept,
# kita harus menggunakan method .add_constant() untuk variabel bebas :

# Variabel tak bebas
nilai_Y = raw_data[['Total']]
# Variabel bebas
nilai_X = sm.add_constant(raw_data['Pendapatan'])

# 3. Selanjutnya kita dapat menggunakan method .OLS untuk membuat model regresi linier sederhana
# dengan memasukkan parameter endog=variabel_tak_bebas dan exog=variabel_bebas,
# disambung dengan method .fit():

# Membuat model regresi linier
model_regresi = sm.OLS(endog=nilai_Y, exog=nilai_X).fit()

# 4. Untuk melihat hasil dari model kita dapat menggunakan method .summary() sebagaimana contoh berikut :
model_regresi.summary()
