from rest_framework.views import APIView
import stripe
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class BuyView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

        session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment'
    )

        data = session.id
        return Response(status=status.HTTP_200_OK, data=data)
