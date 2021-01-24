from django.views import generic
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from extra_views import CreateWithInlinesView, InlineFormSet


from .forms import SignUpForm, activate_user
from .models import Family, Result


class SignUpView(generic.edit.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
class ActivateView(generic.TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)


class PersonCreateView(generic.edit.CreateView):
    success_url = reverse_lazy("person_list")
    model = Family
    fields = ['person']

    def form_valid(self, form):
        form.instance.family_user_id = self.request.user.id
        return super(PersonCreateView, self).form_valid(form)


class PersonListView(generic.ListView):
    model = Family
    paginate_by = 100

    def get_queryset(self):
        family_user_id = self.request.user.id
        return Family.objects.filter(family_user_id=family_user_id)





class PersonDetailView(generic.DetailView):
    model = Family




class PersonUpdateView(generic.UpdateView):
    model = Family
    fields = ['person']
 
    def get_success_url(self):
        return reverse('person_update', kwargs={'pk': self.object.pk})
 
    def get_form(self):
        form = super(PersonUpdateView, self).get_form()
        form.fields['person'].label = '名前'
        return form


class PersonDeleteView(generic.DeleteView):
    model = Family
    success_url = reverse_lazy('person_list')





class ResultListView(generic.ListView):
    model = Result
    paginate_by = 100


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['family'] = self.family
        return context

    def get_queryset(self):
        family = self.family = get_object_or_404(Family, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(result_family_id=family)
        return queryset
    
 

class ResultCreateView(generic.edit.CreateView):
    success_url = reverse_lazy("result_list")
    model = Result
    fields = ['temperature']

    def form_valid(self, form):
        result=self.kwargs['pk']
        form.instance.result_family_id = result
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('result_list', kwargs={'pk': self.kwargs['pk']})


class ResultUpdateView(generic.UpdateView):
    model = Result
    fields = ['temperature']
 
    def get_success_url(self):
        result_id = self.kwargs['pk']
        result_id_object = Result.objects.get(pk=result_id)
        result_foreign_key = result_id_object.result_family_id
        return reverse('result_list', kwargs={'pk':result_foreign_key})
 
    def get_form(self):
        form = super(ResultUpdateView, self).get_form()
        form.fields['temperature'].label = '温度'
        return form


class ResultDeleteView(generic.DeleteView):
    model = Result

    def get_success_url(self):
        result_id = self.kwargs['pk']
        result_id_object = Result.objects.get(pk=result_id)
        result_foreign_key = result_id_object.result_family_id
        return reverse('result_list', kwargs={'pk':result_foreign_key})

"""
family = get_object_or_404(Family, pk=self.kwargs['pk'])
class PersonCreateView(generic.edit.CreateView):
    success_url = reverse_lazy("person_list")
    model = Family
    fields = ['person']

    def form_valid(self, form):
        form.instance.family_user_id = self.request.user.id
        return super(PersonCreateView, self).form_valid(form)
"""