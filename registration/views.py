from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.urls import reverse

from .forms import SignUpForm, activate_user
from .models import Family


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)


class PersonCreateView(CreateView):
    success_url = reverse_lazy("person_list")
    model = Family
    fields = ['person']

    def form_valid(self, form):
        form.instance.family_user_id = self.request.user.id
        return super(PersonCreateView, self).form_valid(form)


class PersonListView(ListView):
    model = Family
    paginate_by = 100

    def get_queryset(self):
        family_user_id = self.request.user.id
        return Family.objects.filter(family_user_id=family_user_id)


class PersonDetailView(DetailView):
    model = Family


class PersonUpdateView(UpdateView):
    model = Family
    fields = ['person']
 
    def get_success_url(self):
        return reverse('person_update', kwargs={'pk': self.object.pk})
 
    def get_form(self):
        form = super(PersonUpdateView, self).get_form()
        form.fields['person'].label = '名前'
        return form


class PersonDeleteView(DeleteView):
    # template_name = 'user/member_confirm_delete.html'
    model = Family
 
    success_url = reverse_lazy('person_list')

"""
class SampleTemplateView(TemplateView):
    template_name = "registration/test.html"
    model = Family

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**data) # はじめに継承元のメソッドを呼び出す
            context["test"] = Family.objects.all()
            return context

class PersonListView(CreateView):
    template_name = "registration/family_list.html"
    model = Family
    paginate_by = 5

    def get_queryset(self):
        family_user_id = self.request.user.id
        return Family.objects.filter(family_user_id=1)




class PersonListView(ListView):
    template_name = "registration/family_list.html"
    model = Family
    paginate_by = 5
    queryset = Family.objects.filter(family_user_id=1)

"""