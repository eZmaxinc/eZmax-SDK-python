# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response import BillingentityexternalGetAutocompleteV2Response
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage

from eZmaxApi.api_client import ApiClient, RequestSerialized
from eZmaxApi.api_response import ApiResponse
from eZmaxApi.rest import RESTResponseType


class ObjectBillingentityexternalApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def billingentityexternal_get_autocomplete_v2(
        self,
        s_selector: Annotated[StrictStr, Field(description="The type of Billingentityexternals to return")],
        e_filter_active: Annotated[Optional[StrictStr], Field(description="Specify which results we want to display.")] = None,
        s_query: Annotated[Optional[StrictStr], Field(description="Allow to filter the returned results")] = None,
        accept_language: Optional[HeaderAcceptLanguage] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BillingentityexternalGetAutocompleteV2Response:
        """Retrieve Billingentityexternals and IDs

        Get the list of Billingentityexternal to be used in a dropdown or autocomplete control.

        :param s_selector: The type of Billingentityexternals to return (required)
        :type s_selector: str
        :param e_filter_active: Specify which results we want to display.
        :type e_filter_active: str
        :param s_query: Allow to filter the returned results
        :type s_query: str
        :param accept_language:
        :type accept_language: HeaderAcceptLanguage
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._billingentityexternal_get_autocomplete_v2_serialize(
            s_selector=s_selector,
            e_filter_active=e_filter_active,
            s_query=s_query,
            accept_language=accept_language,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BillingentityexternalGetAutocompleteV2Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def billingentityexternal_get_autocomplete_v2_with_http_info(
        self,
        s_selector: Annotated[StrictStr, Field(description="The type of Billingentityexternals to return")],
        e_filter_active: Annotated[Optional[StrictStr], Field(description="Specify which results we want to display.")] = None,
        s_query: Annotated[Optional[StrictStr], Field(description="Allow to filter the returned results")] = None,
        accept_language: Optional[HeaderAcceptLanguage] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[BillingentityexternalGetAutocompleteV2Response]:
        """Retrieve Billingentityexternals and IDs

        Get the list of Billingentityexternal to be used in a dropdown or autocomplete control.

        :param s_selector: The type of Billingentityexternals to return (required)
        :type s_selector: str
        :param e_filter_active: Specify which results we want to display.
        :type e_filter_active: str
        :param s_query: Allow to filter the returned results
        :type s_query: str
        :param accept_language:
        :type accept_language: HeaderAcceptLanguage
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._billingentityexternal_get_autocomplete_v2_serialize(
            s_selector=s_selector,
            e_filter_active=e_filter_active,
            s_query=s_query,
            accept_language=accept_language,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BillingentityexternalGetAutocompleteV2Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def billingentityexternal_get_autocomplete_v2_without_preload_content(
        self,
        s_selector: Annotated[StrictStr, Field(description="The type of Billingentityexternals to return")],
        e_filter_active: Annotated[Optional[StrictStr], Field(description="Specify which results we want to display.")] = None,
        s_query: Annotated[Optional[StrictStr], Field(description="Allow to filter the returned results")] = None,
        accept_language: Optional[HeaderAcceptLanguage] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve Billingentityexternals and IDs

        Get the list of Billingentityexternal to be used in a dropdown or autocomplete control.

        :param s_selector: The type of Billingentityexternals to return (required)
        :type s_selector: str
        :param e_filter_active: Specify which results we want to display.
        :type e_filter_active: str
        :param s_query: Allow to filter the returned results
        :type s_query: str
        :param accept_language:
        :type accept_language: HeaderAcceptLanguage
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._billingentityexternal_get_autocomplete_v2_serialize(
            s_selector=s_selector,
            e_filter_active=e_filter_active,
            s_query=s_query,
            accept_language=accept_language,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BillingentityexternalGetAutocompleteV2Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _billingentityexternal_get_autocomplete_v2_serialize(
        self,
        s_selector,
        e_filter_active,
        s_query,
        accept_language,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if s_selector is not None:
            _path_params['sSelector'] = s_selector
        # process the query parameters
        if e_filter_active is not None:
            
            _query_params.append(('eFilterActive', e_filter_active))
            
        if s_query is not None:
            
            _query_params.append(('sQuery', s_query))
            
        # process the header parameters
        if accept_language is not None:
            _header_params['Accept-Language'] = accept_language
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'Authorization'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/2/object/billingentityexternal/getAutocomplete/{sSelector}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


