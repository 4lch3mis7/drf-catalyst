from rest_framework.response import Response


def success_response(data=None, message="Success", status_code=200):
    return Response(
        {
            "success": True,
            "status_code": status_code,
            "message": message,
            "data": data,
        },
        status=status_code,
    )


def error_response(errors=None, message="Error", status_code=400):
    return Response(
        {
            "success": False,
            "status_code": status_code,
            "message": message,
            "errors": errors,
        },
        status=status_code,
    )
