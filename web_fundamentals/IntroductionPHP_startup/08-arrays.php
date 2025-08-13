<?php include 'includes/header.php';

$cart = ['ifhone', 'ipad', 'Macbook Air', 'Macbook Pro'];

// useful for viewing the contents of an array
echo "<pre>";
var_dump($cart[1]);
echo "<pre/>";

// Acces an element of the array 
echo $cart[1];

// adds an element to index four of the array
$cart[4] = 'New Product';
var_dump($cart);

// adds a new element to the end of the array 
array_push($cart, 'AirPods');
var_dump($cart);

// adds a new element to the beggining of the array 
array_unshift($cart, 'Mac Mini');
var_dump($cart);


include 'includes/footer.php';