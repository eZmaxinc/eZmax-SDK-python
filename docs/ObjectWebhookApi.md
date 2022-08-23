# eZmaxApi.ObjectWebhookApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_create_object_v1**](ObjectWebhookApi.md#webhook_create_object_v1) | **POST** /1/object/webhook | Create a new Webhook
[**webhook_delete_object_v1**](ObjectWebhookApi.md#webhook_delete_object_v1) | **DELETE** /1/object/webhook/{pkiWebhookID} | Delete an existing Webhook
[**webhook_edit_object_v1**](ObjectWebhookApi.md#webhook_edit_object_v1) | **PUT** /1/object/webhook/{pkiWebhookID} | Edit an existing Webhook
[**webhook_get_history_v1**](ObjectWebhookApi.md#webhook_get_history_v1) | **GET** /1/object/webhook/{pkiWebhookID}/getHistory | Retrieve the logs for recent Webhook calls
[**webhook_get_list_v1**](ObjectWebhookApi.md#webhook_get_list_v1) | **GET** /1/object/webhook/getList | Retrieve Webhook list
[**webhook_get_object_v1**](ObjectWebhookApi.md#webhook_get_object_v1) | **GET** /1/object/webhook/{pkiWebhookID} | Retrieve an existing Webhook
[**webhook_test_url_v1**](ObjectWebhookApi.md#webhook_test_url_v1) | **POST** /1/object/webhook/{pkiWebhookID}/test | Test the Webhook by calling the Url


# **webhook_create_object_v1**
> WebhookCreateObjectV1Response webhook_create_object_v1(webhook_create_object_v1_request)

Create a new Webhook

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.webhook_create_object_v1_response import WebhookCreateObjectV1Response
from eZmaxApi.model.webhook_create_object_v1_request import WebhookCreateObjectV1Request
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    webhook_create_object_v1_request = WebhookCreateObjectV1Request(
        a_obj_webhook=[
            WebhookRequestCompound(),
        ],
    ) # WebhookCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Webhook
        api_response = api_instance.webhook_create_object_v1(webhook_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_create_object_v1_request** | [**WebhookCreateObjectV1Request**](WebhookCreateObjectV1Request.md)|  |

### Return type

[**WebhookCreateObjectV1Response**](WebhookCreateObjectV1Response.md)

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

# **webhook_delete_object_v1**
> WebhookDeleteObjectV1Response webhook_delete_object_v1(pki_webhook_id)

Delete an existing Webhook



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.webhook_delete_object_v1_response import WebhookDeleteObjectV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    pki_webhook_id = 77 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Webhook
        api_response = api_instance.webhook_delete_object_v1(pki_webhook_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  |

### Return type

[**WebhookDeleteObjectV1Response**](WebhookDeleteObjectV1Response.md)

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

# **webhook_edit_object_v1**
> WebhookEditObjectV1Response webhook_edit_object_v1(pki_webhook_id, webhook_edit_object_v1_request)

Edit an existing Webhook



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.webhook_edit_object_v1_response import WebhookEditObjectV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.webhook_edit_object_v1_request import WebhookEditObjectV1Request
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    pki_webhook_id = 77 # int | 
    webhook_edit_object_v1_request = WebhookEditObjectV1Request(
        obj_webhook=WebhookRequestCompound(),
    ) # WebhookEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Webhook
        api_response = api_instance.webhook_edit_object_v1(pki_webhook_id, webhook_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  |
 **webhook_edit_object_v1_request** | [**WebhookEditObjectV1Request**](WebhookEditObjectV1Request.md)|  |

### Return type

[**WebhookEditObjectV1Response**](WebhookEditObjectV1Response.md)

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

# **webhook_get_history_v1**
> WebhookGetHistoryV1Response webhook_get_history_v1(pki_webhook_id, e_webhook_historyinterval)

Retrieve the logs for recent Webhook calls



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.webhook_get_history_v1_response import WebhookGetHistoryV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    pki_webhook_id = 77 # int | 
    e_webhook_historyinterval = "LastDay" # str | The number of days to return

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the logs for recent Webhook calls
        api_response = api_instance.webhook_get_history_v1(pki_webhook_id, e_webhook_historyinterval)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_get_history_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  |
 **e_webhook_historyinterval** | **str**| The number of days to return |

### Return type

[**WebhookGetHistoryV1Response**](WebhookGetHistoryV1Response.md)

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

# **webhook_get_list_v1**
> WebhookGetListV1Response webhook_get_list_v1()

Retrieve Webhook list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eWebhookModule | Ezsign<br>Management | | eWebhookEzsignevent | DocumentCompleted<br>FolderCompleted | | eWebhookManagementevent | UserCreated |

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.webhook_get_list_v1_response import WebhookGetListV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    e_order_by = "pkiWebhookID_ASC" # str | Specify how you want the results to be sorted (optional)
    i_row_max = FieldIRowMax(100) # int |  (optional)
    i_row_offset = FieldIRowOffset(0) # int |  (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)
    s_filter = "bField1 eq true and iField2 gte 0 and iField2 lte 1000 and sField3 eq 'Other' and eField4 eq 'Paid' and sField5 like '%needle%' and iField6 in '1,2,3' and dtField7 rg '=m,=3mm'" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Webhook list
        api_response = api_instance.webhook_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_get_list_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional]
 **i_row_max** | **int**|  | [optional]
 **i_row_offset** | **int**|  | [optional]
 **accept_language** | **HeaderAcceptLanguage**|  | [optional]
 **s_filter** | **str**|  | [optional]

### Return type

[**WebhookGetListV1Response**](WebhookGetListV1Response.md)

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

# **webhook_get_object_v1**
> WebhookGetObjectV1Response webhook_get_object_v1(pki_webhook_id)

Retrieve an existing Webhook



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.webhook_get_object_v1_response import WebhookGetObjectV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    pki_webhook_id = 77 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Webhook
        api_response = api_instance.webhook_get_object_v1(pki_webhook_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  |

### Return type

[**WebhookGetObjectV1Response**](WebhookGetObjectV1Response.md)

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

# **webhook_test_url_v1**
> WebhookTestV1Response webhook_test_url_v1(pki_webhook_id)

Test the Webhook by calling the Url



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_webhook_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.webhook_test_v1_response import WebhookTestV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_webhook_api.ObjectWebhookApi(api_client)
    pki_webhook_id = 77 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Test the Webhook by calling the Url
        api_response = api_instance.webhook_test_url_v1(pki_webhook_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectWebhookApi->webhook_test_url_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  |

### Return type

[**WebhookTestV1Response**](WebhookTestV1Response.md)

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

