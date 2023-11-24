from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


class ItemAPI(APIView):
    def get(self, request, item_id):
        try:
            item = Item.objects.filter(id=item_id).first()
            serializer = ItemSerializer(item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)


class Create_ItemAPI(APIView):
    def post(self, request):
        try:
            name = request.data.get("name")
            item = Item.objects.create(name=name)
            item.save()
            return Response(status= status.HTTP_201_CREATED)
        except Exception as e:
            return Response(f"Error encountered: {e}",status= status.HTTP_400_BAD_REQUEST)
