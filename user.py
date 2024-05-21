from hashlib import md5 # kullanıcılarımızın şifrelerini güvenli şekilde kaydetmek için eklendi
import pandas as pd  # veri analizi ve işleme gibi işlemler için eklendi csv olarak log kaydetmek için



class User:
    def __init__(self, username, email, password, authority='0'):  # Yetki varsayılan Kullanıclara  '0' olarak ayarlandı
        """
        Kullanıcı nesnesi oluşturmak için kullanılan sınıfın yapıcı metodu.

        Args:
            username (str): Kullanıcının kullanıcı adı.
            email (str): Kullanıcının e-posta adresi.
            password (str): Kullanıcının şifresi.
            authority (enum "0","1"): Kullanıcının yetki seviyesi. Varsayılan değer '0'.
        """
        self.username = username
        self.email = email
        self.password = password
        self.authority = authority

    def register(self, db):
        """
        Kullanıcı kaydını gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
        """
        if not self.username or not self.email or not self.password:
            print("Kayıt olurken kullanıcı adı, e-posta ve şifre zorunludur.")
            return
        
        username_exists = db.listele("users", f"username = '{self.username}'")
        email_exists = db.listele("users", f"email = '{self.email}'")
        
        if username_exists or email_exists:
            print("Bu kullanıcı adı veya eposta zaten kullanımda. Lütfen farklı bir kullanıcı adı veya eposta seçiniz.")
            return
        else:
            hashed_password = md5(self.password.encode()).hexdigest()
            params= [("username", self.username), ("email", self.email), ("password", hashed_password), ("authority", self.authority)]
            db.ekle("users", params )
            print("Kullanıcı başarıyla kaydedildi. Şimdi giriş yapabilirsiniz.")
            db.log_activity(None, f"{self.username} kullanıcısı kaydedildi", '6', 'users')

    
    @staticmethod
    def login(username, password, db):
        """
        Kullanıcı girişini gerçekleştiren ve yetki seviyesini döndüren metod.

        Args:
            username (str): Kullanıcının kullanıcı adı.
            password (str): Kullanıcının şifresi.
            db (Database): Kullanılacak veritabanı nesnesi.

        Returns:
            tuple: Kullanıcı ID'si ve yetki seviyesi.
        """
        if not username or not password:
            print("Kullanıcı adı veya şifrenizi girmediniz.")
            return None, None
        
        hashed_password = md5(password.encode()).hexdigest()
        result = db.listele("users", f"username = '{username}' AND password = '{hashed_password}'")
        
        if result:
            print("Giriş başarılı!")
            db.log_activity(None, f"{username} kullanıcısı Giriş Yaptı", '5', 'users')
            return result[0][0], result[0][4]  # Kullanıcı ID'sini ve yetkiyi döndür
        else:
            print("Kullanıcı adı veya şifre hatalı.")
            return None, None
    
    @staticmethod
    def list_users(db, user_id):
        """
        Kullanıcıları listeleme işlemini gerçekleştiren metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
        users = db.listele("users")
        
        if users:
            columns = ["id", "Kullanıcı Adı", "Eposta", "Yetkisi", "Hesap Açılış Tarihi"]
            print("")
            df = pd.DataFrame(users, columns=columns)
            print(df.to_string(index=False))
            detail = "Kullanıcılar listelendi"
            db.log_activity(user_id, detail, '4', 'users')
        else:
            print("Kullanıcı bulunamadı.")
            
    @staticmethod
    def add_admin(db, username, email, password, user_id):
        """
        Yeni yönetici eklemek için kullanılan metod.

        Args:
            db (Database): Kullanılacak veritabanı nesnesi.
            username (str): Yeni yöneticinin kullanıcı adı.
            email (str): Yeni yöneticinin e-posta adresi.
            password (str): Yeni yöneticinin şifresi.
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
        """
        if not username or not email or not password:  
            print("Kullanıcı adı, e-posta ve şifre zorunludur.")
            return
        hashed_password = md5(password.encode()).hexdigest()
        query = f"INSERT INTO users (username, email, password, authority) VALUES ('{username}', '{email}', '{hashed_password}', '1')"
        db.execute_query(query)
        print("Yönetici başarıyla eklendi.")
        detail = f"Yeni yönetici eklendi: {username}"
        db.log_activity(user_id, detail, '6', 'users')
