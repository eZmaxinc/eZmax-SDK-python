# eZmaxApi.ObjectCommunicationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communication_get_object_v2**](ObjectCommunicationApi.md#communication_get_object_v2) | **GET** /2/object/communication/{pkiCommunicationID} | Retrieve an existing Communication


# **communication_get_object_v2**
> CommunicationGetObjectV2Response communication_get_object_v2(pki_communication_id)

Retrieve an existing Communication



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.communication_get_object_v2_response import CommunicationGetObjectV2Response
from eZmaxApi.rest import ApiException
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
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ObjectCommunicationApi(api_client)
    pki_communication_id = 56 # int | 

    try:
        # Retrieve an existing Communication
        api_response = api_instance.communication_get_object_v2(pki_communication_id)
        print("The response of ObjectCommunicationApi->communication_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommunicationApi->communication_get_object_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_communication_id** | **int**|  | 

### Return type

[**CommunicationGetObjectV2Response**](CommunicationGetObjectV2Response.md)

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

