# eZmaxApi.ObjectSupplyApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supply_create_object_v1**](ObjectSupplyApi.md#supply_create_object_v1) | **POST** /1/object/supply | Create a new Supply
[**supply_delete_object_v1**](ObjectSupplyApi.md#supply_delete_object_v1) | **DELETE** /1/object/supply/{pkiSupplyID} | Delete an existing Supply
[**supply_edit_object_v1**](ObjectSupplyApi.md#supply_edit_object_v1) | **PUT** /1/object/supply/{pkiSupplyID} | Edit an existing Supply
[**supply_get_autocomplete_v2**](ObjectSupplyApi.md#supply_get_autocomplete_v2) | **GET** /2/object/supply/getAutocomplete/{sSelector} | Retrieve Supplys and IDs
[**supply_get_list_v1**](ObjectSupplyApi.md#supply_get_list_v1) | **GET** /1/object/supply/getList | Retrieve Supply list
[**supply_get_object_v2**](ObjectSupplyApi.md#supply_get_object_v2) | **GET** /2/object/supply/{pkiSupplyID} | Retrieve an existing Supply


# **supply_create_object_v1**
> SupplyCreateObjectV1Response supply_create_object_v1(supply_create_object_v1_request)

Create a new Supply

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.supply_create_object_v1_request import SupplyCreateObjectV1Request
from eZmaxApi.models.supply_create_object_v1_response import SupplyCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectSupplyApi(api_client)
    supply_create_object_v1_request = eZmaxApi.SupplyCreateObjectV1Request() # SupplyCreateObjectV1Request | 

    try:
        # Create a new Supply
        api_response = api_instance.supply_create_object_v1(supply_create_object_v1_request)
        print("The response of ObjectSupplyApi->supply_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSupplyApi->supply_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supply_create_object_v1_request** | [**SupplyCreateObjectV1Request**](SupplyCreateObjectV1Request.md)|  | 

### Return type

[**SupplyCreateObjectV1Response**](SupplyCreateObjectV1Response.md)

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

# **supply_delete_object_v1**
> SupplyDeleteObjectV1Response supply_delete_object_v1(pki_supply_id)

Delete an existing Supply



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.supply_delete_object_v1_response import SupplyDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectSupplyApi(api_client)
    pki_supply_id = 56 # int | The unique ID of the Supply

    try:
        # Delete an existing Supply
        api_response = api_instance.supply_delete_object_v1(pki_supply_id)
        print("The response of ObjectSupplyApi->supply_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSupplyApi->supply_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_supply_id** | **int**| The unique ID of the Supply | 

### Return type

[**SupplyDeleteObjectV1Response**](SupplyDeleteObjectV1Response.md)

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

# **supply_edit_object_v1**
> SupplyEditObjectV1Response supply_edit_object_v1(pki_supply_id, supply_edit_object_v1_request)

Edit an existing Supply



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.supply_edit_object_v1_request import SupplyEditObjectV1Request
from eZmaxApi.models.supply_edit_object_v1_response import SupplyEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectSupplyApi(api_client)
    pki_supply_id = 56 # int | The unique ID of the Supply
    supply_edit_object_v1_request = eZmaxApi.SupplyEditObjectV1Request() # SupplyEditObjectV1Request | 

    try:
        # Edit an existing Supply
        api_response = api_instance.supply_edit_object_v1(pki_supply_id, supply_edit_object_v1_request)
        print("The response of ObjectSupplyApi->supply_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSupplyApi->supply_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_supply_id** | **int**| The unique ID of the Supply | 
 **supply_edit_object_v1_request** | [**SupplyEditObjectV1Request**](SupplyEditObjectV1Request.md)|  | 

### Return type

[**SupplyEditObjectV1Response**](SupplyEditObjectV1Response.md)

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

# **supply_get_autocomplete_v2**
> SupplyGetAutocompleteV2Response supply_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Supplys and IDs

Get the list of Supply to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.supply_get_autocomplete_v2_response import SupplyGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectSupplyApi(api_client)
    s_selector = 's_selector_example' # str | The type of Supplys to return
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Supplys and IDs
        api_response = api_instance.supply_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectSupplyApi->supply_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSupplyApi->supply_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Supplys to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**SupplyGetAutocompleteV2Response**](SupplyGetAutocompleteV2Response.md)

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

# **supply_get_list_v1**
> SupplyGetListV1Response supply_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Supply list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.supply_get_list_v1_response import SupplyGetListV1Response
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
    api_instance = eZmaxApi.ObjectSupplyApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Supply list
        api_response = api_instance.supply_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectSupplyApi->supply_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSupplyApi->supply_get_list_v1: %s\n" % e)
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

[**SupplyGetListV1Response**](SupplyGetListV1Response.md)

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

# **supply_get_object_v2**
> SupplyGetObjectV2Response supply_get_object_v2(pki_supply_id)

Retrieve an existing Supply



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.supply_get_object_v2_response import SupplyGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectSupplyApi(api_client)
    pki_supply_id = 56 # int | The unique ID of the Supply

    try:
        # Retrieve an existing Supply
        api_response = api_instance.supply_get_object_v2(pki_supply_id)
        print("The response of ObjectSupplyApi->supply_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSupplyApi->supply_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_supply_id** | **int**| The unique ID of the Supply | 

### Return type

[**SupplyGetObjectV2Response**](SupplyGetObjectV2Response.md)

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

