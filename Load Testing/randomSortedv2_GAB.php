<?php
// Function to generate random numbers
function generateRandomNumbers($count, $min, $max) {
    $numbers = [];
    for ($i = 0; $i < $count; $i++) {
        $numbers[] = mt_rand($min, $max);
    }
    return $numbers;
}

// Function to store random numbers (in this context, just return the array)
function storeRandomNumbers($numbers) {
    return $numbers;
}

// Function to sort and display the numbers
function sortAndDisplayNumbers($numbers, $order = 'ascending') {
    if ($order === 'ascending') {
        sort($numbers);
    } elseif ($order === 'descending') {
        rsort($numbers);
    }
    
    echo "Sorted Array in " . ucfirst($order) . " Order:<br>";
    echo "[ " . implode(", ", $numbers) . " ]<br>";
    
    echo "<br>Detailed view of the sorted array:<br>";
    echo "<pre>";
    print_r($numbers);
    echo "</pre>";
}

// Parameters
$numberOfRandoms = 10;
$minRange = 1;
$maxRange = 100;

// Generate random numbers
$generatedNumbers = generateRandomNumbers($numberOfRandoms, $minRange, $maxRange);

// Store random numbers
$storedNumbers = storeRandomNumbers($generatedNumbers);

// Display unsorted numbers
echo "Generated numbers between $minRange and $maxRange:<br>";
echo implode(" | ", $storedNumbers) . "<br><br>";

echo "Unsorted Array:<br>";
echo "[ " . implode(", ", $storedNumbers) . " ]<br><br>";

// Sort and display numbers in ascending order or descending order
sortAndDisplayNumbers($storedNumbers, 'ascending');

?>
