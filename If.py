us = input("Username :")
ps = input("Password :")
if us == "admin" and ps == "1234" :
        print("---Welcome to my shop---")
        print("1.Padthai shrimp : 100 THB")
        print("2.Fry Rice Pork  : 70  THB")
        print("3.Omelet         : 30  THB")
        print("4.Noodle Chicken : 60  THB")
        food = input("What do you want?>>")
        if food == "1" :
                num = int(input("How many?>>"))
                print("Totol",100*num)
        elif food == "2" :
                num = int(input("How many?>>"))
                print("Totol",70*num)
        elif food == "3" :
                num = int(input("How many?>>"))
                print("Totol", 30 * num)
        elif food == "4" :
                num = int(input("How many?>>"))
                print("Totol", 60 * num)
else :
            print("error")



