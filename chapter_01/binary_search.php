<?php

$arr = [1, 6, 8, 20, 53, 65, 77, 87, 95];

function binary_search($arr, $item) {
    $low = 0;
    $high = count($arr) - 1;
    
    while($low <= $high) {
        $mid = floor(($low + $high) / 2);
        $guess = $arr[$mid];

        if($guess === $item) {
            return $mid;
        } else if($guess > $item) {
            $high = $mid - 1;
        } else {
            $low = $mid + 1;
        }
    }

    return null;
}


echo binary_search($arr, 65);