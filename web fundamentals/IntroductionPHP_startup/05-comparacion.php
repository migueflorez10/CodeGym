<?php include 'includes/header.php';

$number1 = 20;
$number2 = 30;
$number3 = 30;
$number4 = "30";

var_dump($number1 > $number2);

echo "<br/>";

var_dump($number1 < $number2);

echo "<br/>";

var_dump($number1 >= $number2);

echo "<br/>";

var_dump($number1 <= $number2);

echo "<br/>";

var_dump($number2 == $number2);

echo "<br/>";

var_dump($number3 == $number4);

echo "<br/>";

var_dump($number3 === $number4);

echo "<br/>";

// -1 if it is less, 0 if it is equal, and 1 if it is greater
var_dump($number2 <=> $number3);

include 'includes/footer.php';