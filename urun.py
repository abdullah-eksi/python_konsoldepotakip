import pandas as pd  # veri analizi ve işleme gibi işlemler için eklendi csv olarak log kaydetmek için

class Product:
    def __init__(self, name, company, depot_no, quantity, weight, brand):
        """
        Ürün nesnesi oluşturmak için kullanılan sınıfın yapıcı metodu.

        Args:
            name (str): Ürün adı.
            company (str): Ürünün üretici firma adı.
            depot_no (int): Ürünün bulunduğu depo numarası.
            quantity (int): Ürün miktarı.
            weight (float): Ürün ağırlığı.
            brand (str): Ürün markası.
        """
        self.name = name
        self.company = company
        self.depot_no = depot_no
        self.quantity = quantity
        self.weight = weight
        self.brand = brand

    def add_to_depot(self, db, user_id):
        """
        Ürün ekleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
        params = [
                ("urun_adi", self.name),
                ("urun_firma_adi", self.company),
                ("depo_no", self.depot_no),
                ("urun_adet", self.quantity),
                ("urun_kg", self.weight),
                ("urun_marka", self.brand)
            ]   
        process=db.ekle("urunler",params)
        print(f"{self.quantity} adet {self.name} ürün depoya Başarıyla eklendi")
        
        detail = f"{self.quantity} adet {self.name} ürünü depoya eklendi"
        db.log_activity(user_id, detail, '1', 'urunler')
        
    @staticmethod
    def search_product(db, search_query, user_id):
        """
        Ürün arama işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            search_query (str): Aranacak ürün adı veya markası.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
    
        products= db.listele("urunler",f" urun_adi LIKE '%{search_query}%' OR urun_marka LIKE '%{search_query}%'")
        
        if products:
            columns = ["ID", "Ürün Adı", "Firma Adı", "Depo Numarası", "Adet", "Kg", "Marka"]
            print("\n--- Arama Sonuçları ---")
            df = pd.DataFrame(products, columns=columns)
            print(df.to_string(index=False))
            detail = f"Ürün arandı: {search_query}"
            print("Ürün Arama İşlevi Başarıyla Calıştı")
            db.log_activity(user_id, detail, '4', 'urunler')
        else:
            print("Arama sorgusu eşleşen ürün bulunamadı.")
                
    def edit_product(self, db, user_id, product_id):
        """
        Ürün düzenleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
            product_id (int): Düzenlenecek ürünün ID'si.
        """
        query = f"SELECT * FROM urunler WHERE urun_id = {product_id}"
        existing_product = db.execute_query_with_result(query)
        if not existing_product:
            print("Belirtilen ürün bulunamadı.")
            return
        else:
            print("Mevcut Ürün Bilgileri:")
            print(existing_product)
            new_name = input("Yeni Ürün Adı ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_name == 'x':
                new_name = existing_product[0][1]
            new_company = input("Yeni Firma Adı ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_company == 'x':
                new_company = existing_product[0][2]
            depo_number = input("Yeni Deponun Numarası ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if depo_number == 'x':
                depo_number = existing_product[0][3]    
            new_quantity = input("Yeni Adet ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_quantity == 'x':
                new_quantity = existing_product[0][4]
            new_weight = input("Yeni Ağırlık ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_weight == 'x':
                new_weight = existing_product[0][5]
            new_brand = input("Yeni Marka ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_brand == 'x':
                new_brand = existing_product[0][6]
            
            
            params = [
                ("urun_adi", new_name),
                ("urun_firma_adi", new_company),
                ("depo_no", depo_number),
                ("urun_adet",new_quantity),
                ("urun_kg", new_weight),
                ("urun_marka", new_brand)
            ]   
            
            process=db.guncelle("urunler",params,f"urun_id = {product_id}")
            print("Ürün Başarıyla Güncellendi")
            detail = f"{existing_product[0][1]} ürünü düzenlendi"
            db.log_activity(user_id, detail, '3', 'urunler')
            
            
    def remove_product(self, db, user_id, product_id):
        """
        Ürün kaldırma işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
            product_id (int): Kaldırılacak ürünün ID'si.
        """
        query = f"SELECT * FROM urunler WHERE ürün_id = {product_id}"
        existing_product = db.execute_query_with_result(query)
        if not existing_product:
            print("Belirtilen ürün bulunamadı.")
            return
        else:
            process=db.sil("urunler",f"ürün_id = {product_id}")
            print("Ürün Başarıyla Kaldırıldı.")
            detail = f"{existing_product[0][1]} ürünü kaldırıldı"
            db.log_activity(user_id, detail, '2', 'urunler')
                        

    @staticmethod
    def list_products(db, user_id):
        """
        Ürünleri listeleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
        products= db.listele("urunler")
        if products:
            columns = ["ID", "Ürün Adı", "Firma Adı", "Depo Numarası", "Adet", "Kg", "Marka"]
            print("")
            df = pd.DataFrame(products, columns=columns)
            print(df.to_string(index=False))
            print("Ürünler Başarıyla Listelendi")
            detail = "Ürünler listelendi"
            db.log_activity(user_id, detail, '4', 'urunler')
        else:
            print("Ürün bulunamadı.")
