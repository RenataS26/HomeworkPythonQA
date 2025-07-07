class Mailing:

    def __init__(self,to_address,from_address,cost,track):
        self.taddress=to_address
        self.faddress=from_address
        self.cost=cost
        self.track=track

    def __str__(self):
        return (f"Отправление {self.track} из {self.faddress} в {self.taddress}. Стоимость {self.cost} рублей.")
              