![blockchain](Images/blockchain.png)
# **Columbia University Engineering, New York FinTech Bootcamp** 
# **August 2022 Cohort**
# **Module 19, Challenge - building a 'Fintech Finder' application to identify fintech professionals from a candidate list, hire them, and pay them**


Objective - to simulate fintech engineer working at a a major global bank. 

Scenario - Fintech Finder’s lead developer, tasked with integrating the Ethereum blockchain network into an application to enable customers to pay fintech professionals whom they hire with cryptocurrency. 
![blockchain_pay](Images/blockchain_pay.png)

### Product 

Ganache account tab (index 0)
![ganache](Images/ganache_index.png)
App page
![app](Images/fintech_finder.png)
Billable hours selected = 7
![app](Images/billable.png)
Transaction sent and confirmed valid
![app](Images/paid.png)
Ganache index account subtracted, Fintech professional's account added
![app](Images/ganache_paid.png)
Fintech Finder application shows deduction
![app](Images/deducted.png)
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
git clone git@github.com:Billie-LS/find_yo_tech_pro_fin.git
```

---
## **Usage**

In the terminal, navigate to the project folder where you've installed the application; run the streamlit application by using `streamlit run fintech_finder.py`:

```python
> streamlit run fintech_finder.py 

```
___

## **Version control**

Version control can be reviewed at:

```python
https://github.com/Billie-LS/find_yo_tech_pro_fin
```

[repository](https://github.com/Billie-LS/find_yo_tech_pro_fin)


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

[st.success](https://docs.streamlit.io/library/api-reference/status/st.success)

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



