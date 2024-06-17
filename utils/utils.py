
def format_price(val):
    return f'{val:.2f}€'.replace('.',',')

def cart_total_qtd(cart):
    return sum([item['qty'] for item in cart.values()])

# def cart_total(cart):
#     return sum([item['qty'] * item['promo_price'] for item in cart.values()])

def cart_total(cart):
    return sum(
        [
            item.get('qty_promo_price')
            if item.get('qty_promo_price')
            else item.get('qty_price')
            for item
            in cart.values()
        ]
    )