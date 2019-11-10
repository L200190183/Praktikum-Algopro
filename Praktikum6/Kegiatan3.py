Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  Nama = 'Indriarto Dwi Nugroho'
 
SyntaxError: unexpected indent
>>> Nama = 'Indriarto Dwi Nugroho'
>>> NIM = 'L200190183'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Variabel a adalah data yang awalnya berupa string dan diubah menjadi integer.
>>> a / b
56.333333333333336
>>> # Data tersebut bertipe Float karena variabel bernilai 1183 dibagi dengan variabel b yang bernilai 21 dan menghasilkan nilai 56.333333333333336 yang merupakan bilangan Float
>>> a // b
56
>>> # Data tersebut bertipe integer karena variabel bernilai 1183 dibagi dengan variabel b yang bernilai 21 dan menghasilkan nilai 56.333333333333336 dan dibulatkan menjadi 56 yang merupakan bilangan Float.
>>> 10 * (a - 999)
1840
>>>  # Data tersebut bertipe integer karena data dari variabel a yang bernilai 1183 dikurang dengan nilai 999 menghasilkan nilai 184 dan kemudian dikalikan dengan nilai 10 dan menghasilkan nilai 1840.
 
>>> b ** 2
441
>>> # Data tersebut bertipe integer karena data dari variabel b dipangkatkan 2 yang menghasilkan data yang bernili 441.
>>> a % b
7
>>> # Data tersebut bertipe integer karena simbol % merupakan sisa hasil bagi dari data variabel a dibagi data variabel b yaitu 7.
>>> c = 12.5
>>> # data 12.5 disimpan dalam variabel c.
>>> type(c)
<class 'float'>
>>> # variabel c merupakan data float karena mengandung nilai desimal.
>>> a / c
94.64
>>> # Data tersebut bertipe float karena data variabel a dibagi dengan data variabel c  sama dengan 94.64 atau 1183 dibagi 12.5 menghasilkan data 94.64 yang bertipe float atau bernilai desimal.
>>> a // c
94.0
>>> # Data tersebut bertipe float karena dalam variabel c terkandung data bertipe float dan hasil pembagian dibulatkan kebawah dari pada variabel a yang bernilai integer dan menghasilkan data bertipe float (1183 dibagi 12.5 dan dibultkan menjadi 94.0).
>>> a % c
8.0
>>> # Data tersebut bertipe float karena sisa hasil bagi dari antara kedua variabel menghasilkan nilai 8.0 yang bertipe float karena mengandung nilai desimal.
>>> c > b
False
>>> # merupakan data yang bertipe boolean yang bernilai false karena variabel c lebih kecil daripada variabel b dan menghasilkan program yang tidak sesuai dan bernilai salah.
>>> type(c > b)
<class 'bool'>
>>> # Merupakan data yang bertipe boolean yang memiliki 2 kondisi atau nilai yakni true atau false, yang merupakan operator logika.
>>> a > b and b > c
True
>>> # data tersebut bernilai boolean yang bernilai true karena a > b bernilai true b > c bernilai sama. dalam operator and jika keduanya bernilai true maka akan menghasilkan nilai operator True juga.
>>> a > 1100 or b < 10
True
>>> # merupakan data yang bertipe boolean yang berkondisi true a > 1100 dan b < 10 bernilai false, dalam operator 'or' apabila salah akan lebih besaryang bernilai true dan menampilkan nilai yang lebih besar.
