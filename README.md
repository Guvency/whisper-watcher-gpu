# 🎧 Whisper Watcher GPU

Whisper Watcher, input klasörüne sürüklenen `.mp3` dosyalarını otomatik algılayarak metne çeviren bir Python uygulamasıdır. OpenAI'nin Whisper modelini kullanır. `watchdog` kütüphanesi sayesinde klasör izlenir ve yeni gelen dosyalar anında işlenir.

---

## 🚀 GPU Destekli Hızlı Sürüm

Eğer sisteminizde CUDA destekli bir NVIDIA ekran kartı varsa, `whisper_watch_gpu.py` dosyasını çalıştırarak transkripsiyon süresini büyük ölçüde hızlandırabilirsiniz.

---

## 🚀 Özellikler

- 👀 `watchdog` ile gerçek zamanlı klasör izleme
- 🧠 Whisper Large modeli kullanır
- ⚡ GPU desteği (varsa CUDA ile otomatik hızlanır)
- 📄 Çıktıyı `.txt` dosyası olarak `output/` klasörüne kaydeder
- 💬 Türkçe transkripsiyon desteği
- 🪄 Basit, açıklayıcı Python kodu

---

## ⚙️ Gereksinimler

- Python 3.9+ önerilir
- FFmpeg (ayrıca sistem PATH'ine eklenmelidir)
- CUDA destekli ekran kartı (GPU hızlandırma için)

---

### 📦 requirements.txt

```text
torch>=2.0.0
watchdog
openai-whisper
```

---

## GPU Desteği 

Whisper, varsayılan olarak CUDA destekli NVIDIA GPU'ları kullanır. Otomatik olarak algılanır. Eğer sisteminde GPU varsa çok daha hızlı çalışır.

```python
import torch
torch.cuda.is_available()  # True çıkmalı
```

---

## ⚡ Performans

| Kayıt Süresi | CPU Süresi | GPU Süresi |
|--------------|------------|------------|
| 6 dakika     | ~12 dk     | ~1.5 dk    |
| 12 dakika    | ~18 dk     | ~3 dk      |

---

## 📦 Kurulum

```bash
git clone https://github.com/Guvency/whisper-watcher.git
cd whisper-watcher
pip install -r requirements.txt
```

---

## 📂 ffmpeg Kurulumu (Windows için)
1. https://www.gyan.dev/ffmpeg/builds/ adresinden Essentials Build zip dosyasını indir.

2. Dosyayı çıkart, ffmpeg\\bin klasörünü örneğin C:\\ffmpeg\\bin olarak konumlandır.

3. Path ortam değişkenlerine bu yolu ekle:

Denetim Masası → Sistem → Gelişmiş Sistem Ayarları → Ortam Değişkenleri → Path → Yeni → C:\\ffmpeg\\bin

4. Komut satırını kapatıp açtıktan sonra test et:
```bash
ffmpeg -version
```

---

### ▶️ Kullanım

1. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

2. Klasörleri oluşturun:

```bash
mkdir input output
```

3. Scripti başlatın:

```bash
python whisper_watcher.py
```

4. `input/` klasörüne `.mp3` dosyası bırakın. Otomatik olarak yazıya çevrilip `output/` klasörüne `.txt` dosyası olarak kaydedilecektir.

---

## 📁 Klasör Yapısı

```
whisper-watcher/
│
├── input/              # mp3 dosyalarını buraya bırak
├── output/             # .txt sonuçlar buraya yazılır
├── whisper_watch.py    # ana izleyici script
├── README.md           # bu dosya
└── requirements.txt    # bağımlılık listesi
```

---


## 🧠 Whisper Large GPU ile Kullanım

Kod otomatik olarak GPU varsa kullanır, yoksa CPU ile çalışır:

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("large", device=device)
```

---

## 📜 Lisans

MIT License.

---

## ✨ İlham

Bu proje, Whisper ile otomatik transkripsiyonun basit ama etkili bir örneğini gösteren whisper-watcher'ı GPU yardımıyla hızlandırmak için hazırlandı.
