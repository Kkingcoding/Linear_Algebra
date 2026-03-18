def calc(n):
    mul = 1                    # 변수 초기화, 곱셈이므로 0 불가
    for i in range(0,n):       # 0에서 n-1까지의 정수를 순서대로 리스트 생성
        mul *= int(input())    # 키보드로 입력 받음, 그걸 정수로 변환, 받을 때마다 곱함
    return mul                 # 반환

print("Input the number of values to be multipled => ")
count = int(input()) 

while count <= 0:              # 예외 처리, 개수는 음수 불가
    count = int(input())

print("Mul = ", calc(count))