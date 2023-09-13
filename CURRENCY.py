from json import load

with open("currencyy.json",'r',encoding='UTF-8') as f:
    data=load(f)
# print(data)
rates=data.get("conversion_rates")
# print(rates)
# rates={"USD": 1, "AED": 3.6725, "AFN": 86.0330, "ALL": 97.5499, "AZN": 1.7974,"INR":82.0914}
amount=int(input("enter amount you want to ecxhange:>"))
fromcurrcode=input("enter source currency code:>")
tocurrencode=input("enter destination curren code:>")
 # eqn =(amt/from)*to
from_code_rate=rates.get(fromcurrcode)
to_code_rate=rates.get(tocurrencode)
tott=int(amount/from_code_rate)*to_code_rate
print(tott)
