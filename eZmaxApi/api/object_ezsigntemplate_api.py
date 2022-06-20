"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.8
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
from eZmaxApi.model.ezsigntemplate_create_object_v1_request import EzsigntemplateCreateObjectV1Request
from eZmaxApi.model.ezsigntemplate_create_object_v1_response import EzsigntemplateCreateObjectV1Response
from eZmaxApi.model.ezsigntemplate_delete_object_v1_response import EzsigntemplateDeleteObjectV1Response
from eZmaxApi.model.ezsigntemplate_edit_object_v1_request import EzsigntemplateEditObjectV1Request
from eZmaxApi.model.ezsigntemplate_edit_object_v1_response import EzsigntemplateEditObjectV1Response
from eZmaxApi.model.ezsigntemplate_get_list_v1_response import EzsigntemplateGetListV1Response
from eZmaxApi.model.ezsigntemplate_get_object_v1_response import EzsigntemplateGetObjectV1Response
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage


class ObjectEzsigntemplateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsigntemplate_create_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplateCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplate',
                'operation_id': 'ezsigntemplate_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsigntemplate_create_object_v1_request',
                ],
                'required': [
                    'ezsigntemplate_create_object_v1_request',
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
                    'ezsigntemplate_create_object_v1_request':
                        (EzsigntemplateCreateObjectV1Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsigntemplate_create_object_v1_request': 'body',
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
        self.ezsigntemplate_delete_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplateDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplate/{pkiEzsigntemplateID}',
                'operation_id': 'ezsigntemplate_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplate_id',
                ],
                'required': [
                    'pki_ezsigntemplate_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplate_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplate_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplate_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigntemplate_id': 'pkiEzsigntemplateID',
                },
                'location_map': {
                    'pki_ezsigntemplate_id': 'path',
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
        self.ezsigntemplate_edit_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplateEditObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplate/{pkiEzsigntemplateID}',
                'operation_id': 'ezsigntemplate_edit_object_v1',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplate_id',
                    'ezsigntemplate_edit_object_v1_request',
                ],
                'required': [
                    'pki_ezsigntemplate_id',
                    'ezsigntemplate_edit_object_v1_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplate_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplate_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplate_id':
                        (int,),
                    'ezsigntemplate_edit_object_v1_request':
                        (EzsigntemplateEditObjectV1Request,),
                },
                'attribute_map': {
                    'pki_ezsigntemplate_id': 'pkiEzsigntemplateID',
                },
                'location_map': {
                    'pki_ezsigntemplate_id': 'path',
                    'ezsigntemplate_edit_object_v1_request': 'body',
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
        self.ezsigntemplate_get_autocomplete_v1_endpoint = _Endpoint(
            settings={
                'response_type': (CommonGetAutocompleteV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplate/getAutocomplete/{sSelector}',
                'operation_id': 'ezsigntemplate_get_autocomplete_v1',
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
        self.ezsigntemplate_get_list_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplateGetListV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplate/getList',
                'operation_id': 'ezsigntemplate_get_list_v1',
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
                    'i_row_max',
                    'i_row_offset',
                ]
            },
            root_map={
                'validations': {
                    ('i_row_max',): {

                        'inclusive_minimum': 1,
                    },
                    ('i_row_offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                    ('e_order_by',): {

                        "PKIEZSIGNTEMPLATEID_ASC": "pkiEzsigntemplateID_ASC",
                        "PKIEZSIGNTEMPLATEID_DESC": "pkiEzsigntemplateID_DESC",
                        "FKITEAMID_ASC": "fkiTeamID_ASC",
                        "FKITEAMID_DESC": "fkiTeamID_DESC",
                        "FKIEZSIGNFOLDERTYPEID_ASC": "fkiEzsignfoldertypeID_ASC",
                        "FKIEZSIGNFOLDERTYPEID_DESC": "fkiEzsignfoldertypeID_DESC",
                        "FKIUSERIDOWNER_ASC": "fkiUserIDOwner_ASC",
                        "FKIUSERIDOWNER_DESC": "fkiUserIDOwner_DESC",
                        "FKILANGUAGEID_ASC": "fkiLanguageID_ASC",
                        "FKILANGUAGEID_DESC": "fkiLanguageID_DESC",
                        "EEZSIGNTEMPLATETYPE_ASC": "eEzsigntemplateType_ASC",
                        "EEZSIGNTEMPLATETYPE_DESC": "eEzsigntemplateType_DESC",
                        "SEZSIGNTEMPLATETYPEDESCRIPTIONX_ASC": "sEzsigntemplateTypedescriptionX_ASC",
                        "SEZSIGNTEMPLATETYPEDESCRIPTIONX_DESC": "sEzsigntemplateTypedescriptionX_DESC",
                        "SEZSIGNTEMPLATEDOCUMENTDESCRIPTION_ASC": "sEzsigntemplatedocumentDescription_ASC",
                        "SEZSIGNTEMPLATEDOCUMENTDESCRIPTION_DESC": "sEzsigntemplatedocumentDescription_DESC",
                        "IEZSIGNTEMPLATEDOCUMENTPAGETOTAL_ASC": "iEzsigntemplatedocumentPagetotal_ASC",
                        "IEZSIGNTEMPLATEDOCUMENTPAGETOTAL_DESC": "iEzsigntemplatedocumentPagetotal_DESC",
                        "IEZSIGNTEMPLATESIGNATURETOTAL_ASC": "iEzsigntemplateSignaturetotal_ASC",
                        "IEZSIGNTEMPLATESIGNATURETOTAL_DESC": "iEzsigntemplateSignaturetotal_DESC"
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
        self.ezsigntemplate_get_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplateGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplate/{pkiEzsigntemplateID}',
                'operation_id': 'ezsigntemplate_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigntemplate_id',
                ],
                'required': [
                    'pki_ezsigntemplate_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'pki_ezsigntemplate_id',
                ]
            },
            root_map={
                'validations': {
                    ('pki_ezsigntemplate_id',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pki_ezsigntemplate_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigntemplate_id': 'pkiEzsigntemplateID',
                },
                'location_map': {
                    'pki_ezsigntemplate_id': 'path',
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

    def ezsigntemplate_create_object_v1(
        self,
        ezsigntemplate_create_object_v1_request,
        **kwargs
    ):
        """Create a new Ezsigntemplate  # noqa: E501

        The endpoint allows to create one or many elements at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplate_create_object_v1(ezsigntemplate_create_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsigntemplate_create_object_v1_request (EzsigntemplateCreateObjectV1Request):

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
            EzsigntemplateCreateObjectV1Response
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
        kwargs['ezsigntemplate_create_object_v1_request'] = \
            ezsigntemplate_create_object_v1_request
        return self.ezsigntemplate_create_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplate_delete_object_v1(
        self,
        pki_ezsigntemplate_id,
        **kwargs
    ):
        """Delete an existing Ezsigntemplate  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplate_delete_object_v1(pki_ezsigntemplate_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplate_id (int):

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
            EzsigntemplateDeleteObjectV1Response
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
        kwargs['pki_ezsigntemplate_id'] = \
            pki_ezsigntemplate_id
        return self.ezsigntemplate_delete_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplate_edit_object_v1(
        self,
        pki_ezsigntemplate_id,
        ezsigntemplate_edit_object_v1_request,
        **kwargs
    ):
        """Edit an existing Ezsigntemplate  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplate_edit_object_v1(pki_ezsigntemplate_id, ezsigntemplate_edit_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplate_id (int):
            ezsigntemplate_edit_object_v1_request (EzsigntemplateEditObjectV1Request):

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
            EzsigntemplateEditObjectV1Response
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
        kwargs['pki_ezsigntemplate_id'] = \
            pki_ezsigntemplate_id
        kwargs['ezsigntemplate_edit_object_v1_request'] = \
            ezsigntemplate_edit_object_v1_request
        return self.ezsigntemplate_edit_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplate_get_autocomplete_v1(
        self,
        s_selector="All",
        **kwargs
    ):
        """Retrieve Ezsigntemplate and IDs  # noqa: E501

        Get the list of Ezsigntemplate to be used in a dropdown or autocomplete control.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplate_get_autocomplete_v1(s_selector="All", async_req=True)
        >>> result = thread.get()

        Args:
            s_selector (str): The type of Ezsigntemplate to return. defaults to "All", must be one of ["All"]

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
        return self.ezsigntemplate_get_autocomplete_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplate_get_list_v1(
        self,
        **kwargs
    ):
        """Retrieve Ezsigntemplate list  # noqa: E501

        Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsigntemplateType | Company<br>Team<br>User<br>Usergroup |   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplate_get_list_v1(async_req=True)
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
            EzsigntemplateGetListV1Response
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
        return self.ezsigntemplate_get_list_v1_endpoint.call_with_http_info(**kwargs)

    def ezsigntemplate_get_object_v1(
        self,
        pki_ezsigntemplate_id,
        **kwargs
    ):
        """Retrieve an existing Ezsigntemplate  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplate_get_object_v1(pki_ezsigntemplate_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsigntemplate_id (int):

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
            EzsigntemplateGetObjectV1Response
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
        kwargs['pki_ezsigntemplate_id'] = \
            pki_ezsigntemplate_id
        return self.ezsigntemplate_get_object_v1_endpoint.call_with_http_info(**kwargs)

