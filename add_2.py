#׸���� �������� �� �������� ��������� �� 5, �������� ��������

from random import randint

while True: 
    try:
        lenth = int(input("������� ����� ������� ����� ������: "))
        break
    except (TypeError, ValueError):
        print ('��� �� ����� �����, ����������, ������� ����� �����')

a = [0] * lenth                 # ������
        
for i in range(lenth):
    a[i] = randint(-20, 20)     # ����� ��������� �� ������� ����� �������� ������
print("������� ������: ")
print(a)

for i in range(lenth):    
    if a[i] % 2 == 0:
        a[i]+=5
    else: 
        a[i] = 0
print("������ ��� ��� ������ ����� ��������� �� 5, � �������� ��������: ")  
print(a)