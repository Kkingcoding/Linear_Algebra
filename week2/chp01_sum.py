def calc(n):
    sum = 0                    # 변수 초기화
    for i in range(0,n):       # 0에서 n-1까지의 정수를 순서대로 리스트 생성
        sum += int(input())    # 키보드로 입력 받음, 그걸 정수로 변환, 받을 때마다 더함
    return sum                 # 반환

print("Input the number of values to be added => ")
count = int(input()) 

while count <= 0:              # 예외 처리, 음수 불가
    count = int(input())

print("Sum = ", calc(count))

