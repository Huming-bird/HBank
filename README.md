## HBank Console Application

# Description
This project aims at creating a mimic bank application which allows users perform basic
banking transactions such as Deposit, Transfer, Withdraw.
To create this, the following tools were used:

*	Python			-	main programming language
*	Ubuntu Sandbox[Vim]	-	development environment
*	Flask			-	for creating and managing apis
*	Fabric			-	for 

Libraries include 
*	uuid	-	for setting unique customer IDs
*	random	-	for generating random 10digit account numbers
*	datetime-	for setting timestamps

# How to Use this application
* Fork this project to your repository
* Clone the project to your local machine
* execute the console application located in the parent directory (HBank/) either by
	./console.py, or python3 console, or python console.
* Functions to use include:
<ol>
> create	-	creates a bank customer <br>
> deposit	-	deposits funds to a customer account <br>
> withdraw	-	withdraw money from a customer's account <br>
> transfer	-	transfer money from a customer to another customer <br>
> all		-	shows all customers available in the bank's database <br>
> show		-	shows details about a particular customer <br>
> destroy	-	deletes a customer from the database <br>
> update	-	updates customer information <br>
</ol>

N.B:	More details about use cases can be found in the tests dir

