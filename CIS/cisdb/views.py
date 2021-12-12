from django.shortcuts import render
from django.db import transaction
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,TemplateView, UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from cisdb.models import Citizen
from .forms import SearchForm,QueryForm
from cisdb.face_match import identify_citizen


class HomeView(TemplateView):
    template_name = 'home.html'

class FoundView(TemplateView):
    template_name = 'found.html'

class CitizenCreate(CreateView):
    model = Citizen
    template_name = 'create.html'
    fields = "__all__"

    def get_success_url(self):
        self.success_url = reverse_lazy('home')
        return self.success_url
    
class CitizenUpdate(UpdateView):
    model = Citizen
    template_name = 'update.html'
    fields = "__all__"

   
class CitizenDetail(DetailView):
    template_name = 'details/citizen_detail.html'
    model = Citizen



class CitizenDelete(DeleteView):
    model = Citizen
    template_name = 'delete.html'
    
def match_view(request):
    if request.method == "POST":
        result = identify_citizen(request.FILES['image'])
        if result=="Unknown":
            print("No match found")
        else:
            names = result.split()
            full_name = ' '.join(names)
            print(full_name)
            citizen = Citizen.objects.annotate(
                        search=SearchVector('surname','first_name','other_name'),
                        ).filter(search=full_name)
            context = {
                'citizen' : citizen
            }
            return render(request,'found.html',context=context)
        return HttpResponseRedirect(reverse_lazy('home'))

    return render(request,'match.html')



def citizen_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Citizen.objects.annotate(
                        search=SearchVector('surname','first_name','other_name','national_id'),
                        ).filter(search=query)
    return render(request,
                    'search.html',
                     {'form': form,
                     'query': query,
                     'results': results})

def is_valid(arg):
    return arg != '' and arg is not None

def FIlterView(request):
    form = QueryForm()
    qs = Citizen.objects.all()
    
    name_contains = request.GET.get('name_contains')
    '''
    age_min = request.GET.get("age_min")
    age_max = request.GET.get("age_max")
    '''
    state = request.GET.get('state')
    state_residence = request.GET.get('state_residence')
    lga_query = request.GET.get('lga_query')
    occupation_query = request.GET.get('occupation_query')
    blood_group = request.GET.get('blood_group')
    genotype = request.GET.get('genotype')
    date_min = request.GET.get("date_min")
    date_max = request.GET.get("date_max")
    gender = request.GET.get("gender")
    marital_status = request.GET.get("marital_status")
    
    

    print(name_contains)
    #Queries relating to basic bio data
    if is_valid(name_contains):
        qs = qs.filter(first_name=name_contains)
    if is_valid(date_max):
        qs = qs.filter(date_of_birth__gte=date_max)
    if is_valid(date_min):
        qs = qs.filter(date_of_birth__lt=date_min)
    if is_valid(gender) and gender != "Choose...":
        qs = qs.filter(sex=gender)
    if is_valid(marital_status) and marital_status != "Choose...":
        qs = qs.filter(marital_status=marital_status)
    
    
    #Queries relating to location
    if is_valid(state) and state != "Choose...":
        qs = qs.filter(state_of_origin=state)

    elif is_valid(state_residence) and state_residence != "Choose...":
        qs = qs.filter(state_of_residence= state_residence)

    if is_valid(lga_query):
        qs = qs.filter(LGA=lga_query)

    
    #query by job
    if is_valid(occupation_query):
        qs = qs.filter(occupation=occupation_query)
    
    #Queries relating to health
    if is_valid(blood_group) and blood_group != "Choose...":
        qs= qs.filter(blood_type=blood_group)
    
    if is_valid(genotype) and genotype != "Choose...":
        qs= qs.filter(genotype=genotype)
    
    context = {
        'form':form,
        'queryset':qs
    }
    
    return render(request,'filter.html',context)