// Sum all numbers less than 1000 which are divisible by 3 or 5

function sum_to_n(n){
    return n*(n+1)/2
}
var n3 = Math.trunc(999/3);
var n5 = Math.trunc(999/5);
var n15 = Math.trunc(999/15);

console.log(3*sum_to_n(n3) + 5*sum_to_n(n5) - 15*sum_to_n(n15));
