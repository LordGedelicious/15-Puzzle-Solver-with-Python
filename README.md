# Penyelesaian Persoalan 15-Puzzle dengan Algoritma _Branch and Bound_

> Program dalam format `.py` dalam bahasa Python untuk menentukan ada tidaknya solusi pada sebuah 15-puzzle menggunakan algoritma _Branch and Bound_
> Bila ditemukan, maka akan dicari solusi _step-by-step_ menuju solusi
> sebagai Tugas Kecil 3 IF2211 Strategi Algoritma

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Penggunaan](#penggunaan)
- [Identitas](#identitas)

## Deskripsi
Algoritma _Branch and Bound_ (B&B) adalah algoritma yang umum digunakan untuk persoalan optimasi, atau persoalan-persoalan yang perlu memaksimumkan atau meminimumkan suatu fungsi objektif tanpa melanggar fungsi batasan atau constraints. Algoritma ini menggabungkan konsep _Breadth-First Search_ (BFS) dan _least-cost search_. Bila pada algoritma BFS hanya menggunakan aturan FIFO untuk pembangkitan simpul baru, algoritma B&B menggunakan nilai taksiran lintasan tercepat atau dengan cost menuju simpul tujuan atau goal node yang minimum untuk menentukan urutan ekspansi simpul, untuk kasus minimasi.
Sebelum mencari solusi, program akan mencari nilai dari akumulasi KURANG(i) + X dari puzzle. Nilai KURANG(i) dari setiap petak pada puzzle adalah jumlah semua petak selanjutnya yang nilainya kurang dari petak acuan. Lalu, nilai X adalah hasil dari fungsi boolean terhadap posisi petak kosong pada puzzle. Jika nilai totalnya genap, maka terdapat solusi untuk puzzle tersebut. Sebaliknya, jika ganjil, tidak ada solusi untuk puzzle tersebut.
Bila sebuah puzzle memiliki solusi, maka akan dicari langkah-langkah untuk mencapai solusi menggunakan fungsi _branch and bound_. Pembangkitan simpul didasarkan pada semua 
puzzle baru hasil pergerakan satu langkah dari puzzle pada simpul awal. Dari setiap simpul, akan dicari prioritas pengecekan simpul selanjutnya dengan mencari simpul dengan cost minimum. Pada kasus dimana terdapat dua atau lebih simpul dengan cost minimum, maka akan dicari simpul yang lebih dalam (lebih banyak langkah yang dibutuhkan untuk mencapai simpul tersebut dari _root_). Proses ini akan berulang hingga ditemukan simpul dengan susunan puzzle yang tepat.
Setelah ditemukan semua langkah-langkah untuk mencapai solusi, maka akan diprint ke dalam sebuah text file langkah-langkah beserta kondisi puzzle pada langkah tersebut. Akan diprint juga waktu yang dibutuhkan untuk mendapatkan solusi, jumlah langkah yang dibutuhkan dari awal hingga akhir, serta jumlah simpul yang dibangkitkan pada proses pencarian.

Isi direktori adalah sebagai berikut:
```
├── doc  [laporan tugas kecil 3]
├── input  [testcase, 3 puzzle yang dapat diselesaikan, 2 puzzle tidak memiliki solusi]
    ├── inputPossible1.txt
    ├── inputPossible2.txt
    ├── inputPossible3.txt
    ├── inputImpossible1.txt
    ├── inputImpossible2.txt
├── output [tempat menampung semua output file text file]   
├── src   
    ├── main.py [main file yang diakses oleh pengguna]
    ├── matrixCreator.py [helper file untuk inisiasi matriks ke dalam program utama]
    ├── bNb.py [helper file untuk menggunakan algoritma branch and bound]
```

Pada repository ini, terdapat file `output1.txt` pada folder `output`. Ini dilakukan agar folder `output` dapat dimasukkan ke dalam repository (repository melakukan auto-delete terhadap folder yang kosong. File ini dapat didelete atau dioverwrite setelah di-download/di-clone.

## Penggunaan
1. Buka direktori `src` dan buka terminal. Alternatifnya adalah menggunakan command `cd` menuju direktori `src` pada direktori utama ini.
2. Jalankan kode `py main.py`.
3. Tuliskan nama file output untuk menyimpan hasil dari program. Penamaan dibatasi menggunakan karakter alphanumeric.
4. Pilih metode yang diinginkan, random-generated matrix atau user-based file input.
5. Bila pada langkah 4 memilih random-generated matrix, maka cukup menunggu program selesai melakukan kalkulasi. 
6. Bila pada langkah 5 memilih user-based file input, masukkan nama file yang mengandung matriks puzzle. File textfile harus merupakan file yang mengandung angka 1 sampai 16 yang terpisahkan oleh spasi dan dibagi menjadi 4 bilangan pada 4 baris. Angka 16 menunjuk kepada petak kosong pada puzzle. File harus berada di dalam folder `input` dan berekstensi `.txt`.
7. Akan ditampilkan success message dan hasil dapat dilihat pada file text dengan filename yang sama pada input langkah 3 di folder `output`

**[WARNING]** Program membutuhkan waktu yang lama untuk matriks puzzle dengan nilai KURANG(i) + X. Pada proses debugging penulis, dibutuhkan waktu kurang lebih 2 jam untuk memproses matriks yang memiliki nilai KURANG(i) + X = 84.

## Identitas
- <a href = "https://github.com/LordGedelicious">Gede Prasidha Bhawarnawa (13520004 - K01)</a>
