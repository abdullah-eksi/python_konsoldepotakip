from database import Database # Veritabanı sınıfı ve metodlarını içerir ekleme silme düzenleme kaldırma gibi metodlar eklidir
from user import User # kullanıcı sınıfı ve metodlarını içerir
from depo import Depot # Depo sınıfı ve metodlarını içerir
from urun import Product # Ürün sınıfı ve metodlarını içerir

'''

Başlangıç Tarihi : 23/03/2024

Bitiş Tarihi : 8/04/2024

Developer : Abdullah Ekşi

Proje Adı : AeXp Depo Takip Otomosyonu

proje Amacı: Kullanıcıların Sisteme Kayıt olup depolar ekleyip ekledikleri depoya ürün ekleyip stok takipi

ürün takipi gibi işlemleri yapmasını kolaylaştırır

'''

def main():
    db = Database(host="localhost", user="root", password="", database="aexp_takip")
    db.connect()
    
    print("\n#########################################\n")
    print("AeXp Depo Takip Uygulamasına Hoş geldiniz! ")
    print("\n#########################################\n")
    print(" -- Bu Program Ne İşe Yarar \n")
    print(" ;Depolarınızı Rahatca Yönetebilirsiniz ")
    print(" ;Depolarınızdaki Ürünleri Yönetebilirsiniz ")
    print(" ;Ürün Sorgusu yapabilirsiniz ")
    print(" -- Bu Program Nasıl Kullanılır \n")
    print(" ;Öncelikle Sisteme Giriş Yapın / Giriş Yapmak için seçiminizi yapın kısmına 1 girmeniz yeterli olcaktır")
    print(" ;Eğer Üye Değilseniz Kayıt Olun / kayıt olmak için seçiminizi yapın kısmına 2 girmeniz yeterli olcaktır")
    print(" ;Artık Sisteme Giriş Yapmış Bulunmaktasınız  \n")
    print(" ;Yapmak İstediğiniz İşlemi Menüden Bulun")
    print(" ;Yapmak İstediğiniz İşlemin Yanındaki Numarayı Yazınız")
    print(" ;Seçtiğiniz İşleme GÖre Yönergeleri Takip Edin")
    print(" ;Ve İşleminizi Başarıyla Gerçekleştirin")
    
    print("\n#########################################\n")
    print("Developed By - Abdullah Ekşi ")
    print("\n#########################################\n")
    
    
    authority = None 
    while True:
        print("\n--- Menü ---\n")
        print("1. Giriş Yap")
        print("2. Kayıt Ol")
        print("")
        choice = input("Seçiminizi yapın: ")
    
        match choice:
            case "1":
                username = input("Kullanıcı Adı: ")
                password = input("Şifre: ")
                user_id, authority = User.login(username, password, db)

                if user_id:
                    # Giriş başarılı, Program Devam Ediyor
                    break
            case "2":
                username = input("Kullanıcı Adı: ")
                email = input("E-posta: ")
                password = input("Şifre: ")
                new_user = User(username, email, password)  # Yetki parametresi verilmedi, varsayılan olarak '0' atanacak
                new_user.register(db)
            case _:
                print("Geçersiz seçenek. Tekrar deneyin.")
    
    # Kullanıcı girişi başarılı işlemlere devam edebiliriz
    while True:
        print("\n--- Menü ---\n")
        print("1. Depo Ekle")
        print("2. Depo Düzenle")
        print("3. Depo Listele")
        print("4. Depo Kaldır")
        
        print("\n------------\n")
        print("5. Yeni Ürün Ekle")
        print("6. Ürün Düzenle")
        print("7. Ürün Kaldır")
        print("8. Ürün Listele")
        print("9. Ürün Aratma")
        print("\n------------\n")
        
        if authority == "1":  # Eğer kullanıcı yönetici ise
            print("10. Yönetici Ekle")
            print("11. Sistemdeki Kullanıcıları Listele")
            print("12. Logları Excel'e Aktar")
            
        print("0. Çıkış Yap \n")

        choice = input("Seçiminizi yapın: ")

        match choice:
            case "1":
                print("\n--- Depo Ekle ---")
                name = input("Depo Adı: ")
                phone = input("Telefon: ")
                email = input("E-posta: ")
                address = input("Adres: ")
                new_depot = Depot(name, phone, email, address)
                new_depot.add_depot(db, user_id)
                print("Depo başarıyla eklendi.")
            case "2":
                print("\n--- Depo Düzenle ---")
                Depot.list_depots(db, user_id)
                depot_id = int(input("Düzenlemek istediğiniz depo ID'sini girin: "))
                depot = Depot("", "", "", "")  # Boş bir depo örneği oluşturduk, değerler kullanıcıdan alınacak
                depot.edit_depot(db, user_id, depot_id)
                print("Depo başarıyla Düzenlendi.")
            case "3":
                print("\n--- Depo Listele ---")
                Depot.list_depots(db, user_id)
            case "4":
                print("\n--- Depo Kaldır ---")
                Depot.list_depots(db, user_id)
                depot_id = int(input("Kaldırmak istediğiniz depo ID'sini girin: "))
                depot = Depot("", "", "", "")  # Boş bir depo örneği oluşturduk, değerler kullanıcıdan alınacak
                depot.remove_depot(db, user_id, depot_id)
            case "5":
                print("\n--- Yeni Ürün Ekle ---")
                name = input("Ürün Adı: ")
                company = input("Firma Adı: ")
                depot_no = int(input("Depo Numarası: "))
                quantity = int(input("Adet: "))
                weight = float(input("Ağırlık (kg): "))
                brand = input("Marka: ")
                new_product = Product(name, company, depot_no, quantity, weight, brand)
                new_product.add_to_depot(db, user_id)
                print("Ürün başarıyla eklendi.")
            case "6":
                print("\n--- Ürün Düzenle ---")
                Product.list_products(db, user_id)
                product_id = int(input("Düzenlemek istediğiniz ürün ID'sini girin: "))
                product = Product("", "", 0, 0, 0.0, "")  # Boş bir ürün örneği oluşturduk, değerler kullanıcıdan alınacak
                product.edit_product(db, user_id, product_id)
            case "7":
                print("\n--- Ürün Kaldır ---")
                Product.list_products(db)
                product_id = int(input("Kaldırmak istediğiniz ürün ID'sini girin: "))
                product = Product("", "", 0, 0, 0.0, "")  # Boş bir ürün örneği oluşturduk, değerler kullanıcıdan alınacak
                product.remove_product(db, user_id, product_id)
            case "8":
                print("\n--- Ürün Listele ---")
                Product.list_products(db, user_id)
            case "9":
                print("\n--- Ürün Arama ---")
                search_query = input("Aranacak ürün adı veya marka: ")
                Product.search_product(db, search_query, user_id)
            case "0":
                break
            case "10" if authority == "1":
                print("\n--- Yönetici Ekle ---")
                username = input("Yönetici Kullanıcı Adı: ")
                email = input("Yönetici E-posta: ")
                password = input("Yönetici Şifre: ")
                Depot.add_admin(db, username, email, password, user_id)
            case "11" if authority == "1":
                print("\n--- Kullanıcı Listele ---")
                User.list_users(db, user_id)
            case "12" if authority == "1":
                print("\n--- Logları Excel'e Aktar ---")
                print("1. Tüm Logları Excel'e Aktar")
                print("2. İşlem Tipine Göre Logları Excel'e Aktar")
                print("3. Kullanıcıya Göre Logları Excel'e Aktar")
                export_choice = input("Seçiminizi yapın: ")
                match export_choice:
                    case "1":
                        db.export_logs_to_excel()
                    case "2":
                        process_type = input("Listelenmesini istediğiniz işlem tipini girin: ")
                        db.export_logs_to_excel(process_type=process_type)
                    case "3":
                        user_id = input("Listelenmesini istediğiniz kullanıcının ID'sini girin (Tüm kullanıcılar için 'all' girin): ")
                        db.export_logs_to_excel(user_id=user_id)
                    case _:
                        print("Geçersiz seçenek. Tekrar deneyin.")
            case _:
                print("Geçersiz seçenek. Tekrar deneyin.")

    # Veritabanı Bağlantısını Kapat Ve Programı Bitir
    db.disconnect()

if __name__ == "__main__":
    main()
