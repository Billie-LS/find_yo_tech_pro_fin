![blockchain](images/blockchain.png)
# **Columbia University Engineering, New York FinTech Bootcamp** 
# **August 2022 Cohort**
# **Module 18, Challenge - building a blockchain-based ledger system, complete with a user-friendly web interface**


Objective - to simulate fintech engineer working at a a major global bank. 

Scenario - As the lead developer of the decentralized finance team, build a blockchain-based ledger system, complete with a user-friendly web interface. This ledger should allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger. 
![decentralizedledger](images/decentledger.png)
Product - 

>* Create a new data class named Record. This class will serve as the blueprint for the financial transaction records that the blocks of the ledger will store.
>* Change the existing Block data class by replacing the generic data attribute with a record attribute that’s of type Record. 
>* Create additional user input areas in the Streamlit application. These input areas should collect the relevant information for each financial record that you’ll store in the PyChain ledger. 
>* Create additional user input areas in the Streamlit application. These input areas should collect the relevant information for each financial record that you’ll store in the PyChain ledger.

![app](images/app.png)
![app](images/multipleblocks.png)
![app](images/validchain.png)
___

## **Technologies**
___


### **Dependencies**

This project leverages Python version 3.9.13 packaged by conda-forge | (main, May 27 2022, 17:01:00) with the following packages:


* [sys](https://docs.python.org/3/library/sys.html) - module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

* [os](https://docs.python.org/3/library/os.html) - module provides a portable way of using operating system dependent functionality.

* [platform](https://www.geeksforgeeks.org/platform-module-in-python/) - used to retrieve as much possible information about the platform on which the program is being currently executed.

* [watermark](https://pypi.org/project/watermark/) - An IPython magic extension for printing date and time stamps, version numbers, and hardware information.

* [streamlit](https://pypi.org/project/streamlit/) - an all python, free, open source module that enables rapid transformation of data scripts into shareable web apps.

* [dataclasses](https://docs.python.org/3/library/dataclasses.html) - provides a decorator and functions for automatically adding generated special methods.

* [typing](https://docs.python.org/3/library/typing.html) - provides runtime support for type hints.

* [datetime](https://docs.python.org/3/library/datetime.html) - module supplies classes for manipulating dates and times.

* [pandas](https://pandas.pydata.org/docs/) - software library written for the python programming language for data manipulation and analysis.

* [hashlib](https://pypi.org/project/hashlib/) - Secure hash and message digest algorithm library.

___

### **Hardware used for development**

MacBook Pro (16-inch, 2021)

    Chip Appple M1 Max
    macOS Venture version 13.0.1

### **Development Software**

Homebrew 3.6.11

    Homebrew/homebrew-core (git revision 01c7234a8be; last commit 2022-11-15)
    Homebrew/homebrew-cask (git revision b177dd4992; last commit 2022-11-15)

Python Platform: macOS-13.0.1-arm64-arm-64bit

    Python version 3.9.15 packaged by conda-forge | (main, Nov 22 2022, 08:52:10)
    Scikit-Learn 1.1.3
    pandas 1.5.1
    Numpy 1.21.5

pip 22.3 from /opt/anaconda3/lib/python3.9/site-packages/pip (python 3.9)


git version 2.37.2

---
## *Installation of application (i.e. github clone)*

In the terminal, navigate to directory where you want to install this application from the repository and enter the following command

```python
git clone git@github.com:Billie-LS/de_cent_fin_chain_my_block.git
```

---
## **Usage**

In the terminal, navigate to the project folder where you've installed the application; run the streamlit application by using `streamlit run pychain.py`:

```python
> streamlit run pychain.py 

```
___

## **Version control**

Version control can be reviewed at:

```python
https://github.com/Billie-LS/de_cent_fin_chain_my_block
```

[repository](https://github.com/Billie-LS/de_cent_fin_chain_my_block)


___

### **Author**

Loki 'billie' Skylizard
    [LinkedIn](https://www.linkedin.com/in/l-s-6a0316244)
    [@GitHub](https://github.com/Billie-LS)

### **BootCamp lead instructor**

Vinicio De Sola
    [LinkedIn](https://www.linkedin.com/in/vinicio-desola-jr86/)
    [@GitHub](https://github.com/penpen86)


### **BootCamp teaching assistant**

Santiago Pedemonte
    [LinkedIn](https://www.linkedin.com/in/s-pedemonte/)
    [@GitHub](https://github.com/Santiago-Pedemonte)

___

### **Additional references and or resources utilized**

[Open AI](https://openai.com/blog/chatgpt/)

[st.success](https://docs.streamlit.io/library/api-reference/status/st.success)

[st.warning](https://docs.streamlit.io/library/api-reference/status/st.warning)

___
## **License**

MIT License

Copyright (c) [2022] [Loki 'billie' Skylizard]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



