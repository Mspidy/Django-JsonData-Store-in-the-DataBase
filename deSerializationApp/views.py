from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt #because our request is a post request
def student_create(request):
    if request.method == 'POST':
        json_data = request.body #request data store in json_data
        stream = io.BytesIO(json_data) #now stream the data
        pythondata= JSONParser().parse(stream) #stream data change into python data
        serializer= StudentSerializer(data=pythondata) #python data change into complex data
        if serializer.is_valid():   #now check that validation(complex data is correct for our db or not)
            serializer.save() #if vaidate the save
            resp= {'msg':'Data Created'} #now i give the response data is correct or not
            json_data=JSONRenderer().render(resp) #now make json data
            return HttpResponse(json_data, content_type='application/json')  #and now send the data
        json_data=JSONRenderer().render(serializer.erros)
        return HttpResponse(json_data,content_type='application/json')