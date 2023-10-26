from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
import stripe


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    print('total')

    stripe.api_key = 'sk_test_51N0jQuFkBlj7YTVQc30bCmiuqYva3Hz8k7VdQSapFzMmRIORcUdreYL1wl29uMftCNcBmPC8I7cGVQlyaQfk7DOY00lkDA1ddw'
    intent = stripe.PaymentIntent.create(
            amount=total,
            currency='gbp',
            metadata={'userid':request.user.id }

        )

    

    return render(request, 'payment/home.html', {'client_secret':intent.client_secret})
    


