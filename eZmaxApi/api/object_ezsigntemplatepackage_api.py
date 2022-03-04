"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.6
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
from eZmaxApi.model.ezsigntemplatepackage_get_list_v1_response import EzsigntemplatepackageGetListV1Response
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage


class ObjectEzsigntemplatepackageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ezsigntemplatepackage_get_list_v1_endpoint = _Endpoint(
            settings={
                'response_type': (EzsigntemplatepackageGetListV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/object/ezsigntemplatepackage/getList',
                'operation_id': 'ezsigntemplatepackage_get_list_v1',
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

                        "PKIEZSIGNTEMPLATEPACKAGEID_ASC": "pkiEzsigntemplatepackageID_ASC",
                        "PKIEZSIGNTEMPLATEPACKAGEID_DESC": "pkiEzsigntemplatepackageID_DESC",
                        "FKIDEPARTMENTID_ASC": "fkiDepartmentID_ASC",
                        "FKIDEPARTMENTID_DESC": "fkiDepartmentID_DESC",
                        "FKITEAMID_ASC": "fkiTeamID_ASC",
                        "FKITEAMID_DESC": "fkiTeamID_DESC",
                        "FKIEZSIGNFOLDERTYPEID_ASC": "fkiEzsignfoldertypeID_ASC",
                        "FKIEZSIGNFOLDERTYPEID_DESC": "fkiEzsignfoldertypeID_DESC",
                        "FKILANGUAGEID_ASC": "fkiLanguageID_ASC",
                        "FKILANGUAGEID_DESC": "fkiLanguageID_DESC",
                        "EEZSIGNTEMPLATEPACKAGETYPE_ASC": "eEzsigntemplatepackageType_ASC",
                        "EEZSIGNTEMPLATEPACKAGETYPE_DESC": "eEzsigntemplatepackageType_DESC",
                        "SEZSIGNTEMPLATEPACKAGEDESCRIPTION_ASC": "sEzsigntemplatepackageDescription_ASC",
                        "SEZSIGNTEMPLATEPACKAGEDESCRIPTION_DESC": "sEzsigntemplatepackageDescription_DESC",
                        "BEZSIGNTEMPLATEPACKAGEISACTIVE_ASC": "bEzsigntemplatepackageIsactive_ASC",
                        "BEZSIGNTEMPLATEPACKAGEISACTIVE_DESC": "bEzsigntemplatepackageIsactive_DESC",
                        "IEZSIGNTEMPLATEPACKAGEMEMBERSHIP_ASC": "iEzsigntemplatepackagemembership_ASC",
                        "IEZSIGNTEMPLATEPACKAGEMEMBERSHIP_DESC": "iEzsigntemplatepackagemembership_DESC"
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

    def ezsigntemplatepackage_get_list_v1(
        self,
        **kwargs
    ):
        """Retrieve Ezsigntemplatepackage list  # noqa: E501

        Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsigntemplatepackageType | Company<br>Department<br>Team<br>User<br>Usergroup |  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ezsigntemplatepackage_get_list_v1(async_req=True)
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
            async_req (bool): execute request asynchronously

        Returns:
            EzsigntemplatepackageGetListV1Response
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
        return self.ezsigntemplatepackage_get_list_v1_endpoint.call_with_http_info(**kwargs)

