"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.3
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
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfoldertype_get_list_v1_response import EzsignfoldertypeGetListV1Response
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage


class ObjectEzsignfoldertypeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsignfoldertype_get_autocomplete_v1_endpoint = _Endpoint(
            settings={
                'response_type': (CommonGetAutocompleteV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldertype/getAutocomplete/{sSelector}',
                'operation_id': 'ezsignfoldertype_get_autocomplete_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    's_selector',
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
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('s_selector',): {

                        "ACTIVE": "Active",
                        "ALL": "All"
                    },
                },
                'openapi_types': {
                    's_selector':
                        (str,),
                    's_query':
                        (str,),
                    'accept_language':
                        (HeaderAcceptLanguage,),
                },
                'attribute_map': {
                    's_selector': 'sSelector',
                    's_query': 'sQuery',
                    'accept_language': 'Accept-Language',
                },
                'location_map': {
                    's_selector': 'path',
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
        self.ezsignfoldertype_get_list_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldertypeGetListV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldertype/getList',
                'operation_id': 'ezsignfoldertype_get_list_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'e_order_by',
                    'i_row_max',
                    'i_row_offset',
                    'accept_language',
                    's_filter',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'e_order_by',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('e_order_by',): {

                        "PKIEZSIGNFOLDERTYPEID_ASC": "pkiEzsignfoldertypeID_ASC",
                        "PKIEZSIGNFOLDERTYPEID_DESC": "pkiEzsignfoldertypeID_DESC",
                        "EEZSIGNFOLDERTYPEPRIVACYLEVEL_ASC": "eEzsignfoldertypePrivacylevel_ASC",
                        "EEZSIGNFOLDERTYPEPRIVACYLEVEL_DESC": "eEzsignfoldertypePrivacylevel_DESC",
                        "SEZSIGNFOLDERTYPENAMEX_ASC": "sEzsignfoldertypeNameX_ASC",
                        "SEZSIGNFOLDERTYPENAMEX_DESC": "sEzsignfoldertypeNameX_DESC",
                        "BEZSIGNFOLDERTYPEISACTIVE_ASC": "bEzsignfoldertypeIsactive_ASC",
                        "BEZSIGNFOLDERTYPEISACTIVE_DESC": "bEzsignfoldertypeIsactive_DESC"
                    },
                },
                'openapi_types': {
                    'e_order_by':
                        (str,),
                    'i_row_max':
                        (int,),
                    'i_row_offset':
                        (int,),
                    'accept_language':
                        (HeaderAcceptLanguage,),
                    's_filter':
                        (str,),
                },
                'attribute_map': {
                    'e_order_by': 'eOrderBy',
                    'i_row_max': 'iRowMax',
                    'i_row_offset': 'iRowOffset',
                    'accept_language': 'Accept-Language',
                    's_filter': 'sFilter',
                },
                'location_map': {
                    'e_order_by': 'query',
                    'i_row_max': 'query',
                    'i_row_offset': 'query',
                    'accept_language': 'header',
                    's_filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def ezsignfoldertype_get_autocomplete_v1(
        self,
        s_selector,
        **kwargs
    ):
        """Retrieve Ezsignfoldertypes and IDs  # noqa: E501

        Get the list of Ezsignfoldertypes to be used in a dropdown or autocomplete control.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldertype_get_autocomplete_v1(s_selector, async_req=True)
        >>> result = thread.get()

        Args:
            s_selector (str): The type of Ezsignfoldertypes to return

        Keyword Args:
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['s_selector'] = \
            s_selector
        return self.ezsignfoldertype_get_autocomplete_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignfoldertype_get_list_v1(
        self,
        **kwargs
    ):
        """Retrieve Ezsignfoldertype list  # noqa: E501

        Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsignfoldertypePrivacylevel | User<br>Usergroup |  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldertype_get_list_v1(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            e_order_by (str): Specify how you want the results to be sorted. [optional]
            i_row_max (int): [optional]
            i_row_offset (int): [optional]
            accept_language (HeaderAcceptLanguage): [optional]
            s_filter (str): [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            EzsignfoldertypeGetListV1Response
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.ezsignfoldertype_get_list_v1_endpoint.call_with_http_info(**kwargs)

