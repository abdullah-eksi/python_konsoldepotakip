import pandas as pd  # veri analizi ve işleme gibi işlemler için eklendi csv olarak log kaydetmek için

class Depot:
    def __init__(self, name, phone, email, address):
        """
        Depo nesnesi oluşturmak için kullanılan sınıfın yapıcı metodu.

        Args:
            name (str): Depo adı.
            phone (str): Depo telefon numarası.
            email (str): Depo e-posta adresi.
            address (str): Depo adresi.
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def add_depot(self, db, user_id):
        """
        Depo ekleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
      
        params = [
                ("depo_adi", self.name),
                ("depo_telefon", self.phone),
                ("depo_email", self.email),
                ("depo_adres", self.address)
            ]
        
        process=db.ekle("depolar",params)
        
        print("Depo Başarıyla Eklendi.")
        detail = f"{self.name} depo eklendi"
        db.log_activity(user_id, detail, '1', 'depolar')
        
    def remove_depot(self, db, user_id, depot_id):
        """
        Depo kaldırma işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
            depot_id (int): Kaldırılacak depo ID'si.
        """
    
        existing_depot= db.listele("depolar",f"depo_id = {depot_id}")
        
        if not existing_depot:
            print("Belirtilen depo bulunamadı.")
            return
        else:
            process=db.sil("depolar",f"depo_id = {depot_id}")
            print("Depo Başarıyla Kaldırıldı.")
            detail = f"{existing_depot[0][1]} deposu kaldırıldı"
            db.log_activity(user_id, detail, '2', 'depolar')
            
                
    def edit_depot(self, db, user_id, depot_id):
        """
        Depo düzenleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
            depot_id (int): Düzenlenecek depo ID'si.
        """
        existing_depot= db.listele("depolar",f"depo_id = {depot_id}")
        
        if not existing_depot:
            print("Belirtilen depo bulunamadı.")
            return
        else:
            print("Mevcut Depo Bilgileri:")
            print(existing_depot)
            new_name = input("Yeni Depo Adı ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_name == 'x':
                new_name = existing_depot[0][1]
            new_phone = input("Yeni Telefon ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_phone == 'x':
                new_phone = existing_depot[0][2]
            new_email = input("Yeni E-posta ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_email == 'x':
                new_email = existing_depot[0][3]
            new_address = input("Yeni Adres ( 'x' göndererek eski değeri koruyabilirsiniz): ")
            if new_address == 'x':
                new_address = existing_depot[0][4]
            params = [
                ("depo_adi", new_name),
                ("depo_telefon", new_phone),
                ("depo_email", new_email),
                ("depo_adres", new_address)
            ]    
            process=db.guncelle("depolar",params,f"depo_id = {depot_id}")
            print("Depo Başarıyla Güncellendi.")
            detail = f"{existing_depot[0][1]} deposu düzenlendi"
            db.log_activity(user_id, detail, '3', 'depolar')    

    @staticmethod
    def list_depots(db, user_id):
        """
        Depoları listeleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
       
        depots = db.listele("depolar")
        if depots:
            columns = ["Depo İd", "Depo Adı", "Depo Telefon", "Depo Eposta", "Depo Adres"]
            print("")
            df = pd.DataFrame(depots, columns=columns)
            print(df.to_string(index=False))
            print("Depo Başarıyla listelendi.")
            detail = "Depolar listelendi"
            db.log_activity(user_id, detail, '4', 'depolar')
        else:
            print("Depo bulunamadı.")



