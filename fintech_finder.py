# Cryptocurrency Wallet
#
# This script is a Streamlit application that allows the user to:
# - Generate a new Ethereum account instance using mnemonic seed phrase
# - Fetch and display account balance associated with Ethereum account address
# - Calculate total value of Ethereum transaction, including the gas estimate,
#   that pays a Fintech Finder candidate for their work.
# - Digitally sign a transaction that pays a Fintech Finder candidate, and send
#   this transaction to the Ganache blockchain.
########################################################################
# Imports
# crypto_wallet functions
from crypto_wallet import generate_account, get_balance, send_transaction

# Built-in modules
import sys
import os
import platform

# Third-party modules
# Importing Any, Dict, List, and Tuple types from the typing module
from typing import Any, Dict, List, Tuple
from watermark import watermark  # watermark functions
# Streamlit library
import streamlit as st
from dataclasses import dataclass

# Ethereum library
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

################################################################################
# Report Technologies
# prints the python platform and version
print(f'Python Platform: {platform.platform()}')
print(f'Python {sys.version}')

# prints the watermark for the code
print(watermark())
print(watermark(iversions=True, globals_=globals()))
###############################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates
# A single Ether is currently valued at 1348.67

candidate_database: Dict[str, List[Tuple[str, str, float, float, str]]] = {
    'billie': ('billie', '0x892D769cd188Af70E36694d77204d5D4c2084F44', '5.0', 1.45, "Images/billie.png"),
    'Jo': ('Jo', '0x22eF95a42FbA54974cF6b16eB5C300eC936a60B3', '4.7', .19, "Images/jo.jpeg"),
    'Lane': ('Lane', '0x3f6FCb8B5b20DE75DC529CDc30c54385bFCd7A0c', '4.3', .20, "Images/lane.jpeg"),
    'Ash': ('Ash', '0x071Bfb085fF10cD4964BfC2502F750E47994D29a', '4.2', .33, "Images/ash.jpeg"),
    'Kendall': ('Kendall', '0x00172D7420586551E5A6a67Dd1e40a2C21e43B52', '4.1', .16, "Images/kendall.jpeg"),
    'William': ['William', '0x1C855F0FCad0E3d58Cc4677955BaA8af74AF288d', '2.1', .11, 'Images/william.jpeg']
}

# A list of the FinTech Finder candidates' first names
people: List[str] = ['billie', 'Ash', 'Lane', 'Jo', 'Kendall', 'William']


def get_people() -> None:  # do NOT put 'w3' as argument
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write('Name: ', db_list[number][0])
        st.write('Ethereum Account Address: ', db_list[number][1])
        st.write('FinTech Finder Rating: ', db_list[number][2])
        st.write('Hourly Rate per Ether: ', db_list[number][3], 'eth')
        st.text(' \n')


"""
def get_people() -> None:
    
    # Iterate through the list of candidates, and for each one, retrieve the corresponding information from 
    # the candidate_database and display it using the streamlit library.
    
    for person in people:
        candidate_info = candidate_database[person]
        st.image(candidate_info[4], width=200)
        st.write('Name: ', candidate_info[0])
        st.write('Ethereum Account Address: ', candidate_info[1])
        st.write('FinTech Finder Rating: ', candidate_info[2])
        st.write('Hourly Rate per Ether: ', candidate_info[3], 'eth')
        st.text(' \n')
"""

# Streamlit Code
# Streamlit application headings
st.markdown('# Fintech Finder!')
st.markdown('## Hire A Fintech Professional!')
st.text(' \n')

# Streamlit Sidebar Code
st.sidebar.markdown('## Client Account Address and Ethernet Balance in Ether')

# Generate a new Ethereum account
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Get the client's Ethereum balance
balance: str = get_balance(w3, account.address)
st.sidebar.write(balance)

# Create a select box for the user to choose a Fintech hire candidate
person: str = st.sidebar.selectbox('Select a Person', people)

# Create an input field for the user to enter the number of hours the candidate worked
hours: float = st.sidebar.number_input('Number of Hours')

st.sidebar.markdown('## Candidate Name, Hourly Rate, and Ethereum Address')

# Identify the Fintech Hire candidate
candidate: str = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the Fintech Finder candidate's hourly rate
hourly_rate: float = candidate_database[person][3]

# Write the Fintech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the Fintech Finder candidate's Ethereum address
candidate_address: str = candidate_database[person][1]

# Write the Fintech Finder candidate's Ethereum address to the sidebar
st.sidebar.write(candidate_address)

st.sidebar.markdown('## Total Wage in Ether')

# Calculate the total wage by multiplying the hourly rate by the number of hours
wage: float = hourly_rate * hours

st.sidebar.write(wage)

if st.sidebar.button('Send Transaction'):
    # Send the transaction and get the transaction hash
    transaction_hash: str = send_transaction(
        w3, account, candidate_address, wage)

    st.sidebar.markdown('#### Validated Transaction Hash')

    st.sidebar.write(transaction_hash)

    st.balloons()
    st.sidebar.success('This is a valid transaction!', icon="✅")

# Display the database of Fintech Finder candidates on the application page
# The function that starts the Streamlit application
get_people()
