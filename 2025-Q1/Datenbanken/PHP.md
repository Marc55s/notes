~~~sql
try {
	$conn = new PDO("mysql:host=$host;dbname=$dbname",$user, $pw);
} catch(PDOExeception e) {
	die("Error" . $e->getMessage());
}

$stmt = $conn->query("select * from table");
$user = $stmt->fetch(PDO::FETCH_ASSOC);
~~~