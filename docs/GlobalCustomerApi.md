# eZmaxApi.GlobalCustomerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_customer_get_endpoint_v1**](GlobalCustomerApi.md#global_customer_get_endpoint_v1) | **GET** /1/customer/{pksCustomerCode}/endpoint | Get customer endpoint


# **global_customer_get_endpoint_v1**
> GlobalCustomerGetEndpointV1Response global_customer_get_endpoint_v1(pks_customer_code)

Get customer endpoint

Retrieve the customer's specific server endpoint where to send requests. This will help locate the proper region (ie: sInfrastructureregionCode) and the proper environment (ie: sInfrastructureenvironmenttypeDescription) where the customer's data is stored.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import global_customer_api
from eZmaxApi.model.global_customer_get_endpoint_v1_response import GlobalCustomerGetEndpointV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxApi.Configuration(
    host = "https://prod.api.appcluster01.ca-central-1.ezmax.com/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = global_customer_api.GlobalCustomerApi(api_client)
    pks_customer_code = FieldPksCustomerCode("demo") # str | 
    s_infrastructureproduct_code = "appcluster01" # str | The infrastructure product Code  If undefined, \"appcluster01\" is assumed (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get customer endpoint
        api_response = api_instance.global_customer_get_endpoint_v1(pks_customer_code)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling GlobalCustomerApi->global_customer_get_endpoint_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get customer endpoint
        api_response = api_instance.global_customer_get_endpoint_v1(pks_customer_code, s_infrastructureproduct_code=s_infrastructureproduct_code)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling GlobalCustomerApi->global_customer_get_endpoint_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pks_customer_code** | **str**|  |
 **s_infrastructureproduct_code** | **str**| The infrastructure product Code  If undefined, \&quot;appcluster01\&quot; is assumed | [optional]

### Return type

[**GlobalCustomerGetEndpointV1Response**](GlobalCustomerGetEndpointV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

