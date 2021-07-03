from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from era.forms import FacultadForm, CarrerForm
from era.models import Facultad, Carrera


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'era/form.html'


class FaculdadDetails(DetailView):
    model = Facultad
    template_name = 'era/facultadDetails.html'

    def get_context_data(self, **kwargs):
        context = super(FaculdadDetails, self).get_context_data(**kwargs)
        context['careerList'] = context['facultad'].carrera_set.all()
        return context


class FacultadCreate(LoginRequiredMixin, CreateView):
    model = Facultad
    template_name = 'era/form.html'
    form_class = FacultadForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FacultadCreate, self).form_valid(form)


class FacultadDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Facultad
    template_name = 'era/confirmationForm.html'
    success_url = reverse_lazy('era:facultad_list')


class CareerCreate(LoginRequiredMixin, CreateView):
    model = Carrera
    template_name = 'era/form.html'
    form_class = CarrerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.Facultad_idFacultad = Facultad.objects.get(id_Facultad=self.kwargs['pk'])
        return super(CareerCreate, self).form_valid(form)


class CareerDetails(DetailView):
    model = Carrera
    template_name = 'era/careerDetails.html'

    def get_context_data(self, **kwargs):
        context = super(CareerDetails, self).get_context_data(**kwargs)
        context['facultad'] = context['carrera'].get_facultad()
        return context


class CareerDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Carrera
    template_name = 'era/confirmationForm.html'
    success_url = reverse_lazy('era:facultad_list')
