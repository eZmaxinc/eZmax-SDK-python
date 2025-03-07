# eZmaxApi.ObjectAuthenticationexternalApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticationexternal_create_object_v1**](ObjectAuthenticationexternalApi.md#authenticationexternal_create_object_v1) | **POST** /1/object/authenticationexternal | Create a new Authenticationexternal
[**authenticationexternal_delete_object_v1**](ObjectAuthenticationexternalApi.md#authenticationexternal_delete_object_v1) | **DELETE** /1/object/authenticationexternal/{pkiAuthenticationexternalID} | Delete an existing Authenticationexternal
[**authenticationexternal_edit_object_v1**](ObjectAuthenticationexternalApi.md#authenticationexternal_edit_object_v1) | **PUT** /1/object/authenticationexternal/{pkiAuthenticationexternalID} | Edit an existing Authenticationexternal
[**authenticationexternal_get_autocomplete_v2**](ObjectAuthenticationexternalApi.md#authenticationexternal_get_autocomplete_v2) | **GET** /2/object/authenticationexternal/getAutocomplete/{sSelector} | Retrieve Authenticationexternals and IDs
[**authenticationexternal_get_list_v1**](ObjectAuthenticationexternalApi.md#authenticationexternal_get_list_v1) | **GET** /1/object/authenticationexternal/getList | Retrieve Authenticationexternal list
[**authenticationexternal_get_object_v2**](ObjectAuthenticationexternalApi.md#authenticationexternal_get_object_v2) | **GET** /2/object/authenticationexternal/{pkiAuthenticationexternalID} | Retrieve an existing Authenticationexternal
[**authenticationexternal_reset_authorization_v1**](ObjectAuthenticationexternalApi.md#authenticationexternal_reset_authorization_v1) | **POST** /1/object/authenticationexternal/{pkiAuthenticationexternalID}/resetAuthorization | Reset the Authenticationexternal authorization


# **authenticationexternal_create_object_v1**
> AuthenticationexternalCreateObjectV1Response authenticationexternal_create_object_v1(authenticationexternal_create_object_v1_request)

Create a new Authenticationexternal

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_create_object_v1_request import AuthenticationexternalCreateObjectV1Request
from eZmaxApi.models.authenticationexternal_create_object_v1_response import AuthenticationexternalCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    authenticationexternal_create_object_v1_request = eZmaxApi.AuthenticationexternalCreateObjectV1Request() # AuthenticationexternalCreateObjectV1Request | 

    try:
        # Create a new Authenticationexternal
        api_response = api_instance.authenticationexternal_create_object_v1(authenticationexternal_create_object_v1_request)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticationexternal_create_object_v1_request** | [**AuthenticationexternalCreateObjectV1Request**](AuthenticationexternalCreateObjectV1Request.md)|  | 

### Return type

[**AuthenticationexternalCreateObjectV1Response**](AuthenticationexternalCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticationexternal_delete_object_v1**
> AuthenticationexternalDeleteObjectV1Response authenticationexternal_delete_object_v1(pki_authenticationexternal_id)

Delete an existing Authenticationexternal



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_delete_object_v1_response import AuthenticationexternalDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    pki_authenticationexternal_id = 56 # int | The unique ID of the Authenticationexternal

    try:
        # Delete an existing Authenticationexternal
        api_response = api_instance.authenticationexternal_delete_object_v1(pki_authenticationexternal_id)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_authenticationexternal_id** | **int**| The unique ID of the Authenticationexternal | 

### Return type

[**AuthenticationexternalDeleteObjectV1Response**](AuthenticationexternalDeleteObjectV1Response.md)

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

# **authenticationexternal_edit_object_v1**
> AuthenticationexternalEditObjectV1Response authenticationexternal_edit_object_v1(pki_authenticationexternal_id, authenticationexternal_edit_object_v1_request)

Edit an existing Authenticationexternal



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_edit_object_v1_request import AuthenticationexternalEditObjectV1Request
from eZmaxApi.models.authenticationexternal_edit_object_v1_response import AuthenticationexternalEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    pki_authenticationexternal_id = 56 # int | The unique ID of the Authenticationexternal
    authenticationexternal_edit_object_v1_request = eZmaxApi.AuthenticationexternalEditObjectV1Request() # AuthenticationexternalEditObjectV1Request | 

    try:
        # Edit an existing Authenticationexternal
        api_response = api_instance.authenticationexternal_edit_object_v1(pki_authenticationexternal_id, authenticationexternal_edit_object_v1_request)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_authenticationexternal_id** | **int**| The unique ID of the Authenticationexternal | 
 **authenticationexternal_edit_object_v1_request** | [**AuthenticationexternalEditObjectV1Request**](AuthenticationexternalEditObjectV1Request.md)|  | 

### Return type

[**AuthenticationexternalEditObjectV1Response**](AuthenticationexternalEditObjectV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticationexternal_get_autocomplete_v2**
> AuthenticationexternalGetAutocompleteV2Response authenticationexternal_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Authenticationexternals and IDs

Get the list of Authenticationexternal to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_get_autocomplete_v2_response import AuthenticationexternalGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    s_selector = 's_selector_example' # str | The type of Authenticationexternals to return
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Authenticationexternals and IDs
        api_response = api_instance.authenticationexternal_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Authenticationexternals to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**AuthenticationexternalGetAutocompleteV2Response**](AuthenticationexternalGetAutocompleteV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticationexternal_get_list_v1**
> AuthenticationexternalGetListV1Response authenticationexternal_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Authenticationexternal list

Enum values that can be filtered in query parameter *sFilter*:

| Variable | Valid values |
|---|---|
| eAuthenticationexternalType | Salesforce<br>SalesforceSandbox |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_get_list_v1_response import AuthenticationexternalGetListV1Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Authenticationexternal list
        api_response = api_instance.authenticationexternal_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_get_list_v1: %s\n" % e)
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

[**AuthenticationexternalGetListV1Response**](AuthenticationexternalGetListV1Response.md)

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

# **authenticationexternal_get_object_v2**
> AuthenticationexternalGetObjectV2Response authenticationexternal_get_object_v2(pki_authenticationexternal_id)

Retrieve an existing Authenticationexternal



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_get_object_v2_response import AuthenticationexternalGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    pki_authenticationexternal_id = 56 # int | The unique ID of the Authenticationexternal

    try:
        # Retrieve an existing Authenticationexternal
        api_response = api_instance.authenticationexternal_get_object_v2(pki_authenticationexternal_id)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_authenticationexternal_id** | **int**| The unique ID of the Authenticationexternal | 

### Return type

[**AuthenticationexternalGetObjectV2Response**](AuthenticationexternalGetObjectV2Response.md)

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

# **authenticationexternal_reset_authorization_v1**
> AuthenticationexternalResetAuthorizationV1Response authenticationexternal_reset_authorization_v1(pki_authenticationexternal_id, body)

Reset the Authenticationexternal authorization



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.authenticationexternal_reset_authorization_v1_response import AuthenticationexternalResetAuthorizationV1Response
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
    api_instance = eZmaxApi.ObjectAuthenticationexternalApi(api_client)
    pki_authenticationexternal_id = 56 # int | 
    body = None # object | 

    try:
        # Reset the Authenticationexternal authorization
        api_response = api_instance.authenticationexternal_reset_authorization_v1(pki_authenticationexternal_id, body)
        print("The response of ObjectAuthenticationexternalApi->authenticationexternal_reset_authorization_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAuthenticationexternalApi->authenticationexternal_reset_authorization_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_authenticationexternal_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**AuthenticationexternalResetAuthorizationV1Response**](AuthenticationexternalResetAuthorizationV1Response.md)

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

