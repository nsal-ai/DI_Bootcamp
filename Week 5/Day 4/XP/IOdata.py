import json

import random

def get_words_from_file():
    with open('sowpods.txt', 'r') as f:
        word_data = f.readlines()
        return word_data

get_words_from_file()

def get_random_sentence(length):
    a =[]
    
    for word in range(0, length):
        a.append(random.choice(get_words_from_file()).strip().lower())
    #print(a)
    sentence = ' '.join(a)
    print(sentence)
    
#get_random_sentence(4)

def main():
    '''
    This program outputs randomly generated sentences
    from a database of words 
    
    '''
    print('This program outputs randomly generated sentences')
main()

while True:
    number_of_words = input('Enter how many words you want')

    try:
        number_of_words = int(number_of_words)
    except: 
        print('Please use numeric digits')

        continue
    if number_of_words < 2 or number_of_words > 20:
        print('Choose number between 2 and 20')
        continue
    break

get_random_sentence(number_of_words)

#=========================================


import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

print(sampleJson)

json_object = json.loads(sampleJson)

print(json_object["company"]["employee"]["payable"]["salary"])

# new_key = "birth-date: "
# sampleJson["company"]["employee"].append(new_key)

json_object = json.dumps(sampleJson, indent = 2)

with open('secretTxt.txt', 'w') as file_obj:
    json.dump(sampleJson, file_obj)

