Program ini dirancang untuk memprediksi apakah konten media sosial akan menjadi viral berdasarkan berbagai fitur dari konten tersebut. Program ini menggunakan algoritma Machine Learning Classification untuk mengkategorikan konten ke dalam tiga kelas: 'Tidak Viral', 'Lumayan Viral', dan 'Viral'. Machine Learning Classification adalah salah satu teknik dalam machine learning yang digunakan untuk mengkategorikan data ke dalam kelas atau kategori yang telah ditentukan sebelumnya. Dalam machine learning classification, model dilatih menggunakan data yang telah diberi label. Data ini terdiri dari fitur-fitur (atribut) dan label (kelas). Langkah-langkah yang terlibat dalam program ini meliputi prapemrosesan data, penskalaan fitur, pelatihan model, prediksi, evaluasi, dan tuning hyperparameter. Berikut adalah deskripsi rinci dari setiap langkah dalam program ini:
  1. **Mengimpor Library**: Library Python yang diperlukan diimpor, termasuk 'pandas' untuk manipulasi data, 'sklearn' untuk tugas pembelajaran mesin, dan 'numpy' untuk operasi numerik.
  2. **Memuat Dataset**: Dataset dimuat dari file CSV ke dalam DataFrame Pandas. Jalur file ditentukan, dan data dibaca menggunakan pd.read_csv().
  3. **Mengkategorikan Variabel Target**: Variabel target yang kontinu 'shares' diubah menjadi variabel kategori. Fungsi 'categorize_shares' didefinisikan untuk mengategorikan 'shares' ke dalam tiga kategori berdasarkan ambang batas yang ditentukan.
  4. **Memisahkan Fitur dan Target**: Fitur (X) dan variabel target (y) dipisahkan. Kolom 'url', 'shares', dan 'shares_category' dihapus dari set fitur.
  5. **Mengkodekan Variabel Target**: Variabel target 'y' dikodekan menjadi label numerik menggunakan 'LabelEncoder'.
  6. **Membagi Data**: Dataset dibagi menjadi set pelatihan dan pengujian menggunakan 'train_test_split'. 80% dari data digunakan untuk pelatihan, dan 20% untuk pengujian.
  7. **Normalisasi Fitur**: Fitur dinormalisasi menggunakan 'StandardScaler' untuk memastikan semua fitur berkontribusi secara setara pada pelatihan model.
  8. **Melatih Model**: Random Forest Classifier dilatih pada data pelatihan yang telah diskalakan. Model diinisialisasi dengan 100 pohon dan kedalaman maksimum 10.
  9. **Membuat Prediksi**: Prediksi dibuat pada set pengujian menggunakan model yang telah dilatih.
  10. **Mengevaluasi Model**: Kinerja model dievaluasi menggunakan akurasi, presisi, recall, dan laporan klasifikasi.
  11. **Tuning Hyperparameter**: Langkah opsional tuning hyperparameter dilakukan menggunakan GridSearchCV untuk menemukan parameter terbaik untuk Random Forest Classifier.

**Running Model**
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/48cbfa6c-4455-449a-856d-6d6196fded21)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/570f907f-df70-42fe-8695-47816dc1f11c)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/7844cd30-dc30-4798-a9e9-64b4fc8dba50)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/36efe277-c964-4a04-a7e6-3a1cea3e8b70)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/18ebc413-6b39-4978-a694-c346221112b8)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/f347cee3-a786-4c84-aaa4-7de129a97985)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/c4ed017e-2c4f-4af8-ab2e-469dcf0e45ef)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/cf4ebcb8-12a9-46e8-b442-dc84ecb4e178)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/92b79eba-d2ae-4abd-b5f6-2bb06195103c)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/13631d10-74ae-423a-b27f-716d9644f6b0)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/26d6ef35-6049-46ed-889c-e7cc64fb84a0)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/c64ed556-2c0a-4e73-8f80-9367af83abdd)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/b65a0327-b377-4181-85b3-0cafb1a4bed1)

**Running Interface**
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/0876f171-7f6f-456b-8f12-9af3086763aa)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/8f6afa45-d265-496c-87d0-37417bff2e7d)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/2c579ff0-8740-4a22-93fe-52e99c76b849)
![image](https://github.com/rutooya/71220923_Debora-Patricia-Sharon-Rembet_Prediksi-Viral-Konten-Sosial-Media_Classification/assets/117901340/0c0ac7f8-fe55-4389-aa13-a41ad21e94cf)
