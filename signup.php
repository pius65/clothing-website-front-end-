<?php
// signup.php

// Database credentials
$servername = "localhost";
$dsn="mysql:host=localhost;dbname=deron";
$dbusername = "root";
$dbpassword = "";
$dbname = "my_database";
$sql = "SELECT * FROM `logins`;";

try {
    //code...
} catch (\Throwable $th) {
    //throw $th;
}


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve form data
$user = $_POST['username'];
$pass = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hashing the password
$email = $_POST['email'];

// Insert data into database
$sql = "INSERT INTO users (username, password, email) VALUES ('$user', '$pass', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close connection
$conn->close();
?>
