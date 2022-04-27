-- MySQL dump 10.13  Distrib 5.7.33, for Win64 (x86_64)
--
-- Host: localhost    Database: cursos
-- ------------------------------------------------------
-- Server version	5.7.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pais` varchar(100) DEFAULT 'Perú',
  `nota` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES (1,'Orazio','Readitt','oreaditt0@hp.com','Brazil',15),(2,'Joshia','Caverhill','jcaverhill1@acquirethisname.com','Brazil',12),(3,'Garnet','Tacey','gtacey2@elegantthemes.com','Brazil',20),(4,'Blaire','Jessup','bjessup3@nba.com','Colombia',11),(5,'Don','Denzilow','ddenzilow4@geocities.jp','Brazil',18),(6,'Honoria','Duffrie','hduffrie5@tripod.com','Brazil',11),(7,'Fionnula','Grubey','fgrubey6@t-online.de','Colombia',14),(8,'Jandy','Maus','jmaus7@usa.gov','Brazil',18),(9,'Clotilda','O\'Neal','coneal8@pcworld.com','Argentina',15),(10,'Randy','Sexten','rsexten9@nps.gov','Venezuela',20),(11,'Cynde','Paolinelli','cpaolinellia@amazon.de','Argentina',16),(12,'Malchy','Stringman','mstringmanb@zimbio.com','Brazil',17),(13,'Phylys','Mirralls','pmirrallsc@gnu.org','Brazil',19),(14,'Mariana','Surgenor','msurgenord@virginia.edu','Brazil',11),(15,'Addison','Guesford','aguesforde@merriam-webster.com','Argentina',12),(16,'Vittorio','Le Friec','vlefriecf@youku.com','Ecuador',11),(17,'Viola','Skyrme','vskyrmeg@state.tx.us','Brazil',14),(18,'Tabbitha','Sherland','tsherlandh@home.pl','Brazil',11),(19,'Marybelle','Aleksankov','maleksankovi@mtv.com','Peru',13),(20,'Minetta','Waren','mwarenj@meetup.com','Peru',16),(21,'Guy','Orcott','gorcottk@plala.or.jp','Brazil',19),(22,'Ardra','Kivlehan','akivlehanl@google.com.hk','Argentina',10),(23,'Emery','Haggath','ehaggathm@apple.com','Brazil',14),(24,'Clio','Penkman','cpenkmann@irs.gov','Colombia',12),(25,'Vivianna','Hawke','vhawkeo@artisteer.com','Peru',11),(26,'Nicol','Gather','ngatherp@google.ru','Colombia',12),(27,'Alasdair','Runsey','arunseyq@baidu.com','Brazil',18),(28,'Elicia','Andreazzi','eandreazzir@desdev.cn','Brazil',18),(29,'Jaymie','Fellona','jfellonas@ucsd.edu','Brazil',18),(30,'Kent','Anthonsen','kanthonsent@bbc.co.uk','Brazil',19),(31,'Jillana','Kleinstein','jkleinsteinu@furl.net','Colombia',13),(32,'Ruby','Tyrone','rtyronev@sciencedirect.com','Argentina',11),(33,'Toddy','MacGillicuddy','tmacgillicuddyw@netvibes.com','Brazil',14),(34,'Robena','Hearsum','rhearsumx@wordpress.com','Brazil',14),(35,'Helen','Burde','hburdey@photobucket.com','Peru',10),(36,'Lawry','Waterson','lwatersonz@jiathis.com','Venezuela',14),(37,'Devon','Andrzej','dandrzej10@kickstarter.com','Brazil',13),(38,'Petey','Carnew','pcarnew11@blogspot.com','Peru',12),(39,'Giovanna','Frogley','gfrogley12@technorati.com','Brazil',14),(40,'Douglass','Heindl','dheindl13@fotki.com','Peru',11),(41,'Doretta','Goodbody','dgoodbody14@google.com.br','Colombia',15),(42,'Fowler','Flamank','fflamank15@4shared.com','Peru',12),(43,'Claudine','Currier','ccurrier16@ucoz.ru','Argentina',13),(44,'Thomasa','Pardy','tpardy17@xing.com','Argentina',15),(45,'Karon','Foxhall','kfoxhall18@opera.com','Colombia',13),(46,'Beniamino','Peegrem','bpeegrem19@whitehouse.gov','Chile',10),(47,'Babette','Acres','bacres1a@ebay.com','Brazil',19),(48,'Erek','Tod','etod1b@goo.gl','Brazil',10),(49,'Adelina','Iwanczyk','aiwanczyk1c@google.com.au','Brazil',14),(50,'Manon','Durber','mdurber1d@github.com','Chile',10),(51,'Sly','Marcinkus','smarcinkus1e@ucla.edu','Peru',20),(52,'Loralyn','Baudinelli','lbaudinelli1f@storify.com','Brazil',17),(53,'Gusta','Gehricke','ggehricke1g@census.gov','Peru',13),(54,'Gawen','Lettley','glettley1h@who.int','Ecuador',15),(55,'Pauline','Britner','pbritner1i@army.mil','Colombia',20),(56,'Lief','Grewes','lgrewes1j@jiathis.com','Colombia',12),(57,'Timoteo','Baggaley','tbaggaley1k@blogspot.com','Brazil',20),(58,'Sally','Shakesby','sshakesby1l@hud.gov','Brazil',13),(59,'Shirl','Senecaux','ssenecaux1m@mit.edu','Colombia',19),(60,'Merridie','Georgius','mgeorgius1n@economist.com','Peru',12),(61,'Lilia','Rosbotham','lrosbotham1o@pinterest.com','Brazil',19),(62,'Hannie','Scinelli','hscinelli1p@com.com','Brazil',13),(63,'Garrek','Hirsthouse','ghirsthouse1q@marriott.com','Brazil',17),(64,'Athena','Ruddy','aruddy1r@un.org','Peru',14),(65,'Brook','Stangroom','bstangroom1s@census.gov','Chile',18),(66,'Cathee','Rosekilly','crosekilly1t@woothemes.com','Brazil',13),(67,'Oralia','Kneaphsey','okneaphsey1u@cornell.edu','Argentina',12),(68,'Jennine','Smithson','jsmithson1v@sogou.com','Peru',17),(69,'Filip','Clears','fclears1w@blogger.com','Brazil',11),(70,'Manolo','McGrouther','mmcgrouther1x@yandex.ru','Brazil',15),(71,'Gunter','Etuck','getuck1y@woothemes.com','Chile',13),(72,'Alvira','Morffew','amorffew1z@oracle.com','Brazil',14),(73,'Lisa','Pretsel','lpretsel20@w3.org','Brazil',17),(74,'Ly','Justice','ljustice21@symantec.com','Brazil',19),(75,'Milena','Lingner','mlingner22@omniture.com','Argentina',17),(76,'Elli','Grievson','egrievson23@admin.ch','Brazil',17),(77,'Bartholomeus','Schimmang','bschimmang24@goodreads.com','Peru',12),(78,'Dian','Meigh','dmeigh25@senate.gov','Brazil',14),(79,'Kriste','Burnand','kburnand26@list-manage.com','Brazil',14),(80,'Siegfried','Pulver','spulver27@patch.com','Brazil',20),(81,'Gerhard','Buckley','gbuckley28@icio.us','Brazil',13),(82,'Petr','Pre','ppre29@google.ca','Bolivia',16),(83,'King','Cubley','kcubley2a@google.cn','Chile',11),(84,'Haskell','Thonger','hthonger2b@statcounter.com','Bolivia',11),(85,'Beaufort','Brucker','bbrucker2c@deviantart.com','Colombia',11),(86,'Allistir','Dobbings','adobbings2d@posterous.com','Brazil',14),(87,'Edouard','Skillman','eskillman2e@mac.com','Brazil',17),(88,'Cordelie','Whellans','cwhellans2f@bluehost.com','Colombia',14),(89,'Ingra','Jobern','ijobern2g@myspace.com','Bolivia',18),(90,'Helaine','Eaddy','headdy2h@youtu.be','Brazil',17),(91,'Guillema','Dabbes','gdabbes2i@un.org','Colombia',10),(92,'Lela','Sarvar','lsarvar2j@deviantart.com','Brazil',15),(93,'Gigi','Haydock','ghaydock2k@shutterfly.com','Colombia',12),(94,'Padraig','Dicks','pdicks2l@cam.ac.uk','Argentina',20),(95,'Carleton','Frigout','cfrigout2m@cdc.gov','Brazil',17),(96,'Alec','Roggieri','aroggieri2n@rediff.com','Colombia',12),(97,'Bond','Elden','belden2o@discovery.com','Brazil',17),(98,'Giff','Chalk','gchalk2p@umich.edu','Brazil',12),(99,'Sara-ann','Gayter','sgayter2q@google.com.br','Colombia',15),(100,'Felizio','Chene','fchene2r@biglobe.ne.jp','Brazil',16);
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:49:40
