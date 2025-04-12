#create a function calculate_discount(price, discount_percent)
def calculate_discount(price, discount_percent):
    #calculates the final price after applying a discount.
    if discount_percent >= 20:
        final_price = price * (100-discount_percent)/100
        return final_price
    else:
        return price

#prompt the user to enter the original price of an item and the discount percentage.
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount requested: "))

#Print the final price after applying the discount, or if no discount was applied, print the original price.
print(calculate_discount(price, discount_percent))
