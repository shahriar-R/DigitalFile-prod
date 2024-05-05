from django.db import models
from django.contrib.auth.models import User



class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, unique=True)
    mobile_number = models.CharField(max_length=11)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)  # Doctor field
    prescType = models.IntegerField()
    prescDate = models.CharField(max_length=8)
    docId = models.CharField(max_length=10)
    docMobileNo = models.CharField(max_length=11)
    docNationalCode = models.CharField(max_length=10)
    comments = models.TextField(blank=True)
    expireDate = models.CharField(max_length=8)



class NoteDetailEprsc(models.Model):
    prescription = models.ForeignKey(Prescription, related_name='note_detail_eprscs', on_delete=models.CASCADE)
    srvId = models.CharField(max_length=10)
    srvQty = models.IntegerField()
    dateDO = models.CharField(max_length=8)


class NoteDetailsReferral(models.Model):
    prescription = models.ForeignKey(Prescription, related_name='note_details_referrals', on_delete=models.CASCADE)
    docSpecReferred = models.CharField(max_length=10)
    message = models.TextField()
    referralDate = models.DateField()
    quantity = models.IntegerField()
