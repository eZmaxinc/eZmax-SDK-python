# eZmaxApi.GlobalCustomerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_customer_get_endpoint_v1**](GlobalCustomerApi.md#global_customer_get_endpoint_v1) | **GET** /1/customer/{pksCustomerCode}/endpoint | Get customer endpoint


# **global_customer_get_endpoint_v1**
> GlobalCustomerGetEndpointV1Response global_customer_get_endpoint_v1(pks_customer_code, s_infrastructureproduct_code=s_infrastructureproduct_code)

Get customer endpoint

Retrieve the customer's specific server endpoint where to send requests. This will help locate the proper region (ie: sInfrastructureregionCode) and the proper environment (ie: sInfrastructureenvironmenttypeDescription) where the customer's data is stored.

### Example

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.global_customer_get_endpoint_v1_response import GlobalCustomerGetEndpointV1Response
from eZmaxApi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxApi.Configuration(
    host = "https://prod.api.appcluster01.ca-central-1.ezmax.com/rest"
)


# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.GlobalCustomerApi(api_client)
    pks_customer_code = 'pks_customer_code_example' # str | 
    s_infrastructureproduct_code = 's_infrastructureproduct_code_example' # str | The infrastructure product Code  If undefined, \"appcluster01\" is assumed (optional)

    try:
        # Get customer endpoint
        api_response = api_instance.global_customer_get_endpoint_v1(pks_customer_code, s_infrastructureproduct_code=s_infrastructureproduct_code)
        print("The response of GlobalCustomerApi->global_customer_get_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

