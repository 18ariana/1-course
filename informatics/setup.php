<?php
require_once 'connection.php'; // подключаем скрипт
 
$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

echo "Вы подключились!<br>";
 

$query ="CREATE TABLE IF NOT EXISTS enrollee (
  name varchar(250) NOT NULL,
  passport int(11) NOT NULL,
  id_enrollee int(10) NOT NULL AUTO_INCREMENT,
  school varchar(250) NOT NULL,
  medal varchar(250) DEFAULT NULL,
  speciality varchar(250) NOT NULL,
  form varchar(250) NOT NULL,
  points varchar(250) NOT NULL,
  PRIMARY KEY (id_enrollee))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}
 
$sql = "INSERT INTO enrollee (name, passport, school, medal, speciality, form, points) VALUES ('Kateva_Katya', '83752637', '276', 'yes', 'cook', 'budget','300')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

 $query ="CREATE TABLE IF NOT EXISTS college(
  id_college int(10) NOT NULL,
  id_pulpit int(10) NOT NULL,
  id_faculty int(10) NOT NULL,
  name_speciality varchar(250) NOT NULL,
  amount int(10) NOT NULL,
  id_worker int(10) NOT NULL,
  PRIMARY KEY (id_college))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO college VALUES ('11', '0909', '123', 'cook', '80', '0101')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}


$query ="CREATE TABLE IF NOT EXISTS pulpit (
  id_pulpit int(10) NOT NULL,
  name_pulpit varchar(250) NOT NULL,
  id_fac int(10) NOT NULL,
  name_speciality varchar(250) NOT NULL,
  PRIMARY KEY (id_pulpit))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO pulpit VALUES ('0909', 'cooking', '123', 'cook')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}


$query ="CREATE TABLE IF NOT EXISTS exams (
  registration_exam int(50) NOT NULL,
  points1_sub int(10) NOT NULL,
  sum_points int(10) NOT NULL,
  points2_sub int(10) NOT NULL,
  PRIMARY KEY (registration_exam))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO exams VALUES ('967', '100', '300', '100')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS faculty (
  id_fac int(10) NOT NULL,
  id_pulpit int(10) NOT NULL,
  name_faculty varchar(250) NOT NULL,
  name_speciality varchar(250) NOT NULL,
  amount int(10) NOT NULL,
  PRIMARY KEY (id_fac))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO faculty VALUES ('123', '0909', 'cooks', 'cook', '90')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS points (
  id_points int(30) NOT NULL,
  leading_points int(10) NOT NULL,
  average int(10) NOT NULL,
  PRIMARY KEY (id_points))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO points VALUES ('98888333', '305', '243')";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS `registration` (
  id_application int(10) NOT NULL AUTO_INCREMENT,
  id_worker int(10) NOT NULL,
  name varchar(250) NOT NULL,
  passport int(11) NOT NULL,
  id_enrollee int(10) NOT NULL,
  form varchar(250) NOT NULL,
  school varchar(250) NOT NULL,
  name_speciality varchar(250) NOT NULL,
  points int(10) NOT NULL,
  amount int(10) NOT NULL,
  id_fac int(10) NOT NULL,
  id_college int(10) NOT NULL,
  id_points int(10) NOT NULL,
  registration_exam int(50) NOT NULL,
  PRIMARY KEY (id_application))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}
$sql = "INSERT INTO registration VALUES ('01', '0101', 'Kateva_Katya', '83752637', '1', 'budget', '276', 'cook', '300', '80', '123', '11', '98888333' , '967' )";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}

$query ="CREATE TABLE IF NOT EXISTS `workers` (
  id_worker int(10) NOT NULL AUTO_INCREMENT,
  fio varchar(100) NOT NULL,
  id_college int(10) NOT NULL,
  PRIMARY KEY (id_worker))";
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
if($result)
{
    echo "Выполнение запроса прошло успешно";
}

$sql = "INSERT INTO workers VALUES ('0101', 'Marie', '11' )";
if (mysqli_query($link, $sql)) {
  echo "Created successfully<br>";
} else {
  echo "Error creating <br>" . mysqli_error($link);
}



mysqli_close($link);
