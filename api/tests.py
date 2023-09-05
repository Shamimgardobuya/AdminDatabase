from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from wallet.models import Loan
import datetime
import logging
logger = logging.getLogger(__name__)

class ClientSetTests(APITestCase):
    def test_add_loan(self):
        logger.debug("Adding new loan request")
        my_loan = {
        'loan_amount':'5000',
        'loan_type' :"Mshwari",
        'interest_rate' : '3',
        'date': '2021-09-1' 
        }
        # my_loan.save()
        try:
            url = 'http://127.0.0.1:8000/api/loans/loan_request/' %reverse ('loan-view')
            logger.debug('Sending TEST data to url: %s, my_loan: %s' %(url,my_loan))
            response = self.client.post(url,my_loan, format = 'json')
            
            logger.debug('Testing status code response: %s, loan: %d'%(response.json(), response.status_code))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            logger.debug("Testing to ensure requested loan was added to test db")
            self.assertEqual(Loan.objects.count(),1)
            logger.debug("Testing loans details")
            loan_object = Loan.objects.get()
            self.assertEqual(loan_object.loan_amount,5000)
            self.assertEqual(loan_object.loan_type,"Mshwari")
            self.assertEqual(loan_object.interest_rate,3)
            self.assertEqual(loan_object.date,datetime.date(2021, 9, 1))
            logger.debug("Successfully created Loan request")




        except:
            logger.debug("Value error,expecting json object")
    def test_edit_loan(self):
        #Arrange, Act, Assert
        #Have data wishing to be changed, or the one posted
        #call the put function
        #check the http status returned
        try:
            url =  'http://127.0.0.1:8000/api/loans/%s1/' %reverse ('all_loans')
            logger.debug('Sending TEST data to url:%s, data:' %url)
            data = {
                'loan_amount':'7000',
                'loan_type' :"Mshwari",
                'interest_rate' : '3',
                'date': '2021-09-1' 
            }
            response = self.client.put(url,data, format = 'json')
            json = response.json()
            logger.debug('Testing to see if status code is correct')
            self.assertEqual(response.status_code,status.HTTP_200_OK)
            logger.debug("Testing loans details")
            loan_object = Loan.objects.get()
            self.assertEqual(loan_object.loan_amount,7000)
            self.assertEqual(loan_object.loan_type,"Mshwari")
            self.assertEqual(loan_object.interest_rate,3)
            self.assertEqual(loan_object.date,datetime.date(2021, 9, 1))
            logger.debug("Successfully updated Loan request")
        except:
            logger.debug("Value error, ensure it is in Json form")


# Create your tests here.
#test post loan request
#test account request
#Arrange, Act, Assert.
#have dummy data for posting,
#call the request url if it works
#Assert the http response for good posting
#using a logger

