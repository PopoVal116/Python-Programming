slovarik={'1' : 'AEILNORSTU',
          '2' : 'DG',
          '3' : 'BCMP',
          '4' : 'FHVWY',
          '5' : 'K',
          '8' : 'JX',
          '10' : 'QZ'}
shitalovo=0
slovo=input('Введите слово: ').upper()
for bukva in slovo:
    for ball in slovarik:
        if bukva in slovarik[ball]:
            shitalovo+=int(ball)
print(shitalovo)

