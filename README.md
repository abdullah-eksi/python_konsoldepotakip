


# AeXp Depo Takip Konsol Uygulaması
Konsol Üzerinde Çalışan Basit Bir Depo stok takip uygulamasıdır

## Ne İşe Yarar

- Basit Şekilde Depolarınızı Rahatca Yönetebilirsiniz.
- Basit Şekilde Depolarınızdaki Ürünleri Yönetebilirsiniz
- Basit Şekilde Ürün Sorgusu yapabilirsiniz

## Nasıl Kullanılır

 - Öncelikle Sisteme Giriş Yapın / Giriş Yapmak için seçiminizi yapın
 - kısmına 1 girmeniz yeterli olcaktır Eğer Üye Değilseniz Kayıt Olun /
 - kayıt olmak için seçiminizi yapın kısmına 2 girmeniz yeterli olcaktır
 -  Artık Sisteme Giriş Yapmış Bulunmaktasınız  Yapmak İstediğiniz İşlemi
 - Menüden Bulun Yapmak İstediğiniz İşlemin Yanındaki Numarayı Yazınız
 - Seçtiğiniz İşleme Göre Yönergeleri Takip Edin Ve İşleminizi Başarıyla
   Gerçekleştirin
   
## Gereksinimler
-   Python 3.x
-   MySQL veritabanı
## Çalıştırma
Programı çalıştırmak için terminalde aşağıdaki komutu çalıştırın:

    # Gerekli Kütüphaneleri Yükleyin
    
    pip install -r requirements.txt
    
	# Daha  Sonra Kodu Derlemek İçin Terminale Aşağıdaki Kodu Girin
	
    python main.py

## İşleyiş

Program başlatıldığında kullanıcıyı karşılayan bir hoş geldiniz mesajı ve programın nasıl kullanılacağına dair açıklamalar görüntülenir. Kullanıcılar aşağıdaki seçenekler ile programı kullanabilirler:

1.  **Giriş Yap**
    
    -   Kullanıcı adı ve şifre ile sisteme giriş yapılır.
    -   Giriş başarılı olursa, kullanıcı işlemler menüsüne yönlendirilir.
2.  **Kayıt Ol**
    
    -   Yeni bir kullanıcı adı, e-posta ve şifre girerek kayıt oluşturulur.
    -   Kayıt başarılı olursa, kullanıcı tekrar giriş yapma ekranına yönlendirilir.

### Kullanıcı Girişi Sonrası İşlemler

Giriş yaptıktan sonra kullanıcı aşağıdaki işlemleri gerçekleştirebilir:

1.  **Depo İşlemleri**
    
    -   **Depo Ekle:** Yeni bir depo ekler.
    -   **Depo Düzenle:** Var olan bir depoyu düzenler.
    -   **Depo Listele:** Tüm depoları listeler.
    -   **Depo Kaldır:** Var olan bir depoyu kaldırır.
2.  **Ürün İşlemleri**
    
    -   **Yeni Ürün Ekle:** Depoya yeni bir ürün ekler.
    -   **Ürün Düzenle:** Var olan bir ürünü düzenler.
    -   **Ürün Kaldır:** Var olan bir ürünü kaldırır.
    -   **Ürün Listele:** Tüm ürünleri listeler.
    -   **Ürün Arama:** Belirli bir ürün adı veya marka ile arama yapar.
3.  **Yönetici İşlemleri (Yönetici yetkisi olan kullanıcılar için)**
    
    -   **Yönetici Ekle:** Yeni bir yönetici ekler.
    -   **Kullanıcı Listele:** Tüm kullanıcıları listeler.
    -   **Logları Excel'e Aktar:** Tüm logları veya belirli kriterlere göre logları Excel'e aktarır.
4.  **Çıkış Yap**
    
    -   Sistemden çıkış yapar ve programı sonlandırır.


### Sınıfların Ve Modüllerin Çalışma Mantığı

 ###  ---- Modüller / ----
	
-   **Database modülü**: Bu modül içerisinde `Database` sınıfı bulunmaktadır. Bu sınıf, veritabanı bağlantısı ve veritabanı işlemleri ile ilgili metodları içerir. Ayrıca, log kaydı ile ilgili metodlar da bu sınıfta bulunmaktadır.
-   **User modülü**: Bu modül, `User` sınıfını ve kullanıcı işlemlerini barındırmak amacıyla oluşturulmuştur. `User` sınıfı sayesinde, kullanıcı bilgilerini çekebilir ve log kaydı yaparken hangi kullanıcının işlem yaptığını anlayabiliriz. Bu sayede, `Database` sınıfımızdaki log metoduyla log kaydı yapabiliriz.
-   **Depo modülü**: Bu modül içerisinde `Depot` adlı sınıf bulunmaktadır ve depo ile ilgili işlemleri barındıran bazı metodlar içerir.
-   **Ürün modülü**: Bu modülde ise `Product` sınıfı bulunmaktadır ve ürünlerle ilgili işlemleri yapmamızı sağlayan bazı metodlar içerir.
### ---- Sınıflar / Class ----
	
-   **Database**: Database Sınıfı Veritabanı bağlantısını ve temel veritabanı metodlarını İçerir Aynı Zamanda Log Kaydı Gibi İşlemler İçin Bazı Metodlar Bu sınıfta bulunmaktadır.
    
    -   `connect()`: Veritabanına bağlanır.
    -   `disconnect()`: Veritabanı bağlantısını kapatır.
    -   `execute_query(query)`: Veritabanında belirtilen sorguyu çalıştırır.
    -   `export_logs_to_excel()`: Logları Excel dosyasına aktarır.
    
-   **User**: User sınıfı  Kullanıcı işlemlerini ve kullanıcı metodlarını içerir (kayıt, giriş, kullanıcı listesi).
    
    -   `__init__(self, username, email, password)`: Yeni kullanıcı oluşturur.
    -   `register(db)`: Kullanıcıyı veritabanına kaydeder.
    -   `login(username, password, db)`: Kullanıcı girişini doğrular.
    -   `list_users(db)`: Tüm kullanıcıları listeler.
    - 
-   **Depot**: Depo sınıfı Depo işlemlerini yönetir ve depo metodlarını içerir (depo ekleme, düzenleme, listeleme, kaldırma).
    
    -   `__init__(self, name, phone, email, address)`: Yeni depo oluşturur.
    -   `add_depot(db, user_id)`: Depoyu veritabanına ekler.
    -   `edit_depot(db, user_id, depot_id)`: Depoyu düzenler.
    -   `list_depots(db, user_id)`: Kullanıcının depolarını listeler.
    -   `remove_depot(db, user_id, depot_id)`: Depoyu kaldırır.
    -   `add_admin(db, username, email, password, user_id)`: Yeni yönetici ekler.
    - 
-   **Product**: Ürün Sınıfı Ürün işlemlerini yönetir ve bazı ürün metodlarını içerir (ürün ekleme, düzenleme, listeleme, kaldırma, arama).
    
    -   `__init__(self, name, company, depot_no, quantity, weight, brand)`: Yeni ürün oluşturur.
    -   `add_to_depot(db, user_id)`: Ürünü depoya ekler.
    -   `edit_product(db, user_id, product_id)`: Ürünü düzenler.
    -   `list_products(db, user_id)`: Kullanıcının ürünlerini listeler.
    -   `remove_product(db, user_id, product_id)`: Ürünü kaldırır.
    -   `search_product(db, search_query, user_id)`: Belirli kriterlere göre ürün arar.
## Loglar Nereye Kaydoluyor ? 
loglar aktif olarak veritabanına kaydolmakta her işlem yapıldığında fakat eğer yönetici iseniz excele aktar seçeniğini seçip proje dizinindeki `log_kayitlari` klasoru altına kaydedebilirsiniz 

# Lisans 
Bu proje MIT Lisansı kapsamında lisanslanmıştır; ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

## Abdullah Ekşi
