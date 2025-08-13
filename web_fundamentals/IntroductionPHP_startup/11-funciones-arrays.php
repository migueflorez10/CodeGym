<?php include 'includes/header.php';

$cart = array('ifhone', 'macbook air', 'airpods');

// in_array - search for elements in an array
var_dump(in_array('ifhone', $cart));
var_dump(in_array('ipad', $cart));

// sort - sort element of an array

$numbers = array(1,7,3,9,2,5,1);
sort($numbers); //sort from lowest to highest
rsort($numbers);  // sort from highest to lowest

echo '<pre>';
var_dump($numbers);
echo '<pre/>';

// sort associative array
$customer = array(
    'balance' => 200,
    'type' => 'premium',
    'name' => 'Miguel'
);

asort($customer); // Sort by values (alphabetical order) A-Z
arsort($customer); // Sort by values (alphabetical order) Z-A
ksort($customer); // Sort by keys (alphabetical order) A-Z
krsort($customer); // Sort by keys (alphabetical order) Z-A

echo '<pre>';
var_dump($customer);
echo '<pre/>';

include 'includes/footer.php';