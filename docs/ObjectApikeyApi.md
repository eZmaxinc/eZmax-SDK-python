# eZmaxApi.ObjectApikeyApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apikey_create_object_v2**](ObjectApikeyApi.md#apikey_create_object_v2) | **POST** /2/object/apikey | Create a new Apikey
[**apikey_edit_object_v1**](ObjectApikeyApi.md#apikey_edit_object_v1) | **PUT** /1/object/apikey/{pkiApikeyID} | Edit an existing Apikey
[**apikey_edit_permissions_v1**](ObjectApikeyApi.md#apikey_edit_permissions_v1) | **PUT** /1/object/apikey/{pkiApikeyID}/editPermissions | Edit multiple Permissions
[**apikey_get_cors_v1**](ObjectApikeyApi.md#apikey_get_cors_v1) | **GET** /1/object/apikey/{pkiApikeyID}/getCors | Retrieve an existing Apikey&#39;s cors
[**apikey_get_list_v1**](ObjectApikeyApi.md#apikey_get_list_v1) | **GET** /1/object/apikey/getList | Retrieve Apikey list
[**apikey_get_object_v2**](ObjectApikeyApi.md#apikey_get_object_v2) | **GET** /2/object/apikey/{pkiApikeyID} | Retrieve an existing Apikey
[**apikey_get_permissions_v1**](ObjectApikeyApi.md#apikey_get_permissions_v1) | **GET** /1/object/apikey/{pkiApikeyID}/getPermissions | Retrieve an existing Apikey&#39;s Permissions
[**apikey_get_subnets_v1**](ObjectApikeyApi.md#apikey_get_subnets_v1) | **GET** /1/object/apikey/{pkiApikeyID}/getSubnets | Retrieve an existing Apikey&#39;s subnets
[**apikey_regenerate_v1**](ObjectApikeyApi.md#apikey_regenerate_v1) | **POST** /1/object/apikey/{pkiApikeyID}/regenerate | Regenerate the Apikey


# **apikey_create_object_v2**
> ApikeyCreateObjectV2Response apikey_create_object_v2(apikey_create_object_v2_request)

Create a new Apikey

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_create_object_v2_request import ApikeyCreateObjectV2Request
from eZmaxApi.models.apikey_create_object_v2_response import ApikeyCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    apikey_create_object_v2_request = eZmaxApi.ApikeyCreateObjectV2Request() # ApikeyCreateObjectV2Request | 

    try:
        # Create a new Apikey
        api_response = api_instance.apikey_create_object_v2(apikey_create_object_v2_request)
        print("The response of ObjectApikeyApi->apikey_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_create_object_v2_request** | [**ApikeyCreateObjectV2Request**](ApikeyCreateObjectV2Request.md)|  | 

### Return type

[**ApikeyCreateObjectV2Response**](ApikeyCreateObjectV2Response.md)

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

# **apikey_edit_object_v1**
> ApikeyEditObjectV1Response apikey_edit_object_v1(pki_apikey_id, apikey_edit_object_v1_request)

Edit an existing Apikey



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_edit_object_v1_request import ApikeyEditObjectV1Request
from eZmaxApi.models.apikey_edit_object_v1_response import ApikeyEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | The unique ID of the Apikey
    apikey_edit_object_v1_request = eZmaxApi.ApikeyEditObjectV1Request() # ApikeyEditObjectV1Request | 

    try:
        # Edit an existing Apikey
        api_response = api_instance.apikey_edit_object_v1(pki_apikey_id, apikey_edit_object_v1_request)
        print("The response of ObjectApikeyApi->apikey_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**| The unique ID of the Apikey | 
 **apikey_edit_object_v1_request** | [**ApikeyEditObjectV1Request**](ApikeyEditObjectV1Request.md)|  | 

### Return type

[**ApikeyEditObjectV1Response**](ApikeyEditObjectV1Response.md)

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

# **apikey_edit_permissions_v1**
> ApikeyEditPermissionsV1Response apikey_edit_permissions_v1(pki_apikey_id, apikey_edit_permissions_v1_request)

Edit multiple Permissions

Using this endpoint, you can edit multiple Permissions at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_edit_permissions_v1_request import ApikeyEditPermissionsV1Request
from eZmaxApi.models.apikey_edit_permissions_v1_response import ApikeyEditPermissionsV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | 
    apikey_edit_permissions_v1_request = eZmaxApi.ApikeyEditPermissionsV1Request() # ApikeyEditPermissionsV1Request | 

    try:
        # Edit multiple Permissions
        api_response = api_instance.apikey_edit_permissions_v1(pki_apikey_id, apikey_edit_permissions_v1_request)
        print("The response of ObjectApikeyApi->apikey_edit_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_edit_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**|  | 
 **apikey_edit_permissions_v1_request** | [**ApikeyEditPermissionsV1Request**](ApikeyEditPermissionsV1Request.md)|  | 

### Return type

[**ApikeyEditPermissionsV1Response**](ApikeyEditPermissionsV1Response.md)

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

# **apikey_get_cors_v1**
> ApikeyGetCorsV1Response apikey_get_cors_v1(pki_apikey_id)

Retrieve an existing Apikey's cors

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_get_cors_v1_response import ApikeyGetCorsV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | 

    try:
        # Retrieve an existing Apikey's cors
        api_response = api_instance.apikey_get_cors_v1(pki_apikey_id)
        print("The response of ObjectApikeyApi->apikey_get_cors_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_get_cors_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**|  | 

### Return type

[**ApikeyGetCorsV1Response**](ApikeyGetCorsV1Response.md)

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

# **apikey_get_list_v1**
> ApikeyGetListV1Response apikey_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Apikey list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---|

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_get_list_v1_response import ApikeyGetListV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Apikey list
        api_response = api_instance.apikey_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectApikeyApi->apikey_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_get_list_v1: %s\n" % e)
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

[**ApikeyGetListV1Response**](ApikeyGetListV1Response.md)

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

# **apikey_get_object_v2**
> ApikeyGetObjectV2Response apikey_get_object_v2(pki_apikey_id)

Retrieve an existing Apikey



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_get_object_v2_response import ApikeyGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | The unique ID of the Apikey

    try:
        # Retrieve an existing Apikey
        api_response = api_instance.apikey_get_object_v2(pki_apikey_id)
        print("The response of ObjectApikeyApi->apikey_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**| The unique ID of the Apikey | 

### Return type

[**ApikeyGetObjectV2Response**](ApikeyGetObjectV2Response.md)

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

# **apikey_get_permissions_v1**
> ApikeyGetPermissionsV1Response apikey_get_permissions_v1(pki_apikey_id)

Retrieve an existing Apikey's Permissions

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_get_permissions_v1_response import ApikeyGetPermissionsV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | 

    try:
        # Retrieve an existing Apikey's Permissions
        api_response = api_instance.apikey_get_permissions_v1(pki_apikey_id)
        print("The response of ObjectApikeyApi->apikey_get_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_get_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**|  | 

### Return type

[**ApikeyGetPermissionsV1Response**](ApikeyGetPermissionsV1Response.md)

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

# **apikey_get_subnets_v1**
> ApikeyGetSubnetsV1Response apikey_get_subnets_v1(pki_apikey_id)

Retrieve an existing Apikey's subnets

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_get_subnets_v1_response import ApikeyGetSubnetsV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | 

    try:
        # Retrieve an existing Apikey's subnets
        api_response = api_instance.apikey_get_subnets_v1(pki_apikey_id)
        print("The response of ObjectApikeyApi->apikey_get_subnets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_get_subnets_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**|  | 

### Return type

[**ApikeyGetSubnetsV1Response**](ApikeyGetSubnetsV1Response.md)

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

# **apikey_regenerate_v1**
> ApikeyRegenerateV1Response apikey_regenerate_v1(pki_apikey_id, apikey_regenerate_v1_request)

Regenerate the Apikey



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.apikey_regenerate_v1_request import ApikeyRegenerateV1Request
from eZmaxApi.models.apikey_regenerate_v1_response import ApikeyRegenerateV1Response
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
    api_instance = eZmaxApi.ObjectApikeyApi(api_client)
    pki_apikey_id = 56 # int | 
    apikey_regenerate_v1_request = eZmaxApi.ApikeyRegenerateV1Request() # ApikeyRegenerateV1Request | 

    try:
        # Regenerate the Apikey
        api_response = api_instance.apikey_regenerate_v1(pki_apikey_id, apikey_regenerate_v1_request)
        print("The response of ObjectApikeyApi->apikey_regenerate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApikeyApi->apikey_regenerate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_apikey_id** | **int**|  | 
 **apikey_regenerate_v1_request** | [**ApikeyRegenerateV1Request**](ApikeyRegenerateV1Request.md)|  | 

### Return type

[**ApikeyRegenerateV1Response**](ApikeyRegenerateV1Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

