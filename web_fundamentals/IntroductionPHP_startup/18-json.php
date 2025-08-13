<?php include 'includes/header.php';


$products = [
    [
        'name' => 'ifhone',
        'price' => 1500,
        'available' => true
    ],
    [
        'name' => 'MacBook Pro',
        'price' => 3500,
        'available' => true
    ],
    [
        'name' => 'Air Pods Pro 2',
        'price' => 800,
        'available' => false
    ],
];

echo '<pre>';
var_dump($products);
$json = json_encode($products, JSON_UNESCAPED_UNICODE);

$json_array = json_decode($json);
var_dump($json_array);
echo '</pre>';



include 'includes/footer.php';