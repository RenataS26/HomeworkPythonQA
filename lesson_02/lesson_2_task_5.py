n=int(input("Номер месяца:"))
def month_to_season(n):
    if n in [6,7,8]:
        return "Лето"
    elif n in [9,10,11]:
        return "Осень"
    elif n in [12,1,2]:
        return "Зима"
    elif n in [3,4,5]:
        return "Весна"
    else:
        return "Не существует"
    
print(month_to_season(n))    
    
   