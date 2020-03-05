import sys
def recursive_fizzbuzz(start, end, arr = []):
    # Base case
    if start == end + 1:
        return arr
    
    result_str = ""

    if start % 3 == 0:
        result_str += "Fizz"
    if start % 5 == 0:
        result_str += "Buzz"
    
    if len(result_str) == 0:
        arr.append(start)
    else:
        arr.append(result_str)
    return recursive_fizzbuzz(start+1, end)

if __name__ == "__main__":
    print(recursive_fizzbuzz(1,20))