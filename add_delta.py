# 1. ����� ���������� ��������� � �������� ������� ARRAY,
# ������������ �� ������������ �� DELTA
# �����������: array = [1,2,3,5] delta = 4 �����: 1

from random import randint

print("�������, ����������, ������ ����� �����")

while True:
    try: 
        delta = int(input("������� ������: "))
        lenth = int(input("������� ����� �������: "))
        break
    except (TypeError, ValueError):
        print ('��� �� ����� �����, ����������, ������� ����� �����')
        
min_el = 10 * 6
k = 0                           # ���������� ���������
a = [0] * lenth                 # ������

for i in range(lenth):
    a[i] = randint(-15, 15)     # ����� ��������� �� ������� ����� �������� ������
print("�������������� ������: ")
print(a)

for i in range(lenth):          # ����� ������������
    if a[i] < min_el:
        min_el = a[i]

for i in range(lenth):          # �������� ������� ������
    if (min_el + delta) == a[i]:
        k += 1
        
print("���������� ���������, ������������ �� �������� ��", delta, " = ", k)