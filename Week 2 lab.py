#1.)
#Lots of inputs here
fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
street_add = input('Enter your street address: ')
city_name = input('Enter your city name: ')
state_in = input('Enter your state initials: ')
zip_Code = input('Enter your zip code: ')
telePhone = input('Enter your telephone: ')
Cmajor = input('What is your major?: ')

#Who are you?
print(fname, lname)
print(street_add)
print(city_name, state_in, zip_Code)
print(telePhone)
print(Cmajor)
#---------------------------------------------------------------------------------------

#2.)
#Sales predictions
total_sales = float(input('Enter the projected total sales: '))
annual_profit = total_sales * 0.23
print(f'Your projected annual profit will be: {annual_profit}')
#---------------------------------------------------------------------------------------

#3.)
#Converting feet to acres
total_sqft = float(input('Enter the total square feet of land: '))
acres = total_sqft / 43560
print(f'The amount of acres in the tract is {acres:.2f}')
#---------------------------------------------------------------------------------------

#4.)
#Lots of shopping done
item1 = float(input('Enter the price of the first item: '))
item2 = float(input('Enter the price of the second item: '))
item3 = float(input('Enter the price of the third item: '))
item4 = float(input('Enter the price of the fourth item: '))
item5 = float(input('Enter the price of the fifth item: '))

#Equations for totals
subtotal = (item1 + item2 + item1 + item2 + item5)
print(f'Subtotal: {subtotal}')
sales_tax = round(subtotal * 0.07, 2)
print(f'Sales tax: {sales_tax}')
total_price = (subtotal + sales_tax)

#How much are you spending?
print(f'Your total is: {total_price:,.2f}')
#---------------------------------------------------------------------------------------

#5.)
#The distance values and the constant speed 
Speed = 70
Distance6 = Speed * 6
Distance10 = Speed * 10
Distance15 = Speed * 15

#The actual results. I gotta say, I really enjoy using f strings. It makes this much easier to learn.
print(f'The distance the car will travel in 6 hours is: {distance6} miles')
print(f'The distance the car will travel in 10 hours is: {distance10} miles')
print(f'The distance the car will travel in 15 hours is: {distance15} miles')
#---------------------------------------------------------------------------------------

#6.)
#purchases and taxes
total_purchase = float(input('Enter the total purchase value: '))
total_state = total_purchase * 0.05
total_county = total_purchase * 0.025
total_tax = total_state + total_county
total_sum = total_purchase + total_tax
#Amount to pay
print(f'Your purchase subtotal is: {total_purchase:.2f}')
print(f'State sales tax: {total_state:.2f}')
print(f'County sales tax: {total_county:.2f}')
print(f'Total sales tax: {total_tax:.2f}')
print(f'Your purchase total is: {total_sum:.2f}')
#---------------------------------------------------------------------------------------

#7.)
#defining variables
miles_driven = float(input('Enter the amount of miles driven: '))
gallons_of_gas_used = float(input('Enter the amount of gasoline used in gallons : '))
MPG = miles_driven / gallons_of_gas_used
#the total
print(f'The car\'s MPG is: {MPG} miles per gallon')
#---------------------------------------------------------------------------------------

#8.)
#purchases and taxes time
total_food = float(input('Enter the meal cost: '))
total_tip = total_food * 0.18
total_tax = total_food * 0.07
total_sum = total_food + total_tax + total_tip

#More displays
print(f'Cost of the meal: {total_food:,.2f}')
print(f' 18% tip: {total_tip:.2f}')
print(f'Sales tax: {total_tax:.2f}')
print(f'Your total for today\'s visit is: {total_sum:,.2f}')
#---------------------------------------------------------------------------------------
      
#9.)
#The formula
TempC = float(input('Enter the degrees in Celcius: '))
TempF = (1.8 * TempC) + 32
#The output
Print = (f'The temperature is: {TempF} degrees Farenheit'))
#---------------------------------------------------------------------------------------

#10.)
#The question
total_cookie = int(input('How many Cookies do you want to make? ')) 

#The constants
sugar = 1.5 / 48
butter = 1.0 / 48
flour = 2.75 / 48
#the equation
total_sugar = round(sugar * total_cookie, 2)
total_butter = round(butter * total_cookie, 2)
total_flour = round(flour * total_cookie, 2)

#The statement
print(f"You need {total_sugar} cups of sugar, {total_butter} cups of butter, and {total_flour} cups of flour to make {total_cookie} cookies.")
#---------------------------------------------------------------------------------------

#11.)
#Counting big cats
total_lion = int(input('Enter the total number of lions in the exhibit: '))
total_tiger = int(input('Enter the total number of tigers in the exhibit: '))
total_cat = total_lion + total_tiger

#Getting percentages
lionperc = (total_lion / total_cat) 
tigerperc = (total_tiger / total_cat)

#The zoo has:
print(f'The percentage of lions in the exhibit is: {lionperc:.0%}')
print(f'The percentage of tigers in the exhibit is: {tigerperc:.0%}')
#---------------------------------------------------------------------------------------

#12.
#Initial purchase
stockbuy = 2000 * 40
comm1 = stockbuy * .03
total1 = stockbuy + comm1
print(f'Joe spent a total of {total1:,.2f} buying stocks')

#cashing out
stocksell = 2000 * 42.75
comm2 = stocksell * .03
total2 = stocksell + comm2
totalmoney = total2 - total1

#Amount gained?
print(f'After selling the stock Joe earned {total2:,.2f}')

#Was this a good or bad move?
print(f'This ordeal resulted in: {totalmoney:,.2f}')
if totalmoney > 0: print('Joe made money!')
#---------------------------------------------------------------------------------------

#13.)
#The variables
row_length = float(input('Enter the lenght of the row in feet: '))
end_post = float(input('Enter the amount of space used by the end-post assembly in feet: '))
space_betw = float(input('Enter the amount of space between the vines in feet: '))
vinenumber = (row_length - (2 * end_post)) / space_betw

#How many grapevines
print(f'The amount of grapevines that can fit in this row is: {vinenumber:.0f}') 
#---------------------------------------------------------------------------------------

#14.)
#Bank account variables
money_start = float(input('Enter the amount of money originally deposited into the account:> '))
inter_inp = float(input('Enter the annual interest rate percentage as a whole number:> '))
compound = float(input('Enter the number of times per year the interest is compounded: '))
years = float(input('Enter amount of years the account will collect interest: '))
# I asked them to give me a whole number so there's no scenario where a person would 
# input a percentage or whole number and mess with the equation
# And so we have this int_real variable that turns it into a decimal
# was this a good idea or could it have been done better?
int_real = inter_inp / 100

account_total = money_start * ( 1 + int_real / compound) ** (compound * years)

print(f'After {years} year(s) the account will have ${account_total:,.2f}')
