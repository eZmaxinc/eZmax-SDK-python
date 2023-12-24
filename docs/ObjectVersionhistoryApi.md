# eZmaxApi.ObjectVersionhistoryApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**versionhistory_get_object_v2**](ObjectVersionhistoryApi.md#versionhistory_get_object_v2) | **GET** /2/object/versionhistory/{pkiVersionhistoryID} | Retrieve an existing Versionhistory


# **versionhistory_get_object_v2**
> VersionhistoryGetObjectV2Response versionhistory_get_object_v2(pki_versionhistory_id)

Retrieve an existing Versionhistory



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.versionhistory_get_object_v2_response import VersionhistoryGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectVersionhistoryApi(api_client)
    pki_versionhistory_id = 56 # int | 

    try:
        # Retrieve an existing Versionhistory
        api_response = api_instance.versionhistory_get_object_v2(pki_versionhistory_id)
        print("The response of ObjectVersionhistoryApi->versionhistory_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectVersionhistoryApi->versionhistory_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_versionhistory_id** | **int**|  | 

### Return type

[**VersionhistoryGetObjectV2Response**](VersionhistoryGetObjectV2Response.md)

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

