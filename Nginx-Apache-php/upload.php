<?php
//echo "location===" .$_GET['location']."</br>";
$path = $_GET['location'];
// Desired folder structure
$basePath = "/files";
$path = $basePath.$path;
//echo $path."\n";
$uploadLocation = $path;
$filename = basename($path);
$nanotime = system('date +%s%N');
$dirname = str_replace($filename,"",$path);
$path = $dirname.$nanotime."-".rand()."-".$filename;
//$dirname = str_replace("//","/",$dirname);
//$dirname = $basePath.$dirname;
//echo $dirname."\n";
//echo "File Name : ".$path."\n";
if (file_exists($path)) {
	echo "The file $path exists";
	header($_SERVER['SERVER_PROTOCOL'] . ' 403 Forbidden', true, 403);
} else {
	if (file_exists($dirname)) {
		// if(file_put_contents($path,file_get_contents('php://input'))){
			// 
			// 
// 
			// echo "File successfully Stored to photovault";
		// }
		//New way of writing chucked way
		//echo "Creating only file Directory already exists \n";
		$putdata = fopen("php://input", "r");

		/* Open a file for writing */
		$fp = fopen($path, "w");
		
		/* Read the data 1 KB at a time
		   and write to the file */
		while ($data = fread($putdata, 1024))
		  fwrite($fp, $data);
		
		/* Close the streams */
		fclose($fp);
		fclose($putdata);
		echo "File successfully Stored to photovault";
		//New way of writing chucked way
	} else {
		
		if (mkdir($dirname, 0755, true)) {
			// if(file_put_contents($path,file_get_contents('php://input'))){
			// 
				// echo "File successfully Stored to photovault";
			// }
			
			//New way of writing chucked way
			$putdata = fopen("php://input", "r");
			//echo "Creating Directory";

			/* Open a file for writing */
			$fp = fopen($path, "w");
			
			/* Read the data 1 KB at a time
			   and write to the file */
			while ($data = fread($putdata, 1024))
			  fwrite($fp, $data);
			
			/* Close the streams */
			fclose($fp);
			fclose($putdata);
			echo "File successfully Stored to photovault";
			//New way of writing chucked way
			
		}
		else{
			echo "Making Directory Failed!!!";
		}
	}


}
?>
