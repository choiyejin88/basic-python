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
arr=list(map(int,input().split()))
n=int(input())

if arr[n-1] < 0:
    print('-1')
elif arr[n-1]==0:
    print('0')
else:
    print('1')


