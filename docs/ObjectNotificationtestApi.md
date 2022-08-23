# eZmaxApi.ObjectNotificationtestApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationtest_get_elements_v1**](ObjectNotificationtestApi.md#notificationtest_get_elements_v1) | **GET** /1/object/notificationtest/{pkiNotificationtestID}/getElements | Retrieve an existing Notificationtest&#39;s Elements


# **notificationtest_get_elements_v1**
> NotificationtestGetElementsV1Response notificationtest_get_elements_v1(pki_notificationtest_id)

Retrieve an existing Notificationtest's Elements



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_notificationtest_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.notificationtest_get_elements_v1_response import NotificationtestGetElementsV1Response
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
    api_instance = object_notificationtest_api.ObjectNotificationtestApi(api_client)
    pki_notificationtest_id = FieldPkiNotificationtestID(14) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Notificationtest's Elements
        api_response = api_instance.notificationtest_get_elements_v1(pki_notificationtest_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectNotificationtestApi->notificationtest_get_elements_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_notificationtest_id** | **int**|  |

### Return type

[**NotificationtestGetElementsV1Response**](NotificationtestGetElementsV1Response.md)

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

