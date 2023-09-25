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

from typing import Optional

from eZmaxApi.models.activesession_get_current_v1_response import ActivesessionGetCurrentV1Response
from eZmaxApi.models.activesession_get_list_v1_response import ActivesessionGetListV1Response
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage

from eZmaxApi.api_client import ApiClient
from eZmaxApi.api_response import ApiResponse
from eZmaxApi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ObjectActivesessionApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def activesession_get_current_v1(self, **kwargs) -> ActivesessionGetCurrentV1Response:  # noqa: E501
        """Get Current Activesession  # noqa: E501

        Retrieve the details about the current activesession  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.activesession_get_current_v1(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ActivesessionGetCurrentV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the activesession_get_current_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.activesession_get_current_v1_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def activesession_get_current_v1_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Current Activesession  # noqa: E501

        Retrieve the details about the current activesession  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.activesession_get_current_v1_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(ActivesessionGetCurrentV1Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method activesession_get_current_v1" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

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
            '200': "ActivesessionGetCurrentV1Response",
            '350': None,
            '351': None,
            '352': "CommonResponseRedirectSSecretquestionTextX",
            '353': None,
            '354': None,
            '355': None,
            '356': None,
        }

        return self.api_client.call_api(
            '/1/object/activesession/getCurrent', 'GET',
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
    def activesession_get_list_v1(self, e_order_by : Annotated[Optional[StrictStr], Field(description="Specify how you want the results to be sorted")] = None, i_row_max : Optional[conint(strict=True, le=10000, ge=1)] = None, i_row_offset : Optional[conint(strict=True, ge=0)] = None, accept_language : Optional[HeaderAcceptLanguage] = None, s_filter : Optional[StrictStr] = None, **kwargs) -> ActivesessionGetListV1Response:  # noqa: E501
        """Retrieve Activesession list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.activesession_get_list_v1(e_order_by, i_row_max, i_row_offset, accept_language, s_filter, async_req=True)
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
        :rtype: ActivesessionGetListV1Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the activesession_get_list_v1_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.activesession_get_list_v1_with_http_info(e_order_by, i_row_max, i_row_offset, accept_language, s_filter, **kwargs)  # noqa: E501

    @validate_arguments
    def activesession_get_list_v1_with_http_info(self, e_order_by : Annotated[Optional[StrictStr], Field(description="Specify how you want the results to be sorted")] = None, i_row_max : Optional[conint(strict=True, le=10000, ge=1)] = None, i_row_offset : Optional[conint(strict=True, ge=0)] = None, accept_language : Optional[HeaderAcceptLanguage] = None, s_filter : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve Activesession list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.activesession_get_list_v1_with_http_info(e_order_by, i_row_max, i_row_offset, accept_language, s_filter, async_req=True)
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
        :rtype: tuple(ActivesessionGetListV1Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method activesession_get_list_v1" % _key
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
            '200': "ActivesessionGetListV1Response",
            '406': "CommonResponseError",
        }

        return self.api_client.call_api(
            '/1/object/activesession/getList', 'GET',
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
