import random # biblioteka dėl atsitiktinio skaičiaus
print(' ')
print('Sveiki atvykę į žaidimą - atspėk skaičių')
print('Laimingasis skaičius yra tarp 1 ir 10')
print('Jūs turite 3 spėjimus')
print(' ')
skaicius = random.randint(1, 10) # sukuria atsitiiktinį skaičių tarp 1 ir 10
# print(skaicius)
bandymas = 0 # spėjimų pradžia

while bandymas < 3: ## duoda 3 spėjimus
    spejimas = int(input('Jūsų spėjimas: '))
    if spejimas == skaicius:
        print('\nJūs atspėjote!\n')
        break
    elif spejimas > skaicius:
        print('\nSkaičius yra mažesnis \n')
        bandymas += 1
    elif spejimas < skaicius:
        print('\nSkaičius yra didesnis \n')
        bandymas += 1
    else:
        print('\n Klaida \n')

