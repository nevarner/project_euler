//
var n3 = Math.trunc(999/3);
var n5 = Math.trunc(999/5);
var n15 = Math.trunc(999/15);


function sum_to_n(n) {      // Sums from 1 to n 
    return n*(n+1)/2
}

console.log(3*sum_to_n(n3) + 5*sum_to_n(n5) - 15*sum_to_n(n15))
