from django.db import models

# user_identity_management   database classes
class UserAccesses
class ProfilesCharacteristics
class Characteristics

class Profile(models.Model):
    person_id = models.ForeignKey(People)
    

class Facilities(models.Model):
    facility_type_code = models.ForeignKey(FacilityTypes)
    facility_type_name = models.CharField()
    facility_type_description = models.TextField()
    
    
class ProfileContet
class FacilityTypes(models.Model):
    facility_type_code = models.ForeignKey(FacilityTypes)
    facility_type_name = models.CharField()
    facility_type_description = models.TextField()

class People(models.Model):
    date_of_birth = models.DateField()
    palce_of_birth = models.CharField()
    
    
    
    
