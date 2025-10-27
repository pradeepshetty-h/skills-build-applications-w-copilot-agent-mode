from django.http import JsonResponse

def activities_root(request):
    return JsonResponse({'message': 'Activities API is working.'})
