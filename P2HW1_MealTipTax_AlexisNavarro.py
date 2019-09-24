# The user is going to input the Meal, Tip and the Tax.
# Than once the user puts in the information. Fourth line is going to calculate the tip and tax.
# Than the Fifth line is going to print the calculation of the tip and tax and show the user.
# The final line to going to show him the cost of the whole meal.
 # 9/16/2019
 # CTI-110 P2HW1 - Meal Tip Tax Calculator
 # Alexis Navarro

Meal = float(input('How much did the meal cost: ' ))

Tip  = float(input('Tip for server: ' ))

Tax  = float(input('Tax amount:' ))

cost = Tax * Tip

print('This is the calculation for Tax and Tip:',format( cost, '.2f')) 

Total = Meal + Tip + Tax 

print('This is the total cost of the meal, tip and tax:',format( Total, '.2f' ))  

