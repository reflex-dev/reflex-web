class TypesenseClientError(IOError):
    def __init__(self, *args, **kwargs):
        super(TypesenseClientError, self).__init__(*args, **kwargs)


class ConfigError(TypesenseClientError):
    pass


class Timeout(TypesenseClientError):
    pass


class RequestMalformed(TypesenseClientError):
    pass


class RequestUnauthorized(TypesenseClientError):
    pass


class RequestForbidden(TypesenseClientError):
    pass


class ObjectNotFound(TypesenseClientError):
    pass


class ObjectAlreadyExists(TypesenseClientError):
    pass


class ObjectUnprocessable(TypesenseClientError):
    pass


class ServerError(TypesenseClientError):
    pass


class ServiceUnavailable(TypesenseClientError):
    pass


class HTTPStatus0Error(TypesenseClientError):
    pass
