-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: tickets
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('f62af64e2d1f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth`
--

DROP TABLE IF EXISTS `auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth`
--

LOCK TABLES `auth` WRITE;
/*!40000 ALTER TABLE `auth` DISABLE KEYS */;
INSERT INTO `auth` VALUES (1,'mainaowen1997@gmail.com','$2b$12$T5EpN3MHGyuwfyaAgxmFH.Q8sultyzJkG2B3j3IvghvleEK9EtIH2','admin'),(2,'ngaremaina4@gmail.com','$2b$12$x4N2sFRyveYHEI3fpQoI/.Kg7XhmiUv4zcF1A0s6aG6p2zvaTfUKW','client'),(3,'mainaowen@gmail.com','$2b$12$Ojmn1vPunTSi7u.MgzJWyeJuGRVcwyVgMxUhVk36D4PpVqwgbxdAS','client'),(4,'winniejomo23@gmail.com','$2b$12$cI8tmR1gCT4EAFuU57y7seUu2potIJ9lN5ENUrjDXyj23FOdtU4Be','client');
/*!40000 ALTER TABLE `auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `venue` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `max_attendees` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (1,'Birthday Party','Birthday party for everyone to celebrate','Nairobi','2024-02-20','20:20','https://images.pexels.com/photos/796606/pexels-photo-796606.jpeg',85),(2,'Music Festival','Music Festival for everyone to dance','Nairobi','2024-09-28','21:30','https://cdn.pixabay.com/photo/2014/11/26/15/20/saxophone-546303_1280.jpg',98),(3,'Drama Festival','An epic and lively drama festival','Nairobi','2024-03-20','19:30','https://cdn.pixabay.com/photo/2013/11/03/08/05/cheers-204742_1280.jpg',89),(4,'Sulsa','Dance to your fulfilment','Kisumu','2024-03-16','17:30','https://cdn.pixabay.com/photo/2016/05/06/17/06/ballerinas-1376250_1280.jpg',85),(5,'Praise & Worship','Fulfilling Praise & Worship','Mombasa','2024-03-02','09:00','https://cdn.pixabay.com/photo/2017/08/06/09/11/people-2590551_1280.jpg',78),(7,'The Ultimate Frontend Development Experience!','Are you passionate about creating stunning user experiences on the web? ','Nairobi','2024-03-08','10:00','https://cdn.pixabay.com/photo/2015/12/04/14/05/code-1076536_1280.jpg',50),(8,'Backend Development','Are you looking to advertise a backend service, framework, or technology?','Nairobi','2024-03-02','09:00','https://cdn.pixabay.com/photo/2016/11/24/20/48/programming-1857236_1280.jpg',25),(9,'Concert','Live concert','Nairobi','2024-03-30','22:27','https://cdn.pixabay.com/photo/2014/07/09/12/17/live-concert-388160_1280.jpg',1000),(12,'Web Development HTML','Web Development','Kisumu','2024-03-30','14:47','https://cdn.pixabay.com/photo/2016/03/27/18/54/technology-1283624_1280.jpg',1000),(13,'Programming Cohort','JavaScript Programming Cohort','Mombasa','2024-03-23','15:00','https://cdn.pixabay.com/photo/2016/11/30/20/58/programming-1873854_1280.png',100);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `auth_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_id` (`auth_id`),
  CONSTRAINT `profile_ibfk_1` FOREIGN KEY (`auth_id`) REFERENCES `auth` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `venue` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `persons` int NOT NULL,
  `type_name` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `auth_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_id` (`auth_id`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`auth_id`) REFERENCES `auth` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (7,'Drama Festival','An epic and lively drama festival','Nairobi','2024-03-20','19:30','https://cdn.pixabay.com/photo/2013/11/03/08/05/cheers-204742_1280.jpg',1,'Regular',1000,2),(8,'Backend Development','Are you looking to advertise a backend service, framework, or technology?','Nairobi','2024-03-02','09:00','https://cdn.pixabay.com/photo/2016/11/24/20/48/programming-1857236_1280.jpg',1,'VIP',2000,2),(9,'Backend Development','Are you looking to advertise a backend service, framework, or technology?','Nairobi','2024-03-02','09:00','https://cdn.pixabay.com/photo/2016/11/24/20/48/programming-1857236_1280.jpg',1,'Regular',1200,2),(10,'Praise & Worship','Fulfilling Praise & Worship','Mombasa','2024-03-02','09:00','https://cdn.pixabay.com/photo/2017/08/06/09/11/people-2590551_1280.jpg',1,'VIP',2000,2),(11,'Drama Festival','An epic and lively drama festival','Nairobi','2024-03-20','19:30','https://cdn.pixabay.com/photo/2013/11/03/08/05/cheers-204742_1280.jpg',1,'VIP',1500,2),(12,'Praise & Worship','Fulfilling Praise & Worship','Mombasa','2024-03-02','09:00','https://cdn.pixabay.com/photo/2017/08/06/09/11/people-2590551_1280.jpg',1,'VIP',2000,4),(13,'Sulsa','Dance to your fulfilment','Kisumu','2024-03-16','17:30','https://cdn.pixabay.com/photo/2016/05/06/17/06/ballerinas-1376250_1280.jpg',1,'Regular',1800,4),(14,'Music Festival','Music Festival for everyone to dance','Nairobi','2024-09-28','21:30','https://cdn.pixabay.com/photo/2014/11/26/15/20/saxophone-546303_1280.jpg',1,'Regular',1200,4),(15,'Birthday Party','Birthday party for everyone to celebrate','Nairobi','2024-02-20','20:20','https://images.pexels.com/photos/796606/pexels-photo-796606.jpeg',1,'VIP',1000,4),(16,'Drama Festival','An epic and lively drama festival','Nairobi','2024-03-20','19:30','https://cdn.pixabay.com/photo/2013/11/03/08/05/cheers-204742_1280.jpg',1,'Regular',1000,4);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` int NOT NULL,
  `event_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `type_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'Regular',1200,2),(2,'VIP',1000,1),(3,'Regular',500,1),(4,'VIP',2500,2),(5,'VIP',1500,3),(6,'Regular',1000,3),(7,'VIP',2500,4),(8,'Regular',1800,4),(9,'VIP',2000,5),(10,'Regular',1500,5),(11,'VIP',1500,7),(12,'Regular',1000,7),(13,'VIP',2000,8),(14,'Regular',1200,8),(15,'VIP',2500,9),(16,'Regular',1800,9),(17,'VIP',5000,12),(18,'Regular',3000,12),(19,'VIP',1500,13),(20,'Regular',2000,13);
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-01 16:08:15
