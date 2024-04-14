# eZmaxApi.ObjectCreditcardclientApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creditcardclient_create_object_v1**](ObjectCreditcardclientApi.md#creditcardclient_create_object_v1) | **POST** /1/object/creditcardclient | Create a new Creditcardclient
[**creditcardclient_delete_object_v1**](ObjectCreditcardclientApi.md#creditcardclient_delete_object_v1) | **DELETE** /1/object/creditcardclient/{pkiCreditcardclientID} | Delete an existing Creditcardclient
[**creditcardclient_edit_object_v1**](ObjectCreditcardclientApi.md#creditcardclient_edit_object_v1) | **PUT** /1/object/creditcardclient/{pkiCreditcardclientID} | Edit an existing Creditcardclient
[**creditcardclient_get_autocomplete_v2**](ObjectCreditcardclientApi.md#creditcardclient_get_autocomplete_v2) | **GET** /2/object/creditcardclient/getAutocomplete/{sSelector} | Retrieve Creditcardclients and IDs
[**creditcardclient_get_list_v1**](ObjectCreditcardclientApi.md#creditcardclient_get_list_v1) | **GET** /1/object/creditcardclient/getList | Retrieve Creditcardclient list
[**creditcardclient_get_object_v2**](ObjectCreditcardclientApi.md#creditcardclient_get_object_v2) | **GET** /2/object/creditcardclient/{pkiCreditcardclientID} | Retrieve an existing Creditcardclient


# **creditcardclient_create_object_v1**
> CreditcardclientCreateObjectV1Response creditcardclient_create_object_v1(creditcardclient_create_object_v1_request)

Create a new Creditcardclient

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.creditcardclient_create_object_v1_request import CreditcardclientCreateObjectV1Request
from eZmaxApi.models.creditcardclient_create_object_v1_response import CreditcardclientCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectCreditcardclientApi(api_client)
    creditcardclient_create_object_v1_request = eZmaxApi.CreditcardclientCreateObjectV1Request() # CreditcardclientCreateObjectV1Request | 

    try:
        # Create a new Creditcardclient
        api_response = api_instance.creditcardclient_create_object_v1(creditcardclient_create_object_v1_request)
        print("The response of ObjectCreditcardclientApi->creditcardclient_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCreditcardclientApi->creditcardclient_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditcardclient_create_object_v1_request** | [**CreditcardclientCreateObjectV1Request**](CreditcardclientCreateObjectV1Request.md)|  | 

### Return type

[**CreditcardclientCreateObjectV1Response**](CreditcardclientCreateObjectV1Response.md)

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

# **creditcardclient_delete_object_v1**
> CreditcardclientDeleteObjectV1Response creditcardclient_delete_object_v1(pki_creditcardclient_id)

Delete an existing Creditcardclient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.creditcardclient_delete_object_v1_response import CreditcardclientDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectCreditcardclientApi(api_client)
    pki_creditcardclient_id = 56 # int | The unique ID of the Creditcardclient

    try:
        # Delete an existing Creditcardclient
        api_response = api_instance.creditcardclient_delete_object_v1(pki_creditcardclient_id)
        print("The response of ObjectCreditcardclientApi->creditcardclient_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCreditcardclientApi->creditcardclient_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_creditcardclient_id** | **int**| The unique ID of the Creditcardclient | 

### Return type

[**CreditcardclientDeleteObjectV1Response**](CreditcardclientDeleteObjectV1Response.md)

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

# **creditcardclient_edit_object_v1**
> CreditcardclientEditObjectV1Response creditcardclient_edit_object_v1(pki_creditcardclient_id, creditcardclient_edit_object_v1_request)

Edit an existing Creditcardclient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.creditcardclient_edit_object_v1_request import CreditcardclientEditObjectV1Request
from eZmaxApi.models.creditcardclient_edit_object_v1_response import CreditcardclientEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectCreditcardclientApi(api_client)
    pki_creditcardclient_id = 56 # int | The unique ID of the Creditcardclient
    creditcardclient_edit_object_v1_request = eZmaxApi.CreditcardclientEditObjectV1Request() # CreditcardclientEditObjectV1Request | 

    try:
        # Edit an existing Creditcardclient
        api_response = api_instance.creditcardclient_edit_object_v1(pki_creditcardclient_id, creditcardclient_edit_object_v1_request)
        print("The response of ObjectCreditcardclientApi->creditcardclient_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCreditcardclientApi->creditcardclient_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_creditcardclient_id** | **int**| The unique ID of the Creditcardclient | 
 **creditcardclient_edit_object_v1_request** | [**CreditcardclientEditObjectV1Request**](CreditcardclientEditObjectV1Request.md)|  | 

### Return type

[**CreditcardclientEditObjectV1Response**](CreditcardclientEditObjectV1Response.md)

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

# **creditcardclient_get_autocomplete_v2**
> CreditcardclientGetAutocompleteV2Response creditcardclient_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Creditcardclients and IDs

Get the list of Creditcardclient to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.creditcardclient_get_autocomplete_v2_response import CreditcardclientGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectCreditcardclientApi(api_client)
    s_selector = 's_selector_example' # str | The type of Creditcardclients to return
    e_filter_active = 'Active' # str | Specify which results we want to display. (optional) (default to 'Active')
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Creditcardclients and IDs
        api_response = api_instance.creditcardclient_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectCreditcardclientApi->creditcardclient_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCreditcardclientApi->creditcardclient_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Creditcardclients to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to &#39;Active&#39;]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**CreditcardclientGetAutocompleteV2Response**](CreditcardclientGetAutocompleteV2Response.md)

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

# **creditcardclient_get_list_v1**
> CreditcardclientGetListV1Response creditcardclient_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Creditcardclient list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.creditcardclient_get_list_v1_response import CreditcardclientGetListV1Response
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
    api_instance = eZmaxApi.ObjectCreditcardclientApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Creditcardclient list
        api_response = api_instance.creditcardclient_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectCreditcardclientApi->creditcardclient_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCreditcardclientApi->creditcardclient_get_list_v1: %s\n" % e)
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

[**CreditcardclientGetListV1Response**](CreditcardclientGetListV1Response.md)

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

# **creditcardclient_get_object_v2**
> CreditcardclientGetObjectV2Response creditcardclient_get_object_v2(pki_creditcardclient_id)

Retrieve an existing Creditcardclient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.creditcardclient_get_object_v2_response import CreditcardclientGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectCreditcardclientApi(api_client)
    pki_creditcardclient_id = 56 # int | The unique ID of the Creditcardclient

    try:
        # Retrieve an existing Creditcardclient
        api_response = api_instance.creditcardclient_get_object_v2(pki_creditcardclient_id)
        print("The response of ObjectCreditcardclientApi->creditcardclient_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCreditcardclientApi->creditcardclient_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_creditcardclient_id** | **int**| The unique ID of the Creditcardclient | 

### Return type

[**CreditcardclientGetObjectV2Response**](CreditcardclientGetObjectV2Response.md)

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

