# eZmaxApi.ObjectWebhookApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_create_object_v2**](ObjectWebhookApi.md#webhook_create_object_v2) | **POST** /2/object/webhook | Create a new Webhook
[**webhook_delete_object_v1**](ObjectWebhookApi.md#webhook_delete_object_v1) | **DELETE** /1/object/webhook/{pkiWebhookID} | Delete an existing Webhook
[**webhook_edit_object_v1**](ObjectWebhookApi.md#webhook_edit_object_v1) | **PUT** /1/object/webhook/{pkiWebhookID} | Edit an existing Webhook
[**webhook_get_history_v1**](ObjectWebhookApi.md#webhook_get_history_v1) | **GET** /1/object/webhook/{pkiWebhookID}/getHistory | Retrieve the logs for recent Webhook calls
[**webhook_get_list_v1**](ObjectWebhookApi.md#webhook_get_list_v1) | **GET** /1/object/webhook/getList | Retrieve Webhook list
[**webhook_get_object_v2**](ObjectWebhookApi.md#webhook_get_object_v2) | **GET** /2/object/webhook/{pkiWebhookID} | Retrieve an existing Webhook
[**webhook_regenerate_apikey_v1**](ObjectWebhookApi.md#webhook_regenerate_apikey_v1) | **POST** /1/object/webhook/{pkiWebhookID}/regenerateApikey | Regenerate the Apikey
[**webhook_send_webhook_v1**](ObjectWebhookApi.md#webhook_send_webhook_v1) | **POST** /1/object/webhook/sendWebhook | Emit a Webhook event
[**webhook_test_v1**](ObjectWebhookApi.md#webhook_test_v1) | **POST** /1/object/webhook/{pkiWebhookID}/test | Test the Webhook by calling the Url


# **webhook_create_object_v2**
> WebhookCreateObjectV2Response webhook_create_object_v2(webhook_create_object_v2_request)

Create a new Webhook

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.webhook_create_object_v2_request import WebhookCreateObjectV2Request
from eZmaxApi.models.webhook_create_object_v2_response import WebhookCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    webhook_create_object_v2_request = eZmaxApi.WebhookCreateObjectV2Request() # WebhookCreateObjectV2Request | 

    try:
        # Create a new Webhook
        api_response = api_instance.webhook_create_object_v2(webhook_create_object_v2_request)
        print("The response of ObjectWebhookApi->webhook_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectWebhookApi->webhook_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_create_object_v2_request** | [**WebhookCreateObjectV2Request**](WebhookCreateObjectV2Request.md)|  | 

### Return type

[**WebhookCreateObjectV2Response**](WebhookCreateObjectV2Response.md)

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
import eZmaxApi
from eZmaxApi.models.webhook_delete_object_v1_response import WebhookDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    pki_webhook_id = 56 # int | 

    try:
        # Delete an existing Webhook
        api_response = api_instance.webhook_delete_object_v1(pki_webhook_id)
        print("The response of ObjectWebhookApi->webhook_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import eZmaxApi
from eZmaxApi.models.webhook_edit_object_v1_request import WebhookEditObjectV1Request
from eZmaxApi.models.webhook_edit_object_v1_response import WebhookEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    pki_webhook_id = 56 # int | 
    webhook_edit_object_v1_request = eZmaxApi.WebhookEditObjectV1Request() # WebhookEditObjectV1Request | 

    try:
        # Edit an existing Webhook
        api_response = api_instance.webhook_edit_object_v1(pki_webhook_id, webhook_edit_object_v1_request)
        print("The response of ObjectWebhookApi->webhook_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import eZmaxApi
from eZmaxApi.models.webhook_get_history_v1_response import WebhookGetHistoryV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    pki_webhook_id = 56 # int | 
    e_webhook_historyinterval = 'e_webhook_historyinterval_example' # str | The number of days to return

    try:
        # Retrieve the logs for recent Webhook calls
        api_response = api_instance.webhook_get_history_v1(pki_webhook_id, e_webhook_historyinterval)
        print("The response of ObjectWebhookApi->webhook_get_history_v1:\n")
        pprint(api_response)
    except Exception as e:
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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_get_list_v1**
> WebhookGetListV1Response webhook_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Webhook list

Enum values that can be filtered in query parameter *sFilter*:

| Variable | Valid values |
|---|---|
| eWebhookModule | Ezsign<br>Management |
| eWebhookEzsignevent | DocumentCompleted<br>FolderCompleted |
| eWebhookManagementevent | UserCreated |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.webhook_get_list_v1_response import WebhookGetListV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Webhook list
        api_response = api_instance.webhook_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectWebhookApi->webhook_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectWebhookApi->webhook_get_list_v1: %s\n" % e)
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

# **webhook_get_object_v2**
> WebhookGetObjectV2Response webhook_get_object_v2(pki_webhook_id)

Retrieve an existing Webhook



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.webhook_get_object_v2_response import WebhookGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    pki_webhook_id = 56 # int | 

    try:
        # Retrieve an existing Webhook
        api_response = api_instance.webhook_get_object_v2(pki_webhook_id)
        print("The response of ObjectWebhookApi->webhook_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectWebhookApi->webhook_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  | 

### Return type

[**WebhookGetObjectV2Response**](WebhookGetObjectV2Response.md)

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

# **webhook_regenerate_apikey_v1**
> WebhookRegenerateApikeyV1Response webhook_regenerate_apikey_v1(pki_webhook_id, webhook_regenerate_apikey_v1_request)

Regenerate the Apikey



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.webhook_regenerate_apikey_v1_request import WebhookRegenerateApikeyV1Request
from eZmaxApi.models.webhook_regenerate_apikey_v1_response import WebhookRegenerateApikeyV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    pki_webhook_id = 56 # int | 
    webhook_regenerate_apikey_v1_request = eZmaxApi.WebhookRegenerateApikeyV1Request() # WebhookRegenerateApikeyV1Request | 

    try:
        # Regenerate the Apikey
        api_response = api_instance.webhook_regenerate_apikey_v1(pki_webhook_id, webhook_regenerate_apikey_v1_request)
        print("The response of ObjectWebhookApi->webhook_regenerate_apikey_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectWebhookApi->webhook_regenerate_apikey_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  | 
 **webhook_regenerate_apikey_v1_request** | [**WebhookRegenerateApikeyV1Request**](WebhookRegenerateApikeyV1Request.md)|  | 

### Return type

[**WebhookRegenerateApikeyV1Response**](WebhookRegenerateApikeyV1Response.md)

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

# **webhook_send_webhook_v1**
> WebhookSendWebhookV1Response webhook_send_webhook_v1(webhook_send_webhook_v1_request)

Emit a Webhook event

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.webhook_send_webhook_v1_request import WebhookSendWebhookV1Request
from eZmaxApi.models.webhook_send_webhook_v1_response import WebhookSendWebhookV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    webhook_send_webhook_v1_request = eZmaxApi.WebhookSendWebhookV1Request() # WebhookSendWebhookV1Request | 

    try:
        # Emit a Webhook event
        api_response = api_instance.webhook_send_webhook_v1(webhook_send_webhook_v1_request)
        print("The response of ObjectWebhookApi->webhook_send_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectWebhookApi->webhook_send_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_send_webhook_v1_request** | [**WebhookSendWebhookV1Request**](WebhookSendWebhookV1Request.md)|  | 

### Return type

[**WebhookSendWebhookV1Response**](WebhookSendWebhookV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_test_v1**
> WebhookTestV1Response webhook_test_v1(pki_webhook_id, body)

Test the Webhook by calling the Url



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.webhook_test_v1_response import WebhookTestV1Response
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
    api_instance = eZmaxApi.ObjectWebhookApi(api_client)
    pki_webhook_id = 56 # int | 
    body = None # object | 

    try:
        # Test the Webhook by calling the Url
        api_response = api_instance.webhook_test_v1(pki_webhook_id, body)
        print("The response of ObjectWebhookApi->webhook_test_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectWebhookApi->webhook_test_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_webhook_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**WebhookTestV1Response**](WebhookTestV1Response.md)

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

