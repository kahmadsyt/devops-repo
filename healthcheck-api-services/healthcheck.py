#import http.client
import requests
import os
import json
from dotenv import load_dotenv
import time
import datetime

load_dotenv()

def send_slack_message(payload, webhook):
      """Send a Slack message to a channel via a webhook.

      Args:
         payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
         webhook (str): Full Slack webhook URL for your chosen channel.

      Returns:
         HTTP response code, i.e. <Response [503]>
      """
      return requests.post(webhook, json.dumps(textPayload))
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print("--- %s seconds ---" % (time.time() - start_time))
now = datetime.datetime.now()
print(now)

services = ["admin","notification","email","sms","merchant","product","product-graphql","search_product","search_catalog","comment","review","category","cart","shipping","payment","transaction",
"encrypter","assets","session-user","session-administrator","chat","balance-merchant","socket_chat","balance-customer","voucher","customer"]
start_time = time.time()
for x in services:
   apiGateway = os.environ.get('API_GATEWAY')
   #match x:
   if x == "admin":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('ADMIN_APIKEY')
      path   = os.environ.get('ADMIN_PATH')
   elif x == "notification":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('NOTIF_APIKEY')
      path   = os.environ.get('NOTIF_PATH')
   elif x == "email":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #   apiKey = os.environ.get('EMAIL_APIKEY')
   #   path   = os.environ.get('EMAIL_PATH')
   elif x == "sms":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #   apiKey = os.environ.get('SMS_APIKEY')
   #   path   = os.environ.get('SMS_PATH')
   elif x == "merchant":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('MERCHANT_APIKEY')
      path   = os.environ.get('MERCHANT_PATH')
   elif x == "product":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('PRODUCT_APIKEY')
      path   = os.environ.get('PRODUCT_PATH')
   elif x == "product-graphql":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #    apiKey = os.environ.get('PRODUCT-GRAPHQL_APIKEY')
   #    path   = os.environ.get('PRODUCT-GRAPHQL_PATH')
   elif x == "search_product":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('SEARCH_PRODUCT_APIKEY')
      path   = os.environ.get('SEARCH_PRODUCT_PATH')
   elif x == "search_catalog":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('SEARCH_CATALOG_APIKEY')
      path   = os.environ.get('SEARCH_CATALOG_PATH')
   elif x == "comment":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('COMMENT_APIKEY')
      path   = os.environ.get('COMMENT_PATH')
   elif x == "review":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('REVIEW_APIKEY')
      path   = os.environ.get('REVIEW_PATH')
   elif x == "category":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('CATEGORY_APIKEY')
      path   = os.environ.get('CATEGORY_PATH')
   elif x == "cart":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('CART_APIKEY')
      path   = os.environ.get('CART_PATH')
   elif x == "shipping":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('SHIPPING_APIKEY')
      path   = os.environ.get('SHIPPING_PATH')
   elif x == "payment":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('PAYMENT_APIKEY')
      path   = os.environ.get('PAYMENT_PATH')
   elif x == "transaction":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('TRANSACTION_APIKEY')
      path   = os.environ.get('TRANSACTION_PATH')
   elif x == "encrypter":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #   apiKey = os.environ.get('ENCRYPTER_APIKEY')
   #   path   = os.environ.get('ENCRYPTER_PATH')
   elif x == "assets":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #   apiKey = os.environ.get('ASSETS_APIKEY')
   #   path   = os.environ.get('ASSETS_PATH')
   elif x == "session-user":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('SESSION-USER_APIKEY')
      path   = os.environ.get('SESSION-USER_PATH')
   elif x == "session-administrator":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('SESSION-ADMIN_APIKEY')
      path   = os.environ.get('SESSION-ADMIN_PATH')
   elif x == "chat":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('CHAT_APIKEY')
      path   = os.environ.get('CHAT_PATH')
   elif x == "socker-chat":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #   apiKey = os.environ.get('SOCKKET-CHAT_APIKEY')
   #   path   = os.environ.get('SOCKKET-CHAT_PATH')
   elif x == "balance-merchant":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('BALANCE-MERCHANT_APIKEY')
      path   = os.environ.get('BALANCE-MERCHANT_PATH')
   elif x == "balance-customer":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('BALANCE-CUSTOMER_APIKEY')
      path   = os.environ.get('BALANCE-CUSTOMER_PATH')
   elif x == "socket_chat":
       print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   elif x == "voucher":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('VOUCHER_APIKEY')
      path   = os.environ.get('VOUCHER_PATH')
   elif x == "customer":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      apiKey = os.environ.get('CUSTOMER_APIKEY')
      path   = os.environ.get('CUSTOMER_PATH')
   elif x == "xml":
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
   #    apiKey = os.environ.get('XML_APIKEY')
   #    path   = os.environ.get('XML_PATH')
   else:
      apiKey = ""
      path   = "/"
   headers = {'APIKEY': apiKey,'Content-type': 'application/json'}
   r = requests.get(''.join([apiGateway, path]),headers=headers)

   if r.status_code == 200:
      # print(r.status_code)
      res = r.json()

      response = json.dumps(res["response"])
      databases = json.dumps(res["databases"])
      data = json.dumps(res)
      services = json.dumps(res["services"])
      message_broker = json.dumps(res["message_broker"])

      class Response:

         def __init__(self, data):
            self.__dict__ = json.loads(data)

      response = Response(data)

      if hasattr(response , 'databases'):
         if response.databases is not None:
            if not (response.databases.get('postgre') is None):
               if response.databases.get('postgre') != 'up':
                  textPayload = "you have databases postgre integration issue on service"+ str(x) + str(os.environ.get('ENV'))
                  jsonString = json.dumps(textPayload, indent=4)
                  print(f"{bcolors.FAIL}"+"postgre: " + response.databases.get('postgre') +f"{bcolors.ENDC}")
               else:
                  print(f"{bcolors.OKBLUE}"+"postgres: " + response.databases.get('postgre')+f"{bcolors.ENDC}")
            elif not (response.databases.get('mongo') is None):
               if response.databases.get('mongo') != 'up':
                  textPayload = "you have databases mongo integration issue on service"+ str(x) + str(os.environ.get('ENV'))
                  jsonString = json.dumps(textPayload, indent=4)
                  print(f"{bcolors.FAIL}"+"mongo: "+ response.databases.get('mongo') +f"{bcolors.ENDC}")
               else:
                  print(f"{bcolors.OKBLUE}"+"mongo: "+ response.databases.get('mongo')+f"{bcolors.ENDC}")
            if not (response.databases.get('redis') is None):
               if response.databases.get('redis') != 'up':
                  textPayload = "you have redis integration issue on service"+ str(x) + str(os.environ.get('ENV'))
                  jsonString = json.dumps(textPayload, indent=4)
                  print(f"{bcolors.FAIL}"+"redis: " + response.databases.get('redis') +f"{bcolors.ENDC}")
               else:
                  print(f"{bcolors.OKBLUE}"+"redis:" + response.databases.get('redis')+f"{bcolors.ENDC}")
            if not (response.databases.get('elasticsearch') is None):
               if response.databases.get('elasticsearch') != 'up':
                  textPayload = "you have elasticsearch integration issue on service"+ str(x) + str(os.environ.get('ENV'))
                  jsonString = json.dumps(textPayload, indent=4)
                  print(f"{bcolors.FAIL}"+"elasticsearch: "+ response.databases.get('elasticsearch') +f"{bcolors.ENDC}")
               else:
                  print(f"{bcolors.OKBLUE}"+"elasticsearch: "+ response.databases.get('elasticsearch')+f"{bcolors.ENDC}")
         else:
            print(f"{bcolors.WARNING}"+"db not found"+f"{bcolors.ENDC}")

      if hasattr(response , 'services'):
         if response.services is not None:
            services = json.dumps(response.services)
            services = services.replace("down",f"{bcolors.FAIL}"+"down"+f"{bcolors.ENDC}")
            print(services.replace("up",f"{bcolors.OKGREEN}"+"up"+f"{bcolors.ENDC}"))

            values = list(response.services.values())
            for k in values:
               if k != 'up':
                  textPayload = {"text" : "status code:" +str(r.status_code)+ ",services:" +str(response.services)+", message: error from service " +str(x)+ str(os.environ.get('ENV')) +" integration"}
                  jsonString = json.dumps(textPayload, indent=4)
                  # print(f"{bcolors.FAIL}"+ jsonString +f"{bcolors.ENDC}")
                  webhook = os.environ.get('SLACK_WEBHOOK')
                  send_slack_message(jsonString, webhook)
         else:
            print(f"{bcolors.WARNING}"+"service not found"+f"{bcolors.ENDC}")
   elif r.status_code == 404:
      print(f"-{bcolors.HEADER}"+ x.upper()+f"{bcolors.ENDC}-")
      print(f"{bcolors.FAIL}"+ str(r.status_code) +f"{bcolors.ENDC}")
   else:
      print(f"{bcolors.FAIL}"+ str(r.status_code) +f"{bcolors.ENDC}")

      textPayload = {"text" : "status code:" +str(r.status_code)+ ", message: error from service " +str(x)+"-"+ str(os.environ.get('ENV'))+ " request"}
      jsonString = json.dumps(textPayload, indent=4)
      # print(f"{bcolors.FAIL}"+ str(jsonString) +f"{bcolors.ENDC}")

      webhook = os.environ.get('SLACK_WEBHOOK')
      send_slack_message(jsonString, webhook)