import os
import time
import whisper
import torch
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

# ffmpeg yolunu sistem PATH'ine ekle (Windows için)
os.environ["PATH"] += os.pathsep + r"C:\Users\ckjiyat\Desktop\S2T\ffmpeg\bin"

# ffmpeg kontrolü
print("[🧪] ffmpeg bulundu mu?:", shutil.which("ffmpeg"))

# Cihaz kontrolü (GPU varsa kullan)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[🖥️] Kullanılan cihaz: {device}")
if device == "cuda":
    print("🧪 CUDA aktif, cihaz adı:", torch.cuda.get_device_name(0))
    print("🧪 Toplam GPU belleği:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2), "GB")

# Daha hafif model kullanarak hız kazanılabilir (large yerine small)
model = whisper.load_model("large", device=device)

# Giriş ve çıkış klasörleri
input_folder = "input"
output_folder = "output"

# .mp3 dosyası klasöre eklendiğinde yapılacak işlemi tanımladık
class MP3Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".mp3"):
            return

        filename = os.path.basename(event.src_path)
        full_path = os.path.abspath(event.src_path)
        print(f"[🎧] Yeni dosya bulundu: {filename}")
        print(f"[🧩] Tam yol: {full_path}")

        try:
            start_time = time.time()
            result = model.transcribe(full_path, language="turkish")
            print(result["text"])  # Konsola döküm
            print("⏱ Transkripsiyon süresi:", round(time.time() - start_time, 2), "saniye")

            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])
            print(f"[✅] Çeviri tamamlandı → {output_path}")
        except Exception as e:
            print(f"[⛔] Hata: {e}")

# İzleyici başlat
if __name__ == "__main__":
    event_handler = MP3Handler()
    observer = Observer()
    observer.schedule(event_handler, path=input_folder, recursive=False)
    observer.start()
    print("[👀] Klasör izleniyor. Dosya bırakıldığında otomatik işlenecek.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("İzleme durduruldu.")

    observer.join()
