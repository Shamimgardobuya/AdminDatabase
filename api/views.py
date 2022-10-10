from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from wallet.models import Account, Customer, Notifcation, Receipt, Transaction, Walletb,Card,Loan
from .serializers import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer,NotificationSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()  #request info
    serializer_class=CustomerSerializer   #type of Serializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset=Walletb.objects.all()
    serializer_class=WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):  #class based view working with crud operations 
    queryset=Account.objects.all().order_by("customer")
    serializer_class=AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=Receipt.objects.all()
    serializer_class=ReceiptSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notifcation.objects.all()
    serializer_class=NotificationSerializer








