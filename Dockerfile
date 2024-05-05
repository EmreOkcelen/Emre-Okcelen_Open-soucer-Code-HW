# Base image olarak Python 3.11.6 kullan
FROM python:3.11.6

# Host'tan Docker container'a dosyaları kopyala
COPY . /home/ubuntu/Desktop/170421929_Emreokcelen_opensource

# Çalışma dizinini belirle
WORKDIR /home/ubuntu/Desktop/170421929_Emreokcelen_opensource

# Gerekli Python paketlerini yükle
RUN pip install --no-cache-dir -r Requirements.txt

# Uygulamayı başlat
CMD ["python", "app.py"]

# Port 5000'i dışarıya aç
EXPOSE 5000

