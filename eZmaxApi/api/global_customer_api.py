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
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.global_customer_get_endpoint_v1_response import GlobalCustomerGetEndpointV1Response


class GlobalCustomerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.global_customer_get_endpoint_v1_endpoint = _Endpoint(
            settings={
                'response_type': (GlobalCustomerGetEndpointV1Response,),
                'auth': [
                    'Authorization'
                ],
                'endpoint_path': '/1/customer/{pksCustomerCode}/endpoint',
                'operation_id': 'global_customer_get_endpoint_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pks_customer_code',
                    's_infrastructureproduct_code',
                ],
                'required': [
                    'pks_customer_code',
                ],
                'nullable': [
                ],
                'enum': [
                    's_infrastructureproduct_code',
                ],
                'validation': [
                    'pks_customer_code',
                ]
            },
            root_map={
                'validations': {
                    ('pks_customer_code',): {
                        'max_length': 6,
                        'min_length': 2,
                    },
                },
                'allowed_values': {
                    ('s_infrastructureproduct_code',): {

                        "APPCLUSTER01": "appcluster01",
                        "EZSIGNUSER": "ezsignuser"
                    },
                },
                'openapi_types': {
                    'pks_customer_code':
                        (str,),
                    's_infrastructureproduct_code':
                        (str,),
                },
                'attribute_map': {
                    'pks_customer_code': 'pksCustomerCode',
                    's_infrastructureproduct_code': 'sInfrastructureproductCode',
                },
                'location_map': {
                    'pks_customer_code': 'path',
                    's_infrastructureproduct_code': 'query',
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

    def global_customer_get_endpoint_v1(
        self,
        pks_customer_code,
        **kwargs
    ):
        """Get customer endpoint  # noqa: E501

        Retrieve the customer's specific server endpoint where to send requests. This will help locate the proper region (ie: sInfrastructureregionCode) and the proper environment (ie: sInfrastructureenvironmenttypeDescription) where the customer's data is stored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.global_customer_get_endpoint_v1(pks_customer_code, async_req=True)
        >>> result = thread.get()

        Args:
            pks_customer_code (str):

        Keyword Args:
            s_infrastructureproduct_code (str): The infrastructure product Code  If undefined, \"appcluster01\" is assumed. [optional]
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
            GlobalCustomerGetEndpointV1Response
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
        kwargs['pks_customer_code'] = \
            pks_customer_code
        return self.global_customer_get_endpoint_v1_endpoint.call_with_http_info(**kwargs)

