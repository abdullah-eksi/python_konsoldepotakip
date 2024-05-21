-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 08 Nis 2024, 14:41:58
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `aexp_takip`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `depolar`
--

CREATE TABLE `depolar` (
  `depo_id` int(11) NOT NULL,
  `depo_adi` varchar(150) NOT NULL,
  `depo_telefon` varchar(25) NOT NULL,
  `depo_email` varchar(150) NOT NULL,
  `depo_adres` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Tablo döküm verisi `depolar`
--

INSERT INTO `depolar` (`depo_id`, `depo_adi`, `depo_telefon`, `depo_email`, `depo_adres`) VALUES
(2, 'Ankara Merkez Deposuu', '55555555555', 'test', 'Ankara/ çankaya'),
(4, 'İzmir Merkez Deposu', '555555555555555', 'izmir@aexp.com', 'izmir / bornova '),
(6, 'çanakkale merkez deposu', '555555555555', 'canakkale@aexpsoft.com', 'Çanakkale / Gelibolu');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `log`
--

CREATE TABLE `log` (
  `log_id` int(11) NOT NULL,
  `log_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `log_detay` text NOT NULL,
  `process_type` enum('1','2','3','4','5','6') NOT NULL,
  `log_tablo` varchar(100) NOT NULL,
  `log_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Tablo döküm verisi `log`
--

INSERT INTO `log` (`log_id`, `log_date`, `log_detay`, `process_type`, `log_tablo`, `log_user`) VALUES
(225, '2024-04-07 15:13:22', 'admin kullanıcısı Giriş Yaptı', '5', 'users', NULL),
(227, '2024-04-07 15:14:24', 'admin kullanıcısı Giriş Yaptı', '5', 'users', NULL),
(228, '2024-04-07 15:17:14', 'admin kullanıcısı Giriş Yaptı', '5', 'users', NULL),
(229, '2024-04-07 15:18:03', 'admin kullanıcısı Giriş Yaptı', '5', 'users', NULL),
(230, '2024-04-07 15:18:04', 'Depolar listelendi', '4', 'depolar', 2),
(231, '2024-04-08 11:44:20', 'admin kullanıcısı Giriş Yaptı', '5', 'users', NULL);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urunler`
--

CREATE TABLE `urunler` (
  `urun_id` int(11) NOT NULL,
  `urun_adi` varchar(250) NOT NULL,
  `urun_firma_adi` varchar(150) NOT NULL,
  `depo_no` int(11) NOT NULL,
  `urun_adet` int(20) NOT NULL,
  `urun_kg` double NOT NULL,
  `urun_marka` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Tablo döküm verisi `urunler`
--

INSERT INTO `urunler` (`urun_id`, `urun_adi`, `urun_firma_adi`, `depo_no`, `urun_adet`, `urun_kg`, `urun_marka`) VALUES
(2, 'Asus Tuf ', 'mediamarkt', 2, 50, 55, 'asus'),
(3, 'Yazlık Tişört', 'Lcw', 2, 250, 5, 'Lcw'),
(4, 'Aoc monitör', 'teknosa', 4, 24, 2.5, 'Aoc');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(75) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(75) NOT NULL,
  `authority` enum('0','1') NOT NULL DEFAULT '0',
  `create_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `authority`, `create_date`) VALUES
(2, 'admin', 'info@aexpsoft.com', '21232f297a57a5a743894a0e4a801fc3', '1', '2024-03-20 05:47:13'),
(4, 'abdullah', 'info@abdullaheksi.com.tr', '536a76f94cf7535158f66cfbd4b113b6', '0', '2024-03-20 08:36:34'),
(5, 'ahmet', 'demo@demo.com', '6f24cfc67b3249ffcd94973167329d1f', '1', '2024-03-20 08:38:48'),
(8, 'Adminadmin', 'admin@admin.com', '536a76f94cf7535158f66cfbd4b113b6', '0', '2024-03-23 09:07:15'),
(9, 'tester12', 'tester12', '856fc81623da2150ba2210ba1b51d241', '0', '2024-03-23 09:15:26'),
(10, 'tester2222', '66456544', '202cb962ac59075b964b07152d234b70', '0', '2024-03-23 09:17:07'),
(12, 'tester', 'tester', 'f5d1278e8109edd94e1e4197e04873b9', '1', '2024-04-07 12:43:02'),
(13, 'mehmet', 'mehmet@mehmet.com', '202cb962ac59075b964b07152d234b70', '0', '2024-04-07 12:59:01'),
(14, 'bgt', 'bgt@aexpsoft.com', '536a76f94cf7535158f66cfbd4b113b6', '1', '2024-04-07 14:13:07');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `depolar`
--
ALTER TABLE `depolar`
  ADD PRIMARY KEY (`depo_id`);

--
-- Tablo için indeksler `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`log_id`);

--
-- Tablo için indeksler `urunler`
--
ALTER TABLE `urunler`
  ADD PRIMARY KEY (`urun_id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `depolar`
--
ALTER TABLE `depolar`
  MODIFY `depo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `log`
--
ALTER TABLE `log`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=232;

--
-- Tablo için AUTO_INCREMENT değeri `urunler`
--
ALTER TABLE `urunler`
  MODIFY `urun_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
