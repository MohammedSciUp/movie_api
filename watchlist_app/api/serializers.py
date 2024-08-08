''' serialization, used to convert data structures or objects into a format that can be stored or transmitted, such as JSON or'''
''' it maps all the vaules from models'''

from rest_framework import serializers

class MovieSerializer(serializers.Serializer): # serialization, used to convert data structures or objects
    #we need to map all elements from the model to the fields in the serializer'''
    id = serializers.IntegerField(read_only = True) # ''' the id of the movie we don't 
    #want to change the id of the field
    #so read_only = True means that the field will not be included in the output data '''
    
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length= 100) 
    active = serializers.BooleanField(default=True)
    # serializser use is similar to forms in django, it converts model instance to dictionary and vice versa
