## 2019-08-08 fizzbuzz

写一个程序，输出从 1 到 100 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。


### 题目分析：

```
Can I call FizzBuzzWhizz 
- get '1' when I pass in 1 
- get '2' when I pass in 2 
- get 'Fizz' when I pass in 3 or include 3 
- get 'Buzz' when I pass in 5 
- get 'Fizz' when I pass in 6 (a multiple of 3)
- get 'Buzz' when I pass in 10 (a multiple of 5)
- get 'FizzBuzz' when I pass in 15 (a multiple 3 and 5)
- get 'FizzBuzz' when I pass in 30 (a multiple 3 and 5)
```