# eZmaxApi.ObjectPaymenttermApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentterm_create_object_v1**](ObjectPaymenttermApi.md#paymentterm_create_object_v1) | **POST** /1/object/paymentterm | Create a new Paymentterm
[**paymentterm_edit_object_v1**](ObjectPaymenttermApi.md#paymentterm_edit_object_v1) | **PUT** /1/object/paymentterm/{pkiPaymenttermID} | Edit an existing Paymentterm
[**paymentterm_get_autocomplete_v2**](ObjectPaymenttermApi.md#paymentterm_get_autocomplete_v2) | **GET** /2/object/paymentterm/getAutocomplete/{sSelector} | Retrieve Paymentterms and IDs
[**paymentterm_get_list_v1**](ObjectPaymenttermApi.md#paymentterm_get_list_v1) | **GET** /1/object/paymentterm/getList | Retrieve Paymentterm list
[**paymentterm_get_object_v2**](ObjectPaymenttermApi.md#paymentterm_get_object_v2) | **GET** /2/object/paymentterm/{pkiPaymenttermID} | Retrieve an existing Paymentterm


# **paymentterm_create_object_v1**
> PaymenttermCreateObjectV1Response paymentterm_create_object_v1(paymentterm_create_object_v1_request)

Create a new Paymentterm

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.paymentterm_create_object_v1_request import PaymenttermCreateObjectV1Request
from eZmaxApi.models.paymentterm_create_object_v1_response import PaymenttermCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectPaymenttermApi(api_client)
    paymentterm_create_object_v1_request = eZmaxApi.PaymenttermCreateObjectV1Request() # PaymenttermCreateObjectV1Request | 

    try:
        # Create a new Paymentterm
        api_response = api_instance.paymentterm_create_object_v1(paymentterm_create_object_v1_request)
        print("The response of ObjectPaymenttermApi->paymentterm_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymenttermApi->paymentterm_create_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentterm_create_object_v1_request** | [**PaymenttermCreateObjectV1Request**](PaymenttermCreateObjectV1Request.md)|  | 

### Return type

[**PaymenttermCreateObjectV1Response**](PaymenttermCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paymentterm_edit_object_v1**
> PaymenttermEditObjectV1Response paymentterm_edit_object_v1(pki_paymentterm_id, paymentterm_edit_object_v1_request)

Edit an existing Paymentterm



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.paymentterm_edit_object_v1_request import PaymenttermEditObjectV1Request
from eZmaxApi.models.paymentterm_edit_object_v1_response import PaymenttermEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectPaymenttermApi(api_client)
    pki_paymentterm_id = 56 # int | 
    paymentterm_edit_object_v1_request = eZmaxApi.PaymenttermEditObjectV1Request() # PaymenttermEditObjectV1Request | 

    try:
        # Edit an existing Paymentterm
        api_response = api_instance.paymentterm_edit_object_v1(pki_paymentterm_id, paymentterm_edit_object_v1_request)
        print("The response of ObjectPaymenttermApi->paymentterm_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymenttermApi->paymentterm_edit_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentterm_id** | **int**|  | 
 **paymentterm_edit_object_v1_request** | [**PaymenttermEditObjectV1Request**](PaymenttermEditObjectV1Request.md)|  | 

### Return type

[**PaymenttermEditObjectV1Response**](PaymenttermEditObjectV1Response.md)

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

# **paymentterm_get_autocomplete_v2**
> PaymenttermGetAutocompleteV2Response paymentterm_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Paymentterms and IDs

Get the list of Paymentterm to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.paymentterm_get_autocomplete_v2_response import PaymenttermGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectPaymenttermApi(api_client)
    s_selector = 's_selector_example' # str | The type of Paymentterms to return
    e_filter_active = 'Active' # str | Specify which results we want to display. (optional) (default to 'Active')
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Paymentterms and IDs
        api_response = api_instance.paymentterm_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectPaymenttermApi->paymentterm_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymenttermApi->paymentterm_get_autocomplete_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Paymentterms to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to &#39;Active&#39;]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**PaymenttermGetAutocompleteV2Response**](PaymenttermGetAutocompleteV2Response.md)

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

# **paymentterm_get_list_v1**
> PaymenttermGetListV1Response paymentterm_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Paymentterm list

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.paymentterm_get_list_v1_response import PaymenttermGetListV1Response
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
    api_instance = eZmaxApi.ObjectPaymenttermApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 10000 # int |  (optional) (default to 10000)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Paymentterm list
        api_response = api_instance.paymentterm_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectPaymenttermApi->paymentterm_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymenttermApi->paymentterm_get_list_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional] 
 **i_row_max** | **int**|  | [optional] [default to 10000]
 **i_row_offset** | **int**|  | [optional] [default to 0]
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 
 **s_filter** | **str**|  | [optional] 

### Return type

[**PaymenttermGetListV1Response**](PaymenttermGetListV1Response.md)

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

# **paymentterm_get_object_v2**
> PaymenttermGetObjectV2Response paymentterm_get_object_v2(pki_paymentterm_id)

Retrieve an existing Paymentterm



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.paymentterm_get_object_v2_response import PaymenttermGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectPaymenttermApi(api_client)
    pki_paymentterm_id = 56 # int | 

    try:
        # Retrieve an existing Paymentterm
        api_response = api_instance.paymentterm_get_object_v2(pki_paymentterm_id)
        print("The response of ObjectPaymenttermApi->paymentterm_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymenttermApi->paymentterm_get_object_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentterm_id** | **int**|  | 

### Return type

[**PaymenttermGetObjectV2Response**](PaymenttermGetObjectV2Response.md)

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

