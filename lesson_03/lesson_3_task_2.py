from smartphone import Smartphone

catalog=[
    Smartphone("Honor","I5","+79208527485"),
    Smartphone("Apple","16promax","+79001234569"),
    Smartphone("Samsung","S23","+79658974152"),
    Smartphone("Xiaomi","14pro","+79876543232"),
    Smartphone("Poco","5","+79638527441")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")