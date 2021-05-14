<?php
$cmd = "python /var/www/html/python/runCamera.py -c ";
$cmd .= $_POST['cmd'];
$cmd .= " -o /var/www/html/www-data/photo.png";
$cmd .= " --nphotos ";
$cmd .= $_POST['nphotos'];
$cmd .= " --delay ";
$cmd .= $_POST['delay'];
exec( $cmd, $output);
$data=array("file"=>"www-data/photo.png", "shcmd"=>$cmd, "err"=>$output); 
echo json_encode($data); 
?>
