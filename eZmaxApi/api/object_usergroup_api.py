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
from eZmaxApi.model.common_get_autocomplete_v1_response import CommonGetAutocompleteV1Response
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.model.usergroup_get_autocomplete_v2_response import UsergroupGetAutocompleteV2Response


class ObjectUsergroupApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.usergroup_get_autocomplete_v1_endpoint = _Endpoint(
            settings={
                'response_type': (CommonGetAutocompleteV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/usergroup/getAutocomplete/{sSelector}',
                'operation_id': 'usergroup_get_autocomplete_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    's_selector',
                    'e_filter_active',
                    's_query',
                    'accept_language',
                ],
                'required': [
                    's_selector',
                ],
                'nullable': [
                ],
                'enum': [
                    's_selector',
                    'e_filter_active',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('s_selector',): {

                        "ALL": "All"
                    },
                    ('e_filter_active',): {

                        "ALL": "All",
                        "ACTIVE": "Active",
                        "INACTIVE": "Inactive"
                    },
                },
                'openapi_types': {
                    's_selector':
                        (str,),
                    'e_filter_active':
                        (str,),
                    's_query':
                        (str,),
                    'accept_language':
                        (HeaderAcceptLanguage,),
                },
                'attribute_map': {
                    's_selector': 'sSelector',
                    'e_filter_active': 'eFilterActive',
                    's_query': 'sQuery',
                    'accept_language': 'Accept-Language',
                },
                'location_map': {
                    's_selector': 'path',
                    'e_filter_active': 'query',
                    's_query': 'query',
                    'accept_language': 'header',
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
        self.usergroup_get_autocomplete_v2_endpoint = _Endpoint(
            settings={
                'response_type': (UsergroupGetAutocompleteV2Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/2/object/usergroup/getAutocomplete/{sSelector}',
                'operation_id': 'usergroup_get_autocomplete_v2',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    's_selector',
                    'e_filter_active',
                    's_query',
                    'accept_language',
                ],
                'required': [
                    's_selector',
                ],
                'nullable': [
                ],
                'enum': [
                    's_selector',
                    'e_filter_active',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('s_selector',): {

                        "ALL": "All"
                    },
                    ('e_filter_active',): {

                        "ALL": "All",
                        "ACTIVE": "Active",
                        "INACTIVE": "Inactive"
                    },
                },
                'openapi_types': {
                    's_selector':
                        (str,),
                    'e_filter_active':
                        (str,),
                    's_query':
                        (str,),
                    'accept_language':
                        (HeaderAcceptLanguage,),
                },
                'attribute_map': {
                    's_selector': 'sSelector',
                    'e_filter_active': 'eFilterActive',
                    's_query': 'sQuery',
                    'accept_language': 'Accept-Language',
                },
                'location_map': {
                    's_selector': 'path',
                    'e_filter_active': 'query',
                    's_query': 'query',
                    'accept_language': 'header',
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

    def usergroup_get_autocomplete_v1(
        self,
        s_selector="All",
        **kwargs
    ):
        """Retrieve Usergroups and IDs  # noqa: E501

        Get the list of Usergroup to be used in a dropdown or autocomplete control.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.usergroup_get_autocomplete_v1(s_selector="All", async_req=True)
        >>> result = thread.get()

        Args:
            s_selector (str): The type of Usergroups to return. defaults to "All", must be one of ["All"]

        Keyword Args:
            e_filter_active (str): Specify which results we want to display.. [optional] if omitted the server will use the default value of "Active"
            s_query (str): Allow to filter the returned results. [optional]
            accept_language (HeaderAcceptLanguage): [optional]
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
            CommonGetAutocompleteV1Response
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
        kwargs['s_selector'] = \
            s_selector
        return self.usergroup_get_autocomplete_v1_endpoint.call_with_http_info(**kwargs)

    def usergroup_get_autocomplete_v2(
        self,
        s_selector="All",
        **kwargs
    ):
        """Retrieve Usergroups and IDs  # noqa: E501

        Get the list of Usergroup to be used in a dropdown or autocomplete control.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.usergroup_get_autocomplete_v2(s_selector="All", async_req=True)
        >>> result = thread.get()

        Args:
            s_selector (str): The type of Usergroups to return. defaults to "All", must be one of ["All"]

        Keyword Args:
            e_filter_active (str): Specify which results we want to display.. [optional] if omitted the server will use the default value of "Active"
            s_query (str): Allow to filter the returned results. [optional]
            accept_language (HeaderAcceptLanguage): [optional]
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
            UsergroupGetAutocompleteV2Response
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
        kwargs['s_selector'] = \
            s_selector
        return self.usergroup_get_autocomplete_v2_endpoint.call_with_http_info(**kwargs)

