<html>
<body>
	<form action = 'search.php' method = 'get'>
	<p><strong>Введите значения:</strong>
	<p>Имя абитуриента: <input name = 'abit' type = 'text' value='<?=@$_GET['abit']?>'>
	<p>Номер факультета: <input name = 'faculty' type = 'text' value='<?=@$_GET['faculty']?>'>
	<p><input type = 'submit' name = 'button'>
	</form>
</body>
</html>

<?php
include 'connection.php';

$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

echo "Вы подключились!<br>";


if(isset($_GET['button']))
{
	$abit = strtr(trim($_GET['abit']), '*', '%');
	$faculty = strtr(trim($_GET['faculty']), '*', '%');

	$query = "SELECT registration.name, faculty.id_fac from registration join enrollee on registration.id_enrollee = enrollee.id_enrollee join exams on registration.registration_exam=exams.registration_exam join faculty on registration.id_fac = faculty.id_fac
		WHERE registration.name LIKE '%" . $abit . "%' ";
	
	if (!empty($faculty)) {
			$query .= "AND faculty.id_fac LIKE '%" . $faculty . "%'";
	}
	
	$result = mysqli_query($link, $query);
	echo "<table border = 3 align = center> <tr> <td> Имя </td> <td> Факультет </td> </tr>";
	
	while($row = mysqli_fetch_array($result)) {
			echo "<tr> <td>" . $row['name'] . "</td> <td>" . $row['id_fac'] . "</td> </tr>";
	}
	echo "</table>";
	mysqli_close($link);
}
