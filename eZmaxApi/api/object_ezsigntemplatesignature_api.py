"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.15
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
from eZmaxApi.model.ezsigntemplatesignature_create_object_v1_request import EzsigntemplatesignatureCreateObjectV1Request
from eZmaxApi.model.ezsigntemplatesignature_create_object_v1_response import EzsigntemplatesignatureCreateObjectV1Response
from eZmaxApi.model.ezsigntemplatesignature_delete_object_v1_response import EzsigntemplatesignatureDeleteObjectV1Response
from eZmaxApi.model.ezsigntemplatesignature_edit_object_v1_request import EzsigntemplatesignatureEditObjectV1Request
from eZmaxApi.model.ezsigntemplatesignature_edit_object_v1_response import EzsigntemplatesignatureEditObjectV1Response
from eZmaxApi.model.ezsigntemplatesignature_get_object_v1_response import EzsigntemplatesignatureGetObjectV1Response
from eZmaxApi.model.ezsigntemplatesignature_get_object_v2_response import EzsigntemplatesignatureGetObjectV2Response


class ObjectEzsigntemplatesignatureApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsigntemplatesignature_create_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplatesignatureCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplatesignature',
                'operation_id': 'ezsigntemplatesignature_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsigntemplatesignature_create_object_v1_request',
                ],
                'required': [
                    'ezsigntemplatesignature_create_object_v1_request',
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
                    'ezsigntemplatesignature_create_object_v1_request':
                        (EzsigntemplatesignatureCreateObjectV1Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsigntemplatesignature_create_object_v1_request': 'body',
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
        self.ezsigntemplatesignature_delete_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplatesignatureDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}',
                'operation_id': 'ezsigntemplatesignature_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplatesignature_id',
                ],
                'required': [
                    'pki_ezsigntemplatesignature_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplatesignature_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplatesignature_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplatesignature_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigntemplatesignature_id': 'pkiEzsigntemplatesignatureID',
                },
                'location_map': {
                    'pki_ezsigntemplatesignature_id': 'path',
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
        self.ezsigntemplatesignature_edit_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplatesignatureEditObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}',
                'operation_id': 'ezsigntemplatesignature_edit_object_v1',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplatesignature_id',
                    'ezsigntemplatesignature_edit_object_v1_request',
                ],
                'required': [
                    'pki_ezsigntemplatesignature_id',
                    'ezsigntemplatesignature_edit_object_v1_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplatesignature_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplatesignature_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplatesignature_id':
                        (int,),
                    'ezsigntemplatesignature_edit_object_v1_request':
                        (EzsigntemplatesignatureEditObjectV1Request,),
                },
                'attribute_map': {
                    'pki_ezsigntemplatesignature_id': 'pkiEzsigntemplatesignatureID',
                },
                'location_map': {
                    'pki_ezsigntemplatesignature_id': 'path',
                    'ezsigntemplatesignature_edit_object_v1_request': 'body',
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
        self.ezsigntemplatesignature_get_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplatesignatureGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}',
                'operation_id': 'ezsigntemplatesignature_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplatesignature_id',
                ],
                'required': [
                    'pki_ezsigntemplatesignature_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplatesignature_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplatesignature_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplatesignature_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigntemplatesignature_id': 'pkiEzsigntemplatesignatureID',
                },
                'location_map': {
                    'pki_ezsigntemplatesignature_id': 'path',
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
        self.ezsigntemplatesignature_get_object_v2_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplatesignatureGetObjectV2Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/2/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}',
                'operation_id': 'ezsigntemplatesignature_get_object_v2',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplatesignature_id',
                ],
                'required': [
                    'pki_ezsigntemplatesignature_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplatesignature_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplatesignature_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplatesignature_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigntemplatesignature_id': 'pkiEzsigntemplatesignatureID',
                },
                'location_map': {
                    'pki_ezsigntemplatesignature_id': 'path',
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

    def ezsigntemplatesignature_create_object_v1(
        self,
        ezsigntemplatesignature_create_object_v1_request,
        **kwargs
    ):
        """Create a new Ezsigntemplatesignature  # noqa: E501

        The endpoint allows to create one or many elements at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplatesignature_create_object_v1(ezsigntemplatesignature_create_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsigntemplatesignature_create_object_v1_request (EzsigntemplatesignatureCreateObjectV1Request):

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
            EzsigntemplatesignatureCreateObjectV1Response
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
        kwargs['ezsigntemplatesignature_create_object_v1_request'] = \
            ezsigntemplatesignature_create_object_v1_request
        return self.ezsigntemplatesignature_create_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplatesignature_delete_object_v1(
        self,
        pki_ezsigntemplatesignature_id,
        **kwargs
    ):
        """Delete an existing Ezsigntemplatesignature  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplatesignature_delete_object_v1(pki_ezsigntemplatesignature_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplatesignature_id (int):

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
            EzsigntemplatesignatureDeleteObjectV1Response
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
        kwargs['pki_ezsigntemplatesignature_id'] = \
            pki_ezsigntemplatesignature_id
        return self.ezsigntemplatesignature_delete_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplatesignature_edit_object_v1(
        self,
        pki_ezsigntemplatesignature_id,
        ezsigntemplatesignature_edit_object_v1_request,
        **kwargs
    ):
        """Edit an existing Ezsigntemplatesignature  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplatesignature_edit_object_v1(pki_ezsigntemplatesignature_id, ezsigntemplatesignature_edit_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplatesignature_id (int):
            ezsigntemplatesignature_edit_object_v1_request (EzsigntemplatesignatureEditObjectV1Request):

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
            EzsigntemplatesignatureEditObjectV1Response
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
        kwargs['pki_ezsigntemplatesignature_id'] = \
            pki_ezsigntemplatesignature_id
        kwargs['ezsigntemplatesignature_edit_object_v1_request'] = \
            ezsigntemplatesignature_edit_object_v1_request
        return self.ezsigntemplatesignature_edit_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplatesignature_get_object_v1(
        self,
        pki_ezsigntemplatesignature_id,
        **kwargs
    ):
        """Retrieve an existing Ezsigntemplatesignature  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplatesignature_get_object_v1(pki_ezsigntemplatesignature_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplatesignature_id (int):

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
            EzsigntemplatesignatureGetObjectV1Response
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
        kwargs['pki_ezsigntemplatesignature_id'] = \
            pki_ezsigntemplatesignature_id
        return self.ezsigntemplatesignature_get_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplatesignature_get_object_v2(
        self,
        pki_ezsigntemplatesignature_id,
        **kwargs
    ):
        """Retrieve an existing Ezsigntemplatesignature  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplatesignature_get_object_v2(pki_ezsigntemplatesignature_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplatesignature_id (int):

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
            EzsigntemplatesignatureGetObjectV2Response
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
        kwargs['pki_ezsigntemplatesignature_id'] = \
            pki_ezsigntemplatesignature_id
        return self.ezsigntemplatesignature_get_object_v2_endpoint.call_with_http_info(**kwargs)

