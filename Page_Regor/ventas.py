class Ventas:
    def __init__(self, name, email, phone_number, address, cp):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.cp = cp

    def toDBCollection(self):
        return{
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address,
            'cp': self.cp
        }