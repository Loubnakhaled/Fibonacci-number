# Fibonacci Number Calculator

This repository contains three different implementations of the Fibonacci number calculation algorithm using Python on vs code. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.

## Fibonacci Calculation Methods

### 1. Recursive Approach

The first method uses a recursive approach to calculate the Fibonacci number. While this method is simple to implement, it becomes significantly slower as the input number increases due to repeated calculations. Therefore, it's not recommended for large Fibonacci numbers.

### 2. Recursive Approach with Memoization

The second method improves upon the recursive approach by incorporating memoization. Memoization involves caching the intermediate results to avoid redundant calculations. By storing previously computed Fibonacci numbers in a list, this approach significantly improves performance for larger numbers.

### 3. Iterative Approach (Optimized)

The third method utilizes an iterative approach to compute the Fibonacci number. It avoids recursion altogether and calculates the Fibonacci sequence in a loop. This method has the best performance for larger Fibonacci numbers, as it doesn't suffer from the overhead of function calls.

## Time Complexity Analysis

After analyzing the time complexity of each method, it has been determined that the third approach, the iterative method, is the most efficient for larger Fibonacci numbers. It has a time complexity of O(n), where n is the input number.

## Usage

To use the Fibonacci Number Calculator, follow these steps:

1. Clone the repository to your local machine.
2. Open the code in vs code.
3. Run the code and provide an input number to calculate its Fibonacci value.
4. The program will display the Fibonacci number calculated using each of the three methods and the corresponding execution time.


## Contributing

Contributions to this Fibonacci Number Calculator are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to submit a pull request. Ensure that your changes align with the purpose and style of the project.
