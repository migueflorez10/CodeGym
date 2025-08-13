<?php

$db = mysqli_connect("localhost", "root", "", "appSalon");

if(!$db){
    echo "There was an error";
    exit;
}