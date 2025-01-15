# eZmaxApi.ObjectActivesessionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activesession_generate_federation_token_v1**](ObjectActivesessionApi.md#activesession_generate_federation_token_v1) | **POST** /1/object/activesession/generateFederationToken | Generate a federation token
[**activesession_get_current_v1**](ObjectActivesessionApi.md#activesession_get_current_v1) | **GET** /1/object/activesession/getCurrent | Get Current Activesession
[**activesession_get_current_v2**](ObjectActivesessionApi.md#activesession_get_current_v2) | **GET** /2/object/activesession/getCurrent | Get Current Activesession
[**activesession_get_list_v1**](ObjectActivesessionApi.md#activesession_get_list_v1) | **GET** /1/object/activesession/getList | Retrieve Activesession list


# **activesession_generate_federation_token_v1**
> ActivesessionGenerateFederationTokenV1Response activesession_generate_federation_token_v1(activesession_generate_federation_token_v1_request)

Generate a federation token



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.activesession_generate_federation_token_v1_request import ActivesessionGenerateFederationTokenV1Request
from eZmaxApi.models.activesession_generate_federation_token_v1_response import ActivesessionGenerateFederationTokenV1Response
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
    api_instance = eZmaxApi.ObjectActivesessionApi(api_client)
    activesession_generate_federation_token_v1_request = eZmaxApi.ActivesessionGenerateFederationTokenV1Request() # ActivesessionGenerateFederationTokenV1Request | 

    try:
        # Generate a federation token
        api_response = api_instance.activesession_generate_federation_token_v1(activesession_generate_federation_token_v1_request)
        print("The response of ObjectActivesessionApi->activesession_generate_federation_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectActivesessionApi->activesession_generate_federation_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activesession_generate_federation_token_v1_request** | [**ActivesessionGenerateFederationTokenV1Request**](ActivesessionGenerateFederationTokenV1Request.md)|  | 

### Return type

[**ActivesessionGenerateFederationTokenV1Response**](ActivesessionGenerateFederationTokenV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activesession_get_current_v1**
> ActivesessionGetCurrentV1Response activesession_get_current_v1()

Get Current Activesession

Retrieve the details about the current activesession

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.activesession_get_current_v1_response import ActivesessionGetCurrentV1Response
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
    api_instance = eZmaxApi.ObjectActivesessionApi(api_client)

    try:
        # Get Current Activesession
        api_response = api_instance.activesession_get_current_v1()
        print("The response of ObjectActivesessionApi->activesession_get_current_v1:\n")
        pprint(api_response)
    except Exception as e:
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
**350** | The user must authenticate before he can continue with this request |  -  |
**351** | The user is configured with 2FA and needs to validate its phone number before he can continue with this request |  -  |
**352** | The user is configured with 2FA and needs to answer a Secretquestion before he can continue with this request |  -  |
**353** | The user must accept clauses before he can continue with this request |  -  |
**354** | The user&#39;s computer must be validated before he can continue with this request |  -  |
**355** | The user must change its password before he can continue with this request |  -  |
**356** | The user is not running the latest version of the native application. He must valide or update its version before he can continue with this request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activesession_get_current_v2**
> ActivesessionGetCurrentV2Response activesession_get_current_v2()

Get Current Activesession

Retrieve the details about the current activesession

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.activesession_get_current_v2_response import ActivesessionGetCurrentV2Response
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
    api_instance = eZmaxApi.ObjectActivesessionApi(api_client)

    try:
        # Get Current Activesession
        api_response = api_instance.activesession_get_current_v2()
        print("The response of ObjectActivesessionApi->activesession_get_current_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectActivesessionApi->activesession_get_current_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ActivesessionGetCurrentV2Response**](ActivesessionGetCurrentV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**350** | The user must authenticate before he can continue with this request |  -  |
**351** | The user is configured with 2FA and needs to validate its phone number before he can continue with this request |  -  |
**352** | The user is configured with 2FA and needs to answer a Secretquestion before he can continue with this request |  -  |
**353** | The user must accept clauses before he can continue with this request |  -  |
**354** | The user&#39;s computer must be validated before he can continue with this request |  -  |
**355** | The user must change its password before he can continue with this request |  -  |
**356** | The user is not running the latest version of the native application. He must valide or update its version before he can continue with this request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activesession_get_list_v1**
> ActivesessionGetListV1Response activesession_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Activesession list

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.activesession_get_list_v1_response import ActivesessionGetListV1Response
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
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
    api_instance = eZmaxApi.ObjectActivesessionApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Activesession list
        api_response = api_instance.activesession_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectActivesessionApi->activesession_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectActivesessionApi->activesession_get_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional] 
 **i_row_max** | **int**|  | [optional] 
 **i_row_offset** | **int**|  | [optional] [default to 0]
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 
 **s_filter** | **str**|  | [optional] 

### Return type

[**ActivesessionGetListV1Response**](ActivesessionGetListV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

