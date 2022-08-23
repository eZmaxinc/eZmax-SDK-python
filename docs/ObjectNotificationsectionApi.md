# eZmaxApi.ObjectNotificationsectionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationsection_get_notificationtests_v1**](ObjectNotificationsectionApi.md#notificationsection_get_notificationtests_v1) | **GET** /1/object/notificationsection/{pkiNotificationsectionID}/getNotificationtests | Retrieve an existing Notificationsection&#39;s Notificationtests


# **notificationsection_get_notificationtests_v1**
> NotificationsectionGetNotificationtestsV1Response notificationsection_get_notificationtests_v1(pki_notificationsection_id, b_show_hidden)

Retrieve an existing Notificationsection's Notificationtests



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_notificationsection_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.notificationsection_get_notificationtests_v1_response import NotificationsectionGetNotificationtestsV1Response
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
    api_instance = object_notificationsection_api.ObjectNotificationsectionApi(api_client)
    pki_notificationsection_id = FieldPkiNotificationsectionID(1) # int | 
    b_show_hidden = True # bool | Whether or not to return the hidden Notificationtests

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Notificationsection's Notificationtests
        api_response = api_instance.notificationsection_get_notificationtests_v1(pki_notificationsection_id, b_show_hidden)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectNotificationsectionApi->notificationsection_get_notificationtests_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_notificationsection_id** | **int**|  |
 **b_show_hidden** | **bool**| Whether or not to return the hidden Notificationtests |

### Return type

[**NotificationsectionGetNotificationtestsV1Response**](NotificationsectionGetNotificationtestsV1Response.md)

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

