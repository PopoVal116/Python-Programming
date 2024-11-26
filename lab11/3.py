pochtochka = {'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']}
ima= list(pochtochka.values())
mail = list(pochtochka.keys())
mailiki=0
for names_list in ima:
    for i in range(len(names_list)):
        print(f'{names_list[i]}@{mail[mailiki]} ', end=' ')
    mailiki +=1
