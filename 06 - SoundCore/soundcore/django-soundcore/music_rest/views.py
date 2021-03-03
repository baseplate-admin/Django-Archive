from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SoundCoreModelSerializer
from .models import SoundCoreModel

# Create your views here.


@api_view(["GET"])
def all_songs(request):
    data = SoundCoreModel.objects.all()
    serializer = SoundCoreModelSerializer(data, many=True)
    return Response(serializer.data)

