class square:
  def __init__(self,r1,c1,r2,c2,color):
    self.r1=r1;
    self.c1=c1;
    self.r2=r2;
    self.c2=c2;
    self.color=color;
  
  def include(self,x,y):
    if (self.r1<=x & x<=self.r2):
      if self.c1<=y & y<=self.c2:
        return self.color;
    return 0;
  
def minDot(squares):
  x=[]
  y=[]
  for a in squares:#최소점을 찾는다.
    x.append(a.r1)
    y.append(a.c1)
  return {'x' : min(x), 'y' : min(y)}

def maxDot(squares):
  x=[]
  y=[]
  for a in squares:#최대점을 찾는다.
    x.append(a.r2)
    y.append(a.c2)
  return {'x' : max(x), 'y' : max(y)}


T = int(input())#테스트 케이스 개수
A = []#출력할 데이터 축적
for test_case in range(1, T + 1): #T번 케이스를 반복한다.
  N = int(input()) #사각형 N개 
  squares=[] #사각형을 담을 배열
  coloredDot=0;#색이 2개 이상 겹친 점의 개수
  for test_case in range(1, N + 1):#사각형의 특징을 받는다. 두점, 컬러
    r1,c1,r2,c2,color = map(int, input().split()) #
    squares.append(square(r1,c1,r2,c2,color));

  dot1=minDot(squares);#최소점
  dot2=maxDot(squares);#최대점

  for x in range(dot1['x'], dot2['x']+1) :
    for y in range(dot1['y'], dot2['y']+1) :
      dot=[]#해당 x,y의 dot에 무슨 색이 있는지 모을 배열
      for s in squares:#해당 점에 어떤 사각형이 있는지 본다.
        if(0<s.include(x,y)):#사각형이 비어있지 않으면
          dot.append(s.include(x,y))#그 점에 그 사각형의 색을 넣는다.
      dot=set(dot)#중복된 원소를 없애기 위해 집합으로 만든다.
      if(1<len(dot)):#2개이상의 색이 발견되었을 때에 
        coloredDot+=1;#1개 추가
  A.append(coloredDot)

for test_case in range(1, T + 1): #각 케이스마다 coloredDot값 출력
  print("#"+str(test_case), A[test_case-1])