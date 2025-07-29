<?php
declare(strict_types=1);

include 'includes/header.php';

function usuarioAutenticado(): string {
    return "The user is authenticated";
}

$usuario = usuarioAutenticado();

echo $usuario;  // Print: The user is authenticated

include 'includes/footer.php';
