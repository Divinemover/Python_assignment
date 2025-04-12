#create a function calculate_discount(price, discount_percent)
def calculate_discount(price, discount_percent):
    #calculates the final price after applying a discount.
    if discount_percent < 20:
        final_price = price * (100-discount_percent)/100
        return final_price
    else:
        return price

price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount requested: "))
print(calculate_discount(price, discount_percent))
