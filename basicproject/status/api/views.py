from django.db.models import query
from django.db.models.query import QuerySet
from django.http import response
from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics , mixins
from rest_framework.response import Response
from .serializers import StatusSerializer
from status.models import Status
#create your views here

# CreateModelMixin -- POST method
# UpdateModelMixin -- PUT method
# DestroyModelMixin -- DELETE method

class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    #permission_classes = []
    #authentication_classes = []

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id',None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id = passed_id)
            self.check_object_permissions(request , obj)
        return obj 
    def get(self, request , *args, **kwargs):
        passed_id = request.GET.get('id',None)
        if passed_id is not None:
            return self.retrieve(request,*args,**kwargs)
        return super().get(request, *args,**kwargs)
    
    def post(self , request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self, request, *args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self, request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)    


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self,request,format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs,many=True)
#         return Response(serializer.data)
#     def post(self,request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs,many=True)
#         return Response(serializer.data) 

# class StatusAPIView(generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # def perform_create(self, serializer):
#     #     serializer.save(user = self.request.user)

# class StatusDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []

#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
