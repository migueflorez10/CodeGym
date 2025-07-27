<?php include 'includes/header.php';

$customers = [];
$customer2 = array();
$customer3 = array('Miguel', 'Angel', 'Martinez');
$customer = [
    'name' => 'Miguel',
    'balance' => 200
];

// Empty - check if an array is empty
var_dump(empty($customers));
var_dump(empty($customer2));
var_dump(empty($customer3));

// Isset - Check if an array is created or a property is defined
echo "<br/>";
var_dump(isset($customers));
var_dump(isset($customer2));
var_dump(isset($customer3));
var_dump(isset($customer));

// Isset - allows you to check whether a property of an associative array exists!
echo "<br/>";
var_dump(isset($customer['code']));
var_dump(isset($customer['name']));


include 'includes/footer.php';