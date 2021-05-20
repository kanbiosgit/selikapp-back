from rest_framework.response import Response
from rest_framework import status

def respond(response_status, data=[], errors=[]):
    success = True
    if errors or (response_status < 200 or response_status > 299):
        success = False
    return Response({
        "success": success, "status": response_status, "data": data, "error": errors
    }, status=status.HTTP_200_OK)