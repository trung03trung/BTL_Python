from .cart import Cart

def cart_total(request):
	if request.user.is_authenticated:
		cart = Cart(request)
		total_bill = 0.0
		for key,value in request.session['cart'].items():
			total_bill = total_bill + (float(value['price']) * value['quantity'])+30000
		return {'cart_total' : total_bill} 
	else:
		return {'cart_total' : 0} 
def cart_total_amount(request):
	if request.user.is_authenticated:
		cart = Cart(request)
		total_bill = 0.0
		for key,value in request.session['cart'].items():
			total_bill = total_bill + (float(value['price']) * value['quantity'])
		return {'cart_total_amount' : total_bill} 
	else:
		return {'cart_total_amount' : 0} 