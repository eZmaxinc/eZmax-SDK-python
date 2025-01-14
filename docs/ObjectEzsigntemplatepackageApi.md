# eZmaxApi.ObjectEzsigntemplatepackageApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatepackage_create_object_v1**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_create_object_v1) | **POST** /1/object/ezsigntemplatepackage | Create a new Ezsigntemplatepackage
[**ezsigntemplatepackage_delete_object_v1**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_delete_object_v1) | **DELETE** /1/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID} | Delete an existing Ezsigntemplatepackage
[**ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1) | **PUT** /1/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}/editEzsigntemplatepackagesigners | Edit multiple Ezsigntemplatepackagesigners
[**ezsigntemplatepackage_edit_object_v1**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_edit_object_v1) | **PUT** /1/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID} | Edit an existing Ezsigntemplatepackage
[**ezsigntemplatepackage_get_autocomplete_v2**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_get_autocomplete_v2) | **GET** /2/object/ezsigntemplatepackage/getAutocomplete/{sSelector} | Retrieve Ezsigntemplatepackages and IDs
[**ezsigntemplatepackage_get_list_v1**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_get_list_v1) | **GET** /1/object/ezsigntemplatepackage/getList | Retrieve Ezsigntemplatepackage list
[**ezsigntemplatepackage_get_object_v2**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_get_object_v2) | **GET** /2/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID} | Retrieve an existing Ezsigntemplatepackage


# **ezsigntemplatepackage_create_object_v1**
> EzsigntemplatepackageCreateObjectV1Response ezsigntemplatepackage_create_object_v1(ezsigntemplatepackage_create_object_v1_request)

Create a new Ezsigntemplatepackage

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_create_object_v1_request import EzsigntemplatepackageCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatepackage_create_object_v1_response import EzsigntemplatepackageCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    ezsigntemplatepackage_create_object_v1_request = eZmaxApi.EzsigntemplatepackageCreateObjectV1Request() # EzsigntemplatepackageCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatepackage
        api_response = api_instance.ezsigntemplatepackage_create_object_v1(ezsigntemplatepackage_create_object_v1_request)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatepackage_create_object_v1_request** | [**EzsigntemplatepackageCreateObjectV1Request**](EzsigntemplatepackageCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatepackageCreateObjectV1Response**](EzsigntemplatepackageCreateObjectV1Response.md)

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

# **ezsigntemplatepackage_delete_object_v1**
> EzsigntemplatepackageDeleteObjectV1Response ezsigntemplatepackage_delete_object_v1(pki_ezsigntemplatepackage_id)

Delete an existing Ezsigntemplatepackage



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_delete_object_v1_response import EzsigntemplatepackageDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    pki_ezsigntemplatepackage_id = 56 # int | 

    try:
        # Delete an existing Ezsigntemplatepackage
        api_response = api_instance.ezsigntemplatepackage_delete_object_v1(pki_ezsigntemplatepackage_id)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackage_id** | **int**|  | 

### Return type

[**EzsigntemplatepackageDeleteObjectV1Response**](EzsigntemplatepackageDeleteObjectV1Response.md)

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

# **ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1**
> EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1(pki_ezsigntemplatepackage_id, ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request)

Edit multiple Ezsigntemplatepackagesigners

Using this endpoint, you can edit multiple Ezsigntemplatepackagesigners at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request import EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request
from eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_response import EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    pki_ezsigntemplatepackage_id = 56 # int | 
    ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request = eZmaxApi.EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request() # EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request | 

    try:
        # Edit multiple Ezsigntemplatepackagesigners
        api_response = api_instance.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1(pki_ezsigntemplatepackage_id, ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackage_id** | **int**|  | 
 **ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request** | [**EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request**](EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request.md)|  | 

### Return type

[**EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response**](EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response.md)

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

# **ezsigntemplatepackage_edit_object_v1**
> EzsigntemplatepackageEditObjectV1Response ezsigntemplatepackage_edit_object_v1(pki_ezsigntemplatepackage_id, ezsigntemplatepackage_edit_object_v1_request)

Edit an existing Ezsigntemplatepackage



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_edit_object_v1_request import EzsigntemplatepackageEditObjectV1Request
from eZmaxApi.models.ezsigntemplatepackage_edit_object_v1_response import EzsigntemplatepackageEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    pki_ezsigntemplatepackage_id = 56 # int | 
    ezsigntemplatepackage_edit_object_v1_request = eZmaxApi.EzsigntemplatepackageEditObjectV1Request() # EzsigntemplatepackageEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplatepackage
        api_response = api_instance.ezsigntemplatepackage_edit_object_v1(pki_ezsigntemplatepackage_id, ezsigntemplatepackage_edit_object_v1_request)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackage_id** | **int**|  | 
 **ezsigntemplatepackage_edit_object_v1_request** | [**EzsigntemplatepackageEditObjectV1Request**](EzsigntemplatepackageEditObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatepackageEditObjectV1Response**](EzsigntemplatepackageEditObjectV1Response.md)

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

# **ezsigntemplatepackage_get_autocomplete_v2**
> EzsigntemplatepackageGetAutocompleteV2Response ezsigntemplatepackage_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id)

Retrieve Ezsigntemplatepackages and IDs

Get the list of Ezsigntemplatepackage to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_get_autocomplete_v2_response import EzsigntemplatepackageGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    s_selector = 's_selector_example' # str | The type of Ezsigntemplatepackages to return
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    fki_ezsignfoldertype_id = 56 # int | The fkiEzsignfoldertypeID to use with the selector Ezsigntemplatepublic (optional)

    try:
        # Retrieve Ezsigntemplatepackages and IDs
        api_response = api_instance.ezsigntemplatepackage_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezsigntemplatepackages to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 
 **fki_ezsignfoldertype_id** | **int**| The fkiEzsignfoldertypeID to use with the selector Ezsigntemplatepublic | [optional] 

### Return type

[**EzsigntemplatepackageGetAutocompleteV2Response**](EzsigntemplatepackageGetAutocompleteV2Response.md)

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

# **ezsigntemplatepackage_get_list_v1**
> EzsigntemplatepackageGetListV1Response ezsigntemplatepackage_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Ezsigntemplatepackage list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsigntemplatepackageType | Company<br>Team<br>User<br>Usergroup |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_get_list_v1_response import EzsigntemplatepackageGetListV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Ezsigntemplatepackage list
        api_response = api_instance.ezsigntemplatepackage_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_list_v1: %s\n" % e)
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

[**EzsigntemplatepackageGetListV1Response**](EzsigntemplatepackageGetListV1Response.md)

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

# **ezsigntemplatepackage_get_object_v2**
> EzsigntemplatepackageGetObjectV2Response ezsigntemplatepackage_get_object_v2(pki_ezsigntemplatepackage_id)

Retrieve an existing Ezsigntemplatepackage



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackage_get_object_v2_response import EzsigntemplatepackageGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackageApi(api_client)
    pki_ezsigntemplatepackage_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatepackage
        api_response = api_instance.ezsigntemplatepackage_get_object_v2(pki_ezsigntemplatepackage_id)
        print("The response of ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackage_id** | **int**|  | 

### Return type

[**EzsigntemplatepackageGetObjectV2Response**](EzsigntemplatepackageGetObjectV2Response.md)

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

