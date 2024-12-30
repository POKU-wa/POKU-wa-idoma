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
    'war': "obu",
    'knife': "okpa",
    'day': "ojo",
    'forest': "agbo",
    'mouth': "onu",
    'life': "ola",
    'ground': "ikpa",
    'light': "ihe",
    'shadow': "ojiji",
    'oyan': "sun",}

k = 30
while k > 0:

    word = input('enter an english word:')
    if word in idoma_dictionary:
        print(idoma_dictionary[word])

    else:
        print('word is beyond dictionary  scope')

    k -=1
