<?php include 'includes/header.php';

$nameCustomer = "Miguel Angel";

// know the length of the text
echo strlen($nameCustomer);
var_dump($nameCustomer);

// Remove white space
$text = trim($nameCustomer);
echo strlen($text);

// convert text to uppercase
echo strtoupper($nameCustomer);

// convert text to lowercase
echo strtolower($nameCustomer);

$email1 = 'migueflorez10@gmail.com';
$email2 = 'Migueflorez10@gmail.com';

var_dump(strtolower($email1) === strtolower($email2));

echo str_replace('Miguel Angel', 'Mig', $nameCustomer);

// check whether a string is valid or not
echo strpos($nameCustomer, 'Miguel Angel');

echo '<br/>';

$typeCustomer = 'Premium';
echo 'The customer ' . $nameCustomer . ' is ' . $typeCustomer;

echo "<br/>";

echo "The customer {$nameCustomer} is {$typeCustomer} ";
include 'includes/footer.php';  