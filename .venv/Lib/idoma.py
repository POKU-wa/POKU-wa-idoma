idoma_dictionary = {
    'brother': "dy",
    'come': "wa",
    'go': "nnwu",
    'father': "adamm",
    'cloth': "iri",
    'slipper': "adaba",
    'bottle': "ikpemu",
    'spoon': "uko",
    'dress': "uwe",
    'shoes': "ablakpa",
    'welcome': "adoo",
    'thank you': "anya",
    'mother': "abeba",
    'God': "Owoicho",
    'ancestor spirit': "alekwut",
    'work': "ama",
    'leg': "ukwu",
    'yam': "ikpa",
    'goat': "obe",
    'you': "unu",
    'food': "inya",
    'friend': "enya",
    'love': "ocho",
    'sun': "onya",
    'medicine': "owga",
    'shadow': "ojiji",
    'war': "oba",
    'light': "ihe",
    'day': "ojo",
    'forest': "agbo"}
k = 30
while k > 0:

    word = input('enter an english word:')
    if word in idoma_dictionary:
        print(idoma_dictionary[word])

    else:
        print('word is beyond dictionary  scope')

    k -=1
