<?php

require_once 'connection.php';

$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

echo "Вы подключились!<br>";

$query = "SELECT id_application, registration.name, faculty.id_fac from registration join enrollee on registration.id_enrollee = enrollee.id_enrollee join exams on registration.registration_exam=exams.registration_exam join faculty on registration.id_fac = faculty.id_fac";

$result = mysqli_query($link, $query);

if($result) {
	echo "Всё получилось!";
}
else {
	echo " Не всё получилось:(" . mysqli_error($link);
}



echo "<table border = 3 align = center> <tr> <td> Name </td> <td> Факультет </td></tr>";

while($row = mysqli_fetch_array($result)) {
	echo "<tr><td>" . $row['name']. "</td><td>" . $row['id_fac'] . "</td></tr>";
}

echo "</table>";

mysqli_close($link);
