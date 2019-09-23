#Captcha-Solver  
A simple captcha solver in python.  
This project uses PILLOW library for image processing and Google Tesseract-OCR for Optical Character recognition.  
It works on captchas like below:  
![sample 1](https://raw.githubusercontent.com/armooey/Captcha-Solver/master/Demo/11.jpg)  
![sample 1](https://raw.githubusercontent.com/armooey/Captcha-Solver/master/Demo/2.jpg)  
![sample 1](https://raw.githubusercontent.com/armooey/Captcha-Solver/master/Demo/7.jpg)  
![sample 1](https://raw.githubusercontent.com/armooey/Captcha-Solver/master/Demo/9.jpg)  
-------------------------------------------------------------------------------------------------------------  
Before using the code:  
1- Install Google tessract OCR standalone and then install its library by **pip install tesseract**.  
2- Install PILLOW library for Python.  
3- Copy **tessdata** folder to tesseract install location.  
4- Run the code :)))))  
--------------------------------------------------------------------------------------------------------------  
It doesn't have so much accuracy and gives good result half of the times.  
The big problem here is that tesseract doesnt recognize rotated characters.  
Any advise for making it better appreciated.
