#EXERCISE1 

class Phone:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
    def call(self, other_phone):
        self.call_history.append(other_phone.phone_number)
        other_phone.call_history.append(self.phone_number)
        print(f"Calling {other_phone.phone_number} from {self.phone_number}")
    def show_call_history(self):
        print(f"Call history for {self.phone_number}:")
        for number in self.call_history:
            print(number)
    def send_message(self, other_phone, message):
        self.messages.append((other_phone.phone_number, message))
        other_phone.messages.append((self.phone_number, message))
        print(f"Sending message to {other_phone.phone_number}: {message}")
        
    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        for number, message in self.messages:
            if number != self.phone_number:
                print(f"To {number}: {message}")
                
#Test of code
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")
phone1.call(phone2)
phone1.show_call_history()
phone1.send_message(phone2, "Hello!")
phone1.show_outgoing_messages()
phone2.show_outgoing_messages()
