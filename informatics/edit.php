<?php

include "connection.php";

$link = mysqli_connect($host, $user, $password, $database) 
    or die ("Ошибка подключения к базе данных" . mysqli_error());

$id = $_GET['id_application'];
$name_en = $_GET['name'];
$id_fac = $_GET['faculty'];

$query = "SELECT registration.name, faculty.id_fac from registration 
	join enrollee on registration.id_enrollee = enrollee.id_enrollee 
	join exams on registration.registration_exam=exams.registration_exam
	join faculty on registration.id_fac = faculty.id_fac
	WHERE registration.name = $name_en and id_fac = $id_fac";
	
$result = mysqli_query($link, $query);
 
if(isset($_GET['button']))
{
	$id = $_GET['id_application'];
	$name_en = $_GET['name'];
	$id_fac = $_GET['faculty'];
	
	$query = "UPDATE registration
		SET name ='" . $name_en . "'
		WHERE id_application =' " . $id . " '; ";
			
	$result = mysqli_query($link, $query);
			
	$query = "UPDATE faculty
		SET id_fac ='" . $id_fac . "';";
			
	$result = mysqli_query($link, $query);

	header('location: ./list.php'); 
}
?>

<html>
<body>
	<form action = 'edit.php' method = 'get'>
	<i>Редактировать значения:</i>
	<p hidden>ID абитуриента: <input name = 'id_application' type = 'text' value='<?php echo $id; ?>'></p>
	<p>Имя абитуриента: <input name = 'name_en' type = 'text' value='<?=@$_GET['name_en']?>'></p>
	<p>Название кафедры: <input name = 'faculty' type = 'text' value='<?=@$_GET['id_fac']?>'></p>
	<br/>
	<input type = 'submit' name = 'button'>
	</form>
</body>
</html>
