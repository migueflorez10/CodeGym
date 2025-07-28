<?php include 'includes/header.php';

$authenticated = true;
$admin = true;

if($authenticated && $admin){
    echo 'user successfully authenticated';
} else {
    echo'user not authenticated, log in';
}

// if - nested (anidados)
$customer = [
    "name" => 'Miguel',
    "balance" => 200,
    "information" => [
        "type" => 'premium'
    ]
];

echo '<br/>';

if(!empty($customer)){
    echo 'The customer arrangement is not empty ';

    if($customer['balance'] > 0){
        echo 'The customers balance is available';
    } else {
        echo 'No balance';
    }
};

// else if 
echo '<br/>';

if($customer['balance'] > 0){
    echo 'The customer has a balance';
} else if($customer['information']['type'] === 'premium'){
    echo 'The customer is premium';
} else {
    echo 'No customer defined, or no balance, or not premium';
}

// Switch 
echo '<br/>';

$technology = 'php';
switch($technology){
    case 'php':
        echo 'PHP is an excellent language';
        break; 
    case 'Java':
        echo 'Java is an excellent language';
        break; 
    case 'HTML':
        echo 'HTML is an excellent language';
        break; 

    default:
        echo 'JavaScript is better';
        break;
}

include 'includes/footer.php';