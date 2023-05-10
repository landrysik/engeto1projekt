"""

projekt1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Andrysík  

email: lukas@andrysik.cz

discord: lukasandrysik#4601

"""


from task_template import TEXTS
divider = "-"
users = {"bob": "123", 
"ann": "pass123",
"mike": "password123",
"liz": "pass123"
}


occurences = []

counter_all_words = 0
counter_titlecase = 0
counter_uppercase = 0
counter_lowercase = 0
counter_numeric = 0
numeric_sum = 0

nejvyssi_delka = 0


username_input = input ("username: ")
password_input = input ("password: ")

if username_input in users:
    if users[username_input] == password_input:
        print (f"{divider * 40} \nWelcome to the app, {username_input} \nWe have {(len(TEXTS))} texts to be analyzed.")
        print (f"Enter a number btw 1 and {(len(TEXTS))} to select:")
        selected_text_number = input ()
        if selected_text_number.isnumeric() == False or int(selected_text_number)>(len(TEXTS)):
            print ("Input Error")
        else:
#            print ("zadani ok")
            
            selected_text = (TEXTS[(int(selected_text_number)-1)].split())
# Vypocet statistik
            for slovo in selected_text:
                slovo = slovo.replace(",", "")
                slovo = slovo.replace(".", "")
                counter_all_words +=1
                               
                if  slovo.isupper() and slovo.isalpha():
                    counter_uppercase +=1
                    counter_titlecase +=1
#                    print (slovo)
                elif slovo.islower():
                    counter_lowercase +=1                    
                elif slovo.istitle() and slovo.isalpha():
#                    print (slovo)
                    counter_titlecase +=1
                elif slovo.isnumeric():
                    counter_numeric +=1
                    numeric_sum += int(slovo)







            print (f"There are {counter_all_words} words in the selected text.")
            print (f"There are {counter_titlecase} titlecase words.")            
            print (f"There are {counter_uppercase} uppercase words.")   
            print (f"There are {counter_lowercase} lowercase words.")              
            print (f"There are {counter_numeric} numeric strings.")   
            print (f"The sum of all the numbers {numeric_sum}")                                       



# Vytvoreni seznamu o delce nejvetsiho slova

            for slovo in selected_text:             
                if (len(slovo)) > nejvyssi_delka:
                    nejvyssi_delka = len(slovo)

            occurences = [0] * (nejvyssi_delka)


# pridani delek slov do lsitu occurences


            for slovo in selected_text:
                slovo = slovo.replace(",", "")
                slovo = slovo.replace(".", "")
                delka = (len(slovo))
                occurences [(delka-1)] +=1 
#            print (occurences)

            print (divider * 40)


            print ("LEN".rjust(3) + "|" + "OCCURENCES".center (max(occurences)+2) + "|NR")
            print (divider * 40)

            for i in range (len(occurences)):

                print (str((i+1)).rjust(3) + "|" + ("*"* (occurences[i])).ljust(max(occurences)+2) + "|" +str(occurences[i]))







    else:
        print ("bad pass")
else:
    print ("unregistered user, terminating the program...")
    