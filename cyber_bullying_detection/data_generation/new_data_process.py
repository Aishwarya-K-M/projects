import emoji

new_file = open("cyber_bullying_detection/data_generation/hinglish_cyberbullying_dataset.csv",'r', encoding='UTF-8')

final = open("cyber_bullying_detection/data_generation/dataset.csv",'a', encoding='UTF-8')

data = new_file.readlines()

def unicode_escape(chars, data_dict):
    return ' '+chars.encode('unicode-escape').decode()+' '

for i in data[1:]:
    final.write(emoji.replace_emoji(i[:len(i)-2].replace(',','').replace('!','').replace('?','').replace('"',''),replace=unicode_escape)+i[-3:])

new_file.close()
final.close()
