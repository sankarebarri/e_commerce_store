class Basket():
    '''
    A base Basket class, providing some default behaviors
    that can be inherited or overrided as necessary.
    '''

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        '''
        Adding or updating the users basket session data
        '''
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {
                'price': str(product.price),
                'quantity': product_qty
            }
        
        self.session.modified = True

    def __len__(self):
        '''
        Get the basket data and count the quantity of the items
        '''
        return sum(item['quantity'] for item in self.basket.values())
