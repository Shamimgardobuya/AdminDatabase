from datetime import datetime
from random import choices
from django.db import models

class Customer(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    address=models.TextField()
    email= models.EmailField()
    phone_number=models.IntegerField()
    choice_g=(
        ("Male","Male"),
        ("Female","Female")
    )
    gender= models.CharField(max_length=10,choices=choice_g)
    nationality=models.CharField(null=True,max_length=24)
    profile_picture=models.ImageField(null=True,blank=True,upload_to="images/")
    age= models.PositiveBigIntegerField()
    def __str__(self):
         return str(self.first_name)

class Account(models.Model):
    account_number= models.PositiveIntegerField()
    customer=models.ForeignKey(to=Customer,on_delete = models.CASCADE,null=True)
    balance=models.IntegerField()
    pin=models.PositiveSmallIntegerField()
    def __str__(self):
            return str(self.customer)
             

class Walletb(models.Model):
    customer=models.OneToOneField(null=True,on_delete=models.CASCADE,to=Customer)
    currency_supported=models.CharField(max_length=27)
    wallet_id=models.IntegerField(null=True)


    
   

class Transaction(models.Model):
    walletb=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Walletb)
    origin_account=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Account,related_name="account_w")
    destination_account=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Account,related_name="account_x")
    transaction_code=models.CharField(max_length=14)
    transaction_charge=models.IntegerField()
    transaction_amount=models.IntegerField()
    transaction_date=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.walletb)

class Card(models.Model):
    card_number=models.IntegerField()
    expiry_date=models.DateTimeField(default=datetime.now)
    card_type_choices=(
        ('Debit','debit'),
        ('credit','credit')


    )
    card=models.CharField(max_length=6,choices=card_type_choices,null=True)
    card_security_code=models.CharField(max_length=6)
    issuer=models.CharField(max_length=33)
    walletb=models.ForeignKey(on_delete=models.CASCADE,to=Walletb)


class ThirdParty(models.Model):
    account_a=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="acc",null=True)
    walletb=models.ForeignKey(Walletb,on_delete=models.CASCADE,related_name="wall",null=True)
    date_of_issue=models.DateTimeField(default=datetime.now)
    amount=models.BigIntegerField(null=True)


class Notifcation(models.Model):
    message=models.CharField(max_length=10000)
    title=models.CharField(max_length=900)
    date=models.DateTimeField(default=datetime.now)
    state=(
        ('active','active'),
        ('passive','passive')
    )
    status=models.CharField(max_length=7,choices=state,null=True)
    customer=models.ForeignKey(on_delete=models.CASCADE,to=Customer)
class Receipt(models.Model):
    receipt_date=models.DateTimeField(default=datetime.now)
    receipt_number=models.CharField(max_length=6)
    receipt_file=models.FileField()  
    transaction=models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    def  __str__(self):
        return self.transaction

class Loan(models.Model):
    loan_amount=models.BigIntegerField()
    loan_typ=(
        ('Faulu','Mshwari'),
        ('Tala','fuliza')
    )
    loan_type=models.CharField(max_length=10,choices=loan_typ,null=True)
    interest_rate=models.SmallIntegerField()
    date=models.DateTimeField(default=datetime.now)
    loan_Id=models.CharField(max_length=30)
    walletb=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Walletb)
    loan_term=models.IntegerField()

    
class Reward(models.Model):
     date=models.DateTimeField(default=datetime.now)
     recepient=models.ForeignKey(on_delete=models.CASCADE,to=Customer)
     points=models.IntegerField(null=True)







        



        


# Create your models here.
