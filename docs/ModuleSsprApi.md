# eZmaxinc/eZmax-SDK-python.ModuleSsprApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sspr_reset_password_request_v1**](ModuleSsprApi.md#sspr_reset_password_request_v1) | **POST** /1/module/sspr/resetPasswordRequest | Reset Password Request
[**sspr_reset_password_v1**](ModuleSsprApi.md#sspr_reset_password_v1) | **POST** /1/module/sspr/resetPassword | Reset Password
[**sspr_send_usernames_v1**](ModuleSsprApi.md#sspr_send_usernames_v1) | **POST** /1/module/sspr/sendUsernames | Send username(s)
[**sspr_unlock_account_request_v1**](ModuleSsprApi.md#sspr_unlock_account_request_v1) | **POST** /1/module/sspr/unlockAccountRequest | Unlock Account Request
[**sspr_unlock_account_v1**](ModuleSsprApi.md#sspr_unlock_account_v1) | **POST** /1/module/sspr/unlockAccount | Unlock Account
[**sspr_validate_token_v1**](ModuleSsprApi.md#sspr_validate_token_v1) | **POST** /1/module/sspr/validateToken | Validate Token


# **sspr_reset_password_request_v1**
> sspr_reset_password_request_v1(sspr_reset_password_request_v1_request)

Reset Password Request

This endpoint sends an email with a link to reset the user's password.  sEmailAddress must be set if eUserTypeSSPR = EzsignUser  sUserLoginname must be set if eUserTypeSSPR = Native

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.sspr_reset_password_request_v1_request import SsprResetPasswordRequestV1Request
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
    sspr_reset_password_request_v1_request = SsprResetPasswordRequestV1Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        fki_language_id=FieldPkiLanguageID(2),
        e_user_type_sspr=FieldEUserTypeSSPR("Native"),
        s_email_address="example@domain.com",
        s_user_loginname="JohnDoe",
    ) # SsprResetPasswordRequestV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Reset Password Request
        api_instance.sspr_reset_password_request_v1(sspr_reset_password_request_v1_request)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_reset_password_request_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sspr_reset_password_request_v1_request** | [**SsprResetPasswordRequestV1Request**](SsprResetPasswordRequestV1Request.md)|  |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was accepted.  Do not misinterpret as \&quot;the account exists\&quot;. It only means an email will be sent if (and only if) an account exists. |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sspr_reset_password_v1**
> sspr_reset_password_v1(sspr_reset_password_v1_request)

Reset Password

This endpoint resets the user's password.  sEmailAddress must be set if eUserTypeSSPR = EzsignUser  sUserLoginname must be set if eUserTypeSSPR = Native

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.sspr_reset_password_v1_request import SsprResetPasswordV1Request
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
    sspr_reset_password_v1_request = SsprResetPasswordV1Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        fki_language_id=FieldPkiLanguageID(2),
        e_user_type_sspr=FieldEUserTypeSSPR("Native"),
        s_email_address="example@domain.com",
        s_user_loginname="JohnDoe",
        bin_user_ssp_rtoken="012345678901234567890123456789012345678901234567890123456789abcd",
        s_password="Qwerty1234!",
    ) # SsprResetPasswordV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Reset Password
        api_instance.sspr_reset_password_v1(sspr_reset_password_v1_request)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_reset_password_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sspr_reset_password_v1_request** | [**SsprResetPasswordV1Request**](SsprResetPasswordV1Request.md)|  |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The password was reset Successfully |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sspr_send_usernames_v1**
> sspr_send_usernames_v1(sspr_send_usernames_v1_request)

Send username(s)

This endpoint returns an email with the username(s) matching the email address provided in case of forgotten username

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.sspr_send_usernames_v1_request import SsprSendUsernamesV1Request
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
    sspr_send_usernames_v1_request = SsprSendUsernamesV1Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        fki_language_id=FieldPkiLanguageID(2),
        e_user_type_sspr=FieldEUserTypeSSPR("Native"),
        s_email_address="example@domain.com",
    ) # SsprSendUsernamesV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Send username(s)
        api_instance.sspr_send_usernames_v1(sspr_send_usernames_v1_request)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_send_usernames_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sspr_send_usernames_v1_request** | [**SsprSendUsernamesV1Request**](SsprSendUsernamesV1Request.md)|  |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was accepted.  Do not misinterpret as \&quot;the email address has an account attached to it\&quot;. It only means an email will be sent if (and only if) an account exists for that email address. |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sspr_unlock_account_request_v1**
> sspr_unlock_account_request_v1(sspr_unlock_account_request_v1_request)

Unlock Account Request

This endpoint sends an email with a link to unlock the user account.  sEmailAddress must be set if eUserTypeSSPR = EzsignUser  sUserLoginname must be set if eUserTypeSSPR = Native

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.sspr_unlock_account_request_v1_request import SsprUnlockAccountRequestV1Request
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
    sspr_unlock_account_request_v1_request = SsprUnlockAccountRequestV1Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        fki_language_id=FieldPkiLanguageID(2),
        e_user_type_sspr=FieldEUserTypeSSPR("Native"),
        s_email_address="example@domain.com",
        s_user_loginname="JohnDoe",
    ) # SsprUnlockAccountRequestV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Unlock Account Request
        api_instance.sspr_unlock_account_request_v1(sspr_unlock_account_request_v1_request)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_unlock_account_request_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sspr_unlock_account_request_v1_request** | [**SsprUnlockAccountRequestV1Request**](SsprUnlockAccountRequestV1Request.md)|  |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was accepted.  Do not misinterpret as \&quot;the account exists\&quot;. It only means an email will be sent if (and only if) an account exists. |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sspr_unlock_account_v1**
> sspr_unlock_account_v1(sspr_unlock_account_v1_request)

Unlock Account

This endpoint unlocks the user account.  sEmailAddress must be set if eUserTypeSSPR = EzsignUser  sUserLoginname must be set if eUserTypeSSPR = Native

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.sspr_unlock_account_v1_request import SsprUnlockAccountV1Request
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
    sspr_unlock_account_v1_request = SsprUnlockAccountV1Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        fki_language_id=FieldPkiLanguageID(2),
        e_user_type_sspr=FieldEUserTypeSSPR("Native"),
        s_email_address="example@domain.com",
        s_user_loginname="JohnDoe",
        bin_user_ssp_rtoken="012345678901234567890123456789012345678901234567890123456789abcd",
    ) # SsprUnlockAccountV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Unlock Account
        api_instance.sspr_unlock_account_v1(sspr_unlock_account_v1_request)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_unlock_account_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sspr_unlock_account_v1_request** | [**SsprUnlockAccountV1Request**](SsprUnlockAccountV1Request.md)|  |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The account was unlocked Successfully |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sspr_validate_token_v1**
> sspr_validate_token_v1(sspr_validate_token_v1_request)

Validate Token

This endpoint validates if a Token is valid and not expired.  sEmailAddress must be set if eUserTypeSSPR = EzsignUser  sUserLoginname must be set if eUserTypeSSPR = Native

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import module_sspr_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.sspr_validate_token_v1_request import SsprValidateTokenV1Request
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
    sspr_validate_token_v1_request = SsprValidateTokenV1Request(
        pks_customer_code=FieldPksCustomerCode("demo"),
        fki_language_id=FieldPkiLanguageID(2),
        e_user_type_sspr=FieldEUserTypeSSPR("Native"),
        s_email_address="example@domain.com",
        s_user_loginname="JohnDoe",
        bin_user_ssp_rtoken="012345678901234567890123456789012345678901234567890123456789abcd",
    ) # SsprValidateTokenV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Validate Token
        api_instance.sspr_validate_token_v1(sspr_validate_token_v1_request)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ModuleSsprApi->sspr_validate_token_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sspr_validate_token_v1_request** | [**SsprValidateTokenV1Request**](SsprValidateTokenV1Request.md)|  |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The token is valid |  -  |
**403** | You are not allowed to call this function |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

