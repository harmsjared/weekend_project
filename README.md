# Weekend_Project
A weekend project from August 2023. (This took more than 4 hours, but less than 40.) 

## I. Instructions
1. Save or clone the project folder to a location on your computer.
2. In terminal, navigate to the folder containing the Python Project.
3. To begin the program, type 'python main.py'.

## II. Design_Decisions
The goal of designing this program was to make it easy to understand and efficient by following the "DRY",
(Don't Repeat Yourself) principle and emphasizing the "separation of concerns" concept. Similar to the 
AOE (Activity-On-Edge) method, the program was split into distinct sections that address different key 
aspects, like managing messages and handling guest functionalities.

To ensure reasonable time efficiency, we completely removed nested "for loops." None of the functions in 
the program exceed O^n linear efficiency (contain nested functions), allowing for more optimal scalability.

Lastly, the most easy to grasp variables names were used, both for reading purposes and to allow for fluid creation 
of new variables.

## III. Language_Choice
I opted to use Python as my programming language in this project because I had not used Python for OOP, prior to. 
I thought it would be a great learning experience, and it proved to be quite the challenge, as my prior OOP experience 
had mostly been through JS, TS, and Java. 

## IV. Troubleshooting
To address issues in the program and handle unusual situations, I took simple precautions to verify the existence
of data types and variables before moving forward with functions. On a practical level, I ran the program repeatedly
using numerous variables, ensuring its stability even when faced with unusual situations. 

## IV. Future_Plans 
There are several ways to make this program better. Firstly, I could make better use of classes to fully embrace 
Object-Oriented Programming (OOP) principles. For instance, I could create a "guest" class that becomes an object 
instantiated within the main program. 

Secondly, there are specific data structures that can significantly improve the efficiency of certain parts of the program, 
reducing time complexity to constant time (O(1)). For example, instead of iterating through objects, we can organize 
dictionaries based on room numbers. This eliminates the need to cycle through objects until we find the desired one.