Q4 = open('Q4.txt', 'w')

V = [1, 5, 10, 25, 50]

for i in range(2010, 2201, 5):
    Q4.write(str(V) + '\n')
    Q4.write(str(i) + '\n')
    
Q4.close()

Q5 = open('Q5-V1.txt', 'w')
V1 = [1, 2, 6, 12, 24, 48, 60]
for i in range(2000, 2201):
    Q5.write(str(V1) + '\n')
    Q5.write(str(i) + '\n')
Q5.close()

Q5 = open('Q5-V2.txt', 'w')
V2 = [1, 6, 13, 37, 150]
for i in range(2000, 2201):
    Q5.write(str(V2) + '\n')
    Q5.write(str(i) + '\n')
Q5.close()

Q6 = open('Q6.txt', 'w')
V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for i in range(2000, 2201):
    Q6.write(str(V) + '\n')
    Q6.write(str(i) + '\n')
Q6.close()