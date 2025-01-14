# eZmaxApi.ObjectUsergroupexternalApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroupexternal_create_object_v1**](ObjectUsergroupexternalApi.md#usergroupexternal_create_object_v1) | **POST** /1/object/usergroupexternal | Create a new Usergroupexternal
[**usergroupexternal_delete_object_v1**](ObjectUsergroupexternalApi.md#usergroupexternal_delete_object_v1) | **DELETE** /1/object/usergroupexternal/{pkiUsergroupexternalID} | Delete an existing Usergroupexternal
[**usergroupexternal_edit_object_v1**](ObjectUsergroupexternalApi.md#usergroupexternal_edit_object_v1) | **PUT** /1/object/usergroupexternal/{pkiUsergroupexternalID} | Edit an existing Usergroupexternal
[**usergroupexternal_get_autocomplete_v2**](ObjectUsergroupexternalApi.md#usergroupexternal_get_autocomplete_v2) | **GET** /2/object/usergroupexternal/getAutocomplete/{sSelector} | Retrieve Usergroupexternals and IDs
[**usergroupexternal_get_list_v1**](ObjectUsergroupexternalApi.md#usergroupexternal_get_list_v1) | **GET** /1/object/usergroupexternal/getList | Retrieve Usergroupexternal list
[**usergroupexternal_get_object_v2**](ObjectUsergroupexternalApi.md#usergroupexternal_get_object_v2) | **GET** /2/object/usergroupexternal/{pkiUsergroupexternalID} | Retrieve an existing Usergroupexternal
[**usergroupexternal_get_usergroupexternalmemberships_v1**](ObjectUsergroupexternalApi.md#usergroupexternal_get_usergroupexternalmemberships_v1) | **GET** /1/object/usergroupexternal/{pkiUsergroupexternalID}/getUsergroupexternalmemberships | Retrieve an existing Usergroupexternal&#39;s Usergroupexternalmemberships
[**usergroupexternal_get_usergroups_v1**](ObjectUsergroupexternalApi.md#usergroupexternal_get_usergroups_v1) | **GET** /1/object/usergroupexternal/{pkiUsergroupexternalID}/getUsergroups | Get Usergroupexternal&#39;s Usergroups


# **usergroupexternal_create_object_v1**
> UsergroupexternalCreateObjectV1Response usergroupexternal_create_object_v1(usergroupexternal_create_object_v1_request)

Create a new Usergroupexternal

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupexternal_create_object_v1_request import UsergroupexternalCreateObjectV1Request
from eZmaxApi.models.usergroupexternal_create_object_v1_response import UsergroupexternalCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    usergroupexternal_create_object_v1_request = eZmaxApi.UsergroupexternalCreateObjectV1Request() # UsergroupexternalCreateObjectV1Request | 

    try:
        # Create a new Usergroupexternal
        api_response = api_instance.usergroupexternal_create_object_v1(usergroupexternal_create_object_v1_request)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupexternal_create_object_v1_request** | [**UsergroupexternalCreateObjectV1Request**](UsergroupexternalCreateObjectV1Request.md)|  | 

### Return type

[**UsergroupexternalCreateObjectV1Response**](UsergroupexternalCreateObjectV1Response.md)

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

# **usergroupexternal_delete_object_v1**
> UsergroupexternalDeleteObjectV1Response usergroupexternal_delete_object_v1(pki_usergroupexternal_id)

Delete an existing Usergroupexternal



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupexternal_delete_object_v1_response import UsergroupexternalDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    pki_usergroupexternal_id = 56 # int | The unique ID of the Usergroupexternal

    try:
        # Delete an existing Usergroupexternal
        api_response = api_instance.usergroupexternal_delete_object_v1(pki_usergroupexternal_id)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupexternal_id** | **int**| The unique ID of the Usergroupexternal | 

### Return type

[**UsergroupexternalDeleteObjectV1Response**](UsergroupexternalDeleteObjectV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroupexternal_edit_object_v1**
> UsergroupexternalEditObjectV1Response usergroupexternal_edit_object_v1(pki_usergroupexternal_id, usergroupexternal_edit_object_v1_request)

Edit an existing Usergroupexternal



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupexternal_edit_object_v1_request import UsergroupexternalEditObjectV1Request
from eZmaxApi.models.usergroupexternal_edit_object_v1_response import UsergroupexternalEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    pki_usergroupexternal_id = 56 # int | The unique ID of the Usergroupexternal
    usergroupexternal_edit_object_v1_request = eZmaxApi.UsergroupexternalEditObjectV1Request() # UsergroupexternalEditObjectV1Request | 

    try:
        # Edit an existing Usergroupexternal
        api_response = api_instance.usergroupexternal_edit_object_v1(pki_usergroupexternal_id, usergroupexternal_edit_object_v1_request)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupexternal_id** | **int**| The unique ID of the Usergroupexternal | 
 **usergroupexternal_edit_object_v1_request** | [**UsergroupexternalEditObjectV1Request**](UsergroupexternalEditObjectV1Request.md)|  | 

### Return type

[**UsergroupexternalEditObjectV1Response**](UsergroupexternalEditObjectV1Response.md)

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

# **usergroupexternal_get_autocomplete_v2**
> UsergroupexternalGetAutocompleteV2Response usergroupexternal_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Usergroupexternals and IDs

Get the list of Usergroupexternal to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.usergroupexternal_get_autocomplete_v2_response import UsergroupexternalGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    s_selector = 's_selector_example' # str | The type of Usergroupexternals to return
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Usergroupexternals and IDs
        api_response = api_instance.usergroupexternal_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Usergroupexternals to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**UsergroupexternalGetAutocompleteV2Response**](UsergroupexternalGetAutocompleteV2Response.md)

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

# **usergroupexternal_get_list_v1**
> UsergroupexternalGetListV1Response usergroupexternal_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Usergroupexternal list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.usergroupexternal_get_list_v1_response import UsergroupexternalGetListV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Usergroupexternal list
        api_response = api_instance.usergroupexternal_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_get_list_v1: %s\n" % e)
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

[**UsergroupexternalGetListV1Response**](UsergroupexternalGetListV1Response.md)

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

# **usergroupexternal_get_object_v2**
> UsergroupexternalGetObjectV2Response usergroupexternal_get_object_v2(pki_usergroupexternal_id)

Retrieve an existing Usergroupexternal



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupexternal_get_object_v2_response import UsergroupexternalGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    pki_usergroupexternal_id = 56 # int | The unique ID of the Usergroupexternal

    try:
        # Retrieve an existing Usergroupexternal
        api_response = api_instance.usergroupexternal_get_object_v2(pki_usergroupexternal_id)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupexternal_id** | **int**| The unique ID of the Usergroupexternal | 

### Return type

[**UsergroupexternalGetObjectV2Response**](UsergroupexternalGetObjectV2Response.md)

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

# **usergroupexternal_get_usergroupexternalmemberships_v1**
> UsergroupexternalGetUsergroupexternalmembershipsV1Response usergroupexternal_get_usergroupexternalmemberships_v1(pki_usergroupexternal_id)

Retrieve an existing Usergroupexternal's Usergroupexternalmemberships

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupexternal_get_usergroupexternalmemberships_v1_response import UsergroupexternalGetUsergroupexternalmembershipsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    pki_usergroupexternal_id = 56 # int | 

    try:
        # Retrieve an existing Usergroupexternal's Usergroupexternalmemberships
        api_response = api_instance.usergroupexternal_get_usergroupexternalmemberships_v1(pki_usergroupexternal_id)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_get_usergroupexternalmemberships_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_get_usergroupexternalmemberships_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupexternal_id** | **int**|  | 

### Return type

[**UsergroupexternalGetUsergroupexternalmembershipsV1Response**](UsergroupexternalGetUsergroupexternalmembershipsV1Response.md)

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

# **usergroupexternal_get_usergroups_v1**
> UsergroupexternalGetUsergroupsV1Response usergroupexternal_get_usergroups_v1(pki_usergroupexternal_id)

Get Usergroupexternal's Usergroups

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupexternal_get_usergroups_v1_response import UsergroupexternalGetUsergroupsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupexternalApi(api_client)
    pki_usergroupexternal_id = 56 # int | 

    try:
        # Get Usergroupexternal's Usergroups
        api_response = api_instance.usergroupexternal_get_usergroups_v1(pki_usergroupexternal_id)
        print("The response of ObjectUsergroupexternalApi->usergroupexternal_get_usergroups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupexternalApi->usergroupexternal_get_usergroups_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupexternal_id** | **int**|  | 

### Return type

[**UsergroupexternalGetUsergroupsV1Response**](UsergroupexternalGetUsergroupsV1Response.md)

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

