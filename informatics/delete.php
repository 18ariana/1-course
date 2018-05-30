<?php

include "connection.php";

$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

$id_application = $_GET['id_application'];

$query = "DELETE FROM registration
	WHERE id_application ='" . $id_application . "'";

$result = mysqli_query($link, $query);

header('location: ./list.php');
