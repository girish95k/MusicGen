<?php
	if (isset($_POST['data'])) {
		$data = $_POST['data'];
		$filedata = fopen('parameters.txt', "w+");
		fwrite($filedata, $data);
		fclose($filedata);
		$res = shell_exec("python caller.py 2>&1");
		echo $res;
	}
	else {
		echo "Gone case";
	}
?>