-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2019 at 12:41 AM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bwd`
--

-- --------------------------------------------------------

--
-- Table structure for table `padi`
--

CREATE TABLE `padi` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `meanr` float DEFAULT NULL,
  `meang` float DEFAULT NULL,
  `meanb` float DEFAULT NULL,
  `stdr` float DEFAULT NULL,
  `stdg` float DEFAULT NULL,
  `stdb` float DEFAULT NULL,
  `img` varchar(45) NOT NULL,
  `category` varchar(45) DEFAULT NULL,
  `time` varchar(5) DEFAULT NULL,
  `level` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `padi`
--

INSERT INTO `padi` (`id`, `name`, `meanr`, `meang`, `meanb`, `stdr`, `stdg`, `stdb`, `img`, `category`, `time`, `level`) VALUES
(34, 'lv2-3.jpg', 5.3283, 8.1337, 1.152, 16.0335, 23.9064, 4.9073, 'D:/apadibwd/Level 2/lv2-3.jpg', 'testing', 'sore', 2),
(40, 'lv2-4.jpg', 8.2091, 12.2581, 2.4983, 21.6843, 31.9252, 7.5971, 'D:/apadibwd/Level 2/lv2-4.jpg', 'testing', 'siang', 2),
(43, 'lv4-6.jpg', 3.3965, 5.7162, 2.2748, 10.1372, 16.7986, 6.9451, 'D:/apadibwd/Level 4/lv4-6.jpg', 'testing', 'pagi', 4),
(44, 'lv2-7.jpg', 7.891, 11.894, 0.3285, 17.1245, 25.4788, 2.0932, 'D:/apadibwd/Level 2/lv2-7.jpg', 'testing', 'pagi', 2),
(45, 'lv3-2.jpg', 5.6289, 8.7977, 2.2144, 14.9638, 22.6834, 6.5202, 'D:/apadibwd/Level 3/lv3-2.jpg', 'testing', 'sore', 3),
(46, 'lv3-3.jpg', 4.0292, 5.9754, 2.499, 12.9533, 19.1047, 8.1564, 'D:/apadibwd/Level 3/lv3-3.jpg', 'testing', 'sore', 2),
(48, 'lv3-5.jpg', 3.0069, 5.5754, 1.1049, 9.0813, 15.8329, 4.2078, 'D:/apadibwd/Level 3/lv3-5.jpg', 'testing', 'sore', 3),
(49, 'lv3-6.jpg', 2.753, 5.3846, 0.8594, 8.8005, 16.3171, 3.5728, 'D:/apadibwd/Level 3/lv3-6.jpg', 'testing', 'siang', 3),
(50, 'lv3-7.jpg', 5.9004, 10.5689, 4.2952, 16.2489, 28.4086, 12.1791, 'D:/apadibwd/Level 3/lv3-7.jpg', 'testing', 'siang', 3),
(51, 'lv3-8.jpg', 3.7788, 7.3472, 2.2227, 10.3732, 19.3382, 6.7406, 'D:/apadibwd/Level 3/lv3-8.jpg', 'testing', 'pagi', 3),
(52, 'lv4-2.jpg', 3.8283, 5.5887, 3.0235, 12.7666, 18.5655, 10.1607, 'D:/apadibwd/Level 4/lv4-2.jpg', 'testing', 'pagi', 4),
(53, 'lv4-3.jpg', 3.8067, 5.7988, 2.884, 12.3791, 18.6633, 9.4148, 'D:/apadibwd/Level 4/lv4-3.jpg', 'testing', 'sore', 4),
(54, 'lv4-4.jpg', 4.3585, 7.0686, 2.5972, 12.3683, 19.7648, 7.6685, 'D:/apadibwd/Level 4/lv4-4.jpg', 'testing', 'siang', 4),
(55, 'lv4-5.jpg', 6.2557, 10.469, 3.1192, 16.3716, 26.659, 8.8735, 'D:/apadibwd/Level 4/lv4-5.jpg', 'testing', 'pagi', 4),
(56, 'lv4-6.jpg', 3.3965, 5.7162, 2.2748, 10.1372, 16.7986, 6.9451, 'D:/apadibwd/Level 4/lv4-6.jpg', 'testing', 'pagi', 4),
(57, 'lv4-7.jpg', 3.8879, 6.5048, 2.9524, 11.6849, 19.1631, 8.9757, 'D:/apadibwd/Level 4/lv4-7.jpg', 'testing', 'pagi', 4),
(58, 'lv4-8.jpg', 4.4074, 7.4344, 2.8415, 12.2625, 20.0939, 8.1818, 'D:/apadibwd/Level 4/lv4-8.jpg', 'testing', 'pagi', 4),
(69, 'lv4-2.jpg', 3.8283, 5.5887, 3.0235, 12.7666, 18.5655, 10.1607, 'D:/apadibwd/Level 4/lv4-2.jpg', 'training', 'pagi', 4),
(70, 'lv3-4.jpg', 3.7545, 5.8506, 1.7024, 11.2602, 17.4116, 5.4683, 'D:/apadibwd/Level 3/lv3-4.jpg', 'testing', 'pagi', 3),
(71, 'lv2-1.jpg', 8.0809, 13.4839, 1.4755, 19.7153, 32.2035, 4.8529, 'D:/apadibwd/Level 2/lv2-1.jpg', 'testing', 'pagi', 2),
(72, 'lv2-6.jpg', 9.1445, 14.1158, 1.0934, 20.2296, 30.8282, 4.1762, 'D:/apadibwd/Level 2/lv2-6.jpg', 'testing', 'pagi', 2),
(73, 'lv2-2.jpg', 6.6721, 10.0755, 1.2929, 19.578, 29.1526, 5.106, 'D:/apadibwd/Level 2/lv2-2.jpg', 'training', 'pagi', 2),
(74, 'lv3-2.jpg', 5.6289, 8.7977, 2.2144, 14.9638, 22.6834, 6.5202, 'D:/apadibwd/Level 3/lv3-2.jpg', 'training', 'pagi', 3),
(75, 'lv4-2.jpg', 3.8283, 5.5887, 3.0235, 12.7666, 18.5655, 10.1607, 'D:/apadibwd/Level 4/lv4-2.jpg', 'training', 'pagi', 4),
(79, 'lv2-2.jpg', 6.6721, 10.0755, 1.2929, 19.578, 29.1526, 5.106, 'D:/apadibwd/Level 2/lv2-2.jpg', 'training', 'pagi', 2),
(80, 'lv4-4.jpg', 4.3585, 7.0686, 2.5972, 12.3683, 19.7648, 7.6685, 'D:/apadibwd/Level 4/lv4-4.jpg', 'testing', 'pagi', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `padi`
--
ALTER TABLE `padi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `padi`
--
ALTER TABLE `padi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
