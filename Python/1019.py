
# 문제
# 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.


y, m, d= input().split(".")
y= int(y)
m = int(m)
d = int(d)
print("%04d" %y,"%02d" % m,"%02d" % d,sep='.')