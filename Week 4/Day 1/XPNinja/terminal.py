#Ex 1 and 2 done

#Exerise 3

3 <= 3 < 9 #true
3 == 3 == 3 #true
bool(0) #false
bool( 5 == "5") #false
bool(4 ==4) == bool("4"=="4") #true
bool(bool(None)) #false

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

 print("x is", x) # x is true
 print("y is", y) #y is False

 print("a:", a) # a: 5

 print("b:", b) # b: 10 (false reverts to 0 )


 #Exercise 4

 my_text = "this is a sentence i made up by myself. Give me a sticker"

 print(len(my_text))


 #Exercise 5

 sentence = input('type a sentence without the letter A')
a = str('a')
while a in sentence.split():
    sentence = input('input again cannot include A')
    if a not in sentence.split():
        print("congratulations")

