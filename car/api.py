
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from .models import Car
from .serializers import Car_Serializer

#show all cars
@api_view(['GET'])
def car_list_api(request):
    all_cars=Car.objects.all()
    data=Car_Serializer(all_cars,many=True).data
    return Response({'data':data})


#show  just one car
@api_view(['GET'])
def car_details_api(request,id):
    car_details=Car.objects.get(id=id)
    data=Car_Serializer(car_details).data
    return Response({'data':data})

# insert one product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_car(request):
    data=request.data
    serializer=Car_Serializer(data=data)

    if serializer.is_valid():
        car=Car.objects.create(**data,user=request.user)
        data=Car_Serializer(car,many=False)
        return Response({"car":data.data})
    else:
        return Response(serializer.error)

#show  edit car
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_car(request,id):
    car=car_details_api(car,id=id)
    if car.user != request.user:
        return  Response({"error":"Sorry You Can not update this car"},
                         status=status.HTTP_403_FORBIDDEN)
    
    car.maker=request.data['maker']
    car.catigory=request.data['catigory']
    car.image=request.data['image']
    car.model=request.data['model']
    car.year=request.data['year']
    car.color=request.data['color']
    car.price = request.data['price']
    car.mileage = request.data['mileage']
    car.transmission=request.data['transmission']
    car.fuel_type=request.data['fuel_type']
    car.body_style=request.data['body_style']

    car.save()
    serializer=Car_Serializer(Car,many=False)
    return Response({'serializer':serializer.data})


#show  delete car
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_car(request,id):
    car=car_details_api(car,id=id)
    if car.user != request.user:
        return  Response({"error":"Sorry You Can not update this car"},
                         status=status.HTTP_403_FORBIDDEN)
    

    car.delete()
    return Response({"data": "deleted"},
                     status=status.HTTP_200_OK)