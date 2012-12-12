<?php
//echo "location===" .$_GET['location']."</br>";
$path = $_GET['location'];
// Desired folder structure


$uploadLocation = $path;
$filename = basename($path);
$dirname = str_replace($filename,"",$path);
//$dirname = str_replace("//","/",$dirname);
//echo $dirname."\n";
if (file_exists($path)) {
	echo "The file $path exists";
	header($_SERVER['SERVER_PROTOCOL'] . ' 403 Forbidden', true, 403);
} else {
	if (file_exists($dirname)) {
		if(file_put_contents($path,file_get_contents('php://input'))){

			echo "File successfully Stored to photovault";
		}
	} else {
		
		if (mkdir($dirname, 0755, true)) {
			if(file_put_contents($path,file_get_contents('php://input'))){
			
				echo "File successfully Stored to photovault";
			}
		}
		else{
			echo "Making Directory Failed!!!";
		}
	}


}
?>
