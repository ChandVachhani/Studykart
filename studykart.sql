-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 14, 2020 at 07:22 PM
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
-- Database: `studykart`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--


-- --------------------------------------------------------



-- --------------------------------------------------------


INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'hello', NULL, 0, 'dss06', '', '', 'devanshsuthar0612@gmail.com', 0, 1, '2020-04-08 13:57:24.326770'),
(3, 'pbkdf2_sha256$180000$VPj9Fm9K9ikm$HYTYasVxfqb/O6uf8b6Xq8ac84reG4hoROrZYugIHaM=', '2020-04-14 11:52:00.647894', 1, 'dss-0620', 'Devansh', 'Suthar', '18n046@nirmauni.ac.in', 1, 1, '2020-04-09 13:38:01.140558'),
(4, 'pbkdf2_sha256$180000$AeBEe48VL715$bsKhWISuqkBJOQZ4WH5nnENdHKbs47saP50hg+mLick=', NULL, 0, 'helloworld', '', '', '', 0, 1, '2020-04-09 13:40:29.279675'),
(5, 'pbkdf2_sha256$180000$Ol8xuD30AqqS$mMYwGvwyVf/LWfo2vffZjyp5vbcZS2JGJjY2xKLsqcY=', '2020-04-10 14:17:28.489573', 0, 'hello12', 'Devansh', 'Suthar', 'hellowordl12@gmail.com', 0, 1, '2020-04-10 14:17:15.526932'),
(6, 'pbkdf2_sha256$180000$pqrTTcbL4B0h$4OLZHlftmgVmkz2Jfy6JH/4sLWow9YdHZ7glN6ncB2s=', NULL, 0, 'seller12', 'Devansh', 'Suthar', 'seller@gmail.com', 0, 1, '2020-04-10 14:34:08.573927'),
(8, 'pbkdf2_sha256$180000$9kAqg1wicUwz$KlzcVPXFHrYN6tuJmP5dL53SkbJcBc6otjArGsYWNZ0=', '2020-04-10 14:36:59.429074', 0, 'hello12345', 'Devansh', 'Suthar', 'hello9878921@gmail.com', 0, 1, '2020-04-10 14:36:07.564022'),
(9, 'pbkdf2_sha256$180000$3PzMIjU76I6X$lB6hDcSKHco+K6mQ7WDsPkPuBMSfmmnqc/LohDumKCY=', NULL, 0, 'ksjdhkjashd', 'Hello', 'world', 'hasjkdhsakj@kjhsdkjas.com', 0, 1, '2020-04-11 15:33:56.060949'),
(10, 'pbkdf2_sha256$180000$UxKMFe2XmWtu$6jrgN1WS03JcU9NUd2FY0HFFKYQAQKcxvKtJ0EYQrgM=', NULL, 0, '7378387891', 'Devansh', 'Suthar', 'devanshsuthar@gmail.com', 0, 1, '2020-04-11 22:52:27.706965'),
(11, 'pbkdf2_sha256$180000$ZmlQ6sgKRdZU$09++aZc9oXzqzPeYictq0prnd3ORWvkSXht7ZQ4AFBA=', NULL, 0, '8980462565', 'Devansh', 'Suthar', '18bce238@nirmauni.ac.in', 0, 1, '2020-04-11 22:56:38.129100'),
(14, 'pbkdf2_sha256$180000$8uR1irDHMCft$jf+gs/LwIiLTv3R3LC3LrSv6hxU+B1jvSuSUOeS+8TY=', '2020-04-14 15:17:41.148482', 1, 'dss0620', 'Devansh', 'Suthar', 'projecttest@gmail.com', 1, 1, '2020-04-11 23:02:04.991964'),
(15, 'pbkdf2_sha256$180000$cGGyZ39g3zy1$m2xjlR78mqg3B+7Q6fhkPZ8DtjgHZwEqe0iPTE2gEfE=', NULL, 0, 'jghjgjgjgj', 'fhfhgfh', 'gghgghj', 'fhgfhgfhgf@hgfhgfghf.com', 0, 1, '2020-04-12 17:56:01.405031'),
(16, 'pbkdf2_sha256$180000$M2UmJahOnB7N$daEuDJxmHV8YBv//kmCUwykPUHLqfJeqA9jhMi9pf4g=', '2020-04-14 15:17:58.459331', 0, 'dss0612', 'Devansh', 'Suthar', '18n040@nirmauni.ac.in', 0, 1, '2020-04-14 09:56:32.758684'),
(17, 'pbkdf2_sha256$180000$OP2jAt1V0ake$4xbd5CvnZ9WeEs0rXdx4akGt63SIFpfF/W/DFDMufv4=', '2020-04-14 15:27:04.857233', 0, 'dss061200', 'Devansh', 'Suthar', 'devansh.developer06@gmail.com', 0, 1, '2020-04-14 13:16:14.344064');

-- --------------------------------------------------------

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Books'),
(2, 'Lab Coats'),
(3, 'Mechanical Instruments');


-- --------------------------------------------------------

-- --------------------------------------------------------


INSERT INTO `products` (`id`, `product_name`, `product_description`, `product_price`, `products_image`, `is_booked`, `product_category_id`, `product_seller_id`, `user_booked_id`) VALUES
(3, 'Introduction To Algorithms', 'This is a very good book for algorithms often known as C.L.R.S.', 500, '__892374product_8129083_imgs!@__/clrs_WTmpXD1.jpg', 0, 1, 14, NULL),
(4, 'Let Us C', 'Very good book for learning programming concepts.', 140, '__892374product_8129083_imgs!@__/letusc_tANMFR3.jpg', 0, 1, 14, 17),
(9, 'Lab Coat', 'This is a good quality lab coat buy at cheap price.', 60, '__892374product_8129083_imgs!@__/lab_coat_bmzHC6v.jpg', 0, 2, 14, 17),
(10, 'E.G. Drafter', 'This is a good quality drafter it is very useful for E.G. drawings. Buy it at a very low cost.', 100, '__892374product_8129083_imgs!@__/download_sWuZVVK.jfif', 0, 3, 14, NULL),
(11, 'H.C. Verma', 'This is a H.C. Verma.', 150, '__892374product_8129083_imgs!@__/download_SaNl2uZ.jfif', 0, 1, 14, NULL),
(12, 'Linear Algebra', 'This book is good for linear algebra. This book is written by DR. K.R. Kachot. Buy it at a very low price.', 120, '__892374product_8129083_imgs!@__/download_kfmZRpl.jfif', 0, 1, 3, NULL),
(13, 'B.S. Grewal', 'This is good book for C.D.E.', 300, '__892374product_8129083_imgs!@__/download_lKq0dDv.jfif', 0, 1, 14, NULL),
(14, 'B.S. Grewal', 'This is good book for C.D.E.', 600, '__892374product_8129083_imgs!@__/download_1.jfif', 0, 1, 14, NULL),
(15, 'Attitude is Everything', 'This is a very good book to read.', 100, '__892374product_8129083_imgs!@__/att_is_everything.jfif', 0, 1, 14, NULL);

-- --------------------------------------------------------


INSERT INTO `roles` (`id`, `role_name`) VALUES
(1, 'buyer'),
(2, 'seller');

-- --------------------------------------------------------


INSERT INTO `sold_products` (`id`, `product_name`, `product_description`, `product_price`, `products_image`, `product_buyer_id`, `product_category_id`, `product_seller_id`) VALUES
(1, 'B.S. Grewal', 'This is good book for C.D.E. must refer it for excelling in your exams.', 300, '__892374product_8129083_imgs!@__/higher-engineering-mathematics-by-bs-grewal_s1Gg5AD.jpg', 3, 1, 14),
(2, 'Attitude is Everything', 'Do you dread going to work? Do you feel tired, unhappy, weighted down? Have you given up on your dreams? The road to a happier, more successful life starts with your attitude-and your attitude is within you control.', 100, '__892374product_8129083_imgs!@__/att_C7jM1Ux.jpg', 3, 1, 14),
(3, 'B.S. Grewal', 'This is a good book for C.D.E. buy it at a very low price', 500, '__892374product_8129083_imgs!@__/bs_s8VsJGq.jpg', 3, 1, 14),
(4, 'Operating System by Tanenbaum', 'This is a good book to refer for Operating System', 350, '__892374product_8129083_imgs!@__/download.jfif', 17, 1, 14);

-- --------------------------------------------------------


INSERT INTO `user_profile` (`id`, `user_mobile`, `user_id`, `created`) VALUES
(5, '7878787878', 14, '2020-04-11 23:02:05.548380'),
(6, '8678678687', 15, '2020-04-12 17:56:02.019788'),
(7, '6386217871', 3, '2020-04-07 00:00:00.000000'),
(8, '8927398191', 16, '2020-04-14 09:56:33.600630'),
(9, '7878787878', 17, '2020-04-14 13:16:15.263275');

-- --------------------------------------------------------



INSERT INTO `user_roles` (`id`, `role_id`, `user_id`) VALUES
(3, 2, 8),
(4, 2, 9),
(5, 2, 10),
(6, 2, 11),
(7, 2, 14),
(8, 1, 15),
(9, 2, 3),
(10, 1, 16),
(11, 1, 17);

-- --------------------------------------------------------

INSERT INTO `wishlist` (`id`, `buyer_id`, `products_id`) VALUES
(2, 14, 9),
(3, 17, 3);


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
