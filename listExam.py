menuList = []
priceList = []

def showBill():
    print("Fuck my food".center(20,"+"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
def showPrice():
    total = 0
    for price in range(len(priceList)):
        total = total + priceList[price]
    print("Total :",total,"Baht")
while True:
    menuName = input("Please enter menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
showPrice()



