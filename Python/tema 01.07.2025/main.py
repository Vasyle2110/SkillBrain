import random

print('Bine ai venit la par/impar')
print('Spune Par sau Impar pentru a incepe jocul')

history = []
score = 0
rounds = 0
result = input().strip().lower()

while result not in ['par', 'impar', 'stop']:
    print('Introdu o optiune valida ("par", "impar", "stop")')
    result = input().strip().lower()

while result != 'stop':
    rounds += 1
    number1 = int(input('Introdu un numar intre 0 si 10: '))

    while number1 < 0 or number1 > 10:
        number1 = int(input('Introdu un numar intre 0 si 10: '))

    #number2 = random.randint(0,10)
    number2 = 0
    s = number1 + number2
    print('Suma este ',sum)
    if (s % 2 == 0 and result == 'par') or (s % 2 == 1 and result == 'impar'):
        score += 1
        print('Ai castigat!')
        history.append(1)
    else:
        print('Calculatorul a castigat!')
        history.append(0)
    if 0 not in history[-2:] and len(history) >= 2:
        print('Esti tare!!')
    print('Daca vrei sa mai jucam spune "par" sau "impar"')
    print('Daca vrei sa oprim jocul si sa vezi rezultatele spune "stop"')
    result = input().strip().lower()
    while result not in ['par', 'impar', 'stop']:
        print('Introdu o optiune valida')
        result = input().strip().lower()
print('Calculatorul a castigat',rounds-score,' runde si tu ai castigat ',score)
if score > rounds - score:
    print('Felicitari!')
