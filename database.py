import mysql.connector # mysql bağlantısını sağlamak için eklendi
from mysql.connector import Error # mysql bağlantısında hata ayıklamak için eklendi
from datetime import datetime # tarih saat işlemleri için eklendi
import pandas as pd  # veri analizi ve işleme gibi işlemler için eklendi csv olarak log kaydetmek için
import os # işletim sistemi ile ilgili işlemler için dizin alma işlemleri vs için


class Database:
    def __init__(self, host, user, password, database):
        """
        Veritabanı bağlantısı için gerekli bilgileri içeren Database sınıfının yapıcı metodu.

        Args:
            host (str): Veritabanı sunucusunun adresi.
            user (str): Veritabanı kullanıcı adı.
            password (str): Veritabanı şifresi.
            database (str): Kullanılacak veritabanı adı.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Veritabanına bağlanmayı sağlayan metod.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            #print("Bağlantı başarılı!")
        except Error as e:
            print(f"Hata: {e}")

    def disconnect(self):
        """
        Veritabanı bağlantısını sonlandıran metod.
        """
        if self.connection.is_connected():
            self.connection.close()
            print("Program kapatıldı.")

    def execute_query(self, query):
        """
        Veritabanında bir sorguyu çalıştırmayı sağlayan metod.

        Args:
            query (str): Çalıştırılacak SQL sorgusu.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            #print("Sorgu başarıyla çalıştırıldı.")
        except Error as e:
            print(f"Hata: {e}")

    def execute_query_with_result(self, query):
        """
        Veritabanında bir sorguyu çalıştırıp sonuçları almayı sağlayan metod.

        Args:
            query (str): Çalıştırılacak SQL sorgusu.

        Returns:
            list: Sorgu sonuçlarının bulunduğu liste.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Hata: {e}")
            return None
            
                 
              
    def listele(self, table_name, where=None):
        try:
            cursor = self.connection.cursor()
            sorgu = f"SELECT * FROM {table_name}"
            if where:
                sorgu += f" WHERE {where}"
            cursor.execute(sorgu)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Hata: {e}")
            return None

    def ekle(self, table_name, columns_values):
        try:
            cursor = self.connection.cursor()
            columns = ', '.join([item[0] for item in columns_values])
            values = [item[1] for item in columns_values]
            placeholders = ', '.join(['%s' for _ in values])
            sorgu = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sorgu, values)
            self.connection.commit()
        except Error as e:
            print(f"Hata: {e}")

    def guncelle(self, table_name, columns_values, where):
        try:
            cursor = self.connection.cursor()
            set_clause = ', '.join([f"{item[0]} = %s" for item in columns_values])
            values = [item[1] for item in columns_values]
            sorgu = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
            cursor.execute(sorgu, values)
            self.connection.commit()
        except Error as e:
            print(f"Hata: {e}")

    def sil(self, table_name, where):
        """
        Belirli bir Tablodan Belirli Bir Koşula Göre Veri Silme işlevi.

        Args:
            table_name (str): Silme işlem yapılcak tablo adı
            where (str): where koşulu.
        """
        try:
            cursor = self.connection.cursor()
            sorgu = f"DELETE FROM {table_name} WHERE {where}"
            cursor.execute(sorgu)
            self.connection.commit()
        except Error as e:
            print(f"Hata: {e}")   
            
    def log_activity(self, user_id, detail, process_type, table_name):
        """
        Belirli bir işlemi loglama işlevi.

        Args:
            user_id (int): İşlemi gerçekleştiren kullanıcının ID'si.
            detail (str): İşlemle ilgili detaylı bilgi.
            process_type (int): İşlem tipi. Aşağıdaki değerlerden biri olabilir:
                1: Ekleme
                2: Silme
                3: Düzenleme
                4: Listeleme - Görüntüleme
                5: Giriş Yapma
                6: Kayıt Olma
            table_name (str): İşlem yapılan tablo adı.
        """
        try:
            log_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            columns_values = [
                ("log_date", log_date),
                ("log_detay", detail),
                ("process_type", process_type),
                ("log_tablo", table_name)
            ]
            if user_id is not None:
                columns_values.append(("log_user", user_id))
            self.ekle("log", columns_values)
        except Error as e:
            print(f"Hata: {e}")
            



    def export_logs_to_excel(self, process_type='all', user_id='all'):
        """
        Belirli işlem tiplerine veya belirli kullanıcıya ait logları Excel'e aktarma işlevi.

        Args:
            process_type (str, optional): Aktarılacak işlem tipleri. Varsayılan değer 'all'dir.
            user_id (str, optional): Aktarılacak kullanıcının ID'si. Varsayılan değer 'all'dir.
        """
        try:
            if process_type == 'all' and user_id == 'all':
                logs = self.listele('log')
                filename = f"log_all"
            elif process_type == 'all':
                logs = self.listele('log', f"log_user = {user_id}")
                filename = f"log_user_{user_id}_all"
            elif user_id == 'all':
                logs = self.listele('log', f"process_type = '{process_type}'")
                filename = f"log_process_{process_type}_all"
            else:
                logs = self.listele('log', f"process_type = '{process_type}' AND log_user = {user_id}")
                filename = f"log_process_{process_type}_user_{user_id}"
            
            # Kaydedilecek dosyanın adını belirleme
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = f"{timestamp}_{filename}.xlsx"
            
            # Dosya yolunu oluşturma
            file_path = os.path.join("log_kayitlari", log_filename)
            
            # Verileri Excel'e kaydetme
            self.save_to_csv(logs, file_path)
            
            print(f"{log_filename} adlı Excel dosyası 'log_kayitlari' klasörüne kaydedildi. \n")
        except Exception as e:
            print(f"Hata: {e}") 
            

    def save_to_csv(self, logs, file_path):
        """
        Verilen logları bir Excel dosyasına kaydeden metod.

        Args:
            logs (list): Kaydedilecek log verileri.
            file_path (str): Kaydedilecek Excel dosyasının dosya yolu.
        """
        try:
            columns = ['Log İd', 'Log Tarihi', 'Log Açıklama', 'İşlem Türü', 'Log Tablo', 'Kullanıcı No']
            # DataFrame oluşturma
            df = pd.DataFrame(logs,columns=columns)
            
            # Excel'e yazma
            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)
            
            print(f"{file_path} adlı Excel dosyası oluşturuldu. \n")
        except Exception as e:
            print(f"Hata: {e}")           