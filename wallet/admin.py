from django.contrib import admin

from .models import Customer
from .models import Account
from .models import Walletb
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notifcation
from .models import Receipt
from .models import Loan
from .models import Reward



class CustomerAdmin(admin.ModelAdmin):
     list_display=('first_name','last_name','age','email')
     search_fields=('first_name','last_name')
admin.site.register(Customer,CustomerAdmin)
class AccountAdmin(admin.ModelAdmin):
     list_display=('account_number',Customer,'pin')
     search_fields=('account_number',Customer,'pin')
admin.site.register(Account,AccountAdmin)
class WalletbAdmin(admin.ModelAdmin):
     list_display=(Customer,'wallet_id')
     search_fields=(Customer,'wallet-id')
admin.site.register(Walletb,WalletbAdmin)
class TransactionAdmin(admin.ModelAdmin):
     list_display=("transaction_charge","transaction_code")
     search_fields=("transaction_charge",'transaction_code')
admin.site.register(Transaction,TransactionAdmin)
class CardAdmin(admin.ModelAdmin):
     list_display=('card_number',Walletb)
     search_fields=('card_number',Walletb)
admin.site.register(Card,CardAdmin)
class ThirdpartyAdmin(admin.ModelAdmin):
     list_display=('walletb','date_of_issue')
     search_fields=('walletb','date_of_issue')
admin.site.register(ThirdParty,ThirdpartyAdmin)
class NotificationAdmin(admin.ModelAdmin):
     list_display=('title','status',Customer)
     search_fields=('title','status',Customer)
admin.site.register(Notifcation,NotificationAdmin)
class ReceiptAdmin(admin.ModelAdmin):
     list_display=('receipt_number','receipt_date',Transaction)
     search_fields=('receipt_number','receipt_date',Transaction)
admin.site.register(Receipt,ReceiptAdmin)
class LoanAdmin(admin.ModelAdmin):
     list_display=('loan_Id','loan_term',Walletb)
     search_fields=('loan_Id','loan_term',Walletb)
admin.site.register(Loan,LoanAdmin)
class RewardAdmin(admin.ModelAdmin):
     list_display=('date','points',Customer)
     search_fields=('date','points',Customer)
admin.site.register(Reward,RewardAdmin)



# admin.site.register(Account)
# admin.site.register(Customer,CustomerAdmin)
# admin.site.register(Walletb,WalletbAdmin)
# admin.site.register(Transaction,TransactionAdmin)
# admin.site.register(Card,CardAdmin)
# admin.site.register(ThirdParty,ThirdpartyAdmin)
# admin.site.register(Notifcation,NotificationAdmin)
# admin.site.register(Receipt,ReceiptAdmin)
# admin.site.register(Loan,LoanAdmin)
# admin.site.register(Reward,RewardAdmin)