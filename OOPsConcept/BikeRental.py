# Display available bikes
# Request a bike rent
# Exit


class bikeShop:
    def __init__(self,stock):
        self.stock = stock


    def displayBikes(self):
        print("Total Bikes",self.stock)


    def rentForBike(self,q):

        if q <=0:
            print("Enter the positive value or greater then Zero")


        if q >self.stock:
            print("Enter the value less than stock ")

        else:
            self.stock=self.stock-q
            print("Total Prices",q*100)
            print("Total Bikes",self.stock)



while True:
    obj =bikeShop(100)
    uc = int(input('''
    
1 Display Stocks
2 Rent a Bike
3 Exit   
    
    '''))


    if uc==1:
        obj.displayBikes()

    elif uc==2:
        n =int(input("Enter the Qty:___"))

        obj.rentForBike(n)

    else:
        break



# toptel , endela , turing.com