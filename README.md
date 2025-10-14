<div align="center">

# Fall Detection with MediaPipe & YOLOv8

### **Detecting and automatically clipping the falling moments from video**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-8.2.81-purple.svg)](https://github.com/ultralytics/ultralytics)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.14-green.svg)](https://mediapipe.dev/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.10.0-red.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


https://github.com/user-attachments/assets/28cb6c5f-01f8-475c-84ad-77d337183929

*This video demonstrates automatic fall detection and extraction from the original video*

---

**[🇹🇷 Türkçe](#tr)** • **[🇬🇧 English](#en)**

---

</div>

<a name="en"></a>
## 🇬🇧 English

### 📋 Table of Contents
- [About the Project](#about-en)
- [How It Works](#how-en)
- [Requirements](#requirements-en)
- [Usage](#usage-en)
- [Important Notes](#notes-en)

<a name="about-en"></a>
### 🎯 About the Project

This project detects people in videos using **YOLOv8** and analyzes their posture with **MediaPipe**. When a fall is detected, **the falling moment is automatically clipped from the video** and saved as a separate file.

**Key Features:**
- Detects humans in video frames using YOLOv8
- Analyzes body posture through MediaPipe pose estimation
- Calculates torso angle based on shoulder and hip positions
- Automatically clips and saves fall moments from the video

<a name="how-en"></a>
### ⚙️ How It Works

1. **Person Detection**: YOLOv8 detects people in each frame
2. **Posture Analysis**: MediaPipe calculates the torso angle using shoulder and hip landmarks
3. **Fall Classification**: If the torso angle exceeds a threshold, the person is classified as falling
4. **Automatic Clipping**: Fall moments are automatically extracted and saved as separate video files

<a name="requirements-en"></a>
### 📦 Requirements

```bash
pip install numpy==2.1.0 opencv-python==4.10.0.84 ultralytics==8.2.81 mediapipe==0.10.14 collection==0.1.6
```

<a name="usage-en"></a>
### 🚀 Usage

```bash
python main.py
```

> [!NOTE]
> On first run, YOLOv8 will automatically download the `yolov8n.pt` model file (~6MB). Internet connection required for initial setup.

<a name="notes-en"></a>
### ⚠️ Important Notes

> [!IMPORTANT]
> If you encounter this error:
> ```
> ValueError: while processing the input streams of subgraph node InferenceCalculator: 
> TAG:index:name is invalid...
> ```
> 
> This issue occurs when your system locale is set to Turkish. MediaPipe requires English locale.
>
> **Solution:**
> 
> 1. Edit locale configuration:
>    ```bash
>    sudo nano /etc/locale.gen
>    ```
>
> 2. Enable English and disable Turkish:
>    - Remove `#` from `en_US.UTF-8 UTF-8`
>    - Add `#` to `tr_TR.UTF-8 UTF-8`
>
> 3. Update locale:
>    ```bash
>    sudo update-locale LANG=en_US.UTF-8
>    ```
>
> 4. Reboot:
>    ```bash
>    sudo reboot
>    ```

---

<a name="tr"></a>
## 🇹🇷 Türkçe

### 📋 İçindekiler
- [Proje Hakkında](#about-tr)
- [Nasıl Çalışır](#how-tr)
- [Gereksinimler](#requirements-tr)
- [Kullanım](#usage-tr)
- [Önemli Notlar](#notes-tr)

<a name="about-tr"></a>
### 🎯 Proje Hakkında

Bu proje, **YOLOv8** kullanarak videodaki insanları tespit eder ve **MediaPipe** ile duruş analizi yapar. Düşme tespit edildiğinde, **düşme anı otomatik olarak videodan kırpılır** ve ayrı bir dosya olarak kaydedilir.

**Temel Özellikler:**
- YOLOv8 ile video karelerinde insan tespiti
- MediaPipe ile vücut duruşu analizi
- Omuz ve kalça pozisyonlarına göre gövde açısı hesaplama
- Düşme anlarının otomatik olarak kırpılması ve kaydedilmesi

<a name="how-tr"></a>
### ⚙️ Nasıl Çalışır

1. **İnsan Tespiti**: YOLOv8 her karede insanları tespit eder
2. **Duruş Analizi**: MediaPipe omuz ve kalça işaretleyicilerini kullanarak gövde açısını hesaplar
3. **Düşme Sınıflandırması**: Gövde açısı belirli bir eşiği aştığında kişi düşüyor olarak sınıflandırılır
4. **Otomatik Kırpma**: Düşme anları otomatik olarak ayıklanır ve ayrı video dosyaları olarak kaydedilir

<a name="requirements-tr"></a>
### 📦 Gereksinimler

```bash
pip install numpy==2.1.0 opencv-python==4.10.0.84 ultralytics==8.2.81 mediapipe==0.10.14 collection==0.1.6
```

<a name="usage-tr"></a>
### 🚀 Kullanım

```bash
python main.py
```

> [!NOTE]
> İlk çalıştırmada YOLOv8 otomatik olarak `yolov8n.pt` model dosyasını indirecektir (~6MB). İlk kurulum için internet bağlantısı gereklidir.

<a name="notes-tr"></a>
### ⚠️ Önemli Notlar

> [!IMPORTANT]
> Şu hatayı alıyorsanız:
> ```
> ValueError: while processing the input streams of subgraph node InferenceCalculator: 
> TAG:index:name is invalid...
> ```
> 
> Bu sorun, sistem dilinizin Türkçe olmasından kaynaklanır. MediaPipe İngilizce yerel ayar gerektirir.
>
> **Çözüm:**
> 
> 1. Dil yapılandırmasını düzenleyin:
>    ```bash
>    sudo nano /etc/locale.gen
>    ```
>
> 2. İngilizce'yi etkinleştirin, Türkçe'yi devre dışı bırakın:
>    - `en_US.UTF-8 UTF-8` satırından `#` işaretini kaldırın
>    - `tr_TR.UTF-8 UTF-8` satırına `#` ekleyin
>
> 3. Dil ayarlarını güncelleyin:
>    ```bash
>    sudo update-locale LANG=en_US.UTF-8
>    ```
>
> 4. Bilgisayarı yeniden başlatın:
>    ```bash
>    sudo reboot
>    ```
