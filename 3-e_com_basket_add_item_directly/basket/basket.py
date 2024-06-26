
class Basket():

    """
        A base basket class, providing some default behaviours that 
        can be inherited or overrided, as necessary
    """

    def __init__(self, request):
        self.session = request.session                   
        basket = self.session.get('skey')
        print(basket)
           

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

       
    def add(self, product, qty):
        """
            Adding and updating the users basket session data 
        """
        product_id = product.id

        # product_id basket da bo'lsa qo'shmaydi chunki mantiqqa tug'ri kelmaydi.
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty':int(qty)}
            
        self.session.modified = True
    
   