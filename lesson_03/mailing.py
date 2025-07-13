from address import Address

class Mailing:

    def __init__(self,to_address,from_address,cost,track):
        self.taddress=to_address
        self.faddress=from_address
        self.cost=cost
        self.track=track


    def __str__(self):
        faddress_str=",". join([str(address) for address in self.faddress])
        taddress_str=",". join([str(address) for address in self.taddress])
        return f"Отправление {self.track} из {faddress_str} в {taddress_str}. Стоимость {self.cost} рублей."
              
