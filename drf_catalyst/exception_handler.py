from django.core.exceptions import NON_FIELD_ERRORS as DJ_NON_FIELD_ERRORS
from django.core.exceptions import ValidationError as DjValidationError
from rest_framework.exceptions import ValidationError as DRFValidateionError
from rest_framework.views import api_settings
from rest_framework.views import exception_handler as drf_exception_handler

DRF_NON_FIELD_ERRORS = api_settings.NON_FIELD_ERRORS_KEY


def handle(exc, context):
    """
    Translates Django validation error (which causes HTTP 500 status)
    to DRF validation error which causes HTTP 400 status
    """
    if isinstance(exc, DjValidationError):
        data = exc.message_dict

        if DJ_NON_FIELD_ERRORS in data:
            data[DRF_NON_FIELD_ERRORS] = data[DJ_NON_FIELD_ERRORS]
            del data[DJ_NON_FIELD_ERRORS]

        exc = DRFValidateionError(detail=data)

    return drf_exception_handler(exc, context)
