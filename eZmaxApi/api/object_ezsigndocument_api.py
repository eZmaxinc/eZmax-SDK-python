"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.45
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
from eZmaxApi.model.ezsigndocument_apply_ezsigntemplate_v1_request import EzsigndocumentApplyEzsigntemplateV1Request
from eZmaxApi.model.ezsigndocument_apply_ezsigntemplate_v1_response import EzsigndocumentApplyEzsigntemplateV1Response
from eZmaxApi.model.ezsigndocument_create_object_v1_request import EzsigndocumentCreateObjectV1Request
from eZmaxApi.model.ezsigndocument_create_object_v1_response import EzsigndocumentCreateObjectV1Response
from eZmaxApi.model.ezsigndocument_delete_object_v1_response import EzsigndocumentDeleteObjectV1Response
from eZmaxApi.model.ezsigndocument_get_download_url_v1_response import EzsigndocumentGetDownloadUrlV1Response
from eZmaxApi.model.ezsigndocument_get_object_v1_response import EzsigndocumentGetObjectV1Response


class ObjectEzsigndocumentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __ezsigndocument_apply_ezsigntemplate_v1(
            self,
            pki_ezsigndocument_id,
            ezsigndocument_apply_ezsigntemplate_v1_request,
            **kwargs
        ):
            """Apply an Ezsign Template to the Ezsigndocument.  # noqa: E501

            This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsigndocument_apply_ezsigntemplate_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v1_request, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsigndocument_id (int): The unique ID of the Ezsigndocument
                ezsigndocument_apply_ezsigntemplate_v1_request (EzsigndocumentApplyEzsigntemplateV1Request):

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
                EzsigndocumentApplyEzsigntemplateV1Response
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
            kwargs['pki_ezsigndocument_id'] = \
                pki_ezsigndocument_id
            kwargs['ezsigndocument_apply_ezsigntemplate_v1_request'] = \
                ezsigndocument_apply_ezsigntemplate_v1_request
            return self.call_with_http_info(**kwargs)

        self.ezsigndocument_apply_ezsigntemplate_v1 = _Endpoint(
            settings={
                'response_type': (EzsigndocumentApplyEzsigntemplateV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate',
                'operation_id': 'ezsigndocument_apply_ezsigntemplate_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigndocument_id',
                    'ezsigndocument_apply_ezsigntemplate_v1_request',
                ],
                'required': [
                    'pki_ezsigndocument_id',
                    'ezsigndocument_apply_ezsigntemplate_v1_request',
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
                    'pki_ezsigndocument_id':
                        (int,),
                    'ezsigndocument_apply_ezsigntemplate_v1_request':
                        (EzsigndocumentApplyEzsigntemplateV1Request,),
                },
                'attribute_map': {
                    'pki_ezsigndocument_id': 'pkiEzsigndocumentID',
                },
                'location_map': {
                    'pki_ezsigndocument_id': 'path',
                    'ezsigndocument_apply_ezsigntemplate_v1_request': 'body',
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
            callable=__ezsigndocument_apply_ezsigntemplate_v1
        )

        def __ezsigndocument_create_object_v1(
            self,
            ezsigndocument_create_object_v1_request,
            **kwargs
        ):
            """Create a new Ezsigndocument  # noqa: E501

            The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsigndocument_create_object_v1(ezsigndocument_create_object_v1_request, async_req=True)
            >>> result = thread.get()

            Args:
                ezsigndocument_create_object_v1_request ([EzsigndocumentCreateObjectV1Request]):

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
                EzsigndocumentCreateObjectV1Response
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
            kwargs['ezsigndocument_create_object_v1_request'] = \
                ezsigndocument_create_object_v1_request
            return self.call_with_http_info(**kwargs)

        self.ezsigndocument_create_object_v1 = _Endpoint(
            settings={
                'response_type': (EzsigndocumentCreateObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigndocument',
                'operation_id': 'ezsigndocument_create_object_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ezsigndocument_create_object_v1_request',
                ],
                'required': [
                    'ezsigndocument_create_object_v1_request',
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
                    'ezsigndocument_create_object_v1_request':
                        ([EzsigndocumentCreateObjectV1Request],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ezsigndocument_create_object_v1_request': 'body',
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
            callable=__ezsigndocument_create_object_v1
        )

        def __ezsigndocument_delete_object_v1(
            self,
            pki_ezsigndocument_id,
            **kwargs
        ):
            """Delete an existing Ezsigndocument  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsigndocument_delete_object_v1(pki_ezsigndocument_id, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsigndocument_id (int): The unique ID of the Ezsigndocument

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
                EzsigndocumentDeleteObjectV1Response
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
            kwargs['pki_ezsigndocument_id'] = \
                pki_ezsigndocument_id
            return self.call_with_http_info(**kwargs)

        self.ezsigndocument_delete_object_v1 = _Endpoint(
            settings={
                'response_type': (EzsigndocumentDeleteObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigndocument/{pkiEzsigndocumentID}',
                'operation_id': 'ezsigndocument_delete_object_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigndocument_id',
                ],
                'required': [
                    'pki_ezsigndocument_id',
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
                    'pki_ezsigndocument_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigndocument_id': 'pkiEzsigndocumentID',
                },
                'location_map': {
                    'pki_ezsigndocument_id': 'path',
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
            callable=__ezsigndocument_delete_object_v1
        )

        def __ezsigndocument_get_children_v1(
            self,
            pki_ezsigndocument_id,
            **kwargs
        ):
            """Retrieve an existing Ezsigndocument's children IDs  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsigndocument_get_children_v1(pki_ezsigndocument_id, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsigndocument_id (int): The unique ID of the Ezsigndocument

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
            kwargs['pki_ezsigndocument_id'] = \
                pki_ezsigndocument_id
            return self.call_with_http_info(**kwargs)

        self.ezsigndocument_get_children_v1 = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigndocument/{pkiEzsigndocumentID}/getChildren',
                'operation_id': 'ezsigndocument_get_children_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigndocument_id',
                ],
                'required': [
                    'pki_ezsigndocument_id',
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
                    'pki_ezsigndocument_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigndocument_id': 'pkiEzsigndocumentID',
                },
                'location_map': {
                    'pki_ezsigndocument_id': 'path',
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
            callable=__ezsigndocument_get_children_v1
        )

        def __ezsigndocument_get_download_url_v1(
            self,
            pki_ezsigndocument_id,
            e_document_type,
            **kwargs
        ):
            """Retrieve a URL to download documents.  # noqa: E501

            This endpoint returns URLs to different files that can be downloaded during the signing process.  These links will expire after 5 minutes so the download of the file should be made soon after retrieving the link.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsigndocument_id (int): The unique ID of the Ezsigndocument
                e_document_type (str): The type of document to retrieve.  1. **Initial** Is the initial document before any signature were applied. 2. **Signed** Is the final document once all signatures were applied. 3. **Proofdocument** Is the evidence report. 4. **Proof** Is the complete evidence archive including all of the above and more. 

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
                EzsigndocumentGetDownloadUrlV1Response
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
            kwargs['pki_ezsigndocument_id'] = \
                pki_ezsigndocument_id
            kwargs['e_document_type'] = \
                e_document_type
            return self.call_with_http_info(**kwargs)

        self.ezsigndocument_get_download_url_v1 = _Endpoint(
            settings={
                'response_type': (EzsigndocumentGetDownloadUrlV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigndocument/{pkiEzsigndocumentID}/getDownloadUrl/{eDocumentType}',
                'operation_id': 'ezsigndocument_get_download_url_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigndocument_id',
                    'e_document_type',
                ],
                'required': [
                    'pki_ezsigndocument_id',
                    'e_document_type',
                ],
                'nullable': [
                ],
                'enum': [
                    'e_document_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('e_document_type',): {

                        "INITIAL": "Initial",
                        "SIGNED": "Signed",
                        "PROOF": "Proof",
                        "PROOFDOCUMENT": "Proofdocument"
                    },
                },
                'openapi_types': {
                    'pki_ezsigndocument_id':
                        (int,),
                    'e_document_type':
                        (str,),
                },
                'attribute_map': {
                    'pki_ezsigndocument_id': 'pkiEzsigndocumentID',
                    'e_document_type': 'eDocumentType',
                },
                'location_map': {
                    'pki_ezsigndocument_id': 'path',
                    'e_document_type': 'path',
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
            callable=__ezsigndocument_get_download_url_v1
        )

        def __ezsigndocument_get_object_v1(
            self,
            pki_ezsigndocument_id,
            **kwargs
        ):
            """Retrieve an existing Ezsigndocument  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ezsigndocument_get_object_v1(pki_ezsigndocument_id, async_req=True)
            >>> result = thread.get()

            Args:
                pki_ezsigndocument_id (int): The unique ID of the Ezsigndocument

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
                EzsigndocumentGetObjectV1Response
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
            kwargs['pki_ezsigndocument_id'] = \
                pki_ezsigndocument_id
            return self.call_with_http_info(**kwargs)

        self.ezsigndocument_get_object_v1 = _Endpoint(
            settings={
                'response_type': (EzsigndocumentGetObjectV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigndocument/{pkiEzsigndocumentID}',
                'operation_id': 'ezsigndocument_get_object_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pki_ezsigndocument_id',
                ],
                'required': [
                    'pki_ezsigndocument_id',
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
                    'pki_ezsigndocument_id':
                        (int,),
                },
                'attribute_map': {
                    'pki_ezsigndocument_id': 'pkiEzsigndocumentID',
                },
                'location_map': {
                    'pki_ezsigndocument_id': 'path',
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
            callable=__ezsigndocument_get_object_v1
        )
