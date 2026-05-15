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


