from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from crud.models import Item
import json

# Disable CSRF for Postman requests
@csrf_exempt
def create_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            dob = parse_date(data.get('dob'))

            item = Item(name=name, email=email, dob=dob)
            item.clean()  # Validate data
            item.save()
            return JsonResponse({"message": "Item created successfully!"}, status=201)
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "Invalid data , check data is correct or not"}, status=400)

@csrf_exempt
def read_item(request, id):
    if request.method == "GET":
        try:
            item = Item.objects.get(id=id)
            data = {
                "id": item.id,
                "name": item.name,
                "email": item.email,
                "dob": item.dob.isoformat()
            }
            return JsonResponse(data, status=200)
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found in DataBase"}, status=404)

@csrf_exempt
def get_all_items(request):
    if request.method == "GET":
        try:
            # Fetch all items from the database
            items = Item.objects.all()
            
            # Prepare a list of item data
            data = []
            for item in items:
                data.append({
                    "id": item.id,
                    "name": item.name,
                    "email": item.email,
                    "dob": item.dob.isoformat()
                })
            
            return render(request, 'index.html', {'items': items}) # safe=False allows a list of objects
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)            

@csrf_exempt
def update_item(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            item = Item.objects.get(id=id)

            item.name = data.get('name', item.name)
            item.email = data.get('email', item.email)
            item.dob = parse_date(data.get('dob')) or item.dob

            item.clean()  # Validate data
            item.save()
            return JsonResponse({"message": "Item updated successfully!"}, status=200)
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Invalid data"}, status=400)

@csrf_exempt
def delete_item(request, id):
    if request.method == "DELETE":
        try:
            item = Item.objects.get(id=id)
            item.delete()
            return JsonResponse({"message": "Item deleted successfully!"}, status=200)
        except Item.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)