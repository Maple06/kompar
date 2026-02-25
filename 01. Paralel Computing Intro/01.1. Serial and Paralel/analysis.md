# Serial vs Paralel Computing
This code shows whether paralel computing really shows increase in performance.
### Parameters
1. Process: Sum of square
2. Number count: 5,000,000

### Result
1. Serial
PS D:\01.1. Serial and Paralel> python serial.py
Total sum: 41666679166667500000
Time taken: <b>606102800 nanoseconds</b>
2. Paralel
PS D:\01.1. Serial and Paralel> python paralel.py
Processes:  4
Total sum: 41666679166667500000
Time taken: <b>432452600 nanoseconds</b>

With this, we can see that there is an improvement of time in paralel computation, with 173650200 nanoseconds difference.

&copy; 152024003 - Malendra Rizky