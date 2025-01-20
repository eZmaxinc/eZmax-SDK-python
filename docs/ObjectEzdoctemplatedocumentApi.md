# eZmaxApi.ObjectEzdoctemplatedocumentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezdoctemplatedocument_create_object_v1**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_create_object_v1) | **POST** /1/object/ezdoctemplatedocument | Create a new Ezdoctemplatedocument
[**ezdoctemplatedocument_download_v1**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_download_v1) | **GET** /1/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID}/download | Retrieve the content
[**ezdoctemplatedocument_edit_object_v1**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_edit_object_v1) | **PUT** /1/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID} | Edit an existing Ezdoctemplatedocument
[**ezdoctemplatedocument_get_autocomplete_v2**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_get_autocomplete_v2) | **GET** /2/object/ezdoctemplatedocument/getAutocomplete/{sSelector} | Retrieve Ezdoctemplatedocuments and IDs
[**ezdoctemplatedocument_get_list_v1**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_get_list_v1) | **GET** /1/object/ezdoctemplatedocument/getList | Retrieve Ezdoctemplatedocument list
[**ezdoctemplatedocument_get_object_v2**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_get_object_v2) | **GET** /2/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID} | Retrieve an existing Ezdoctemplatedocument
[**ezdoctemplatedocument_patch_object_v1**](ObjectEzdoctemplatedocumentApi.md#ezdoctemplatedocument_patch_object_v1) | **PATCH** /1/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID} | Patch an existing Ezdoctemplatedocument


# **ezdoctemplatedocument_create_object_v1**
> EzdoctemplatedocumentCreateObjectV1Response ezdoctemplatedocument_create_object_v1(ezdoctemplatedocument_create_object_v1_request)

Create a new Ezdoctemplatedocument

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezdoctemplatedocument_create_object_v1_request import EzdoctemplatedocumentCreateObjectV1Request
from eZmaxApi.models.ezdoctemplatedocument_create_object_v1_response import EzdoctemplatedocumentCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    ezdoctemplatedocument_create_object_v1_request = eZmaxApi.EzdoctemplatedocumentCreateObjectV1Request() # EzdoctemplatedocumentCreateObjectV1Request | 

    try:
        # Create a new Ezdoctemplatedocument
        api_response = api_instance.ezdoctemplatedocument_create_object_v1(ezdoctemplatedocument_create_object_v1_request)
        print("The response of ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezdoctemplatedocument_create_object_v1_request** | [**EzdoctemplatedocumentCreateObjectV1Request**](EzdoctemplatedocumentCreateObjectV1Request.md)|  | 

### Return type

[**EzdoctemplatedocumentCreateObjectV1Response**](EzdoctemplatedocumentCreateObjectV1Response.md)

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

# **ezdoctemplatedocument_download_v1**
> ezdoctemplatedocument_download_v1(pki_ezdoctemplatedocument_id)

Retrieve the content

Using this endpoint, you can retrieve the content of an ezdoctemplatedocument.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (Presigned):

```python
import eZmaxApi
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

# Configure API key authorization: Presigned
configuration.api_key['Presigned'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Presigned'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    pki_ezdoctemplatedocument_id = 56 # int | 

    try:
        # Retrieve the content
        api_instance.ezdoctemplatedocument_download_v1(pki_ezdoctemplatedocument_id)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezdoctemplatedocument_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization), [Presigned](../README.md#Presigned)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | The user has been redirected |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezdoctemplatedocument_edit_object_v1**
> CommonResponse ezdoctemplatedocument_edit_object_v1(pki_ezdoctemplatedocument_id, ezdoctemplatedocument_edit_object_v1_request)

Edit an existing Ezdoctemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.ezdoctemplatedocument_edit_object_v1_request import EzdoctemplatedocumentEditObjectV1Request
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
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    pki_ezdoctemplatedocument_id = 56 # int | The unique ID of the Ezdoctemplatedocument
    ezdoctemplatedocument_edit_object_v1_request = eZmaxApi.EzdoctemplatedocumentEditObjectV1Request() # EzdoctemplatedocumentEditObjectV1Request | 

    try:
        # Edit an existing Ezdoctemplatedocument
        api_response = api_instance.ezdoctemplatedocument_edit_object_v1(pki_ezdoctemplatedocument_id, ezdoctemplatedocument_edit_object_v1_request)
        print("The response of ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezdoctemplatedocument_id** | **int**| The unique ID of the Ezdoctemplatedocument | 
 **ezdoctemplatedocument_edit_object_v1_request** | [**EzdoctemplatedocumentEditObjectV1Request**](EzdoctemplatedocumentEditObjectV1Request.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

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

# **ezdoctemplatedocument_get_autocomplete_v2**
> EzdoctemplatedocumentGetAutocompleteV2Response ezdoctemplatedocument_get_autocomplete_v2(s_selector, e_type, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Ezdoctemplatedocuments and IDs

Get the list of Ezdoctemplatedocument to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezdoctemplatedocument_get_autocomplete_v2_response import EzdoctemplatedocumentGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    s_selector = 's_selector_example' # str | The type of Ezdoctemplatedocuments to return
    e_type = CompanyEzsignfoldertype # str | The type of Ezdoctemplatedocument (default to CompanyEzsignfoldertype)
    fki_ezsignfoldertype_id = 'fki_ezsignfoldertype_id_example' # str | Specify which fkiEzsignfoldertypeID we want to display. only used when eType = Ezsignfoldertype (optional)
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Ezdoctemplatedocuments and IDs
        api_response = api_instance.ezdoctemplatedocument_get_autocomplete_v2(s_selector, e_type, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezdoctemplatedocuments to return | 
 **e_type** | **str**| The type of Ezdoctemplatedocument | [default to CompanyEzsignfoldertype]
 **fki_ezsignfoldertype_id** | **str**| Specify which fkiEzsignfoldertypeID we want to display. only used when eType &#x3D; Ezsignfoldertype | [optional] 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**EzdoctemplatedocumentGetAutocompleteV2Response**](EzdoctemplatedocumentGetAutocompleteV2Response.md)

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

# **ezdoctemplatedocument_get_list_v1**
> EzdoctemplatedocumentGetListV1Response ezdoctemplatedocument_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Ezdoctemplatedocument list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezdoctemplatedocument_get_list_v1_response import EzdoctemplatedocumentGetListV1Response
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
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Ezdoctemplatedocument list
        api_response = api_instance.ezdoctemplatedocument_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_get_list_v1: %s\n" % e)
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

[**EzdoctemplatedocumentGetListV1Response**](EzdoctemplatedocumentGetListV1Response.md)

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

# **ezdoctemplatedocument_get_object_v2**
> EzdoctemplatedocumentGetObjectV2Response ezdoctemplatedocument_get_object_v2(pki_ezdoctemplatedocument_id)

Retrieve an existing Ezdoctemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezdoctemplatedocument_get_object_v2_response import EzdoctemplatedocumentGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    pki_ezdoctemplatedocument_id = 56 # int | The unique ID of the Ezdoctemplatedocument

    try:
        # Retrieve an existing Ezdoctemplatedocument
        api_response = api_instance.ezdoctemplatedocument_get_object_v2(pki_ezdoctemplatedocument_id)
        print("The response of ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezdoctemplatedocument_id** | **int**| The unique ID of the Ezdoctemplatedocument | 

### Return type

[**EzdoctemplatedocumentGetObjectV2Response**](EzdoctemplatedocumentGetObjectV2Response.md)

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

# **ezdoctemplatedocument_patch_object_v1**
> CommonResponse ezdoctemplatedocument_patch_object_v1(pki_ezdoctemplatedocument_id, ezdoctemplatedocument_patch_object_v1_request)

Patch an existing Ezdoctemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.ezdoctemplatedocument_patch_object_v1_request import EzdoctemplatedocumentPatchObjectV1Request
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
    api_instance = eZmaxApi.ObjectEzdoctemplatedocumentApi(api_client)
    pki_ezdoctemplatedocument_id = 56 # int | The unique ID of the Ezdoctemplatedocument
    ezdoctemplatedocument_patch_object_v1_request = eZmaxApi.EzdoctemplatedocumentPatchObjectV1Request() # EzdoctemplatedocumentPatchObjectV1Request | 

    try:
        # Patch an existing Ezdoctemplatedocument
        api_response = api_instance.ezdoctemplatedocument_patch_object_v1(pki_ezdoctemplatedocument_id, ezdoctemplatedocument_patch_object_v1_request)
        print("The response of ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzdoctemplatedocumentApi->ezdoctemplatedocument_patch_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezdoctemplatedocument_id** | **int**| The unique ID of the Ezdoctemplatedocument | 
 **ezdoctemplatedocument_patch_object_v1_request** | [**EzdoctemplatedocumentPatchObjectV1Request**](EzdoctemplatedocumentPatchObjectV1Request.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

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

