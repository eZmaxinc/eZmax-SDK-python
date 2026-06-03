# eZmaxApi.ModuleEzmaxmaillinglistApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezmaxmaillinglist_subscribe_v1**](ModuleEzmaxmaillinglistApi.md#ezmaxmaillinglist_subscribe_v1) | **POST** /1/module/ezmaxmaillinglist/subscribe | Subscribe to specific Ezmaxmaillinglist


# **ezmaxmaillinglist_subscribe_v1**
> EzmaxmaillinglistSubscribeV1Response ezmaxmaillinglist_subscribe_v1(ezmaxmaillinglist_subscribe_v1_request)

Subscribe to specific Ezmaxmaillinglist

Users can subscribe to specific Ezmaxmaillinglist

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxmaillinglist_subscribe_v1_request import EzmaxmaillinglistSubscribeV1Request
from eZmaxApi.models.ezmaxmaillinglist_subscribe_v1_response import EzmaxmaillinglistSubscribeV1Response
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
    api_instance = eZmaxApi.ModuleEzmaxmaillinglistApi(api_client)
    ezmaxmaillinglist_subscribe_v1_request = eZmaxApi.EzmaxmaillinglistSubscribeV1Request() # EzmaxmaillinglistSubscribeV1Request | 

    try:
        # Subscribe to specific Ezmaxmaillinglist
        api_response = api_instance.ezmaxmaillinglist_subscribe_v1(ezmaxmaillinglist_subscribe_v1_request)
        print("The response of ModuleEzmaxmaillinglistApi->ezmaxmaillinglist_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleEzmaxmaillinglistApi->ezmaxmaillinglist_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezmaxmaillinglist_subscribe_v1_request** | [**EzmaxmaillinglistSubscribeV1Request**](EzmaxmaillinglistSubscribeV1Request.md)|  | 

### Return type

[**EzmaxmaillinglistSubscribeV1Response**](EzmaxmaillinglistSubscribeV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

