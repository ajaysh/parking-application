from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Parking(models.Model):
    slot_name = models.CharField(max_length=256)
    lane = models.CharField(max_length=256, default='WestLane')
    locality = models.CharField(max_length=256,default='Magarpatta')
    def __str__(self):
        return self.locality+'->'+self.lane+'->'+self.slot_name

    def get_absolute_url(self):
        return reverse('parking_reservation:detail', kwargs={'pk':self.pk}) # pk stands for Primary Key

class SlotDetail(models.Model):
        slot = models.ForeignKey(Parking,related_name='slotDetails')
        start_date = models.DateField(auto_now=False, auto_now_add=False)
        end_date = models.DateField(auto_now=False, auto_now_add=False)
        reserved = models.BooleanField(default=False)

        def __str__(self):
            return 'Slot->'+self.slot.slot_name

        def get_absolute_url(self):
            return reverse('parking_reservation:detail', kwargs={'pk':self.slot.pk}) # pk stands for Primary Key
