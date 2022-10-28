"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
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
from eZmaxApi.model.ezsignformfieldgroup_create_object_v1_request import EzsignformfieldgroupCreateObjectV1Request
from eZmaxApi.model.ezsignformfieldgroup_create_object_v1_response import EzsignformfieldgroupCreateObjectV1Response
from eZmaxApi.model.ezsignformfieldgroup_delete_object_v1_response import EzsignformfieldgroupDeleteObjectV1Response
from eZmaxApi.model.ezsignformfieldgroup_edit_object_v1_request import EzsignformfieldgroupEditObjectV1Request
from eZmaxApi.model.ezsignformfieldgroup_edit_object_v1_response import EzsignformfieldgroupEditObjectV1Response
from eZmaxApi.model.ezsignformfieldgroup_get_object_v1_response import EzsignformfieldgroupGetObjectV1Response
from eZmaxApi.model.ezsignformfieldgroup_get_object_v2_response import EzsignformfieldgroupGetObjectV2Response


class ObjectEzsignformfieldgroupApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsignformfieldgroup_create_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignformfieldgroupCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignformfieldgroup',
                'operation_id': 'ezsignformfieldgroup_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsignformfieldgroup_create_object_v1_request',
                ],
                'required': [
                    'ezsignformfieldgroup_create_object_v1_request',
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
                    'ezsignformfieldgroup_create_object_v1_request':
                        (EzsignformfieldgroupCreateObjectV1Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsignformfieldgroup_create_object_v1_request': 'body',
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
        self.ezsignformfieldgroup_delete_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignformfieldgroupDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID}',
                'operation_id': 'ezsignformfieldgroup_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignformfieldgroup_id',
                ],
                'required': [
                    'pki_ezsignformfieldgroup_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsignformfieldgroup_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsignformfieldgroup_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsignformfieldgroup_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignformfieldgroup_id': 'pkiEzsignformfieldgroupID',
                },
                'location_map': {
                    'pki_ezsignformfieldgroup_id': 'path',
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
        self.ezsignformfieldgroup_edit_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignformfieldgroupEditObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID}',
                'operation_id': 'ezsignformfieldgroup_edit_object_v1',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignformfieldgroup_id',
                    'ezsignformfieldgroup_edit_object_v1_request',
                ],
                'required': [
                    'pki_ezsignformfieldgroup_id',
                    'ezsignformfieldgroup_edit_object_v1_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsignformfieldgroup_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsignformfieldgroup_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsignformfieldgroup_id':
                        (int,),
                    'ezsignformfieldgroup_edit_object_v1_request':
                        (EzsignformfieldgroupEditObjectV1Request,),
                },
                'attribute_map': {
                    'pki_ezsignformfieldgroup_id': 'pkiEzsignformfieldgroupID',
                },
                'location_map': {
                    'pki_ezsignformfieldgroup_id': 'path',
                    'ezsignformfieldgroup_edit_object_v1_request': 'body',
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
        self.ezsignformfieldgroup_get_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignformfieldgroupGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID}',
                'operation_id': 'ezsignformfieldgroup_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignformfieldgroup_id',
                ],
                'required': [
                    'pki_ezsignformfieldgroup_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsignformfieldgroup_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsignformfieldgroup_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsignformfieldgroup_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignformfieldgroup_id': 'pkiEzsignformfieldgroupID',
                },
                'location_map': {
                    'pki_ezsignformfieldgroup_id': 'path',
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
        self.ezsignformfieldgroup_get_object_v2_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignformfieldgroupGetObjectV2Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/2/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID}',
                'operation_id': 'ezsignformfieldgroup_get_object_v2',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignformfieldgroup_id',
                ],
                'required': [
                    'pki_ezsignformfieldgroup_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsignformfieldgroup_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsignformfieldgroup_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsignformfieldgroup_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignformfieldgroup_id': 'pkiEzsignformfieldgroupID',
                },
                'location_map': {
                    'pki_ezsignformfieldgroup_id': 'path',
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

    def ezsignformfieldgroup_create_object_v1(
        self,
        ezsignformfieldgroup_create_object_v1_request,
        **kwargs
    ):
        """Create a new Ezsignformfieldgroup  # noqa: E501

        The endpoint allows to create one or many elements at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignformfieldgroup_create_object_v1(ezsignformfieldgroup_create_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsignformfieldgroup_create_object_v1_request (EzsignformfieldgroupCreateObjectV1Request):

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
            EzsignformfieldgroupCreateObjectV1Response
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
        kwargs['ezsignformfieldgroup_create_object_v1_request'] = \
            ezsignformfieldgroup_create_object_v1_request
        return self.ezsignformfieldgroup_create_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignformfieldgroup_delete_object_v1(
        self,
        pki_ezsignformfieldgroup_id,
        **kwargs
    ):
        """Delete an existing Ezsignformfieldgroup  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignformfieldgroup_delete_object_v1(pki_ezsignformfieldgroup_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignformfieldgroup_id (int):

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
            EzsignformfieldgroupDeleteObjectV1Response
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
        kwargs['pki_ezsignformfieldgroup_id'] = \
            pki_ezsignformfieldgroup_id
        return self.ezsignformfieldgroup_delete_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignformfieldgroup_edit_object_v1(
        self,
        pki_ezsignformfieldgroup_id,
        ezsignformfieldgroup_edit_object_v1_request,
        **kwargs
    ):
        """Edit an existing Ezsignformfieldgroup  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignformfieldgroup_edit_object_v1(pki_ezsignformfieldgroup_id, ezsignformfieldgroup_edit_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignformfieldgroup_id (int):
            ezsignformfieldgroup_edit_object_v1_request (EzsignformfieldgroupEditObjectV1Request):

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
            EzsignformfieldgroupEditObjectV1Response
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
        kwargs['pki_ezsignformfieldgroup_id'] = \
            pki_ezsignformfieldgroup_id
        kwargs['ezsignformfieldgroup_edit_object_v1_request'] = \
            ezsignformfieldgroup_edit_object_v1_request
        return self.ezsignformfieldgroup_edit_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignformfieldgroup_get_object_v1(
        self,
        pki_ezsignformfieldgroup_id,
        **kwargs
    ):
        """Retrieve an existing Ezsignformfieldgroup  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignformfieldgroup_get_object_v1(pki_ezsignformfieldgroup_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignformfieldgroup_id (int):

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
            EzsignformfieldgroupGetObjectV1Response
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
        kwargs['pki_ezsignformfieldgroup_id'] = \
            pki_ezsignformfieldgroup_id
        return self.ezsignformfieldgroup_get_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignformfieldgroup_get_object_v2(
        self,
        pki_ezsignformfieldgroup_id,
        **kwargs
    ):
        """Retrieve an existing Ezsignformfieldgroup  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignformfieldgroup_get_object_v2(pki_ezsignformfieldgroup_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignformfieldgroup_id (int):

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
            EzsignformfieldgroupGetObjectV2Response
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
        kwargs['pki_ezsignformfieldgroup_id'] = \
            pki_ezsignformfieldgroup_id
        return self.ezsignformfieldgroup_get_object_v2_endpoint.call_with_http_info(**kwargs)

