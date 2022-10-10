from django.urls import path,include
from rest_framework import routers
from wallet.models import Card, Customer, Notifcation, Receipt, Transaction, Walletb,Account,Loan
from .views import AccountViewSet, CardViewSet, CustomerViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet,LoanViewSet,NotificationViewSet

router=routers.DefaultRouter()  #fetch resource dynamically
router.register(r'customers',CustomerViewSet,basename=Customer)
router.register(r'wallet',WalletViewSet,basename=Walletb)
router.register(r'accounts',AccountViewSet,basename=Account)
router.register(r'cards/',CardViewSet,basename=Card)
router.register(r'transactions/',TransactionViewSet,basename=Transaction)
router.register(r'loans/',LoanViewSet,basename=Loan)
router.register(r'receipts/',ReceiptViewSet,basename=Receipt)
router.register(r'notifications/',NotificationViewSet,basename=Notifcation)








urlpatterns=[
      path("",include(router.urls)),
]



