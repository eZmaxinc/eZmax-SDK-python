# eZmaxApi.ObjectDocumenttypechecklistApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documenttypechecklist_create_object_v1**](ObjectDocumenttypechecklistApi.md#documenttypechecklist_create_object_v1) | **POST** /1/object/documenttypechecklist | Create a new Documenttypechecklist
[**documenttypechecklist_delete_object_v1**](ObjectDocumenttypechecklistApi.md#documenttypechecklist_delete_object_v1) | **DELETE** /1/object/documenttypechecklist/{pkiDocumenttypechecklistID} | Delete an existing Documenttypechecklist
[**documenttypechecklist_edit_object_v1**](ObjectDocumenttypechecklistApi.md#documenttypechecklist_edit_object_v1) | **PUT** /1/object/documenttypechecklist/{pkiDocumenttypechecklistID} | Edit an existing Documenttypechecklist
[**documenttypechecklist_get_list_v1**](ObjectDocumenttypechecklistApi.md#documenttypechecklist_get_list_v1) | **GET** /1/object/documenttypechecklist/getList | Retrieve Documenttypechecklist list
[**documenttypechecklist_get_object_v2**](ObjectDocumenttypechecklistApi.md#documenttypechecklist_get_object_v2) | **GET** /2/object/documenttypechecklist/{pkiDocumenttypechecklistID} | Retrieve an existing Documenttypechecklist


# **documenttypechecklist_create_object_v1**
> DocumenttypechecklistCreateObjectV1Response documenttypechecklist_create_object_v1(documenttypechecklist_create_object_v1_request)

Create a new Documenttypechecklist

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.documenttypechecklist_create_object_v1_request import DocumenttypechecklistCreateObjectV1Request
from eZmaxApi.models.documenttypechecklist_create_object_v1_response import DocumenttypechecklistCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectDocumenttypechecklistApi(api_client)
    documenttypechecklist_create_object_v1_request = eZmaxApi.DocumenttypechecklistCreateObjectV1Request() # DocumenttypechecklistCreateObjectV1Request | 

    try:
        # Create a new Documenttypechecklist
        api_response = api_instance.documenttypechecklist_create_object_v1(documenttypechecklist_create_object_v1_request)
        print("The response of ObjectDocumenttypechecklistApi->documenttypechecklist_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDocumenttypechecklistApi->documenttypechecklist_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documenttypechecklist_create_object_v1_request** | [**DocumenttypechecklistCreateObjectV1Request**](DocumenttypechecklistCreateObjectV1Request.md)|  | 

### Return type

[**DocumenttypechecklistCreateObjectV1Response**](DocumenttypechecklistCreateObjectV1Response.md)

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

# **documenttypechecklist_delete_object_v1**
> DocumenttypechecklistDeleteObjectV1Response documenttypechecklist_delete_object_v1(pki_documenttypechecklist_id)

Delete an existing Documenttypechecklist



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.documenttypechecklist_delete_object_v1_response import DocumenttypechecklistDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectDocumenttypechecklistApi(api_client)
    pki_documenttypechecklist_id = 56 # int | The unique ID of the Documenttypechecklist

    try:
        # Delete an existing Documenttypechecklist
        api_response = api_instance.documenttypechecklist_delete_object_v1(pki_documenttypechecklist_id)
        print("The response of ObjectDocumenttypechecklistApi->documenttypechecklist_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDocumenttypechecklistApi->documenttypechecklist_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_documenttypechecklist_id** | **int**| The unique ID of the Documenttypechecklist | 

### Return type

[**DocumenttypechecklistDeleteObjectV1Response**](DocumenttypechecklistDeleteObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documenttypechecklist_edit_object_v1**
> DocumenttypechecklistEditObjectV1Response documenttypechecklist_edit_object_v1(pki_documenttypechecklist_id, documenttypechecklist_edit_object_v1_request)

Edit an existing Documenttypechecklist



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.documenttypechecklist_edit_object_v1_request import DocumenttypechecklistEditObjectV1Request
from eZmaxApi.models.documenttypechecklist_edit_object_v1_response import DocumenttypechecklistEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectDocumenttypechecklistApi(api_client)
    pki_documenttypechecklist_id = 56 # int | The unique ID of the Documenttypechecklist
    documenttypechecklist_edit_object_v1_request = eZmaxApi.DocumenttypechecklistEditObjectV1Request() # DocumenttypechecklistEditObjectV1Request | 

    try:
        # Edit an existing Documenttypechecklist
        api_response = api_instance.documenttypechecklist_edit_object_v1(pki_documenttypechecklist_id, documenttypechecklist_edit_object_v1_request)
        print("The response of ObjectDocumenttypechecklistApi->documenttypechecklist_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDocumenttypechecklistApi->documenttypechecklist_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_documenttypechecklist_id** | **int**| The unique ID of the Documenttypechecklist | 
 **documenttypechecklist_edit_object_v1_request** | [**DocumenttypechecklistEditObjectV1Request**](DocumenttypechecklistEditObjectV1Request.md)|  | 

### Return type

[**DocumenttypechecklistEditObjectV1Response**](DocumenttypechecklistEditObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documenttypechecklist_get_list_v1**
> DocumenttypechecklistGetListV1Response documenttypechecklist_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Documenttypechecklist list

Enum values that can be filtered in query parameter *sFilter*:

| Variable | Valid values |
|---|---|
| eDocumenttypechecklistStatus | Not required<br>Required<br>Filed<br>Justified |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.documenttypechecklist_get_list_v1_response import DocumenttypechecklistGetListV1Response
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
    api_instance = eZmaxApi.ObjectDocumenttypechecklistApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Documenttypechecklist list
        api_response = api_instance.documenttypechecklist_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectDocumenttypechecklistApi->documenttypechecklist_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDocumenttypechecklistApi->documenttypechecklist_get_list_v1: %s\n" % e)
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

[**DocumenttypechecklistGetListV1Response**](DocumenttypechecklistGetListV1Response.md)

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

# **documenttypechecklist_get_object_v2**
> DocumenttypechecklistGetObjectV2Response documenttypechecklist_get_object_v2(pki_documenttypechecklist_id)

Retrieve an existing Documenttypechecklist



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.documenttypechecklist_get_object_v2_response import DocumenttypechecklistGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectDocumenttypechecklistApi(api_client)
    pki_documenttypechecklist_id = 56 # int | The unique ID of the Documenttypechecklist

    try:
        # Retrieve an existing Documenttypechecklist
        api_response = api_instance.documenttypechecklist_get_object_v2(pki_documenttypechecklist_id)
        print("The response of ObjectDocumenttypechecklistApi->documenttypechecklist_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDocumenttypechecklistApi->documenttypechecklist_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_documenttypechecklist_id** | **int**| The unique ID of the Documenttypechecklist | 

### Return type

[**DocumenttypechecklistGetObjectV2Response**](DocumenttypechecklistGetObjectV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

