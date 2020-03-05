// 0,1,1,2,3,5,8,13,21,34,55,89, 144...
// each value is the sum of the previous values

// O(n)
function fibonacciIteractive(n){
    let arr = [0,1];
    for(let i = 2; i < n + 1; i++){
        arr.push(arr[i-2] + arr[i-1]);
    }
    return arr[n]
}
// 0(2^n)
function fibonacciRecursive(n){
    if(n < 2){
        return n;
    }
    let result = fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    return result
}
console.log(fibonacciIteractive(8))
console.log(fibonacciRecursive(8))