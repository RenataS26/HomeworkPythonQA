class StringUtils:

#делает первую букву заглавной и возращает текст
    def capitalaze(self,string:str):
        return string.capitalize()
    
#удаляет пробелы в начале, если они есть    
    def trim(self,string:str):
        whitespace=" "
        while string.startswith(whitespace):
            string=string.removeprefix(whitespace)
        return string
    
#возвращает "True", если содержит искомый символ, "False"если нет    
    def contains(self,string:str, symbol:str):
        try: res=string.index(symbol)
        except ValueError: pass
        return res
    
    
#удаляет символ, строку 
def  delete_symbol(self,string:str, symbol:str):
        if self.contains(string,symbol):
            string=string.replace(symbol, "")
        return string
 
