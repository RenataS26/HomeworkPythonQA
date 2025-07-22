import pytest
from string_utils import StringUtils

string_utils=StringUtils()

#первая функция(заглавная)
@pytest.mark.positiv
@pytest.mark.parametrize("input_str, expected",[
    ("skypro", "Skypro"), 
    ("hello world", "Hello world"),
    ("python", "Python"),
    ])
def test_capitalaze_positiv(input_str, expected):
    assert string_utils.capitalaze(input_str)== expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",[
    ("123abc", "123abc"),
    ("", ""),
    (" ", " "),
])
def test_capitalaze_negativ (input_str, expected):
    assert string_utils.capitalaze(input_str)== expected 

#вторая функция(пробел)
@pytest.mark.positiv
@pytest.mark.parametrize("input_str, expected",[
    (" skypro", "skypro"),
    (" 123abc", "123abc"),
    ("hello ", "hello "),
])
def test_trim_positiv(input_str,expected):
    assert string_utils.trim(input_str) == expected    

@pytest.mark.negativ
@pytest.mark.parametrize("input_string", [
    None,
    425,
    ["testing test"],
        
])
def test_trim_negative_exceptions(input_string):
    obj = StringUtils()
    with pytest.raises(Exception):
        obj.trim(input_string)
    
    
    
#содержит искомый символ
@pytest.mark.positiv
@pytest.mark.parametrize("input_str, expected, symbol", [
    ("hello", "hello", "h"),
    ("skypro", "skypro", "f"),
])
def test_contain_positiv(input_str, expected, symbol):
    assert string_utils.contains(input_str)== expected 

@pytest.mark.negativ
@pytest.mark.parametrize("string,symbol", [
    (None, "a"),
    ("test", None),
    (123, "a"),
    ("test", 5),
    ("test", ["a"]),
])
def test_contains_negative(string, symbol):
    obj = StringUtils()  
    with pytest.raises(Exception):
        obj.contains(string, symbol)   


#удаляет символ
@pytest.mark.positiv
@pytest.mark.parametrize("string,symbol,expected", [
    ("hello world", "o", "hell wrld"),
    ("test", "t", "es"),
    ("aaaaa", "a", ""),
    ("python", "z", "python"), 
])
def test_delete_symbol_positive(string, symbol, expected):
    obj = StringUtils()  
    result = obj.delete_symbol(string, symbol)
    assert result == expected

@pytest.mark.negative
@pytest.mark.parametrize(
    "input_string, symbol, expected",
    [
        ("hello world", "x", "hello world"),        
        ("test string", "z", "test string"),        
        ("abcdef", "1", "abcdef"),                   
        ("12345", "a", "12345"),                     
        ("", "a", ""),                              
    ]
)
def test_delete_symbol_negative(input_string, symbol, expected):
    obj = StringUtils()
    result = obj.delete_symbol(input_string, symbol)
    assert result == expected, f"Expected '{expected}' but got '{result}'"