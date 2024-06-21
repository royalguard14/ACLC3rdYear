<?php
$numberOfRandoms = 10;
$minRange = 1;
$maxRange = 100;

$randomNumbers = [];

for ($i = 0; $i < $numberOfRandoms; $i++) {
    $randomNumbers[] = mt_rand($minRange, $maxRange); 
}

echo "Generated numbers between $minRange and $maxRange:<br>";
echo implode(", ", $randomNumbers) . "<br><br>";

echo "Array before sorting:<br>";
echo "[" . implode(", ", $randomNumbers) . "]<br><br>";

asort($randomNumbers); 

$sortedNumbers = array_values($randomNumbers);

echo "Array after sorting in ascending order:<br>";
echo "[" . implode(", ", $sortedNumbers) . "]<br>";

echo "<br>Detailed view of the sorted array:<br>";
echo "<pre>";
print_r($sortedNumbers);
echo "</pre>";
?>
