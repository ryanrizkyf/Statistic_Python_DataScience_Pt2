# Untuk menggambar scatter plot kita dapat menggunakan
# method .plot.scatter() pada pandas atau menggunakan .scatter() pada matplotlib

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
