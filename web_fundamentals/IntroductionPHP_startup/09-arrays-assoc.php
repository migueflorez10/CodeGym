<?php include 'includes/header.php';

$customer = [
    "name" => 'Miguel',
    "balance" => 200,
    "information" => [
        "type" => 'premium',
        "available" => 100
    ]
];

echo "<pre>";
var_dump($customer['name']);
echo "<pre/>";

// echo $customer['name'];
// echo $customer['information']['type'];

$customer['code'] = 1929919102;

echo "<pre>";
var_dump($customer);
echo "<pre/>";

include 'includes/footer.php';