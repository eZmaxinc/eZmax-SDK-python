"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
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
from eZmaxApi.model.ezsignfoldersignerassociation_create_object_v1_request import EzsignfoldersignerassociationCreateObjectV1Request
from eZmaxApi.model.ezsignfoldersignerassociation_create_object_v1_response import EzsignfoldersignerassociationCreateObjectV1Response
from eZmaxApi.model.ezsignfoldersignerassociation_create_object_v2_request import EzsignfoldersignerassociationCreateObjectV2Request
from eZmaxApi.model.ezsignfoldersignerassociation_create_object_v2_response import EzsignfoldersignerassociationCreateObjectV2Response
from eZmaxApi.model.ezsignfoldersignerassociation_delete_object_v1_response import EzsignfoldersignerassociationDeleteObjectV1Response
from eZmaxApi.model.ezsignfoldersignerassociation_edit_object_v1_request import EzsignfoldersignerassociationEditObjectV1Request
from eZmaxApi.model.ezsignfoldersignerassociation_edit_object_v1_response import EzsignfoldersignerassociationEditObjectV1Response
from eZmaxApi.model.ezsignfoldersignerassociation_get_in_person_login_url_v1_response import EzsignfoldersignerassociationGetInPersonLoginUrlV1Response
from eZmaxApi.model.ezsignfoldersignerassociation_get_object_v1_response import EzsignfoldersignerassociationGetObjectV1Response


class ObjectEzsignfoldersignerassociationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsignfoldersignerassociation_create_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldersignerassociationCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldersignerassociation',
                'operation_id': 'ezsignfoldersignerassociation_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsignfoldersignerassociation_create_object_v1_request',
                ],
                'required': [
                    'ezsignfoldersignerassociation_create_object_v1_request',
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
                    'ezsignfoldersignerassociation_create_object_v1_request':
                        ([EzsignfoldersignerassociationCreateObjectV1Request],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsignfoldersignerassociation_create_object_v1_request': 'body',
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
        self.ezsignfoldersignerassociation_create_object_v2_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldersignerassociationCreateObjectV2Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/2/object/ezsignfoldersignerassociation',
                'operation_id': 'ezsignfoldersignerassociation_create_object_v2',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsignfoldersignerassociation_create_object_v2_request',
                ],
                'required': [
                    'ezsignfoldersignerassociation_create_object_v2_request',
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
                    'ezsignfoldersignerassociation_create_object_v2_request':
                        (EzsignfoldersignerassociationCreateObjectV2Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsignfoldersignerassociation_create_object_v2_request': 'body',
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
        self.ezsignfoldersignerassociation_delete_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldersignerassociationDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}',
                'operation_id': 'ezsignfoldersignerassociation_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfoldersignerassociation_id',
                ],
                'required': [
                    'pki_ezsignfoldersignerassociation_id',
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
                    'pki_ezsignfoldersignerassociation_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignfoldersignerassociation_id': 'pkiEzsignfoldersignerassociationID',
                },
                'location_map': {
                    'pki_ezsignfoldersignerassociation_id': 'path',
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
        self.ezsignfoldersignerassociation_edit_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldersignerassociationEditObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}',
                'operation_id': 'ezsignfoldersignerassociation_edit_object_v1',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfoldersignerassociation_id',
                    'ezsignfoldersignerassociation_edit_object_v1_request',
                ],
                'required': [
                    'pki_ezsignfoldersignerassociation_id',
                    'ezsignfoldersignerassociation_edit_object_v1_request',
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
                    'pki_ezsignfoldersignerassociation_id':
                        (int,),
                    'ezsignfoldersignerassociation_edit_object_v1_request':
                        (EzsignfoldersignerassociationEditObjectV1Request,),
                },
                'attribute_map': {
                    'pki_ezsignfoldersignerassociation_id': 'pkiEzsignfoldersignerassociationID',
                },
                'location_map': {
                    'pki_ezsignfoldersignerassociation_id': 'path',
                    'ezsignfoldersignerassociation_edit_object_v1_request': 'body',
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
        self.ezsignfoldersignerassociation_get_in_person_login_url_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldersignerassociationGetInPersonLoginUrlV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/getInPersonLoginUrl',
                'operation_id': 'ezsignfoldersignerassociation_get_in_person_login_url_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfoldersignerassociation_id',
                ],
                'required': [
                    'pki_ezsignfoldersignerassociation_id',
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
                    'pki_ezsignfoldersignerassociation_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignfoldersignerassociation_id': 'pkiEzsignfoldersignerassociationID',
                },
                'location_map': {
                    'pki_ezsignfoldersignerassociation_id': 'path',
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
        self.ezsignfoldersignerassociation_get_object_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsignfoldersignerassociationGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}',
                'operation_id': 'ezsignfoldersignerassociation_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsignfoldersignerassociation_id',
                ],
                'required': [
                    'pki_ezsignfoldersignerassociation_id',
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
                    'pki_ezsignfoldersignerassociation_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsignfoldersignerassociation_id': 'pkiEzsignfoldersignerassociationID',
                },
                'location_map': {
                    'pki_ezsignfoldersignerassociation_id': 'path',
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

    def ezsignfoldersignerassociation_create_object_v1(
        self,
        ezsignfoldersignerassociation_create_object_v1_request,
        **kwargs
    ):
        """Create a new Ezsignfoldersignerassociation  # noqa: E501

        The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldersignerassociation_create_object_v1(ezsignfoldersignerassociation_create_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsignfoldersignerassociation_create_object_v1_request ([EzsignfoldersignerassociationCreateObjectV1Request]):

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
            EzsignfoldersignerassociationCreateObjectV1Response
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
        kwargs['ezsignfoldersignerassociation_create_object_v1_request'] = \
            ezsignfoldersignerassociation_create_object_v1_request
        return self.ezsignfoldersignerassociation_create_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignfoldersignerassociation_create_object_v2(
        self,
        ezsignfoldersignerassociation_create_object_v2_request,
        **kwargs
    ):
        """Create a new Ezsignfoldersignerassociation  # noqa: E501

        The endpoint allows to create one or many elements at once.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldersignerassociation_create_object_v2(ezsignfoldersignerassociation_create_object_v2_request, async_req=True)
        >>> result = thread.get()

        Args:
            ezsignfoldersignerassociation_create_object_v2_request (EzsignfoldersignerassociationCreateObjectV2Request):

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
            EzsignfoldersignerassociationCreateObjectV2Response
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
        kwargs['ezsignfoldersignerassociation_create_object_v2_request'] = \
            ezsignfoldersignerassociation_create_object_v2_request
        return self.ezsignfoldersignerassociation_create_object_v2_endpoint.call_with_http_info(**kwargs)

    def ezsignfoldersignerassociation_delete_object_v1(
        self,
        pki_ezsignfoldersignerassociation_id,
        **kwargs
    ):
        """Delete an existing Ezsignfoldersignerassociation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldersignerassociation_delete_object_v1(pki_ezsignfoldersignerassociation_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignfoldersignerassociation_id (int):

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
            EzsignfoldersignerassociationDeleteObjectV1Response
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
        kwargs['pki_ezsignfoldersignerassociation_id'] = \
            pki_ezsignfoldersignerassociation_id
        return self.ezsignfoldersignerassociation_delete_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignfoldersignerassociation_edit_object_v1(
        self,
        pki_ezsignfoldersignerassociation_id,
        ezsignfoldersignerassociation_edit_object_v1_request,
        **kwargs
    ):
        """Edit an existing Ezsignfoldersignerassociation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldersignerassociation_edit_object_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_edit_object_v1_request, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignfoldersignerassociation_id (int):
            ezsignfoldersignerassociation_edit_object_v1_request (EzsignfoldersignerassociationEditObjectV1Request):

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
            EzsignfoldersignerassociationEditObjectV1Response
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
        kwargs['pki_ezsignfoldersignerassociation_id'] = \
            pki_ezsignfoldersignerassociation_id
        kwargs['ezsignfoldersignerassociation_edit_object_v1_request'] = \
            ezsignfoldersignerassociation_edit_object_v1_request
        return self.ezsignfoldersignerassociation_edit_object_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignfoldersignerassociation_get_in_person_login_url_v1(
        self,
        pki_ezsignfoldersignerassociation_id,
        **kwargs
    ):
        """Retrieve a Login Url to allow In-Person signing  # noqa: E501

        This endpoint returns a Login Url that can be used in a browser or embedded in an I-Frame to allow in person signing.  The signer Login type must be configured as In-Person.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldersignerassociation_get_in_person_login_url_v1(pki_ezsignfoldersignerassociation_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignfoldersignerassociation_id (int):

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
            EzsignfoldersignerassociationGetInPersonLoginUrlV1Response
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
        kwargs['pki_ezsignfoldersignerassociation_id'] = \
            pki_ezsignfoldersignerassociation_id
        return self.ezsignfoldersignerassociation_get_in_person_login_url_v1_endpoint.call_with_http_info(**kwargs)

    def ezsignfoldersignerassociation_get_object_v1(
        self,
        pki_ezsignfoldersignerassociation_id,
        **kwargs
    ):
        """Retrieve an existing Ezsignfoldersignerassociation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsignfoldersignerassociation_get_object_v1(pki_ezsignfoldersignerassociation_id, async_req=True)
        >>> result = thread.get()

        Args:
            pki_ezsignfoldersignerassociation_id (int):

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
            EzsignfoldersignerassociationGetObjectV1Response
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
        kwargs['pki_ezsignfoldersignerassociation_id'] = \
            pki_ezsignfoldersignerassociation_id
        return self.ezsignfoldersignerassociation_get_object_v1_endpoint.call_with_http_info(**kwargs)

