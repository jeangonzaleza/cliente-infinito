from datetime import datetime
import time
import requests

def Main():
  while(True):
    try:
      host = 'http://34.66.186.52:8080/keepalive'
      requests.get(host, timeout=30)
      time.sleep(10)
    except:
      print("Something went wrong. The process will call the server again in 10 minutes")
      time.sleep(600)
      continue

if __name__ == '__main__': 
    Main() 