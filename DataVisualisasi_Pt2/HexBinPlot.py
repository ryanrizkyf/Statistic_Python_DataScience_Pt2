# Untuk menggambar scatter plot kita dapat menggunakan
# method .plot.scatter() pada pandas atau menggunakan .scatter() pada matplotlib

import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.clf()

# mengambil data contoh
raw_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# melihat isi dari data
print(raw_data)

plt.figure()
# visualisasi diagram pencar untuk variabel 'Pendapatan' dan 'Total' menggunakan 'plot.scatter' dari pandas
raw_data.plot.scatter(x='Pendapatan', y='Total')
plt.title('plot.scatter dari pandas', size=14)
plt.tight_layout()
plt.show()

# visualisasi diagram pencar untuk variabel 'Pendapatan' dan 'Total' menggunakan 'plt.scatter' dari matplotlib
plt.scatter(x='Pendapatan', y='Total', data=raw_data)
plt.title('plt.scatter dari matplotlib', size=14)
plt.tight_layout()
plt.show()


# Catatan: Perhatikan bahwa walaupun keduanya mengeluarkan gambar yang sama,
# namun dapat dilihat bahwa hasil dari plot.scatter lebih lengkap karena terdapat label untuk masing-masing
# variabel yang secara otomatis dibuat, tidak seperti plt.scatter yang harus ditulis manual.

# visualisasi diagram pencar untuk variabel 'Pendapatan' dan 'Total' menggunakan 'plt.scatter' dari matplotlib.pyplot
plt.scatter(x='Pendapatan', y='Total', data=raw_data)
plt.xlabel('Pendapatan')
plt.ylabel('Total')
plt.show()


# Untuk menggambar histogram kita dapat menggunakan method .hist() dari pandas
# atau menggunakan pyplot.hist() dari matplotlib.

plt.clf()

plt.figure()
# melihat distribusi data kolom 'Pendapatan' menggunakan 'hist' dari pandas
raw_data.hist(column='Pendapatan')
plt.title('.hist dari pandas', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# melihat distribusi data kolom 'Pendapatan' menggunakan 'pyplot.hist' dari matplotlib.pyplot
plt.hist(x='Pendapatan', data=raw_data)
plt.xlabel('Pendapatan')
plt.title('pyplot.hist dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()


# Pada bagian ini, kita akan membuat box plot. Ada 2 box plot yang akan dihasilkan.

plt.clf()

# melihat box plot dari kolom 'Pendapatan' menggunakan method '.boxplot' dari pandas
plt.figure()
raw_data.boxplot(column='Pendapatan')
plt.title('.boxplot dari pandas', size=14)
plt.tight_layout()
plt.show()

# melihat box plot dari kolom 'Pendapatan' menggunakan method '.boxplot' dari matplotlib
plt.figure()
plt.boxplot(x='Pendapatan', data=raw_data)
plt.xlabel('Pendapatan')
plt.title('pyplot.boxplot dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()


# Diagram batang atau bar plot adalah plot yang digunakan untuk menghitung frekuensi dari data.

plt.clf()

# hitung frekuensi dari masing-masing nilai pada kolom 'Produk'
class_freq = raw_data['Produk'].value_counts()

# lihat nilai dari class_freq
print(class_freq)

plt.figure()
# membuat bar plot dengan method `plot.bar()` dari pandas
class_freq.plot.bar()
plt.title('.bar dari pandas', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# membuat bar plot dengan method `plt.bar()` dari matplotlib
plt.bar(x=class_freq.index, height=class_freq.values)
plt.title('plt.bar dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()


# Diagram pie atau pie chart adalah plot lainnya yang dapat digunakan
# untuk menampilkan frekuensi dalam bentuk proporsi.

# Untuk menampilkan diagram pie kita dapat
# menggunakan pyplot.pie dari matplotlib atau method plot.pie() dari pandas.

plt.clf()

plt.figure()
# membuat pie chart menggunakan method 'pyplot.pie()' dari matplotlib
plt.pie(class_freq.values, labels=class_freq.index)
plt.title('plt.pie dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# membuat pie chart menggunakan method 'plot.pie' dari pandas
class_freq.plot.pie()
plt.title('plot.pie dari pandas', size=14)
plt.tight_layout()
plt.show()


# Kita sudah mempelajari bagaimana membuat histogram pada materi sebelumnya.
# Pada kesempatan kali ini kita akan mencoba melakukan transformasi data untuk mengubah distribusi data
# yang tadinya skew menjadi berdistribusi normal.

# Transformasi Untuk Data Skew ke Kanan
# Perhatikan beberapa distribusi berikut :
# Lihat gambar pada file TransformasiData_Kaitannya_DistribusiData.png

# Perhatikan bahwa variabel Pendapatan memiliki distribusi data dengan skewness ke kanan.
# Sedangkan variabel seperti Harga memiliki distribusi data dengan skewness ke kiri.

# Untuk mengubah distribusi data menjadi normal untuk data skew ke kanan kita dapat menggunakan
# fungsi logaritma, akar kuadrat, akar tiga dan akar resiprokal lainnya.

# Sedangkan untuk mengubah distribusi data menjadi normal untuk data skew ke kiri kita bisa menggunakan
# kuadrat, pangkat 3 dan pangkat n.

# Untuk menggunakan fungsi-fungsi berikut kita dapat menggunakan
# method .log(), .sqrt(), .power() dari numpy atau dengan operasi matematika biasa.

# Kita dapat menguji dengan mudah apakah hasil transformasi sudah mendekati distribusi normal
# atau belum dengan menggunakan Q-Q plot.
# Untuk membuat Q-Q plot kita cukup memanggil fungsi qqplot dari statsmodels.

# Perhatikan bahwa jika hampir semua titik terletak pada garis,
# maka distribusi dari data sudah mendekati distribusi normal.
# Perhatikan perbedaannya sebelum dilakukan transformasi.

plt.clf()

plt.figure()
raw_data.hist()
plt.title('Histogram seluruh kolom', size=14)
plt.tight_layout()
plt.show()

plt.figure()
raw_data['Pendapatan'].hist()
plt.title('Histogram pendapatan', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# transformasi menggunakan akar lima
np.power(raw_data['Pendapatan'], 1/5).hist()
plt.title('Histogram pendapatan - ransformasi menggunakan akar lima', size=14)
plt.tight_layout()
plt.show()

# simpan hasil transformasi
pendapatan_akar_lima = np.power(raw_data['Pendapatan'], 1/5)

plt.figure()
# membuat qqplot pendapatan - transformasi menggunakan akar lima
stats.probplot(pendapatan_akar_lima, plot=plt)
plt.title('qqplot pendapatan - transformasi menggunakan akar lima', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# membuat qqplot pendapatan
stats.probplot(raw_data['Pendapatan'], plot=plt)
plt.title('qqplot pendapatan', size=14)
plt.tight_layout()
plt.show()


# Salah satu cara yang paling mudah untuk melakukan transformasi secara otomatis
# adalah dengan menggunakan transformasi Box-Cox.

# Untuk melakukan transformasi Box-Cox, kita dapat menggunakan method .boxcox dari scipy.

plt.clf()

hasil, _ = stats.boxcox(raw_data['Pendapatan'])

plt.figure()
# Histogram
plt.hist(hasil)
plt.title('Histogram', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# QQPlot
stats.probplot(hasil, plot=plt)
plt.title('qqplot', size=14)
plt.tight_layout()
plt.show()


# Untuk data yang bernilai kategorik agar bisa diolah oleh program harus berupa data berbentuk angka.
# Hal ini akan menjadi masalah tersendiri jika data yang diterima memiliki
# banyak sekali data yang bernilai karakter atau string.
# Untuk menanggulangi hal ini kita bisa menggunakan dummy encoding.

# Dummy encoding atau disebut juga sebagai one-hot encoding adalah suatu metode transformasi
# yang dapat mengubah data bertipe karakter menjadi angka bernilai 1 dan 0 yang menandakan ada
# atau ketiadaan nilai tersebut pada baris data.
# Untuk melakukan dummy encoding pada data kita cukup menggunakan method .get_dummies() dari pandas.

# Perhatikan bahwa variabel class bertipe object.

# Dapat diperhatikan bahwa setelah dilakukan dummy encoding,
# akan terbentuk kolom baru sesuai dengan jumlah kategori pada kolom bertipe object tersebut.
# Nilai 0 menandakan ketiadaan nilai tertentu pada kolom tersebut.
# Sebagai contoh pada kolom B pada baris pertama bernilai 0 karena pada baris pertama raw_data sebelumnya
# tidak ada nilai B namun A.

print(raw_data['Produk'])

data_dummy_produk = pd.get_dummies(raw_data['Produk'])

print(data_dummy_produk)


# Matriks korelasi ada visualisasi data yang dapat menampilkan
# korelasi dari beberapa variabel numerik sekaligus.
# Untuk membuat korelasi matriks, kita dapat menggunakan method .corr() dari pandas
# untuk mendapatkan nilai korelasi dari tiap pasang variabel,
# lalu menggunakan pyplot.matshow() dari matplotlib untuk membuat visualisasi.

# Perhatikan bahwa kita tidak bisa mengetahui dengan tepat variabel apa saja yang dibandingkan.
# Untuk memperoleh visualisasi korelasi matriks yang lebih baik kita dapat menggunakan
# package seaborn dan method .heatmap().

plt.clf()

# mengatur ukuran gambar/plot
plt.rcParams['figure.dpi'] = 100

plt.figure()
plt.matshow(raw_data.corr())
plt.title('Plot correlation matriks dengan .matshow', size=14)
plt.tight_layout()
plt.show()

plt.figure()
sns.heatmap(raw_data.corr(), annot=True)
plt.title('Plot correlation matriks dengan sns.heatmap', size=14)
plt.tight_layout()
plt.show()


# Misalkan kita memiliki variabel yang digunakan untuk mengelompokkan nilai-nilai tertentu,
# misalnya variabel seperti gender, kelas, jenis pekerjaan dan variabel-variabel yang umumnya bertipe nominal.
# Maka kita dapat plot untuk masing-masing grup dengan bantuan grouped plot.


plt.clf()

plt.figure()
# boxplot biasa tanpa pengelompokkan
raw_data.boxplot(rot=90)
plt.title('Boxplot tanpa pengelompokkan', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# box plot dengan pengelompokkan dilakukan oleh kolom 'Produk'
raw_data.boxplot(by='Produk')
plt.tight_layout()
plt.show()


# Kita dapat menggabungkan beberapa histogram dengan bantuan method .groupby
# atau mengelompokkan berdasarkan kolom bertipe kategori melalui
# nama_dataframe[nama_dataframe['kolom_kategori'] == kategori1]
# dengan dari pandas lalu menggunakan method .hist() untuk menggambar histogram.
# Disini kita akan menghasilkan 5 kelompok kolom.

plt.clf()

plt.figure()
raw_data[raw_data['Produk'] == 'A'].hist()
plt.tight_layout()
plt.show()

plt.figure()
raw_data[raw_data['Produk'] == 'B'].hist()
plt.tight_layout()
plt.show()

plt.figure()
raw_data[raw_data['Produk'] == 'C'].hist()
plt.tight_layout()
plt.show()

plt.figure()
raw_data[raw_data['Produk'] == 'D'].hist()
plt.tight_layout()
plt.show()

plt.figure()
raw_data[raw_data['Produk'] == 'E'].hist()
plt.tight_layout()
plt.show()


# Hex bin plot adalah variasi dari scatter plot yang biasanya digunakan ketika
# kita mengolah data yang memiliki banyak sekali titik data.
# Sangat bermanfaat jika kita ingin memvisualisasikan data berukuran sangat besar.
# Kali ini kita akan coba melihat perbandingan Pendapatan dan Total.

plt.clf()

plt.figure()
raw_data.plot.hexbin(x='Pendapatan', y='Total', gridsize=25, rot=90)
plt.tight_layout()
plt.show()
