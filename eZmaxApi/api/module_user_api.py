"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.44
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eZmaxApi.api_client import ApiClient, Endpoint as _Endpoint
from eZmaxApi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from eZmaxApi.model.user_create_ezsignuser_v1_request import UserCreateEzsignuserV1Request
from eZmaxApi.model.user_create_ezsignuser_v1_response import UserCreateEzsignuserV1Response


class ModuleUserApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __user_create_ezsignuser_v1(
            self,
            user_create_ezsignuser_v1_request,
            **kwargs
        ):
            """Create a new User of type Ezsignuser  # noqa: E501

            The endpoint allows to initiate the creation or a user of type Ezsignuser.  The user will be created only once the email verification process will be completed  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.user_create_ezsignuser_v1(user_create_ezsignuser_v1_request, async_req=True)
            >>> result = thread.get()

            Args:
                user_create_ezsignuser_v1_request ([UserCreateEzsignuserV1Request]):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserCreateEzsignuserV1Response
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_create_ezsignuser_v1_request'] = \
                user_create_ezsignuser_v1_request
            return self.call_with_http_info(**kwargs)

        self.user_create_ezsignuser_v1 = _Endpoint(
            settings={
                'response_type': (UserCreateEzsignuserV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/module/user/createezsignuser',
                'operation_id': 'user_create_ezsignuser_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_create_ezsignuser_v1_request',
                ],
                'required': [
                    'user_create_ezsignuser_v1_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_create_ezsignuser_v1_request':
                        ([UserCreateEzsignuserV1Request],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'user_create_ezsignuser_v1_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__user_create_ezsignuser_v1
        )
