from django.test import TestCase
from account.models import Account
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure
import datetime

class TestModels(TestCase):
    
    def test_constructor_for_usl_model(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_usl = UnCertifiedSickLeave(usl_officer_id=user, usl_date=test_date, reason_for_usl="User Sick")
        test_usl.save()
        
        self.assertEqual(test_usl.usl_officer_id, user)
        self.assertEqual(test_usl.usl_date, test_date)
        self.assertEqual(test_usl.reason_for_usl, "User Sick")
        self.assertFalse(test_usl.usl_checked_by_validator)
        self.assertFalse(test_usl.usl_accepted)
        self.assertIsNone(test_usl.reason_usl_rejected)
        
    def test_constructor_for_fm_model(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_fm = ForceMajeure(fm_officer_id=user, fm_date=test_date, reason_for_fm="User Force Majeure")
        test_fm.save()
        
        self.assertEqual(test_fm.fm_officer_id, user)
        self.assertEqual(test_fm.fm_date, test_date)
        self.assertEqual(test_fm.reason_for_fm, "User Force Majeure")
        self.assertFalse(test_fm.fm_checked_by_validator)
        self.assertFalse(test_fm.fm_accepted)
        self.assertIsNone(test_fm.reason_fm_rejected)
        
    def test_constructor_for_csl_model(self):
        user = Account()
        user.save()
        test_start_date = datetime.datetime(2021, 3, 1)
        test_end_date = datetime.datetime(2021, 3, 6)
        test_csl = CertifiedSickLeave(csl_officer_id=user, first_day_of_cert=test_start_date, last_day_of_cert=test_end_date)
        test_csl.save()
        
        self.assertEqual(test_csl.csl_officer_id, user)
        self.assertEqual(test_csl.first_day_of_cert, test_start_date)
        self.assertEqual(test_csl.last_day_of_cert, test_end_date)
        self.assertFalse(test_csl.csl_image)
        self.assertFalse(test_csl.csl_checked_by_validator)
        self.assertFalse(test_csl.csl_accepted)
        self.assertIsNone(test_csl.reason_csl_rejected)
        
    def test_usl_as_string(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_usl = UnCertifiedSickLeave(usl_officer_id=user, usl_date=test_date, reason_for_usl="User Sick")
        test_usl.save()
        
        self.assertEqual(str(test_usl.usl_officer_id) + " taken U.S.L. on " + str(test_usl.usl_date), str(test_usl))
        
    def test_fm_as_string(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_fm = ForceMajeure(fm_officer_id=user, fm_date=test_date, reason_for_fm="User FM")
        test_fm.save()
        
        self.assertEqual(str(test_fm.fm_officer_id) + " took F.M. on " + str(test_fm.fm_date), str(test_fm))
    
    def test_csl_as_string(self):
        user = Account()
        user.save()
        test_start_date = datetime.datetime(2021, 3, 1)
        test_end_date = datetime.datetime(2021, 3, 6)
        test_csl = CertifiedSickLeave(csl_officer_id=user, first_day_of_cert=test_start_date, last_day_of_cert=test_end_date)
        test_csl.save()
        
        self.assertEqual(str(test_csl.csl_officer_id) + " : " + str(test_csl.first_day_of_cert) + " to " + str(test_csl.last_day_of_cert), str(test_csl))
    
    
    
    