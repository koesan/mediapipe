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
3. **Düşme Algılama**: Eğer kişi düşme durumunda tespit edilirse, bu durum bir video dosyasına kaydedilir. Düşme sonrası belirli bir süre boyunca da kayıt yapılır. Düşme süresi ve kayıt süresi, video üzerinde düşmenin nasıl tespit edildiğini ve işlendiğini gösterir.
4. **Video Çıkışı**: İşlenen video ve tespit edilen düşme olaylarını içeren videolar çıktı olarak kaydedilir.

## Gereksinimler

- `numpy 2.1.0`
- `opencv-python 4.10.0.84`
- `ultralytics 8.2.81` 
- `mediapipe 0.10.14`
- `collection 0.1.6`


Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install numpy==2.1.0 opencv-python==4.10.0.84 ultralytics==8.2.81 mediapipe==0.10.14 collection==0.1.6
```
