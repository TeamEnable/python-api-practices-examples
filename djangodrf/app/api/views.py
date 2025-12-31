from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from services.payments import create_payment


class PaymentsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        body = request.data
        result = create_payment(
            amount=int(body["amount"]),
            currency=str(body["currency"]),
        )
        return Response(result, status=status.HTTP_200_OK)
