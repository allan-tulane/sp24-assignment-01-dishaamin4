

# CMPS 2200 Assignment 1

**Name:**_Disha Amin___________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  Yes. In order for 2^n+1 to exist in O(2^n), there must be a constant for which 2^n+1 <= c * 2^n. 2^n+1 = 2*2n. The limit as x --> infinity for (2^(n+1))/(2^n) = 2. So, there exists a constant for which 2^n can be an upper bound for 2^n+1, and for values that exceed that constant. Therefore, 2^n+1 exists in O(2n). 
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No. In order for 2^n+1 to exist in O(2^n), there must be a constant for which 2^(2^n) <= c * 2^n., and there exists no such values because 2^(2^n) will always grow exponentially faster than 2^n, so O(2^n) cannot be an upper bound for 2^(2^n). We can visualize this by seeing that the limit as x --> infinity for (2^(2^n))/(2^n) = infinity.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?
    No. In order for 2^n+1 to exist in O(2^n), there must be a constant for which n^1.01 <= c * (log^2)*n. If we compare the growth rates of these 2 functions, there is no constant for which we can multiplu (log^2)*n that will cause it to grow faster than n^1.01 because the limit as x --> infintity for (n^1.01)/(log^2)n = infinity.
.  
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.   Yes. In order for n^1.01 to exist in Omega((log^2)*n), there must exist a constant, c, and n sub 0, for which n^1.01 is greater than ((log^2)*n) for all values of n greater than n sub 0, and there exists such a constant.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No. In order for sqrt(n) to exist in O(logn^3), there must be a constant for which sqrt(n) <= c*logn^3, and there exists no such constant value for the limit of x --> infinity for sqrt(n)/logn^3.
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes. In order for sqrt(n) to exist in Omega(logn^3), there must be a constant, c, and n sub 0 for which sqrt(n) is greater than (logn^), and there exists such a constant.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  - COMPLETE

  - 2b. (6 pts) What does this function do, in your own words?  
  This function is the recursive implementation of the fibonacci sequence, which is a sequence that determines the next number by adding the previous 2 numbers. The function has a base case of the size of x equaling 1, in which case it will return x. Otherwise, it will recursively run foo to keep adding (x-1) + (x-2).

.  
.  
.  
.  
.  
3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  - COMPLETE

  - 3b. (4 pts) What is the Work and Span of this implementation?  
    Work - The work of this function is O(n). This is because the function uses a for loop to iterate through each item of the list one time.
    Span - The span of this function is O(n). This is because the function's loop operates sequentially.
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`. - COMPLETE   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  The work for this algorithm is w(n) = 2w(n/2) + O(1). The span for this algorithm is O(n).
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

  The work of this function is w(n) = 2w(n/2) + O(1). The span for this function is O(log2_n).
.  
.  
.  
.  
.  
.  
.  
.  

