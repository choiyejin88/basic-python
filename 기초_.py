print(99)
print(80+2*6/3)
print()
print(889.2-4.5)
print(True)
print(False)
print('hello'); print("world")
print(5>2)
print(6==6)#==은 같다
print(3!=3)#!=같지않다


print('오늘은 수요일이고 엄청 날이 좋다.\
그리고 이따가 점심약속이 있다.')

print('''aksjdh

kas
jdhkajs
hdk''')
#싱글쿼터 3개로, 더블쿼터로 감싸면 멀티라인글을 쓸수 있다

'''여기는 멀티 주석(코멘트)가능'''


#변수:variable,데이터를 컴퓨터 공간에 저장하는 기능

num1=1000 #=은 대입연산자

num2=3.141592
str1='zzz'
print(num1,num2,str1,'입니다')




num1=145
num2=-256
num3=-265
print(num1,num2,num3)

num1=2.34
num2=3.33
num3=4.12
num4=-4
print(num1,num2,num2,num3,num4)

my='나의 나이는'
age='13'
phone='내 전화번호는'
num='010-1234-5678'
print(my,age,phone,num)


a=378.23
b=775.45
c=a+b
print(c)

n1=10; n2=20;n3=3.2
print(n1*n2) #정수끼리 정수결과
print(n1*n3) #실수가 하나라도 있으면 실수 결과
print('나누기',9/3) #무조건 소수
print(9//3.0) #몫 3.0 -> 9를 9.0으로 자동형 변환
print(9%2) #나머지1
print(float(2**3)) #2x2x2
#명시형변환 int('5'), float(3), ttr(6.25),bool()
print(pow(2,3)) #2**3
#bool()에 대해서
print(bool())
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(-99))
print(bool('a'))

#수학명령어 sum()
s1=(-1,2,3,-6,-8)
print('합은',sum(s1))
print(abs(-7)), #절대값
print('최소값은',min(s1))
print('최소값은',min(s1,key=abs))
print('최대값은',max(s1))
print('최대값은',max(s1,key=abs))
print('반올림은',round(3.14))
print('반올림은',round(3.141592,4)) #소수점 4번째 자리 반올림


    #교재 32p  
num1=15
num1+=45
num2 = num1
num2-=15
num3=num2
num3*=2
num4=num3
num4/=3
print(num4)


#연산,대입을 한번에 복합대입연산자 += -+ /= **=...

u1=5
u1+=3 # u1=u1+3
print(u1)
u1=0
u3=u2=u1
print(u3,u2,u1) # 0,0,0이 된다.
a,b=10,15

#문자열의 특징
sct1='red python!!!.'
#"+더하기"는 연결 연산자로 바뀐다. *는 반복연산자
print('나는 '+sct1) #한칸띄어쓰기가 없다.
print('*'*4)
#인덱스(index):위치
print(sct1[0]) #[]index기호 =위치에 있는 값을 보여줘
print(sct1[4])
print(sct1[1:6:1]) #[시작:끝-1:간격]->1은 안싸도 기본값으로 됨
print(sct1[1:6:2])
print(sct1[:6]) # 시작 생략
print(sct1[6:]) # 끝 생략
print(sct1[:]) #처음부터 끝까지
print(sct1[::-1]) #역순출력
p='madam'
if p[:] ==p[::-1]:
    print('회문맞아')
else:
    print('회문아니야')

print(len(sct1)) #길이갯수 세기

a1=' 010-1234-5678'
a2='나의 전화번호는'
a3='입니다'
print(a2+a1+a3)

a4='엄마사랑해.'
print(a4*5)

sct1='python'
print(sct1[2])
print(sct1[4])
print(sct1[-1])

sct2='I like to learn python.'
print(sct2[3:5])
print(sct2[10:12])
print(sct2[:6])
print(sct2[13:])


#260415

b="=I love my mom"
c=len(b)
d="a의 길이:"+str(c)
print(d)
e="a의 길이는 "+str(c)+"입니다"
print(e)


a="아빠"
b="나는 "+a+"를 사랑해."
print(b)

c=b*5
print(c)

print(len(c))


#입력함수(명령어 _input) 문자로 받는다.
##flower=input('좋아하는 꽃은?')
##print(flower+'를 좋아하는 구나')
##int(정수),float(소수),bool(참/거짓),str(문자)
##n1=input('숫자1? ')
##n2=input('숫자2? ')
##print(n1+n2)

##n1=1=input('숫자1?')
##n2=2=input('숫자2?')
##n1,n2=int(n1),int(n2)
##print(n1+n2) #print(int(n1)+int(n2))

#4 5 6
##a,b,c=map(int,input('숫자 3개를 넣으세요').split())
####a,b,c=int(a),int(b),int(c)
##print(a+b+c)


#옵션명령어 sep='', end=''
print('010','1234','5678',sep='-')
print('생기 있는', end='**') # 밑에 있는 데이터 붙여오기
print('4월의 봄날')

#포맷팅코드 %i %d(digit) %s %f(부동소수점)
age=2; name='연탄이'; hobby='산책'
weight= 15.699 #부동소수점은 반올림_원래는15.699000  6자리 나옴
print('우리집 %s는 %03d살이고 취미는 %s이고 몸무게는 %.2fkg입니다'%(name,age,hobby,weight))


#f-string
#정렬 >(오른쪽), <(왼쪽, ^(중앙정렬)
print(f'우리집 {name:^8}는 {age:03d}살이고 취미는 {hobby}이고 몸무게는 {weight:.2f}입니다')

a=89.3
print('%d'%a) #int(a)

ban="1학년 3반"
average=76.435
print(f'{ban}의 평균 점수는 {average:.1f}입니다.')

name="김민수"
year=2008
month=3
day=9
print("%s님의 생년월일은 %d/%02d/%02d입니다."%(name,year,month,day))

#260416

##fahrenheit=input("오늘의 기온은 화씨 몇도 인가요?")
##centigrade=5/9*(int(fahrenheit)-32)
##print("화씨 온도:",float(fahrenheit))
##print("섭씨 온도:",round(centigrade,1))
##

##원화=input("오늘의 원 달러 환율은 얼마인가요?")
##달러=input("당신은 몇 달러를 환전하시겠습니까?")
##환전=int(달러)*int(원화)
##print('-'*15)
##print(f'{달러},{환전}')

##los=input("미국의 샌프란시스코에서 로스앤젤레스까지거리는?")
##mile=(1.609344*int(los))
##print(mile,"km")

##부산=input("서울에서 부산까지 거리는?")
##mile=(1.609344*int(부산))
##print(round(mile,1),"km")
##


##month=input("월을 입력하세요:")
#if month in '345':
##if month =="3"or month =="4" or month =="5":
##    print("%s월은 봄입니다."%(month))

##level=input("회원 레벨을 입력하세요:")
##if int(level)==1:
##    print("당신의 회원 등급은 비회원입니다.")
##if int(level)>=2 and int(level)<=4:
##    #2<=int(level)<=4:
##    print("당신의 회원 등급은 준회원입니다.")
##if int(level)>=5 and int(level)<=8: 
##    print("당신의 회원 등급은 정회원입니다.")
##if int(level)==9 and int(level)>=9: 
##    print("당신의 회원 등급은 우수회원입니다.")


##num=input("정수를 입력하세요:")
##if int(num)%2==0:
##    print("짝수입니다.")
##if int(num)%2!=0: #else:
##    print("홀수입니다.")

#260417
#조건문 : 조건에 따른 선택, 비교연산자, 논리연산자
##n1=int(input())
##n2=int(input())
##if n1==n2:
##    print('같습니다.')
##elif n1>n2:
##    print(str(n1)+'이 큽니다.')
##else:
##    print(str(n2)+'이 큽니다.')

##
##num=int(input("숫자를 입력하세요:"))
##if num%15==0:
##    print("3의 배수이면서 5의 배수입니다.")
##elif num%5==0:
##    print("5의 배수입니다.")
##elif num%3==0:
##    print("3의 배수입니다.")
##else:
##    print("3의 배수도 5의 배수도 아닙니다.")
##    


##num=int(input("정수를 입력하세요:"))
##if num>0:
##    if 1<num<100:
##        print("1에서 100사이의 정수입니다.")
##    else:
##        print("100보다 큰 정수입니다.")
##elif num==0:
##    print("0입니다.")
##else:
##    print("음수입니다.")

#반복문 for while 조건식
##while true: #무한반복
##    print('hi')

##while True: #1번 반복문
##    print('hi')
##    break
##print()
##while True: #3번 반복문
##    print('hi')
##    print('hi')
##    print('hi')
##    break
##
##print()
##i=1
##while True:
##    if i>100:
##        break
##    print(i,'hi')
##    i+=1 # = i+1
##print()
##
##i=1
##while i<=100: # or i<101 
##    print(f'{i:03d}hi')
##    i+=1 # = i+1


##print()
##i=1
##while i<=10: #1~10 사이 짝수출력하기
##    if i%2==0:
##        print(i,end=" ")
##    i+=1
##print()
##
##i=1
##while i<=10:
##    if i%2==1:
##        i+=1
##        continue
##    print(i,end=" ")
##    i+=1
##print()
##i=1
##while i<=10:
##    print(i,end=" ")
##    i+=2
##    
##print()
##
##i=1
##n=int(input("출력할 마지막 숫자를 입력하세요:"))
##while i<=n:
##    print(i,end=" ")
##    i+=1

#240424
#for: 가지고 있는 횟수 만큼 반복
#숫자의 범위
for i in(1,2,3,4,5):
    print(i)

#range(시작,끝+1,간격)->'1'은 생략 가능
##for i in range(1,101,2)
##    print(i,end=' ')
##print()
##
##for i in range(5,0,-1):
##    print(i,end=' ')
##print()
##
##for i in range(3):
##    print('^^')
##print()
##
##str5='xxzzrr'
##for i in range(len(str5)):#0~5
##    print(str5[i],end='')#값 출력 

##for i in range(10):
##    print('안녕하세요?')
##
##for i in range(1,100,2):
##    print(i,end=" ")
##
##print()
##
##for i in range(0,101,5):
##    print(i,end=" ")
##
##print()
##
##for i in range(0,101):
##    if i%5==0:
##        print(i,end=" ")

##sum=0
##for i in range(1,11):
##    sum=sum+i
##print("1~10의 합계:%d"%sum)

##for i in range(1,11):
##    print(" "*(10-i),end="")
##    print("*"*i,end="")
##    print()

##for i in range(5):
##    for j in range(10):
##        print('*',end=' ')
##    print()

##sum=0
##for i in range(1,101):
##    if i%2==0:
##        sum=sum+i
##print(f'1~100 사이 짝수의 합계:{sum}')
##
##sum=0
##count=0
##for i in range(101):
##    if i%3==0:
##        sum=sum+i
##        print('%04d'%sum,end=" ")
##        count=count+1
##
##        if count%10==0:
##            print()
##print('0부터 100사이의 3의 배수의 합은 %04d입니다.'%sum)

##for i in range(5):
##    print('*')
##for i in range(5):
##    print('*',end="")

##for i in range(5):
##    for j in range(5):
##        print('*',end="")
##    print()

##for i in range(1,6):
##    print((6-i)*"",end="")
##    print(i*"*",end="")
##    print()

##for i in range(5,0,-1):
##    print(i*"*",end="")
##    print((6-i)*"",end="")
##    print()
##
##dallarR=int(input('오늘의 원/달러 환율을입력하세요:'))
##yenR=int(input('오늘의 100엔 당 원/엔 환율을 입력하세요:'))
##print('-'*40)
##print("%8s %8s %8s"%("원","달러","엔"))
##print('-'*40)
##won=10000
##while won<=100000:
##    dollar=won/dallarR
##    yen=won/yenR*100
##    print('%8d %10.2f %10d'%(won,dollar,yen))
##    won=won+10000
##print("-"*40)


#260427
##for i in range(5,0,-1):
##    print((6-i)*" ",end="")
##    print(i*"*",end="")
##    print()

##for i in range(5):    p.15
##    for j in range(5):
##        if i > j:
##            print(" ",end="")
##        else:
##            print("*",end="")
##    print()
##

##key=input('문장을 넣으세요:')
##for i in key:
##    print(i, end=" ")

##number=input('-가 포함된 전화번호를 입력하세요:')
##for i in number:
##    if i=="-":
##        print("/",end="")
##    else:
##        print(i,end="")

##number=input('전화번호를 숫자만 입력하세요:')
##phone=""
##for i in range(0,len(number)):
##    if i ==2:
##        phone=phone+(number[2]+"-")
##    elif i ==6:
##        phone=phone+(number[6]+"-")
##    else:
##        phone=phone+number[i]
##print('당신의 전화번호는 %s입니다.'%(phone))

##day=input('생일을 12/15형식으로 입력하세요:')
##print("당신의 생일은 ",end="")
##
##for i in day:
##    if i =="/":
##      print("월 ",end="")
##    else:
##        print(i, end="")
##print("일입니다.")

##for i in range(4):
##    for j in range(4):
##        print(i+j,end="")
##    print()

##furuit=input('좋아하는 과일을 입력하세요:')
##for i in furuit:
##    if i ==" ":
##        print("/",end="")
##    else:
##        print(i,end="")

##sentence=input('영어 문장을 입력하세요:')
##count=0
##print("모음:",end="")
##for i in sentence:
##    if i=="a" or i=="e" or  i=="i" or i=="o" or i=="u":
##        count=count+1
##        print(i,end="")
##print()
##print('모음의 개수:%d'%count)
##        
##        

for i in range(100):
    if i %10 != 4 :  #if i %10 ==4: print(i,end=' ')
        continue
    print(i,end=" ")

    
