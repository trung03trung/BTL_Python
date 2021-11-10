-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: onlineshop
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `home_order`
--

DROP TABLE IF EXISTS `home_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_order` (
  `Order_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `quantity` varchar(5) NOT NULL,
  `price` double NOT NULL,
  `address` longtext NOT NULL,
  `phone` varchar(12) NOT NULL,
  `date` date NOT NULL,
  `product` varchar(200) NOT NULL,
  `user_id` int NOT NULL,
  `image` varchar(100) NOT NULL,
  `total` double NOT NULL,
  `size` varchar(4) NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `home_order_user_id_a9204bb2_fk_auth_user_id` (`user_id`),
  CONSTRAINT `home_order_user_id_a9204bb2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_order`
--

LOCK TABLES `home_order` WRITE;
/*!40000 ALTER TABLE `home_order` DISABLE KEYS */;
INSERT INTO `home_order` VALUES (39,'Nguyễn Văn A','1',320000,'Hà Nội','0965584453','2021-11-10','Áo nỉ nam hàn quốc',1,'/ao-ni-nam-han-quoc-1.jpg',320000,'L'),(40,'Nguyễn Văn A','2',250000,'Hà Nội','0965584453','2021-11-10','Bộ Quần Áo Thể Thao Nam Kẻ Sọc Thời Trang Cao Cấp',1,'/c87212a113b633e994a0f0c4907fc9b4.jpg',500000,'XL'),(41,'Nguyễn Văn B','1',250000,'Hồ Chí Minh','0965584453','2021-11-10','Áo thun phản quang 7 màu ITS REAL tay lỡ',1,'ao-thun-phan-quang-7-mau-its-real-tay-lo-chat-cotton-4-chieu-mem-min-1.jpg',250000,'XL');
/*!40000 ALTER TABLE `home_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-10 23:16:57
