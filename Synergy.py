print('Введите грузоподьемность одной лодки (по условию m (1 ≤ m ≤ 10e6))')
m = int(input('M = '))
print('Введите количество рыбаков (по условию n (1 ≤ n ≤ 100))')
n = int(input('N = '))

countBoat = 0

if m < 1 or m > 1000000 or n < 1 or n > 100:
    print('Неверно введены данные')
else:
    totalMassTravelers = []
    print('Введите вес каждого путешественника')
    for i in range(n):
        totalMassTravelers.append(int(input(f'Масса {i + 1} путешественника = ')))

    totalReversed = list(reversed(list(sorted(totalMassTravelers))))

    for i in range(len(totalReversed)):
        maxMassTraveler = totalReversed[i]
        countJ = i + 1
        if i != len(totalReversed) - 1:
            if maxMassTraveler > m:
                continue
            if maxMassTraveler == m:
                totalReversed[i] = -1
                countBoat += 1
            elif maxMassTraveler != -1:
                for j in range(i + 1, len(totalReversed)):
                    if totalReversed[j] != -1 and maxMassTraveler + totalReversed[j] <= m:
                        totalReversed[i] = -1
                        totalReversed[j] = -1
                        countBoat += 1
                        break
                    elif countJ == len(totalReversed) - 1:
                        totalReversed[i] = -1
                        countBoat += 1
                     
                    countJ += 1
                        
        elif maxMassTraveler != -1:
            if maxMassTraveler <= m:
                totalReversed[i] = -1
                countBoat +=1
    
    print(countBoat)