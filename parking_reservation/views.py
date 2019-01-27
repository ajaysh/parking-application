from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)

from parking_reservation import models
from django.core.urlresolvers import reverse_lazy
from parking_reservation.forms import SlotDetailForm


# Create your views here.
class ParkingListView(ListView):
    # The ListView is creating a school_list for us and returning
    # It takes the model you called (School), lower cases everythhing
    #and returns a list with school_list
    context_object_name = 'parkings' # This will make the class no longer return parking_list but
                                    #a object calld parkings
    model = models.Parking

class ParkingDetailview(DetailView):
    #   Differently of the ListView, the DetailView just returns the name in
    #lower case. Here, just school
    context_object_name = 'parking_detail'
    model = models.Parking
    template_name = 'parking_reservation/parking_detail.html'

class ParkingUpdateView(UpdateView):
    fields = ('locality','lane','slot_name')
    model = models.Parking

class ParkingslotUpdateView(UpdateView):
    fields = ('reserved',)
    model = models.SlotDetail

class ParkingCreateView(CreateView):
    fields = ('locality','lane','slot_name')
    model = models.Parking

class ParkingslotCreateView(CreateView):
    #fields = ('slot','start_date','end_date','reserved')
    model = models.SlotDetail
    form_class = SlotDetailForm
    #def form_valid(self, form):
    #    form.instance.slot = self.request.slot_name
    #    return super(ParkingslotCreateView, self).form_valid(form)


class ParkingDeleteView(DeleteView):
    model = models.Parking
    success_url = reverse_lazy("parking_reservation:list")

class IndexView(TemplateView):

    # This probably happens because, I think, TemplateView is an abstract class.
    template_name = 'index.html' #this is the name of our tamplate. Remmember: this variable HAS to be named template_name !!!!
