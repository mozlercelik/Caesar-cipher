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
while True:
    lang = input("Select language: ")
    if lang == "1" or lang == "2":
        break
    else:
        print("Please chose 1 or 2")
        continue
text = input("Enter encrypted/decrypted text: ")
text = text.lower()
length = len(text)

rot.rot(text, lang, length)
