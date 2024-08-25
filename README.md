# Düşme Tespiti

Proje, YOLOv8 modelini kullanarak videodaki insanları tespit eder, tespit edilen insan bölgelerini keser ve MediaPipe kütüphanesi ile duruş analizi yapar.

Projenin temel amacı, bir kişinin düşme durumlarını doğru bir şekilde belirlemek ve bu durumları videoya kaydeder. Bu işlem, video üzerindeki hareketleri ve duruşları analiz ederek gerçekleştirilir.

## Özellikler

- **İnsan Tespiti**: YOLOv8 modelini kullanarak videodaki insanları tespit eder.
- **Duruş Analizi**: MediaPipe ile kişinin duruşunu analiz eder.
- **Düşme Algılama**: Düşme durumlarını belirleyip kaydeder.
- **Video Çıkışı**: Düşme durumlarını içeren videoları ve genel video akışını kaydeder.

## Nasıl Çalışır?

1. **İnsan Tespiti**: YOLOv8 modeli, her video karesinde insanları tespit eder ve insan bölgelerini keser.
2. **Duruş Analizi**: Kesilen insan bölgeleri, MediaPipe kullanılarak duruş analizi için işlenir. Duruş açısı hesaplanır ve kişinin ayakta mı, yatıyor mu, yoksa düşüyor mu olduğu belirlenir.
   - **Duruş Açısı Hesaplama**: Kişinin omuzları ve kalçaları arasındaki açıyı hesaplamak için bu bölgelerin merkezleri arasındaki açı ölçülür. Omuz ve kalça merkezleri hesaplanarak bu merkezler arasındaki açı belirlenir. Bu açı, kişinin dik durup durmadığını anlamak için kullanılır.
   - **Düşme Durumu Tespiti**: Duruş açısı belirli bir eşik değerinin altına düştüğünde kişinin düşme durumunda olduğu tespit edilir. Örneğin, kişi neredeyse yatay bir pozisyondaysa bu düşme olarak değerlendirilir. Bu eşik değerleri, kişinin duruşunu doğru bir şekilde sınıflandırmak için ayarlanabilir.
3. **Düşme Algılama**: Eğer kişi düşme durumunda tespit edilirse, bu durum bir video dosyasına kaydedilir. Düşme sonrası belirli bir süre boyunca da kayıt yapılır.
4. **Video Çıkışı**: İşlenen video ve tespit edilen düşme olaylarını içeren videolar çıktı olarak kaydedilir.

***

## Gereksinimler

- `numpy 2.1.0`
- `opencv-python 4.10.0.84`
- `ultralytics 8.2.81` 
- `mediapipe 0.10.14`
- `collection 0.1.6`

```bash
pip install numpy==2.1.0 opencv-python==4.10.0.84 ultralytics==8.2.81 mediapipe==0.10.14 collection==0.1.6
```
> [!NOTE]
> 
> ```
> ValueError: while processing the input streams of subgraph node InferenceCalculator: TAG:index:name is invalid, "TENSORS:posedetectioncpu__Inferencecalculator__posedetectioncpu__input_tensors" does not match "([A-Z_][A-Z0-9_]*:((0|[1-9][0-9]*):)?)?[a-z_][a-z0-9_]*" (examples: "TAG:name" "VIDEO:2:name_b", "longer_name").
> ```
> 
> Yukardaki hatayı alıyorsanız, bu sorun bilgisayarınızın dilinin Türkçe olmasından kaynaklanıyor olabilir. Bu sorunu çözmek için bilgisayarınızın dilini İngilizce olarak değiştirmeniz gerekebilir. Aşağıdaki adımları izleyin:
> 
> 1. **Dil Dosyasını Düzenleyin:**
>
>    ```bash
>    sudo nano /etc/locale.gen
>    ```
>
> 2. **İngilizce Dil Seçeneğini Etkinleştirin ve Türkçe'yi Yorum Satırı Haline Getirin:**
>
>    - `en_US.UTF-8 UTF-8` satırındaki yorum satırını kaldırın (satırın başındaki `#` karakterini silin).
>    - `tr_TR.UTF-8 UTF-8` satırına yorum satırı ekleyin (satırın başına `#` karakterini ekleyin).
>
>3. **Yerelleştirme Ayarlarını Güncelleyin:**
>
>    ```bash
>    sudo update-locale
>    ```
>
>4. **Bilgisayarı Yeniden Başlatın:**
>
>    ```bash
>    sudo reboot
>    ```
>
> 5. **Sorun Devam Ediyorsa:**
>
>    - Dil ayarını doğrudan İngilizce olarak ayarlayın:
>
>        ```bash
>        sudo update-locale LANG=en_US.UTF-8
>        ```
>
>    - Türkçe dil paketini kaldırın:
>
>        ```bash
>        sudo apt remove language-pack-tr
>        ```
>
>    - Bilgisayarı tekrar yeniden başlatın:
>
>        ```bash
>        sudo reboot
>        ```
>
> Bu adımlar, dil kaynaklı hatayı düzeltmeli ve ilgili kodunuzun çalışmasını sağlamalıdır.
>

![gif](https://github.com/koesan/mediapipe/blob/main/video/dusme_1.mp4)

