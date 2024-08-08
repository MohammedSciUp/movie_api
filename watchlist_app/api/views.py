from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
    # first we need to get the complex data from the database by intiating an object of Movie model
    movies = Movie.objects.all()
    # then we create a serializer object to convert the complex data into a format that can be easily consumed by the frontend
    serializer = MovieSerializer(movies, many=True)
    # finally, we return the serialized data in a json format
    return Response(serializer.data)
    # .data is a built-in method of the Response class that returns the serialized data in a json format
    # Response class is a built-in Django class that handles HTTP responses
@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    # we use pk as a parameter in the function to specify which movie details to retrieve
    # we use the get method of the Movie model to retrieve the movie with the specified id
    # we then create a serializer object to convert the movie data into a format that can be easily consumed by the frontend
    # finally, we return the serialized data in a json format
    # .data is a built-in method of the Response class that returns the serialized data in a json format
    # Response class is a built-in Django class that handles HTTP responses