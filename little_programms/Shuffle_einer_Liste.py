# Shuffle einer Liste
# – Schreiben Sie eine Funktion, die eine list<int> als Parameter übernimmt und diese mithilfe eines Zufallszahlengenerators durcheinanderwürfelt

# – Ideen zur Implementierung:
# ● Items an zufälligen Positionen vertauschen
# ● Item an zufälliger Position entfernen und hinten anhängen

import random

def shuffle_list(my_list):
    change_list = []

    while len(my_list) > 0:
        new_list = random.choice(my_list)
        change_list.append(new_list)
        my_list.remove(new_list)

    print(change_list)

my_list = [1,2,3,4,5]
shuffle_list(my_list)