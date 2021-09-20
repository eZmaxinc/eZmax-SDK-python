# eZmaxApi.ModuleUserApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create_ezsignuser_v1**](ModuleUserApi.md#user_create_ezsignuser_v1) | **POST** /1/module/user/createezsignuser | Create a new User of type Ezsignuser


# **user_create_ezsignuser_v1**
> UserCreateEzsignuserV1Response user_create_ezsignuser_v1(user_create_ezsignuser_v1_request)

Create a new User of type Ezsignuser

The endpoint allows to initiate the creation or a user of type Ezsignuser.  The user will be created only once the email verification process will be completed

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import module_user_api
from eZmaxApi.model.user_create_ezsignuser_v1_request import UserCreateEzsignuserV1Request
from eZmaxApi.model.user_create_ezsignuser_v1_response import UserCreateEzsignuserV1Response
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
    api_instance = module_user_api.ModuleUserApi(api_client)
    user_create_ezsignuser_v1_request = [
        UserCreateEzsignuserV1Request(
            fki_language_id=FieldPkiLanguageID(2),
            s_user_firstname="John",
            s_user_lastname="Doe",
            s_email_address="example@domain.com",
            s_phone_region="514",
            s_phone_exchange="990",
            s_phone_number="1516",
            s_phone_extension="123",
        ),
    ] # [UserCreateEzsignuserV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new User of type Ezsignuser
        api_response = api_instance.user_create_ezsignuser_v1(user_create_ezsignuser_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ModuleUserApi->user_create_ezsignuser_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_ezsignuser_v1_request** | [**[UserCreateEzsignuserV1Request]**](UserCreateEzsignuserV1Request.md)|  |

### Return type

[**UserCreateEzsignuserV1Response**](UserCreateEzsignuserV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

