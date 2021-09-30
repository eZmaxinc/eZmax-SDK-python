"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
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
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignsignature_create_object_v1_request import EzsignsignatureCreateObjectV1Request
from eZmaxApi.model.ezsignsignature_create_object_v1_response import EzsignsignatureCreateObjectV1Response
from eZmaxApi.model.ezsignsignature_delete_object_v1_response import EzsignsignatureDeleteObjectV1Response
from eZmaxApi.model.ezsignsignature_get_object_v1_response import EzsignsignatureGetObjectV1Response


class ObjectEzsignsignatureApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsignsignature_create_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignsignatureCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignsignature',
                'operation_id': 'ezsignsignature_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsignsignature_create_object_v1_request',
                ],
                'required': [
                    'ezsignsignature_create_object_v1_request',
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
                    'ezsignsignature_create_object_v1_request':
                        ([EzsignsignatureCreateObjectV1Request],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsignsignature_create_object_v1_request': 'body',
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
        self.ezsignsignature_delete_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignsignatureDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignsignature/{pkiEzsignsignatureID}',
                'operation_id': 'ezsignsignature_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignsignature_id',
                ],
                'required': [
                    'pki_ezsignsignature_id',
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
                    'pki_ezsignsignature_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignsignature_id': 'pkiEzsignsignatureID',
                },
                'location_map': {
                    'pki_ezsignsignature_id': 'path',
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
            api_client=api_client
        )
        self.ezsignsignature_get_children_v1_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignsignature/{pkiEzsignsignatureID}/getChildren',
                'operation_id': 'ezsignsignature_get_children_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignsignature_id',
                ],
                'required': [
                    'pki_ezsignsignature_id',
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
                    'pki_ezsignsignature_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignsignature_id': 'pkiEzsignsignatureID',
                },
                'location_map': {
                    'pki_ezsignsignature_id': 'path',
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
            api_client=api_client
        )
        self.ezsignsignature_get_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignsignatureGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignsignature/{pkiEzsignsignatureID}',
                'operation_id': 'ezsignsignature_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignsignature_id',
                ],
                'required': [
                    'pki_ezsignsignature_id',
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
                    'pki_ezsignsignature_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignsignature_id': 'pkiEzsignsignatureID',
                },
                'location_map': {
                    'pki_ezsignsignature_id': 'path',
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
            api_client=api_client
        )

    def ezsignsignature_create_object_v1(
        self,
        ezsignsignature_create_object_v1_request,
        **kwargs
    ):
        """Create a new Ezsignsignature  # noqa: E501

        The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsignsignature_create_object_v1_request ([EzsignsignatureCreateObjectV1Request]):

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
            EzsignsignatureCreateObjectV1Response
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
        kwargs['ezsignsignature_create_object_v1_request'] = \
            ezsignsignature_create_object_v1_request
        return self.ezsignsignature_create_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignsignature_delete_object_v1(
        self,
        pki_ezsignsignature_id,
        **kwargs
    ):
        """Delete an existing Ezsignsignature  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignsignature_delete_object_v1(pki_ezsignsignature_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignsignature_id (int):

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
            EzsignsignatureDeleteObjectV1Response
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
        kwargs['pki_ezsignsignature_id'] = \
            pki_ezsignsignature_id
        return self.ezsignsignature_delete_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignsignature_get_children_v1(
        self,
        pki_ezsignsignature_id,
        **kwargs
    ):
        """Retrieve an existing Ezsignsignature's children IDs  # noqa: E501

        ## ⚠️EARLY ADOPTERS WARNING  ### This endpoint is not officially released. Its definition might still change and it might not be available in every environment and region.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignsignature_get_children_v1(pki_ezsignsignature_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignsignature_id (int):

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
        kwargs['pki_ezsignsignature_id'] = \
            pki_ezsignsignature_id
        return self.ezsignsignature_get_children_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignsignature_get_object_v1(
        self,
        pki_ezsignsignature_id,
        **kwargs
    ):
        """Retrieve an existing Ezsignsignature  # noqa: E501

        ## ⚠️EARLY ADOPTERS WARNING  ### This endpoint is not officially released. Its definition might still change and it might not be available in every environment and region.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignsignature_get_object_v1(pki_ezsignsignature_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignsignature_id (int):

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
            EzsignsignatureGetObjectV1Response
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
        kwargs['pki_ezsignsignature_id'] = \
            pki_ezsignsignature_id
        return self.ezsignsignature_get_object_v1_endpoint.call_with_http_info(**kwargs)

