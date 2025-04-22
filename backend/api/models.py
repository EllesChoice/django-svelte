from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

    # här kommer min model in senare
    # Define a model (a table)
    # class Profile(Model):
    #     personal_identity_no = CharField()
    #     status = CharField()
    #     protected_identity = BooleanField(default=False)
    #     date_added = DateTimeField(default=datetime.datetime.now)
    #     changed_date = DateTimeField()
    #     first_name = CharField()
    #     middle_name = CharField()
    #     last_name = CharField()
    #     full_name = CharField()
    #     land_code = CharField()
    #     co_address = CharField()
    #     street_address = CharField()
    #     postal_code = CharField()
    #     area_code = CharField()
    #     city = CharField()
    #     phone_no = CharField()
    #     mobile_no = CharField()
    #     longitude = DoubleField()
    #     latitude = DoubleField()