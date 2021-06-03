# eZmaxApi.ModuleAuthenticateApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_authenticate_v2**](ModuleAuthenticateApi.md#authenticate_authenticate_v2) | **POST** /2/module/authenticate/authenticate/{eSessionType} | Authenticate a user


# **authenticate_authenticate_v2**
> AuthenticateAuthenticateV2Response authenticate_authenticate_v2(authenticate_authenticate_v2_request)

Authenticate a user

This endpoint authenticates a user.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxApi
from eZmaxApi.api import module_authenticate_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.authenticate_authenticate_v2_response import AuthenticateAuthenticateV2Response
from eZmaxApi.model.authenticate_authenticate_v2_request import AuthenticateAuthenticateV2Request
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
    api_instance = module_authenticate_api.ModuleAuthenticateApi(api_client)
    authenticate_authenticate_v2_request = AuthenticateAuthenticateV2Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        s_email_address="example@domain.com",
        s_user_loginname="JohnDoe",
        s_password="Qwerty1234!",
        s_password_encrypted="VGhpcyBpcyBhbiBlbmNyeXB0ZWQgcGFzc3dvcmQ=",
    ) # AuthenticateAuthenticateV2Request | 

    # example passing only required values which don't have defaults set
    try:
        # Authenticate a user
        api_response = api_instance.authenticate_authenticate_v2(authenticate_authenticate_v2_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ModuleAuthenticateApi->authenticate_authenticate_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticate_authenticate_v2_request** | [**AuthenticateAuthenticateV2Request**](AuthenticateAuthenticateV2Request.md)|  |
 **e_session_type** | **str**|  | defaults to "ezsignuser"

### Return type

[**AuthenticateAuthenticateV2Response**](AuthenticateAuthenticateV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

