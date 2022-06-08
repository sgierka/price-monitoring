# Price monitoring

<sup align = "left"> 
  
   *Status: This app is still in development*
  
</sup>

<p>
A simple program for monitoring the prices of selected products in the Hebe online store. Created with Python and tkinter.
</p>

## List of contents
1. [Project description](#project-description)
3. [Libraries used](#libraries-used)
4. [How to install](#how-to-install)

## Project description
The project was entirely created using Python 3.7.2 and tkinter (GUI).
<p></p>

 <b> Price monitoring </b> is a window application that scrapes the most important information of the selected product from the [Hebe](www.hebe.pl) online store (product name, regular price, sale price, product link) and displays this information on the screen. 
  <p></p>
Ultimately, the application will compare the prices of the added products every day and inform you about the discount, if any. The information will be sent to the e-mail address provided by the user.
In the future more stores will be added i.e Rossman, Natura, Xkom.

#### Libraries used
* tkinter
* requests
* BeautifulSoup

## How to install
1. Download `main.py` and `shops.py`.
2. You should get api key, it works from [Bitly](https://bitly.com/)
3. Add api key in `shops.py` to:

        def ShortenUrl(self):
           type_bitly = pyshorteners.Shortener(api_key='your_api_key')
  
  
  
4. Run `main.py`.

##
