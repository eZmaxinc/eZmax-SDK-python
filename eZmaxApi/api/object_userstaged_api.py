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

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conint

from typing import Any, Dict, Optional

from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.userstaged_create_user_v1_response import UserstagedCreateUserV1Response
from eZmaxApi.models.userstaged_delete_object_v1_response import UserstagedDeleteObjectV1Response
from eZmaxApi.models.userstaged_get_list_v1_response import UserstagedGetListV1Response
from eZmaxApi.models.userstaged_get_object_v2_response import UserstagedGetObjectV2Response
from eZmaxApi.models.userstaged_map_v1_request import UserstagedMapV1Request
from eZmaxApi.models.userstaged_map_v1_response import UserstagedMapV1Response

from eZmaxApi.api_client import ApiClient
from eZmaxApi.api_response import ApiResponse
from eZmaxApi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ObjectUserstagedApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def userstaged_create_user_v1(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), body : Dict[str, Any], **kwargs) -> UserstagedCreateUserV1Response:  # noqa: E501
        """Create a User from a Userstaged and then map it  # noqa: E501

        Default values will be used while creating the User. If you need to change those values, you should use the route to edit a User.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_create_user_v1(pki_userstaged_id, body, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
        :param body: (required)
        :type body: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserstagedCreateUserV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the userstaged_create_user_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.userstaged_create_user_v1_with_http_info(pki_userstaged_id, body, **kwargs)  # noqa: E501

    @validate_arguments
    def userstaged_create_user_v1_with_http_info(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), body : Dict[str, Any], **kwargs) -> ApiResponse:  # noqa: E501
        """Create a User from a Userstaged and then map it  # noqa: E501

        Default values will be used while creating the User. If you need to change those values, you should use the route to edit a User.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_create_user_v1_with_http_info(pki_userstaged_id, body, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
        :param body: (required)
        :type body: object
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
        :rtype: tuple(UserstagedCreateUserV1Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pki_userstaged_id',
            'body'
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
                    " to method userstaged_create_user_v1" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['pki_userstaged_id']:
            _path_params['pkiUserstagedID'] = _params['pki_userstaged_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Authorization']  # noqa: E501

        _response_types_map = {
            '200': "UserstagedCreateUserV1Response",
            '404': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/1/object/userstaged/{pkiUserstagedID}/createUser', 'POST',
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

    @validate_arguments
    def userstaged_delete_object_v1(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), **kwargs) -> UserstagedDeleteObjectV1Response:  # noqa: E501
        """Delete an existing Userstaged  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_delete_object_v1(pki_userstaged_id, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserstagedDeleteObjectV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the userstaged_delete_object_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.userstaged_delete_object_v1_with_http_info(pki_userstaged_id, **kwargs)  # noqa: E501

    @validate_arguments
    def userstaged_delete_object_v1_with_http_info(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), **kwargs) -> ApiResponse:  # noqa: E501
        """Delete an existing Userstaged  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_delete_object_v1_with_http_info(pki_userstaged_id, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
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
        :rtype: tuple(UserstagedDeleteObjectV1Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pki_userstaged_id'
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
                    " to method userstaged_delete_object_v1" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['pki_userstaged_id']:
            _path_params['pkiUserstagedID'] = _params['pki_userstaged_id']


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
            '200': "UserstagedDeleteObjectV1Response",
            '404': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/1/object/userstaged/{pkiUserstagedID}', 'DELETE',
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

    @validate_arguments
    def userstaged_get_list_v1(self, e_order_by : Annotated[Optional[StrictStr], Field(description="Specify how you want the results to be sorted")] = None, i_row_max : Optional[conint(strict=True, le=10000, ge=1)] = None, i_row_offset : Optional[conint(strict=True, ge=0)] = None, accept_language : Optional[HeaderAcceptLanguage] = None, s_filter : Optional[StrictStr] = None, **kwargs) -> UserstagedGetListV1Response:  # noqa: E501
        """Retrieve Userstaged list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_get_list_v1(e_order_by, i_row_max, i_row_offset, accept_language, s_filter, async_req=True)
        >>> result = thread.get()

        :param e_order_by: Specify how you want the results to be sorted
        :type e_order_by: str
        :param i_row_max:
        :type i_row_max: int
        :param i_row_offset:
        :type i_row_offset: int
        :param accept_language:
        :type accept_language: HeaderAcceptLanguage
        :param s_filter:
        :type s_filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserstagedGetListV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the userstaged_get_list_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.userstaged_get_list_v1_with_http_info(e_order_by, i_row_max, i_row_offset, accept_language, s_filter, **kwargs)  # noqa: E501

    @validate_arguments
    def userstaged_get_list_v1_with_http_info(self, e_order_by : Annotated[Optional[StrictStr], Field(description="Specify how you want the results to be sorted")] = None, i_row_max : Optional[conint(strict=True, le=10000, ge=1)] = None, i_row_offset : Optional[conint(strict=True, ge=0)] = None, accept_language : Optional[HeaderAcceptLanguage] = None, s_filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve Userstaged list  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_get_list_v1_with_http_info(e_order_by, i_row_max, i_row_offset, accept_language, s_filter, async_req=True)
        >>> result = thread.get()

        :param e_order_by: Specify how you want the results to be sorted
        :type e_order_by: str
        :param i_row_max:
        :type i_row_max: int
        :param i_row_offset:
        :type i_row_offset: int
        :param accept_language:
        :type accept_language: HeaderAcceptLanguage
        :param s_filter:
        :type s_filter: str
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
        :rtype: tuple(UserstagedGetListV1Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'e_order_by',
            'i_row_max',
            'i_row_offset',
            'accept_language',
            's_filter'
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
                    " to method userstaged_get_list_v1" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('e_order_by') is not None:  # noqa: E501
            _query_params.append(('eOrderBy', _params['e_order_by']))

        if _params.get('i_row_max') is not None:  # noqa: E501
            _query_params.append(('iRowMax', _params['i_row_max']))

        if _params.get('i_row_offset') is not None:  # noqa: E501
            _query_params.append(('iRowOffset', _params['i_row_offset']))

        if _params.get('s_filter') is not None:  # noqa: E501
            _query_params.append(('sFilter', _params['s_filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['accept_language']:
            _header_params['Accept-Language'] = _params['accept_language']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Authorization']  # noqa: E501

        _response_types_map = {
            '200': "UserstagedGetListV1Response",
            '406': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/1/object/userstaged/getList', 'GET',
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

    @validate_arguments
    def userstaged_get_object_v2(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), **kwargs) -> UserstagedGetObjectV2Response:  # noqa: E501
        """Retrieve an existing Userstaged  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_get_object_v2(pki_userstaged_id, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserstagedGetObjectV2Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the userstaged_get_object_v2_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.userstaged_get_object_v2_with_http_info(pki_userstaged_id, **kwargs)  # noqa: E501

    @validate_arguments
    def userstaged_get_object_v2_with_http_info(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve an existing Userstaged  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_get_object_v2_with_http_info(pki_userstaged_id, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
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
        :rtype: tuple(UserstagedGetObjectV2Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pki_userstaged_id'
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
                    " to method userstaged_get_object_v2" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['pki_userstaged_id']:
            _path_params['pkiUserstagedID'] = _params['pki_userstaged_id']


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
            '200': "UserstagedGetObjectV2Response",
            '404': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/2/object/userstaged/{pkiUserstagedID}', 'GET',
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

    @validate_arguments
    def userstaged_map_v1(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), userstaged_map_v1_request : UserstagedMapV1Request, **kwargs) -> UserstagedMapV1Response:  # noqa: E501
        """Map the Userstaged to an existing user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_map_v1(pki_userstaged_id, userstaged_map_v1_request, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
        :param userstaged_map_v1_request: (required)
        :type userstaged_map_v1_request: UserstagedMapV1Request
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserstagedMapV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the userstaged_map_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.userstaged_map_v1_with_http_info(pki_userstaged_id, userstaged_map_v1_request, **kwargs)  # noqa: E501

    @validate_arguments
    def userstaged_map_v1_with_http_info(self, pki_userstaged_id : conint(strict=True, le=65535, ge=1), userstaged_map_v1_request : UserstagedMapV1Request, **kwargs) -> ApiResponse:  # noqa: E501
        """Map the Userstaged to an existing user  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.userstaged_map_v1_with_http_info(pki_userstaged_id, userstaged_map_v1_request, async_req=True)
        >>> result = thread.get()

        :param pki_userstaged_id: (required)
        :type pki_userstaged_id: int
        :param userstaged_map_v1_request: (required)
        :type userstaged_map_v1_request: UserstagedMapV1Request
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
        :rtype: tuple(UserstagedMapV1Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pki_userstaged_id',
            'userstaged_map_v1_request'
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
                    " to method userstaged_map_v1" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['pki_userstaged_id']:
            _path_params['pkiUserstagedID'] = _params['pki_userstaged_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['userstaged_map_v1_request'] is not None:
            _body_params = _params['userstaged_map_v1_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Authorization']  # noqa: E501

        _response_types_map = {
            '200': "UserstagedMapV1Response",
            '404': "CommonResponseError",
            '422': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/1/object/userstaged/{pkiUserstagedID}/map', 'POST',
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