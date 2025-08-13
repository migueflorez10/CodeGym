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

foreach($products as $product){ ?>

    <li>
        <p>Product: <?php echo $product['name']; ?> </p>
        <p>price: <?php echo '$' . $product['price']; ?>  </p>
        <?php
        if($product['available']){
            echo '<p>Available</p>';
        }else {
            echo '<p>Not Available</p>';
        }
        ?>
    </li>
    <?php
    
}


include 'includes/footer.php';