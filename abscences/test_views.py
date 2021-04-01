from django.test import TestCase
from django.contrib.auth.models import AbstractBaseUser
from django.shortcuts import get_object_or_404
from account.models import Account
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure
import datetime
import json

class LoggedInTestCase(TestCase):

    def setUp(self):
        user = Account.objects.create_user(email='test_user@email.com', username='test_user', firstname='John', lastname='TestUser', password='fake_pass')
        self.client.login(email='test_user@email.com', password='fake_pass')


class TestViews(LoggedInTestCase):
    
    def test_get_abscences_page(self):
        page = self.client.get("/abscences/abscences_page/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "abscences_page.html")
        
    def test_submit_csl(self):
        page = self.client.get("/abscences/submit_csl/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "submit_csl.html")
        
    def test_view_csl_application(self):
        user = Account()
        user.save()
        test_start_date = datetime.datetime(2021, 3, 1)
        test_end_date = datetime.datetime(2021, 3, 6)
        test_csl = CertifiedSickLeave(csl_officer_id=user, first_day_of_cert=test_start_date, last_day_of_cert=test_end_date)
        test_csl.save()

        page = self.client.get("/abscences/{0}/view_csl_application/".format(test_csl.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_csl_application.html")
        
    def test_edit_csl(self):
        user = Account()
        user.save()
        test_start_date = datetime.datetime(2021, 3, 1)
        test_end_date = datetime.datetime(2021, 3, 6)
        test_csl = CertifiedSickLeave(csl_officer_id=user, first_day_of_cert=test_start_date, last_day_of_cert=test_end_date)
        test_csl.save()

        page = self.client.get("/abscences/{0}/edit_csl/".format(test_csl.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_csl_application.html")
        
    def test_get_view_csl_page_for_csl_that_does_not_exist(self):
        page = self.client.get("/issues/{1}/view_csl_application/")
        self.assertEqual(page.status_code, 404)
        
    def test_submit_usl(self):
        page = self.client.get("/abscences/submit_usl/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "submit_usl.html")
        
    def test_view_usl_application(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_usl = UnCertifiedSickLeave(usl_officer_id=user, usl_date=test_date, reason_for_usl="User Sick")
        test_usl.save()

        page = self.client.get("/abscences/{0}/view_usl_application/".format(test_usl.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_usl_application.html")
        
    def test_edit_usl(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_usl = UnCertifiedSickLeave(usl_officer_id=user, usl_date=test_date, reason_for_usl="User Sick")
        test_usl.save()

        page = self.client.get("/abscences/{0}/edit_usl/".format(test_usl.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_usl_application.html")
        
    def test_get_view_usl_page_for_usl_that_does_not_exist(self):
        page = self.client.get("/issues/{1}/view_usl_application/")
        self.assertEqual(page.status_code, 404)
        
    def test_submit_fm(self):
        page = self.client.get("/abscences/submit_fm/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "submit_fm.html")
        
    def test_view_fm_application(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_fm = ForceMajeure(fm_officer_id=user, fm_date=test_date, reason_for_fm="User Sick")
        test_fm.save()

        page = self.client.get("/abscences/{0}/view_fm_application/".format(test_fm.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_fm_application.html")
        
    def test_edit_fm(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_fm = ForceMajeure(fm_officer_id=user, fm_date=test_date, reason_for_fm="User Sick")
        test_fm.save()

        page = self.client.get("/abscences/{0}/edit_fm/".format(test_fm.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_fm_application.html")
        
    def test_get_view_fm_page_for_fm_that_does_not_exist(self):
        page = self.client.get("/issues/{1}/view_fm_application/")
        self.assertEqual(page.status_code, 404)
        
    def test_view_staff_sick_leave_applications(self):
        page = self.client.get("/abscences/view_staff_sick_leave_applications/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "staff_sick_leave_submissions.html")
        
    def test_view_my_sick_leave(self):
        page = self.client.get("/abscences/view_my_sick_leave/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "my_sick_leave.html")
        
    def test_reject_csl(self):
        user = Account()
        user.save()
        test_start_date = datetime.datetime(2021, 3, 1)
        test_end_date = datetime.datetime(2021, 3, 6)
        test_csl = CertifiedSickLeave(csl_officer_id=user, first_day_of_cert=test_start_date, last_day_of_cert=test_end_date)
        test_csl.save()
        
        page = self.client.get("/abscences/{0}/reject_csl/".format(test_csl.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reject_csl.html")
        
    def test_reject_usl_page(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_usl = UnCertifiedSickLeave(usl_officer_id=user, usl_date=test_date, reason_for_usl="User Sick")
        test_usl.save()
        
        page = self.client.get("/abscences/{0}/reject_usl/".format(test_usl.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reject_usl.html")
        
    def test_reject_fm_page(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        test_fm = ForceMajeure(fm_officer_id=user, fm_date=test_date, reason_for_fm="User Sick")
        test_fm.save()
        
        page = self.client.get("/abscences/{0}/reject_fm/".format(test_fm.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reject_fm.html")
        
    '''def test_post_submit_usl(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        
        response = self.client.post("/submit_usl/", {"usl_officer_id": "user", "usl_date": "test_date", "reason_for_usl": "User ill."})
        test_usl = get_object_or_404(UnCertifiedSickLeave, pk=1)
        self.assertEqual(test_usl.usl_checked_by_validator, False)
        self.assertEqual(test_usl.usl_accepted, False)
    
    def test_post_edit_usl(self):
        user = Account()
        user.save()
        test_date = datetime.datetime(2021, 3, 1)
        
        test_usl = UnCertifiedSickLeave(usl_officer_id=user, usl_date=test_date, reason_for_usl="Test edit USL")
        test_usl.save()
        id = test_usl.id

        response = self.client.post("/edit_usl/{0}".format(id), {"reason_for_usl": "A different test edit USL"})
        test_usl = get_object_or_404(UnCertifiedSickLeave, pk=id)
        test_usl.save()

        self.assertEqual("A different test edit USL", test_usl.reason_for_usl)'''