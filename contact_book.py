from abc import ABC, abstractmethod


class Contact_book(ABC):
    @abstractmethod
    def print_Contact_book ():
        pass

class Contact_info:
    First_name = ""
    Last_name =""
    Phone_number = ""
    Email_address = ""

class Contact_info_manager(Contact_info,Contact_book):

    def print_Contact_book(self):
        # name = [self.First_name, self.Last_name]
        # phone_number = [self.Phone_number]
        # email_address = [self.Email_address]

        Contact_dict= {
           "Name" : f"{self.First_name} {self.Last_name}",
           "Phone Number" : self.Phone_number,
           "Email address" :self.Email_address
        }
        # print(f"{Contact_dict.items()}")
        for key,value in Contact_dict.items():
            print (key ,value)
            


contact = Contact_info_manager()
contact.First_name = "Oluwabunmi"
contact.Last_name = "Ogundare"
contact.Phone_number = "08177623814"
contact.Email_address = "bumary2016@gmail.com"
contact.print_Contact_book()




