<?php

$cmd = "sudo service motion restart && sudo motion";
exec( $cmd, $output);

$data=array("shcmd"=>$cmd, "err"=>$output); 
echo json_encode($data); 
?>
