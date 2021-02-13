# eZmaxinc/eZmax-SDK-python.ModuleSsprApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sspr_remind_usernames_v1**](ModuleSsprApi.md#sspr_remind_usernames_v1) | **POST** /1/module/sspr/remindUsernames | Remind of forgotten username(s)


# **sspr_remind_usernames_v1**
> sspr_remind_usernames_v1()

Remind of forgotten username(s)

This endpoint returns an email with the username(s) matching the email address provided in case of forgotten username

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = module_sspr_api.ModuleSsprApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Remind of forgotten username(s)
        api_instance.sspr_remind_usernames_v1()
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_remind_usernames_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was accepted.  Do not misinterpret as \&quot;the email address has an account attached to it\&quot;. It only means an email will be sent if (and only if) an account exists for that email address. |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

