from address import Address
from mailing import Mailing

to_address=Address(601503,"Гусь-Хрустальный","Каховского",10, 67)
from_address=Address(600000,"Владимир","Дворянская",45, 4)

mailing=Mailing(from_address,to_address,300,"456789")

print(mailing)
