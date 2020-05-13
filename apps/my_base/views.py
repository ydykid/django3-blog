from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class BaseSerializerAPIView(APIView):
    """
    Base API View that various JWT interactions inherit from.
    """
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'view': self,
        }

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__)
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         user = serializer.object.get('user') or request.user
    #         token = serializer.object.get('token')
    #         response_data = jwt_response_payload_handler(token, user, request)
    #         response = Response(response_data)
    #         if api_settings.JWT_AUTH_COOKIE:
    #             expiration = (datetime.utcnow() +
    #                           api_settings.JWT_EXPIRATION_DELTA)
    #             response.set_cookie(api_settings.JWT_AUTH_COOKIE,
    #                                 token,
    #                                 expires=expiration,
    #                                 httponly=True)
    #         return response
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
