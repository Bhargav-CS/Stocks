import requests
from bs4 import BeautifulSoup
import time

url = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE?hl=en&sa=X&ved=2ahUKEwjJ3J6V9J7zAhXJzDgGHY1vDZQQ3ecFegQIARAT"
ticker = "NIFTY_50:INDEXNSE"



for i in range(3):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    last_price = "YMlKec fxKbKc"
    percentage = "JwB6zf V7hZne"
    points = "BAftM"
    print("last price",soup.find(class_=last_price).text)
    print("percentage",soup.find(class_=percentage).text)
    print("points",soup.find(class_=points).text)
    time.sleep(2)
    
    
