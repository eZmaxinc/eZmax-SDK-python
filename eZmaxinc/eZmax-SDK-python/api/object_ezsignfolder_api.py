"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.37
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eZmaxinc/eZmax-SDK-python.api_client import ApiClient, Endpoint as _Endpoint
from eZmaxinc/eZmax-SDK-python.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_create_object_v1_request import EzsignfolderCreateObjectV1Request
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_create_object_v1_response import EzsignfolderCreateObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_delete_object_v1_response import EzsignfolderDeleteObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_get_object_v1_response import EzsignfolderGetObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_send_v1_request import EzsignfolderSendV1Request
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_send_v1_response import EzsignfolderSendV1Response


class ObjectEzsignfolderApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __ezsignfolder_create_object_v1(
            self,
            ezsignfolder_create_object_v1_request,
            **kwargs
        ):
            """Create a new Ezsignfolder  # noqa: E501

            The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsignfolder_create_object_v1(ezsignfolder_create_object_v1_request, async_req=True)
            >>> result = thread.get()

            Args:
                ezsignfolder_create_object_v1_request ([EzsignfolderCreateObjectV1Request]):

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
                EzsignfolderCreateObjectV1Response
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
            kwargs['ezsignfolder_create_object_v1_request'] = \
                ezsignfolder_create_object_v1_request
            return self.call_with_http_info(**kwargs)

        self.ezsignfolder_create_object_v1 = _Endpoint(
            settings={
                'response_type': (EzsignfolderCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfolder',
                'operation_id': 'ezsignfolder_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsignfolder_create_object_v1_request',
                ],
                'required': [
                    'ezsignfolder_create_object_v1_request',
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
                    'ezsignfolder_create_object_v1_request':
                        ([EzsignfolderCreateObjectV1Request],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsignfolder_create_object_v1_request': 'body',
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
            callable=__ezsignfolder_create_object_v1
        )

        def __ezsignfolder_delete_object_v1(
            self,
            pki_ezsignfolder_id,
            **kwargs
        ):
            """Delete an existing Ezsignfolder  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsignfolder_delete_object_v1(pki_ezsignfolder_id, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsignfolder_id (int): The unique ID of the Ezsignfolder

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
                EzsignfolderDeleteObjectV1Response
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
            kwargs['pki_ezsignfolder_id'] = \
                pki_ezsignfolder_id
            return self.call_with_http_info(**kwargs)

        self.ezsignfolder_delete_object_v1 = _Endpoint(
            settings={
                'response_type': (EzsignfolderDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfolder/{pkiEzsignfolderID}',
                'operation_id': 'ezsignfolder_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfolder_id',
                ],
                'required': [
                    'pki_ezsignfolder_id',
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
                    'pki_ezsignfolder_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignfolder_id': 'pkiEzsignfolderID',
                },
                'location_map': {
                    'pki_ezsignfolder_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__ezsignfolder_delete_object_v1
        )

        def __ezsignfolder_get_children_v1(
            self,
            pki_ezsignfolder_id,
            **kwargs
        ):
            """Retrieve an existing Ezsignfolder's children IDs  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsignfolder_get_children_v1(pki_ezsignfolder_id, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsignfolder_id (int): The unique ID of the Ezsignfolder

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
                None
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
            kwargs['pki_ezsignfolder_id'] = \
                pki_ezsignfolder_id
            return self.call_with_http_info(**kwargs)

        self.ezsignfolder_get_children_v1 = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfolder/{pkiEzsignfolderID}/getChildren',
                'operation_id': 'ezsignfolder_get_children_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfolder_id',
                ],
                'required': [
                    'pki_ezsignfolder_id',
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
                    'pki_ezsignfolder_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignfolder_id': 'pkiEzsignfolderID',
                },
                'location_map': {
                    'pki_ezsignfolder_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__ezsignfolder_get_children_v1
        )

        def __ezsignfolder_get_object_v1(
            self,
            pki_ezsignfolder_id,
            **kwargs
        ):
            """Retrieve an existing Ezsignfolder  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsignfolder_get_object_v1(pki_ezsignfolder_id, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsignfolder_id (int): The unique ID of the Ezsignfolder

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
                EzsignfolderGetObjectV1Response
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
            kwargs['pki_ezsignfolder_id'] = \
                pki_ezsignfolder_id
            return self.call_with_http_info(**kwargs)

        self.ezsignfolder_get_object_v1 = _Endpoint(
            settings={
                'response_type': (EzsignfolderGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfolder/{pkiEzsignfolderID}',
                'operation_id': 'ezsignfolder_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfolder_id',
                ],
                'required': [
                    'pki_ezsignfolder_id',
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
                    'pki_ezsignfolder_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignfolder_id': 'pkiEzsignfolderID',
                },
                'location_map': {
                    'pki_ezsignfolder_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__ezsignfolder_get_object_v1
        )

        def __ezsignfolder_send_v1(
            self,
            pki_ezsignfolder_id,
            ezsignfolder_send_v1_request,
            **kwargs
        ):
            """Send the Ezsignfolder to the signatories for signature  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsignfolder_send_v1(pki_ezsignfolder_id, ezsignfolder_send_v1_request, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
                ezsignfolder_send_v1_request (EzsignfolderSendV1Request):

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
                EzsignfolderSendV1Response
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
            kwargs['pki_ezsignfolder_id'] = \
                pki_ezsignfolder_id
            kwargs['ezsignfolder_send_v1_request'] = \
                ezsignfolder_send_v1_request
            return self.call_with_http_info(**kwargs)

        self.ezsignfolder_send_v1 = _Endpoint(
            settings={
                'response_type': (EzsignfolderSendV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfolder/{pkiEzsignfolderID}/send',
                'operation_id': 'ezsignfolder_send_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfolder_id',
                    'ezsignfolder_send_v1_request',
                ],
                'required': [
                    'pki_ezsignfolder_id',
                    'ezsignfolder_send_v1_request',
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
                    'pki_ezsignfolder_id':
                        (int,),
                    'ezsignfolder_send_v1_request':
                        (EzsignfolderSendV1Request,),
                },
                'attribute_map': {
                    'pki_ezsignfolder_id': 'pkiEzsignfolderID',
                },
                'location_map': {
                    'pki_ezsignfolder_id': 'path',
                    'ezsignfolder_send_v1_request': 'body',
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
            callable=__ezsignfolder_send_v1
        )
