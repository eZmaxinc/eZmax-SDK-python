"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
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
from eZmaxApi.model.ezsignbulksenddocumentmapping_create_object_v1_request import EzsignbulksenddocumentmappingCreateObjectV1Request
from eZmaxApi.model.ezsignbulksenddocumentmapping_create_object_v1_response import EzsignbulksenddocumentmappingCreateObjectV1Response
from eZmaxApi.model.ezsignbulksenddocumentmapping_delete_object_v1_response import EzsignbulksenddocumentmappingDeleteObjectV1Response
from eZmaxApi.model.ezsignbulksenddocumentmapping_get_object_v1_response import EzsignbulksenddocumentmappingGetObjectV1Response


class ObjectEzsignbulksenddocumentmappingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsignbulksenddocumentmapping_create_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignbulksenddocumentmappingCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignbulksenddocumentmapping',
                'operation_id': 'ezsignbulksenddocumentmapping_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsignbulksenddocumentmapping_create_object_v1_request',
                ],
                'required': [
                    'ezsignbulksenddocumentmapping_create_object_v1_request',
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
                    'ezsignbulksenddocumentmapping_create_object_v1_request':
                        (EzsignbulksenddocumentmappingCreateObjectV1Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsignbulksenddocumentmapping_create_object_v1_request': 'body',
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
        self.ezsignbulksenddocumentmapping_delete_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignbulksenddocumentmappingDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID}',
                'operation_id': 'ezsignbulksenddocumentmapping_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignbulksenddocumentmapping_id',
                ],
                'required': [
                    'pki_ezsignbulksenddocumentmapping_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsignbulksenddocumentmapping_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsignbulksenddocumentmapping_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsignbulksenddocumentmapping_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignbulksenddocumentmapping_id': 'pkiEzsignbulksenddocumentmappingID',
                },
                'location_map': {
                    'pki_ezsignbulksenddocumentmapping_id': 'path',
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
        self.ezsignbulksenddocumentmapping_get_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignbulksenddocumentmappingGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID}',
                'operation_id': 'ezsignbulksenddocumentmapping_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignbulksenddocumentmapping_id',
                ],
                'required': [
                    'pki_ezsignbulksenddocumentmapping_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsignbulksenddocumentmapping_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsignbulksenddocumentmapping_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsignbulksenddocumentmapping_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignbulksenddocumentmapping_id': 'pkiEzsignbulksenddocumentmappingID',
                },
                'location_map': {
                    'pki_ezsignbulksenddocumentmapping_id': 'path',
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

    def ezsignbulksenddocumentmapping_create_object_v1(
        self,
        ezsignbulksenddocumentmapping_create_object_v1_request,
        **kwargs
    ):
        """Create a new Ezsignbulksenddocumentmapping  # noqa: E501

        The endpoint allows to create one or many elements at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignbulksenddocumentmapping_create_object_v1(ezsignbulksenddocumentmapping_create_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsignbulksenddocumentmapping_create_object_v1_request (EzsignbulksenddocumentmappingCreateObjectV1Request):

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EzsignbulksenddocumentmappingCreateObjectV1Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ezsignbulksenddocumentmapping_create_object_v1_request'] = \
            ezsignbulksenddocumentmapping_create_object_v1_request
        return self.ezsignbulksenddocumentmapping_create_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignbulksenddocumentmapping_delete_object_v1(
        self,
        pki_ezsignbulksenddocumentmapping_id,
        **kwargs
    ):
        """Delete an existing Ezsignbulksenddocumentmapping  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignbulksenddocumentmapping_delete_object_v1(pki_ezsignbulksenddocumentmapping_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignbulksenddocumentmapping_id (int):

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EzsignbulksenddocumentmappingDeleteObjectV1Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['pki_ezsignbulksenddocumentmapping_id'] = \
            pki_ezsignbulksenddocumentmapping_id
        return self.ezsignbulksenddocumentmapping_delete_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignbulksenddocumentmapping_get_object_v1(
        self,
        pki_ezsignbulksenddocumentmapping_id,
        **kwargs
    ):
        """Retrieve an existing Ezsignbulksenddocumentmapping  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignbulksenddocumentmapping_get_object_v1(pki_ezsignbulksenddocumentmapping_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignbulksenddocumentmapping_id (int):

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EzsignbulksenddocumentmappingGetObjectV1Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['pki_ezsignbulksenddocumentmapping_id'] = \
            pki_ezsignbulksenddocumentmapping_id
        return self.ezsignbulksenddocumentmapping_get_object_v1_endpoint.call_with_http_info(**kwargs)

