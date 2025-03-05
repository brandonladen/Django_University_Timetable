-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: masenodjangotimetable
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `timetabling_department`
--

DROP TABLE IF EXISTS `timetabling_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timetabling_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `school_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `timetabling_departme_school_id_8134c400_fk_timetabli` (`school_id`),
  CONSTRAINT `timetabling_departme_school_id_8134c400_fk_timetabli` FOREIGN KEY (`school_id`) REFERENCES `timetabling_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetabling_department`
--

LOCK TABLES `timetabling_department` WRITE;
/*!40000 ALTER TABLE `timetabling_department` DISABLE KEYS */;
INSERT INTO `timetabling_department` VALUES (48,'Department of Education Management & Foundation',1),(49,'Department of Educational Communication, Technology & Curriculum Studies',1),(50,'Department of Special Needs Education & Rehabilitation',1),(51,'Department of Education Psychology',1),(52,'Department of Nursing',2),(53,'Department of Pure & Applied Mathematics',3),(54,'Department of Statistics & Actuarial Science',3),(55,'Department of Computer Science',4),(56,'Department of Information Technology',4),(57,'Department of Economics',5),(58,'Department of Management Science',5),(59,'Department of Business Administration',5),(60,'Department of Accounting & Finance',5),(61,'Department of Applied Plant Sciences',6),(62,'Department of Soil Science',6),(63,'Department of Animal Science',6),(64,'Department of Fisheries and Natural Resources',6),(65,'Department of Communication & Media Technology',7),(66,'Department of History & Archaeology',7),(67,'Department of Music & Theatre Studies',7),(68,'Department of Linguistics',7),(69,'Department of Kiswahili & Other African Languages',7),(70,'Department of French & Other Foreign Languages',7),(71,'Department of Religion, Theology & Philosophy',7),(72,'Department of Sociology & Anthropology',7),(73,'Department of Art & Design',7),(74,'Department of Psychology',7),(75,'Department of Literary Studies',7),(76,'Department of Development Studies',8),(77,'Department of Strategic Studies',8),(78,'Department of Planning',9),(79,'Department of Architecture',9),(80,'Department of Pharmacy',10),(81,'Department of Human Anatomy',11),(82,'Department of Medical Physiology',11),(83,'Department of Medical Microbiology',11),(84,'Department of Human Pathology',11),(85,'Department of Pharmacology',11),(86,'Department of Paediatrics & Child Health',11),(87,'Department of Obstetrics and Gynaecology',11),(88,'Department of Public Health',12),(89,'Department of Nutrition and Health',12),(90,'Department of Biomedical Sciences and Technology',12),(91,'Department of Physics & Materials Science',13),(92,'Department of Zoology',13),(93,'Department of Botany',13),(94,'Department of Law',14);
/*!40000 ALTER TABLE `timetabling_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetabling_school`
--

DROP TABLE IF EXISTS `timetabling_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timetabling_school` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetabling_school`
--

LOCK TABLES `timetabling_school` WRITE;
/*!40000 ALTER TABLE `timetabling_school` DISABLE KEYS */;
INSERT INTO `timetabling_school` VALUES (1,'School of Education'),(2,'School of Nursing'),(3,'School of Mathematics, Statistics and Actuarial Science'),(4,'School of Computing and Informatics'),(5,'School of Business and Economics'),(6,'School of Agriculture, Food Security and Environmental Sciences'),(7,'School of Arts and Social Sciences'),(8,'School of Development and Strategic Studies'),(9,'School of Planning and Architecture'),(10,'School of Pharmacy'),(11,'School of Medicine'),(12,'School of Public Health and Community Development'),(13,'School of Physical and Biological Science'),(14,'School of Law');
/*!40000 ALTER TABLE `timetabling_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'masenodjangotimetable'
--

--
-- Dumping routines for database 'masenodjangotimetable'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-05 23:47:36
