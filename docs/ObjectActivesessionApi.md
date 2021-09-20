# eZmaxApi.ObjectActivesessionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activesession_get_current_v1**](ObjectActivesessionApi.md#activesession_get_current_v1) | **GET** /1/object/activesession/getCurrent | Get Current Activesession


# **activesession_get_current_v1**
> ActivesessionGetCurrentV1Response activesession_get_current_v1()

Get Current Activesession

Retrieve the details about the current activesession

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_activesession_api
from eZmaxApi.model.activesession_get_current_v1_response import ActivesessionGetCurrentV1Response
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
    api_instance = object_activesession_api.ObjectActivesessionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Current Activesession
        api_response = api_instance.activesession_get_current_v1()
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectActivesessionApi->activesession_get_current_v1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ActivesessionGetCurrentV1Response**](ActivesessionGetCurrentV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

