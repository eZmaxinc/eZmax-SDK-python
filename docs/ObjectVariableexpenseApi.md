# eZmaxApi.ObjectVariableexpenseApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variableexpense_create_object_v1**](ObjectVariableexpenseApi.md#variableexpense_create_object_v1) | **POST** /1/object/variableexpense | Create a new Variableexpense
[**variableexpense_edit_object_v1**](ObjectVariableexpenseApi.md#variableexpense_edit_object_v1) | **PUT** /1/object/variableexpense/{pkiVariableexpenseID} | Edit an existing Variableexpense
[**variableexpense_get_autocomplete_v2**](ObjectVariableexpenseApi.md#variableexpense_get_autocomplete_v2) | **GET** /2/object/variableexpense/getAutocomplete/{sSelector} | Retrieve Variableexpenses and IDs
[**variableexpense_get_list_v1**](ObjectVariableexpenseApi.md#variableexpense_get_list_v1) | **GET** /1/object/variableexpense/getList | Retrieve Variableexpense list
[**variableexpense_get_object_v2**](ObjectVariableexpenseApi.md#variableexpense_get_object_v2) | **GET** /2/object/variableexpense/{pkiVariableexpenseID} | Retrieve an existing Variableexpense


# **variableexpense_create_object_v1**
> VariableexpenseCreateObjectV1Response variableexpense_create_object_v1(variableexpense_create_object_v1_request)

Create a new Variableexpense

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.variableexpense_create_object_v1_request import VariableexpenseCreateObjectV1Request
from eZmaxApi.models.variableexpense_create_object_v1_response import VariableexpenseCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectVariableexpenseApi(api_client)
    variableexpense_create_object_v1_request = eZmaxApi.VariableexpenseCreateObjectV1Request() # VariableexpenseCreateObjectV1Request | 

    try:
        # Create a new Variableexpense
        api_response = api_instance.variableexpense_create_object_v1(variableexpense_create_object_v1_request)
        print("The response of ObjectVariableexpenseApi->variableexpense_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectVariableexpenseApi->variableexpense_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variableexpense_create_object_v1_request** | [**VariableexpenseCreateObjectV1Request**](VariableexpenseCreateObjectV1Request.md)|  | 

### Return type

[**VariableexpenseCreateObjectV1Response**](VariableexpenseCreateObjectV1Response.md)

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

# **variableexpense_edit_object_v1**
> VariableexpenseEditObjectV1Response variableexpense_edit_object_v1(pki_variableexpense_id, variableexpense_edit_object_v1_request)

Edit an existing Variableexpense



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.variableexpense_edit_object_v1_request import VariableexpenseEditObjectV1Request
from eZmaxApi.models.variableexpense_edit_object_v1_response import VariableexpenseEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectVariableexpenseApi(api_client)
    pki_variableexpense_id = 56 # int | 
    variableexpense_edit_object_v1_request = eZmaxApi.VariableexpenseEditObjectV1Request() # VariableexpenseEditObjectV1Request | 

    try:
        # Edit an existing Variableexpense
        api_response = api_instance.variableexpense_edit_object_v1(pki_variableexpense_id, variableexpense_edit_object_v1_request)
        print("The response of ObjectVariableexpenseApi->variableexpense_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectVariableexpenseApi->variableexpense_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_variableexpense_id** | **int**|  | 
 **variableexpense_edit_object_v1_request** | [**VariableexpenseEditObjectV1Request**](VariableexpenseEditObjectV1Request.md)|  | 

### Return type

[**VariableexpenseEditObjectV1Response**](VariableexpenseEditObjectV1Response.md)

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

# **variableexpense_get_autocomplete_v2**
> VariableexpenseGetAutocompleteV2Response variableexpense_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Variableexpenses and IDs

Get the list of Variableexpense to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.variableexpense_get_autocomplete_v2_response import VariableexpenseGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectVariableexpenseApi(api_client)
    s_selector = 's_selector_example' # str | The type of Variableexpenses to return
    e_filter_active = 'Active' # str | Specify which results we want to display. (optional) (default to 'Active')
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Variableexpenses and IDs
        api_response = api_instance.variableexpense_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectVariableexpenseApi->variableexpense_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectVariableexpenseApi->variableexpense_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Variableexpenses to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to &#39;Active&#39;]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**VariableexpenseGetAutocompleteV2Response**](VariableexpenseGetAutocompleteV2Response.md)

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

# **variableexpense_get_list_v1**
> VariableexpenseGetListV1Response variableexpense_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Variableexpense list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eVariableexpenseTaxable | Yes<br>No<br>Included |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.variableexpense_get_list_v1_response import VariableexpenseGetListV1Response
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
    api_instance = eZmaxApi.ObjectVariableexpenseApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Variableexpense list
        api_response = api_instance.variableexpense_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectVariableexpenseApi->variableexpense_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectVariableexpenseApi->variableexpense_get_list_v1: %s\n" % e)
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

[**VariableexpenseGetListV1Response**](VariableexpenseGetListV1Response.md)

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

# **variableexpense_get_object_v2**
> VariableexpenseGetObjectV2Response variableexpense_get_object_v2(pki_variableexpense_id)

Retrieve an existing Variableexpense



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.variableexpense_get_object_v2_response import VariableexpenseGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectVariableexpenseApi(api_client)
    pki_variableexpense_id = 56 # int | 

    try:
        # Retrieve an existing Variableexpense
        api_response = api_instance.variableexpense_get_object_v2(pki_variableexpense_id)
        print("The response of ObjectVariableexpenseApi->variableexpense_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectVariableexpenseApi->variableexpense_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_variableexpense_id** | **int**|  | 

### Return type

[**VariableexpenseGetObjectV2Response**](VariableexpenseGetObjectV2Response.md)

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

