import time
import uuid
import webbrowser

class Train:
    def __init__(self,TrainName):
        self.train = TrainName

    def show_name(self):
        print("Trains Avaliable at the moment are:")
        for train in self.train:
            print("* "+train)


    def get_data(self,TrainName):
        print(f"Your Train name is {TrainName}")
        print("Your Train time is 10:45 pm ")
        print("Your Train is coming on the Plaform number 2")


    def bookTkt(self,TrainName):
        ref_number = uuid.uuid4().hex
        print("Please wait a moment Ticket is booking......")
        time.sleep(15)
        print(f"Thanks for using this software your further refrence number is {ref_number} for train {TrainName}")
        print(f"Use this ref {ref_number} to confirm seat :)")
        time.sleep(10)
        get_url= webbrowser.open('/home/manish/Desktop/railway_management_system/index.html')
        
    
class Pasanger:
    def get_info(self):
        self.name = input("Enter the train name from the list to get information: ")
        return self.name

    def bookTicket(self):
        self.msg = input("Enter the train name which you want to book:")
        return self.msg

class Route:
    def __init__(self,route_list):
        self.route = route_list

    def routes_train(self):
        print("Routes of Train are:")
        for routes in self.route:
            print("->"+routes)


if __name__ == "__main__":
    train_list = Train(["Shatabdi Express","Goa Express","Passanger Express","Unchahar Sf Train"])
    route_list = Route(["Delhi","Haryana","Palwal","Rajasthan","UttarParadesh"])
    passanger = Pasanger()
    while(True):
        welcome_msg = '''
        *****Railway System****
        Please Choose Option:
        1.List Train
        2.Book Ticket
        3.List Route of Train
        4.Get Info
        5.Exit system
        '''
        print(welcome_msg)
        a = int(input("Enter choice::::"))
        if a ==1:
            rail_sys = train_list.show_name()

        elif a ==2:
            rail_sys = train_list.bookTkt(passanger.bookTicket())

        elif a ==3:
            rail_sys = route_list.routes_train()

        elif a == 4:
            rail_sys = train_list.get_data(passanger.get_info())

        elif a == 5:
            print("Thanks for choosing our system.....")
            exit()
        else:
            print("Invalid Choice:::")