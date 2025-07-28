<?php include 'includes/header.php';

$i = 0;//initializer

while($i < 10){
    echo $i . "<br>";
    $i++; //increase
}

echo "<br/>";

// Do While
$i = 0;
do {
    echo $i . "<br>";
    $i++;

} while ($i < 10);

echo "<br/>";

// for loop 
for ($i = 0; $i < 10; $i++){
    echo $i . "<br>";
}

/**
 * 3 imprimir FIZZ
 * 5 imprimir BUZZ
 * 15 imprimir FIZZ-BUZZ
 */

echo "<br/>";

// for ($i = 1; $i < 1000; $i++){
//     if($i % 3 === 0 && $i % 5 === 0 ){
//         echo $i . "--FIZZ BUZZ <br>";
//     }else if($i % 3 === 0){
//         echo $i . "--FIZZ <br>";
//     }else if($i % 5 === 0){
//         echo $i . "--BUZZ <br>";
//     } else {
//         echo $i . "<br>";
//     }
// }


// for Each

$customers = array('Miguel', 'Antonio', 'David');

foreach($customers as $customer){
    echo $customer . "<br>";
}

$customer = [
    'name' => 'Miguel',
    'balance' => 1000,
    'type' => 'premium'
];

foreach($customer as $key => $values){
    echo $key. '-' .$values . "<br>";
}



include 'includes/footer.php';

