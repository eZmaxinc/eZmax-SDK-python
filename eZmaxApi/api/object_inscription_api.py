# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import conint

from eZmaxApi.models.inscription_get_communication_list_v1_response import InscriptionGetCommunicationListV1Response

from eZmaxApi.api_client import ApiClient
from eZmaxApi.api_response import ApiResponse
from eZmaxApi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ObjectInscriptionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def inscription_get_communication_list_v1(self, pki_inscription_id : conint(strict=True, ge=0), **kwargs) -> InscriptionGetCommunicationListV1Response:  # noqa: E501
        """Retrieve Communication list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.inscription_get_communication_list_v1(pki_inscription_id, async_req=True)
        >>> result = thread.get()

        :param pki_inscription_id: (required)
        :type pki_inscription_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InscriptionGetCommunicationListV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the inscription_get_communication_list_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.inscription_get_communication_list_v1_with_http_info(pki_inscription_id, **kwargs)  # noqa: E501

    @validate_arguments
    def inscription_get_communication_list_v1_with_http_info(self, pki_inscription_id : conint(strict=True, ge=0), **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve Communication list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.inscription_get_communication_list_v1_with_http_info(pki_inscription_id, async_req=True)
        >>> result = thread.get()

        :param pki_inscription_id: (required)
        :type pki_inscription_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InscriptionGetCommunicationListV1Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pki_inscription_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inscription_get_communication_list_v1" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['pki_inscription_id']:
            _path_params['pkiInscriptionID'] = _params['pki_inscription_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Authorization']  # noqa: E501

        _response_types_map = {
            '200': "InscriptionGetCommunicationListV1Response",
            '404': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/1/object/inscription/{pkiInscriptionID}/getCommunicationList', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
