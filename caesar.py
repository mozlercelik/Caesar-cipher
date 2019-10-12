import rot

print("""
   _____                             _____           
  / ____|                           |  __ \          
 | |     __ _  ___  ___  __ _ _ __  | |__) | __ ___  
 | |    / _` |/ _ \/ __|/ _` | '__| |  ___/ '__/ _ \ 
 | |___| (_| |  __/\__ \ (_| | |    | |   | | | (_) |
  \_____\__,_|\___||___/\__,_|_|    |_|   |_|  \___/ 
                                                                                                                                        
Welcome!
Please select language:
1) English alphabet
2) Turkish alphabet

""")
lang = int(input("Select language: "))
if lang != 1 or lang != 2:
    x = 1
while x==1:
    print("Please chose 1 or 2")
    lang = int(input("Select language: "))
    if lang == 1 or lang == 2:
        x=0
text = input("Enter encrypted/decrypted text: ")
if lang != 1 or lang != 2:
    print("Please chose 1 or 2")
text = text.lower()
en_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
tr_list = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s",
           "ş", "t", "u", "ü", "v", "y", "z", "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l",
           "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
length = len(text)
alinan_deger = list(text)

rot.rot(text, lang, en_list, tr_list, length)
