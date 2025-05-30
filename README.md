# Hangman Game (Adam Asmaca)

Bu, Python ve Pygame kullanılarak geliştirilmiş klasik bir **Hangman (Adam Asmaca)** oyunudur. Oyuncu, gizli kelimeyi tahmin etmeye çalışırken sınırlı sayıda yanlış yapma hakkına sahiptir. Oyun, zorluk seviyesi seçimi, skor takibi ve ipucu butonu gibi özellikler içerir.

## 🎮 Özellikler

* 3 zorluk seviyesi: **Kolay**, **Normal**, **Zor**
* 100'den fazla kelimelik kelime havuzu
* Skor takibi: doğru tahminlerde puan kazanılır, yanlışlarda puan kaybedilir
* **İpucu** (Hint) butonu ile rastgele bir harf açılır
* Oyun sonunda **Yeni Oyun** ve **Çıkış** seçenekleri
* Kullanıcı dostu grafik arayüz

## 🛠 Kurulum

1. Python 3 yüklü olduğundan emin olun.
2. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install pygame
   ```
3. `hangman0.png` ile `hangman6.png` arası 7 farklı resim dosyasını proje dizinine yerleştirin. Bu dosyalar, adam asmaca figürünün aşamalarını temsil eder.

## ▶️ Oyunu Başlatma

```bash
python hangman.py
```

## 🎯 Oyun Kuralları

* Oyuna başlamadan önce **Kolay**, **Normal**, veya **Zor** seviyelerinden biri seçilir.
* Harf butonlarına tıklayarak kelime tahmin edilir.
* Yanlış tahminler adam asmaca çizimini ilerletir.
* 6 yanlış tahminden sonra oyun sona erer.
* **Hint** butonuna tıklayarak doğru kelimeden rastgele bir harf açılır.
* Her doğru tahmin +50 puan kazandırır, her yanlış tahmin -10 puan kaybettirir.

## 📁 Dosya Yapısı

```
hangman_game/
│
├── hangman.py             # Ana oyun kodu
├── hangman0.png           # Adam asmaca resmi (başlangıç)
├── hangman1.png
├── ...
├── hangman6.png           # Adam asmaca resmi (tamamlandı)
└── README.md              # Bu dosya
```

## 🧠 Geliştirici Notları

* Kodda `pygame.Rect` nesneleri ile butonlar tanımlanmıştır.
* Zorluk seçim ekranı dinamik olarak çizilir.
* Harf butonları ve oyun ekranı pikseller üzerinden manuel konumlandırılmıştır.
* Yeni oyun için ekran sıfırlanır ve skor devam eder.

## 📌 Gereksinimler

* Python 3.6+
* Pygame 2.0+

## 📝 Lisans

Bu proje öğrenim ve eğlence amaçlı olarak açık kaynak şekilde paylaşılmıştır. Ticari olmayan projelerde serbestçe kullanılabilir.
