"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
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
from eZmaxApi.model.authenticate_authenticate_v2_request import AuthenticateAuthenticateV2Request
from eZmaxApi.model.authenticate_authenticate_v2_response import AuthenticateAuthenticateV2Response
from eZmaxApi.model.common_response_error import CommonResponseError


class ModuleAuthenticateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.authenticate_authenticate_v2_endpoint = _Endpoint(
            settings={
                'response_type': (AuthenticateAuthenticateV2Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/2/module/authenticate/authenticate/{eSessionType}',
                'operation_id': 'authenticate_authenticate_v2',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'e_session_type',
                    'authenticate_authenticate_v2_request',
                ],
                'required': [
                    'e_session_type',
                    'authenticate_authenticate_v2_request',
                ],
                'nullable': [
                ],
                'enum': [
                    'e_session_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('e_session_type',): {

                        "EZSIGNUSER": "ezsignuser"
                    },
                },
                'openapi_types': {
                    'e_session_type':
                        (str,),
                    'authenticate_authenticate_v2_request':
                        (AuthenticateAuthenticateV2Request,),
                },
                'attribute_map': {
                    'e_session_type': 'eSessionType',
                },
                'location_map': {
                    'e_session_type': 'path',
                    'authenticate_authenticate_v2_request': 'body',
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
            api_client=api_client
        )

    def authenticate_authenticate_v2(
        self,
        authenticate_authenticate_v2_request,
        e_session_type="ezsignuser",
        **kwargs
    ):
        """Authenticate a user  # noqa: E501

        This endpoint authenticates a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.authenticate_authenticate_v2(authenticate_authenticate_v2_request, e_session_type="ezsignuser", async_req=True)
        >>> result = thread.get()

        Args:
            authenticate_authenticate_v2_request (AuthenticateAuthenticateV2Request):
            e_session_type (str): defaults to "ezsignuser", must be one of ["ezsignuser"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            AuthenticateAuthenticateV2Response
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
        kwargs['e_session_type'] = \
            e_session_type
        kwargs['authenticate_authenticate_v2_request'] = \
            authenticate_authenticate_v2_request
        return self.authenticate_authenticate_v2_endpoint.call_with_http_info(**kwargs)

