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
-- Table structure for table `tb_categorychild`
--

DROP TABLE IF EXISTS `tb_categorychild`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_categorychild` (
  `catec_id` int NOT NULL AUTO_INCREMENT,
  `catec_name` varchar(100) NOT NULL,
  `catep_id` int NOT NULL,
  `date_create` date NOT NULL,
  PRIMARY KEY (`catec_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_categorychild`
--

LOCK TABLES `tb_categorychild` WRITE;
/*!40000 ALTER TABLE `tb_categorychild` DISABLE KEYS */;
INSERT INTO `tb_categorychild` VALUES (1,'Áo khoác',1,'2021-10-05'),(2,'Áo sơ mi',1,'2021-10-05'),(4,'Quần jean',2,'2021-10-06'),(5,'Áo thun',1,'2021-10-14'),(6,'Áo nỉ/Áo hoodie',1,'2021-10-14'),(7,'Quần dài/Quần âu',2,'2021-10-14'),(8,'Quần short',2,'2021-10-15'),(9,'Giày thể thao/Sneakers',3,'2021-10-18'),(10,'Giày tây lười',3,'2021-10-18'),(11,'Giày lười',3,'2021-10-18'),(12,'Đồ ngủ',5,'2021-10-22'),(13,'Đồ thể thao',5,'2021-10-22'),(14,'Quần jogger',2,'2021-10-25');
/*!40000 ALTER TABLE `tb_categorychild` ENABLE KEYS */;
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
