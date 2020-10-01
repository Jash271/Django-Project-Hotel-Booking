# Hotel Booking Application

A hotel booking app written in Django (v2.2.4) with sqlite as DB engine. 

## Install and Run

	# Clone repository
	$ git clone https://github.com/Jash271/Django-Project-Hotel-Booking
     
	# Install necessary required packages
	$ pip3 install -r requirements.txt 

	# Apply migrations by running
	$ python3 manage.py migrate

	# Run app locally
	$ python3 manage.py runserver

	# Quit the server with CONTROL-C

## Usage

Available room types are listed on index page along with their maximum capacity and room codes. 

By clicking 'Book', user is redirected to reservation page.

During booking user is prompted to enter:
 - first name 
 - aadhar number 
 - number of children
 - number of adults 
 - number of nights
 - check-in date
 - email

 Razorpay is listed as payment option.


 



