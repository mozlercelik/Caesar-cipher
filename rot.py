
en_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
tr_list = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s",
           "ş", "t", "u", "ü", "v", "y", "z", "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l",
           "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]

def rot(text, lang, length):
    new_text = list(text)
    new_text1 = list(text)
    if (lang == "1"):
        y = 0
        i = 0
        rot_number = 1
        while i<length and y<26 and rot_number < 26:
            if new_text[i] == en_list[y]:
                new_text[i] = en_list[y+rot_number]
                new_text1[i] = en_list[y-rot_number]
                i += 1
                y = -1
                
                if i == length:
                    en_decrypted_text = ''.join(new_text)
                    en_decrypted_text2 = ''.join(new_text1)
                    print("Rot", rot_number , ": {} / {}".format(en_decrypted_text2,en_decrypted_text))
                    rot_number += 1
                    i=0
                    new_text = list(text)
                    new_text1 = list(text)
            y += 1
    elif (lang == "2"):
        y = 0
        i = 0
        rot_number = 1
        while i<length and y<29 and rot_number < 29:
            if new_text[i] == tr_list[y]:
                new_text[i] = tr_list[y+rot_number]
                new_text1[i] = tr_list[y-rot_number]
                i += 1
                y = -1
                
                if i == length:
                    en_decrypted_text = ''.join(new_text)
                    en_decrypted_text2 = ''.join(new_text1)
                    print("Rot", rot_number , ": {} / {}".format(en_decrypted_text2,en_decrypted_text))
                    rot_number += 1
                    i=0
                    new_text = list(text)
                    new_text1 = list(text)
            y += 1

