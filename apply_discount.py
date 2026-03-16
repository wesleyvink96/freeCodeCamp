price = int(input('Enter the price: '))
discount = int(input('Enter the discount percentage: '))


def apply_discount(price, discount):
    # 1. Check of price een getal is
    if type(price) not in [int, float]:
        return "The price should be a number"
    
    # 2. Check of discount een getal is
    if type(discount) not in [int, float]:
        return "The discount should be a number"
    
    # 3. Check of price > 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # 4. Check of discount tussen 0 en 100 ligt
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # 5. Als alles klopt: bereken de nieuwe prijs
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price
apply_discount(100, 20)
print(apply_discount(price, discount))