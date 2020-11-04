# -*- coding: utf-8 -*-



import streamlit as st
import streamlit.components.v1 as components

import requests

# our key will be stores in this file (for security purposes)
from personal_key import api_key

# API URL
url = "https://free.currconv.com/api/v7/currencies?apiKey={}".format(api_key)

response = requests.get(url)

# Print the status code of the response.
print(response.status_code)

# our output will be a dictionary enclosed within the strings
# convert the result into dictionary using eval
curr_dict = eval(response.content.decode("utf-8"))

# access the value of the key 'results'
curr_dict = curr_dict['results']

# get the keys, convert them into a list and store them in a variable currency
currency = list(curr_dict.keys())

# extract the locality from the dictionary 'curr_dict'
locality = []
for curr in currency:
    locality.append(curr_dict[curr]['currencyName'])

# zip the currency and the locality in the form of a dictionary  
final_dict = dict(zip(locality, currency))

# combine the key and value as a string so that we can show them in a selectbox
box_menu = []
for key, value in final_dict.items():
    box_menu.append("{} : {}".format(value, key))
    


# Web App Building

# Set title and image
from PIL import Image
img = Image.open("currency.jpg")

html_code = """
        <div style="background-color: #3cba54 ; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">LIVE Currency Converter</h1>
        </div>
        """
components.html(html_code)

st.image(img, width=700)


# Convert From
convert_from = box_menu
from_choice = st.selectbox("Convert From", box_menu)
from_choice = from_choice.split(':')[0].strip()

# Convert From
convert_to = box_menu
to_choice = st.selectbox("Convert To", box_menu)
to_choice = to_choice.split(':')[0].strip()

# Input Price
money_to_convert = st.number_input("Enter the amount you want convert")



if(st.button('Convert')):
    # Conversion
    url = "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey={}".format(from_choice, to_choice, api_key)
    response = requests.get(url)
    
    price = list(eval(response.content.decode("utf-8")).values())[0]
    
    
    # Converted money
    converted_money = money_to_convert * price
    st.success(converted_money)















