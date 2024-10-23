from django.http import HttpResponse
from django.template import loader
def page5(request):
    template=loader.get_template('project.html')
    return HttpResponse(template.render())
# Create your views here.
