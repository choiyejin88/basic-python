'''
#Q1
s='Python'
print(s[0]+s[-1])

#Q2
name='hello soft'
print(name.upper())

#Q3
msg='apple,banana,grape'
print(msg.split(','))

#Q4
word='banana'
print(word.count('a'))

#Q5
text='coding class'
print('class' in text )

#Q6
n=583
a=str(n)
print((int(a[0])+int(a[1])+int(a[2])))

#Q7
n=4729
b=str(n)
print(b[0])

#Q8
n=2468
c=str(n)
d=int(len(c))
print(d)
print((int(c[0])+int(c[1])+int(c[2])+int(c[3]))/d)

#Q9
n=2395
e=str(n)
cnt=0
i=0
while i < len(e):
    if e[i] in '2357':
        cnt +=1
    i+=1
print(cnt)

#Q10
n=8641
f=str(n)
sum=0
i=0
while i <len(f):
    if f[i] in '2357':   
        sum+=int(f[i])
    i+=1
print(sum)

#Q10
g='level'
if g[:]==g[::-1]:
    print('yes')

#Q13
s='abcdef'
print(s[1:4])

#cospro 3급 예제 문제 2
#문제1
##n=int(input())
##arr=list(map(int,input().split()))
##sum=0
##for i in range(1,n,2):
##    sum=sum+int(arr[i])
##print(f'{sum}')


#문제2
##counter=0
##str=input()
## if 'a' <= str[i] <='z':
##for i in range(0,len(str)):
##    if str[i] == str.lower()[i]:
##        counter+=1
##print(f'{counter}')

#문제3
##str1=input()
##str2=input()
##print(f'{str1}&{str2}')

#문제4

##str1=input()
##str2=input()
##print( str1 if str1 > str2 else str2)

#문제5
##str=input()
##for i in range(0,len(str)):
##    for j in range(0,i+1):
##        print(f'{str[j]}',end="")
##    print(end=" ")

#문제6
##k=int(input())
##n=int(input())
##for i in range(n):
##    print(k,end=" ")
##    k+=3


#문제7
##N=list(map(int,input().split()))
##cnt=0
##for i in N:
##    if i !=7:
##        cnt+=1
##    else:
##        break
##print(f'{cnt}')
##    
        
## 14 45 50 3 7 11 5 23 9 80
##11 17 4 10 29 7 8 


#문제8
##n1=int(input())
##n2=int(input())
##
##if n1 < n2 :
##    print(n1)
##else:
##    print(n2)

#문제 9 
##n=int(input())
##for i in range(n):
##    print('-'*i,end="")
##    print('*'*(n-i),end="")

#문제 10
##n1=int(input())
##n2=int(input())
##n3=n1-n2
##
##print(abs(n3))
'''

#cospro 3급 예상 문제
#문제01
##score=list(map(int,input().split()))
##total_score=0
##
##for subject in score:
##    total_score+=subject
##
##average=total_score/len(score)
##print('%.2f'%average)

#문제02
##a=int(input())
##b=int(input())
##
##abs_a=abs(a)
##abs_b=abs(b)
##
##if abs_a > abs_b:
##    print(f'{a}')
##elif abs_a < abs_b:
##    print(f'{b}')
##else:
##    print(a)

#문제03
##base=int(input())
##height=int(input())
##
##triangle=base*height/2
##rectangle=base*height
##
##print(f'{triangle:.1f} {rectangle}')
##print('%.1f %d'%(triangle,rectangle))

#문제04
##a=int(input())
##b=int(input())
##c=int(input())
##
##if c%(a*b) == 0 :
##    print('true')
##else:
##    print('false')

#문제05 ***
##cards=input().split()
##
##priorty='JKQ'
##winner='A'
##
##for i in range(len(priorty)):
##    if priorty[i]==cards[0]:
##        for k in range(i+1,len(priorty)):
##            if priorty[k] == cards[1]:
##                winner='B'
##print(winner)

#문제 06
##arr=list(map(int,input().split()))
##cnt=0
##
##for i in range(len(arr)):
##    if arr[i]%2 == 0:
##        cnt+=1
##result=(len(arr)-cnt)*cnt
##print(f'{result}')

#문제 07
##password=input()
##result=password.lower()
##print(f'{result}')

#문제08
##green=list(map(int,input().split()))
##yellow=list(map(int,input().split()))
##green_large=max(green)
##yellow_large=max(yellow)
##print(f'{green_large} {yellow_large}')

#문제09
##name=input()
##cnt=0
##for i in range(0,len(name)):
##    if name[i] in 'kK':
##        cnt+=1
##print(f'{cnt}')

#문제10
##arr=list(map(int,input().split()))
##n=int(input())
##
##if arr[n-1] < 0:
##    print('-1')
##elif arr[n-1]==0:
##    print('0')
##else:
##    print('1')

#cos pro 3급 실전형 연습문제

#문제1. 짝수 개수 세기

def count_even(nums):
    cnt=0
    for x in nums:
        if x%2==0:
            cnt+=1
    return cnt
print(count_even([1,2,4,7]))

#문제2. 문자열에서 숫자 합 
def sum_digits(s):
    total=0
    for ch in s:
        if ch in '1234r567890':
            total+=int(ch)
    return total
print(sum_digits('a1b20c3'))

#문제3. 최솟값 위치 ***
def min_index(a):
    m=a[0]
    idx=0
    for i in range(1,len(a)):
        if a[i] < m:
            m=a[i]
            idx=i
    return idx
print(min_index([5,3,9,3]))

#문제5. 리스트 필터링
def only_mul3(nums):
    return[x for x in nums if x%3==0]
print(only_mul3([1,3,6,7,9]))

#문제6. 문자열 뒤집기
def reverse_str(s):
    return[s[::-1]]
print(reverse_str('abc'))

#문제8. 구간 합
def range_sum(a,i,j):
    return sum(a[i:j+1])
print(range_sum([10,20,30,40],1,2))

#문제9. 문자열에서 단어개수
def word_count(s):
    return len(s.split())
print(word_count('  hi  there  '))

#문제10. 절댓값 최댓값
def max_abs(nums):
    return max(nums,key=abs)
print(max_abs([-2,5,-10,3]))

#문제11. 디버깅: 평균 계산
def avg(nums):
    total=0
    for i in range(len(nums)):
        total+=nums[i]
    return total/len(nums)
print(avg([2,4,6]))

#문제12. 디버깅:리스트 끝까지
def total(a):
    s=0
    for i in range(0,len(a)):
        s+=a[i]
    return s
print(total([1,2,3]))

#문제13. 디버깅:문자열 자르기
def drop_first(s):
    return s[1:]
print(drop_first('python'))

#문제15.디버깅: 함수가 none 반환
def sorted_copy(a):
##    a.sort()
    b=sorted(a)
    return b #a
print(sorted_copy([3,1,2]))


