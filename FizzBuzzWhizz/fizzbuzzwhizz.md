## 2020-3-27 fizzbuzzwhizz 

你是一名体育老师，在某次课距离下课还有五分钟时，你决定搞一个游戏。此时有100名学生在上课。游戏的规则是： 

1. 你首先说出三个不同的特殊数，要求必须是个位数，比如3、5、7。     
2. 让所有学生拍成一队，然后按顺序报数。 
3. 学生报数时，如果所报数字是第一个特殊数（3）的倍数，那么不能说该数字，而要说Fizz；如果所报数字是第二个特殊数（5）的倍数，那么要说Buzz；如果所报数字是第三个特殊数（7）的倍数，那么要说Whizz。 
4.  学生报数时，如果所报数字同时是两个特殊数的倍数情况下，也要特殊处理，比如第一个特殊数和第二个特殊数的倍数，那么不能说该数字，而是要说FizzBuzz, 以此类推。如果同时是三个特殊数的倍数，那么要说FizzBuzzWhizz。   
5. 学生报数时，如果所报数字包含了第一个特殊数，那么也不能说该数字，而是要说相应的单词，比如本例中第一个特殊数是3，那么要报13的同学应该说Fizz。如果数字中包含了第一个特殊数，那么忽略规则3和规则4，比如要报35的同学只报Fizz，不报BuzzWhizz。

### 题目分析：

```
Can I call FizzBuzzWhizz 
- get '1' when I pass in 1 
- get '2' when I pass in 2 
- get 'Fizz' when I pass in 3 or include 3 
- get 'Buzz' when I pass in 5 
- get 'Whizz' when I pass in 7 
- get 'Fizz' when I pass in 6 (a multiple of 3)
- get 'Buzz' when I pass in 10 (a multiple of 5)
- get 'Whizz' when I pass in 14 (a multiple of 7)
- get 'Fizz' when I pass in 13 (include 3)
- get 'Fizz' when I pass in 23 (include 3)
- get 'FizzBuzz' when I pass in 15 (a multiple 3 and 5)
- get 'FizzWhizz' when I pass in 21 (a multiple 3 and 7)
- get 'BuzzWhizz' when I pass in 70 (a multiple 5 and 7)
- get 'FizzBuzzWhizz' when I pass in 105 (a multiple 3 and 5 and 7)
```