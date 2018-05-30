<?php

require_once 'connection.php';

$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

echo "Вы подключились!<br>";

$query = "SELECT id_application, registration.name, faculty.id_fac from registration 
	join enrollee on registration.id_enrollee = enrollee.id_enrollee 
	join exams on registration.registration_exam=exams.registration_exam 
	join faculty on registration.id_fac = faculty.id_fac";

$result = mysqli_query($link, $query);
echo "<table border = 1 align=center>";
echo "<tr><td>Имя</td>";
echo "<td>Факультет</td>";
echo "<td colspan = 2>Редактировать</td></tr>";

while($row = mysqli_fetch_array($result)) {
	echo "<tr><td>" . $row['name']. "</td>";
	echo "<td>" . $row['id_fac'] . "</td>";
	echo "<td><a href = './edit.php?id_application=" . $row['id_application'] . "&name_en=" . $row['name'] . "&faculty=" . $row['id_fac'] . "'>Update</a></td>";
	echo "<td><a href = './delete.php?id_application=". $row['id_application'] . "'>Delete</a></td></tr>";
}
echo "</table>";
mysqli_close($link);
