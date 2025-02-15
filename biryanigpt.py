#This is Khan bhai BiryaniGPT.. The best biryani in the whole world!

print("Asalam O Alaikum! Bhai Jaan Kia haal Hein..")

name = input("Jii pyare bhai jaan kia naam hai apka?\n")

if name == "Aslam Bhai":

    choor_status = input("kia tum woh he Asalam Bhai ho to pechi gali mai rehta hai?\n")
    if choor_status == "Yes":
        print("Bhai apka to pahlay ka hisaab baqi hai... pahlay wala paisa do phir order do...warna yaha say chaltay bano")
        exit()
    else:
        print("ohh pher theak hai! pechli gali ak aur Aslam Bhai rehta hain malik nai bola tha uska hisaab baqi hai woh aya to uska paisa lo phir order do.. Ji + name + " "jaan kia khidmat karon apki?")
else:    

    print("Bohat sukria " + name + " bhai jaan hamari shop per anay ka!!! InshahAllah maza ajaiga apko!!! Kasam say!!!\n")

menu = "Chicken Biryani?, Beef Biryani?, Beef Nalli Biryani?, Raita?, Salad?"

print(name + " bhai jaan!!! konsi Biryani do?\n\n" + menu)

order = input()

#Set Price for Biryani..

if order == "Chicken Biryani":
    price = 250
elif order == "Beef Biryani":
    price = 500
elif order == "Beef Nalli Biryani":
    price = 700

else:
    print("Sorry bhai Cold Drink Khatam hogaya hai...")
    price = 0


quantity = input("Kitni Biryani chayea bhai apko?\n")

total = price * int(quantity)

print("Ok " + name + " Bhaai jaan Biryani ka total hogaya Rs. " + str(total))

print("\n")

menu2 = "Raita?, Salad?"

print(name + " bhai apki " + order + " ready hai ... aur kuch chayea iskay sath?\n\n" + menu2)

order = input()

price = 50

quantity = input("Kitnay dedo bhai?\n")

total2 = price * int(quantity)

final_total = total + total2

print("Ok " + name + " Bhaai jaan apka total hogaya Rs. " + str(final_total))

print("Ok " + name + " bhai apka complete order ready hai, Thank you inshshAllah pher zarror ana")


