import math
import numpy as np
import cv2
from collections import deque
from ultralytics import YOLO
import mediapipe as mp

# YOLO modelini yükle
model = YOLO('yolov8n.pt')
# Video dosyasının yolu
video_yolu = 'fall.mp4'

# Video kaynağını aç
kamera = cv2.VideoCapture(video_yolu)
fps = kamera.get(cv2.CAP_PROP_FPS)  # FPS değerini al
genislik = int(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))  # Videonun genişliği
yukseklik = int(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Videonun yüksekliği

# Çıkış videosu için VideoWriter tanımla
video_yazici = cv2.VideoWriter('4_cikis_video_uyari.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (genislik, yukseklik))

# Değişkenlerin başlangıç değerlerini tanımla
dusme_sayaci = 0
dusme_tespit_edildi = False
dusme_video_yazici = None
dusme_video_sayisi = 0
dusme_sonrasi_kareler = 0
dusme_sonrasi_bekleme_suresi = 10  # Düşme sonrası 2 saniye daha kayıt yap

tampon_boyutu = 10  # 1 saniyelik video tamponu
kare_tamponu = deque(maxlen=tampon_boyutu)  # Halka tamponu (circular buffer)

# Mediapipe çizim ve pose (duruş) modüllerini yükle
mp_cizim = mp.solutions.drawing_utils
mp_poz = mp.solutions.pose

# İki nokta arasındaki açıyı hesaplayan fonksiyon
def aci_hesapla(omuz_merkezi, kalca_merkezi):
    dy = omuz_merkezi[1] - kalca_merkezi[1]  # Y eksenindeki fark
    dx = omuz_merkezi[0] - kalca_merkezi[0]  # X eksenindeki fark
    aci = math.atan2(dy, dx)  # Atan2 ile açıyı hesapla
    return abs(90 - np.degrees(aci))  # Açı farkını derecelere çevir ve 90'dan çıkar

# Torso açısına göre duruşu sınıflandıran fonksiyon
def durus_siniflandir(torso_aci, ayakta_esik=20, yatay_esik=50):
    if torso_aci < ayakta_esik:
        return "Ayakta"
    elif torso_aci > yatay_esik:
        return "Yatıyor"
    else:
        return "Düşüyor"

# Pose modülü ile işlemleri başlat
with mp_poz.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as poz:
    while kamera.isOpened():
        ret, kare = kamera.read() 
        if not ret:
            break  # Video bittiğinde döngüyü sonlandır

        sonuclar = model(kare)  
        for sonuc in sonuclar:
            for bbox, sinif in zip(sonuc.boxes.xyxy, sonuc.boxes.cls):
                if int(sinif) == 0:  # "0" sınıfı insan sınıfı olarak kabul ediliyor
                    x1, y1, x2, y2 = map(int, bbox) 
                    kisi_bbox = kare[y1:y2, x1:x2]  # İlgili kişinin çerçevesini al

                    kisi_bbox_rgb = cv2.cvtColor(kisi_bbox, cv2.COLOR_BGR2RGB)  # Kişi çerçevesini RGB renk formatına çevir
                    kisi_sonuclari = poz.process(kisi_bbox_rgb)  # Pose modülü ile kişinin duruşunu analiz et

                    if kisi_sonuclari.pose_landmarks:  # Eğer duruş işaretleri bulunursa
                        isaretler = kisi_sonuclari.pose_landmarks.landmark
                        omuzlar = [
                            (isaretler[mp_poz.PoseLandmark.LEFT_SHOULDER.value].x * kisi_bbox.shape[1], isaretler[mp_poz.PoseLandmark.LEFT_SHOULDER.value].y * kisi_bbox.shape[0]),
                            (isaretler[mp_poz.PoseLandmark.RIGHT_SHOULDER.value].x * kisi_bbox.shape[1], isaretler[mp_poz.PoseLandmark.RIGHT_SHOULDER.value].y * kisi_bbox.shape[0])
                        ]
                        kalcalar = [
                            (isaretler[mp_poz.PoseLandmark.LEFT_HIP.value].x * kisi_bbox.shape[1], isaretler[mp_poz.PoseLandmark.LEFT_HIP.value].y * kisi_bbox.shape[0]),
                            (isaretler[mp_poz.PoseLandmark.RIGHT_HIP.value].x * kisi_bbox.shape[1], isaretler[mp_poz.PoseLandmark.RIGHT_HIP.value].y * kisi_bbox.shape[0])
                        ]

                        # Omuz ve kalça merkezlerini hesapla
                        omuz_merkezi = ((omuzlar[0][0] + omuzlar[1][0]) / 2, (omuzlar[0][1] + omuzlar[1][1]) / 2)
                        kalca_merkezi = ((kalcalar[0][0] + kalcalar[1][0]) / 2, (kalcalar[0][1] + kalcalar[1][1]) / 2)

                        # Torso açısını hesapla
                        torso_aci = aci_hesapla(kalca_merkezi, omuz_merkezi)
                        durus = durus_siniflandir(torso_aci)  # Duruşu sınıflandır

                        # Düşme durumu algılandığında yapılacak işlemler
                        if durus == "Düşüyor":
                            dusme_sayaci += 1
                            dusme_sonrasi_kareler = 0  # Yeni bir düşme algılandığında süreyi sıfırla
                            if dusme_sayaci >= 0.1 * fps and dusme_sayaci <= 0.5 * fps and dusme_video_yazici is None:
                                dusme_video_sayisi += 1
                                dusme_video_dosyasi = f'dusme_{dusme_video_sayisi}.mp4'  # Düşme videosunun dosya adı
                                dusme_video_yazici = cv2.VideoWriter(dusme_video_dosyasi, cv2.VideoWriter_fourcc(*'mp4v'), fps, (genislik, yukseklik))
                                
                                # Tampondaki tüm kareleri yaz
                                while kare_tamponu:
                                    dusme_video_yazici.write(kare_tamponu.popleft())
                        else:
                            dusme_sayaci = 0  # Düşme tespit edilmezse sayacı sıfırla

                        # Eğer düşme videosu kaydediliyorsa kareyi kaydet
                        if dusme_video_yazici is not None:
                            dusme_video_yazici.write(kare)

                        # Ayakta duruş algılandığında, düşme sonrası kayıt süresini say
                        if durus == "Ayakta" and dusme_video_yazici is not None:
                            dusme_sonrasi_kareler += 1

                    # Kişinin çerçevesini videodaki orijinal kareye yerleştir
                    kare[y1:y2, x1:x2] = kisi_bbox

        # Kareyi tampona ekle
        kare_tamponu.append(kare)

        # Video kaydını yaz
        video_yazici.write(kare)

        # Eğer düşme sonrası bekleme süresi tamamlandıysa, video kaydını sonlandır
        if dusme_sonrasi_kareler > dusme_sonrasi_bekleme_suresi and dusme_video_yazici is not None:
            dusme_video_yazici.release()
            dusme_video_yazici = None

# Tüm kaynakları serbest bırak
kamera.release()
video_yazici.release()

if dusme_video_yazici is not None:
    dusme_video_yazici.release()
