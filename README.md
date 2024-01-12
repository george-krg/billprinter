
# Title: 
Bill Printer
# Estimated Time:
1h 30 min for tasks 1,2
2h for task 3
# Difficulty Level:
Beginner for tasks 1,2
Intermediate for task 3
# Prerequisites:
2.2 Python Basics - Texts for task 1

2.11 Python Basics - OOP Advanced for task 2

2.15 Python Basics - Input-Output for task 3
# Topics:
Script Execution, String variables, print command, Dates, Function call, classes, input,files. 
# Scenario:
In this project, you will create a bill generator application that can print out bills with specific formatting. The project will be implemented in three versions. In the first version, you will write a script to print out a hardcoded bill with a specific line length. In the second version, you will create a function that accepts a list of products, and the function will be called by the script to print out the bill. In the third version the user will first select the products form a list of availabe products that are read from a file. After selecting the desired ones to the shopping bag he will proceed to checkout and print the receipt.

## Version 1:

1. Write a script that can print the following bill with a specific line length of 50 characters:

```
**************************************************
*               Company Name, Inc.               *
*               Xxx Roadname St.                 *
*               Areaname, Xx                     *
*================================================*
*       Product Name    Product Price            *
*       Item 1          $49.95                   *
*       Item 2          $579.99                  *
*       Item 3          $124.89                  *
*================================================*
*                       Total                    *
*                       $754.83                  *
*================================================*
*                                                *
*       Thanks for shopping with us today!       *
*                                                *
**************************************************
```
2. Use hardcoded company and product data to generate the bill.

## Version 2:

1. Define a Product class that includes a product description and price.

2. Create a function that accepts a list of Product objects and generates the bill. The bill should include the current date and the total price of all the products.

3. The bill should have the following format:

```
**************************************************
*               Company Name, Inc.               *
*               Xxx Roadname St.                 *
*               Areaname, Xx                     *
*================================================*
*       Product Name    Product Price            *
*       Item 1          $49.95                   *
*       Item 2          $579.99                  *
*       Item 3          $124.89                  *
*================================================*
*                       Total                    *
*                       $754.83                  *
*================================================*
*                                                *
*       Thanks for shopping with us today!       *
*                                                *
*               11/05/2023                       *
**************************************************
```

4. Call the function with a hardcoded list of products and print the bill.

## Version 3:

1. Write a script that reads a file and displays a list of items with their prices. The user has the ability to select sequentially any desired items and place them in the shopping cart. A menu will be provided to add items, checkout, or exit. When checkout is selected the bill will be printed as in version 2.



