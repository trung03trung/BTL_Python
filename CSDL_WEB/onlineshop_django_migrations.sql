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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-10-05 09:42:25.592618'),(2,'auth','0001_initial','2021-10-05 09:42:26.422144'),(3,'admin','0001_initial','2021-10-05 09:42:26.656842'),(4,'admin','0002_logentry_remove_auto_add','2021-10-05 09:42:26.673800'),(5,'admin','0003_logentry_add_action_flag_choices','2021-10-05 09:42:26.692875'),(6,'contenttypes','0002_remove_content_type_name','2021-10-05 09:42:26.847525'),(7,'auth','0002_alter_permission_name_max_length','2021-10-05 09:42:26.954249'),(8,'auth','0003_alter_user_email_max_length','2021-10-05 09:42:27.011275'),(9,'auth','0004_alter_user_username_opts','2021-10-05 09:42:27.028881'),(10,'auth','0005_alter_user_last_login_null','2021-10-05 09:42:27.177826'),(11,'auth','0006_require_contenttypes_0002','2021-10-05 09:42:27.184807'),(12,'auth','0007_alter_validators_add_error_messages','2021-10-05 09:42:27.213732'),(13,'auth','0008_alter_user_username_max_length','2021-10-05 09:42:27.392253'),(14,'auth','0009_alter_user_last_name_max_length','2021-10-05 09:42:27.543941'),(15,'auth','0010_alter_group_name_max_length','2021-10-05 09:42:27.610766'),(16,'auth','0011_update_proxy_permissions','2021-10-05 09:42:27.642678'),(17,'auth','0012_alter_user_first_name_max_length','2021-10-05 09:42:27.793689'),(18,'sessions','0001_initial','2021-10-05 09:42:27.886056'),(19,'home','0001_initial','2021-10-05 12:52:39.795733'),(20,'home','0002_auto_20211008_1919','2021-10-08 12:20:44.817128'),(21,'home','0003_auto_20211008_1932','2021-10-08 12:32:36.840828'),(22,'home','0004_userpassword','2021-10-14 05:37:09.385918'),(23,'home','0005_product_product_amount','2021-10-14 07:17:58.128853'),(24,'home','0006_auto_20211014_1442','2021-10-14 07:42:45.910879'),(25,'home','0007_auto_20211014_2238','2021-10-14 15:38:47.021132'),(26,'home','0008_product_pro_price','2021-10-14 15:39:09.211878'),(27,'home','0007_auto_20211015_0930','2021-10-15 02:30:56.033417'),(28,'home','0008_auto_20211015_0933','2021-10-15 02:33:56.956620'),(29,'home','0009_auto_20211018_2033','2021-10-18 13:33:43.951769'),(30,'home','0010_alter_order_product','2021-10-18 14:11:47.461777'),(31,'home','0011_auto_20211020_2126','2021-10-20 14:26:46.072572'),(32,'home','0012_auto_20211022_0957','2021-10-22 02:57:18.785452'),(33,'home','0013_auto_20211028_1548','2021-10-28 08:52:22.806538'),(34,'home','0014_remove_product_promotion','2021-10-28 08:55:52.405874'),(35,'home','0015_product_promotion','2021-10-28 08:57:30.115726'),(36,'home','0016_auto_20211029_1711','2021-10-29 10:11:19.908597'),(37,'home','0017_auto_20211030_1556','2021-10-30 08:56:16.203882'),(38,'home','0018_auto_20211030_1613','2021-10-30 09:14:02.369896'),(39,'home','0019_auto_20211110_1652','2021-11-10 09:52:19.811729');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-10 23:16:58
