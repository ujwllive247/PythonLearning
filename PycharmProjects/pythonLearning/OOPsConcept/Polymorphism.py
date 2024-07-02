

class Ws:
    def displayinfo(self,name=''):
        # print("Welcome to Wscubetech"+name)
        print("Welcome to Wscubetech")


class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()  # Calling the parent function

        print("Welcome to IIP")


obj = IIP()

obj.displayinfo()
# obj.displayinfo(' Python')   # Overloading......