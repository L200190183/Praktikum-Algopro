## Program Akun
## Dibuat Oleh Indriarto Dwi Nugroho L200190183
import random
angka = random.randint(0,1000)

Nama = 'Indriarto Dwi Nugroho'
TanggalLahir = '25 Agustus 2001'
NamaSingkat = Nama[0] + '.' + Nama[10] + '.' + Nama[14:21]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:17]
Password = Nama[0:3] + str(angka)
