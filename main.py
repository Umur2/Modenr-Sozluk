meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            'OK BOOMER': 'Tamam şampion',
            'AGGRO':'agresifleşmek/sinirlenmek'
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")



if word in meme_di.keys():
    print(meme_di[word])
else:
    print('Bu kelimeyi biliyorsun')
