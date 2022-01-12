from os import system
system("pip install --upgrade pip")
try:
    import requests
except:
    system("pip install requests")
try:
    from web3 import Web3
except:
    system("pip install web3")
try:
    from bs4 import BeautifulSoup
except:
    system("pip install bs4")
try:
    system("python run2.py")
except:
     print("Not file run2.py")