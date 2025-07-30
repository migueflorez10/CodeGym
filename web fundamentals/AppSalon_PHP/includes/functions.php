<?php

function get_services(){
    try { 
        // Import credentials
        require 'database.php';
        
        // SQL query
        $sql = "SELECT * FROM servicios;";

        // Run query
        $query = mysqli_query($db, $sql);
        return $query;

        // Access results 
        // echo "<pre>";
        // var_dump(mysqli_fetch_assoc($query));
        // echo "</pre>";

        // Close connection (optional)
        $result = mysqli_close($db);
        echo $result;

    } catch (\Throwable $th) {
        var_dump($th);
    }
}

get_services();