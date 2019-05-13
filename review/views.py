
from django.shortcuts import render
from .forms import MyForm
from django.template import loader
from django.http import HttpResponse


def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            #email = myForm.cleaned_data['email']
            feedback = myForm.cleaned_data['feedback']

            context = {
            'name': name,
           # 'email': email,
            'feedback': feedback
            }

            template = loader.get_template('responseform.html')

            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()

     return render(request, 'responseform.html', {'form':form});
