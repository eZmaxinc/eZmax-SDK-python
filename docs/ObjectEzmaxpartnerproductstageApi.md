# eZmaxApi.ObjectEzmaxpartnerproductstageApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1**](ObjectEzmaxpartnerproductstageApi.md#ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1) | **GET** /1/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}/getEzmaxpartnerproductstagepermissions | Retrieve an existing Ezmaxpartnerproductstage&#39;s Ezmaxpartnerproductstagepermissions
[**ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1**](ObjectEzmaxpartnerproductstageApi.md#ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1) | **GET** /1/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}/getEzmaxpartnerproductstagewebhooks | Retrieve an existing Ezmaxpartnerproductstage&#39;s Ezmaxpartnerproductstagewebhooks
[**ezmaxpartnerproductstage_get_list_v1**](ObjectEzmaxpartnerproductstageApi.md#ezmaxpartnerproductstage_get_list_v1) | **GET** /1/object/ezmaxpartnerproductstage/getList | Retrieve Ezmaxpartnerproductstage list
[**ezmaxpartnerproductstage_get_object_v2**](ObjectEzmaxpartnerproductstageApi.md#ezmaxpartnerproductstage_get_object_v2) | **GET** /2/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID} | Retrieve an existing Ezmaxpartnerproductstage
[**ezmaxpartnerproductstage_subscribe_v1**](ObjectEzmaxpartnerproductstageApi.md#ezmaxpartnerproductstage_subscribe_v1) | **POST** /1/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}/subscribe | Subscribe to the Ezmaxpartnerproductstage
[**ezmaxpartnerproductstage_unsubscribe_v1**](ObjectEzmaxpartnerproductstageApi.md#ezmaxpartnerproductstage_unsubscribe_v1) | **POST** /1/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}/unsubscribe | Unsubscribe to the Ezmaxpartnerproductstage


# **ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1**
> EzmaxpartnerproductstageGetEzmaxpartnerproductstagepermissionsV1Response ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1(pki_ezmaxpartnerproductstage_id)

Retrieve an existing Ezmaxpartnerproductstage's Ezmaxpartnerproductstagepermissions

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1_response import EzmaxpartnerproductstageGetEzmaxpartnerproductstagepermissionsV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerproductstageApi(api_client)
    pki_ezmaxpartnerproductstage_id = 56 # int | 

    try:
        # Retrieve an existing Ezmaxpartnerproductstage's Ezmaxpartnerproductstagepermissions
        api_response = api_instance.ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1(pki_ezmaxpartnerproductstage_id)
        print("The response of ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_ezmaxpartnerproductstagepermissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxpartnerproductstage_id** | **int**|  | 

### Return type

[**EzmaxpartnerproductstageGetEzmaxpartnerproductstagepermissionsV1Response**](EzmaxpartnerproductstageGetEzmaxpartnerproductstagepermissionsV1Response.md)

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

# **ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1**
> EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1(pki_ezmaxpartnerproductstage_id)

Retrieve an existing Ezmaxpartnerproductstage's Ezmaxpartnerproductstagewebhooks

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response import EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerproductstageApi(api_client)
    pki_ezmaxpartnerproductstage_id = 56 # int | 

    try:
        # Retrieve an existing Ezmaxpartnerproductstage's Ezmaxpartnerproductstagewebhooks
        api_response = api_instance.ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1(pki_ezmaxpartnerproductstage_id)
        print("The response of ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxpartnerproductstage_id** | **int**|  | 

### Return type

[**EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response**](EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response.md)

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

# **ezmaxpartnerproductstage_get_list_v1**
> EzmaxpartnerproductstageGetListV1Response ezmaxpartnerproductstage_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Ezmaxpartnerproductstage list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartnerproductstage_get_list_v1_response import EzmaxpartnerproductstageGetListV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerproductstageApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Ezmaxpartnerproductstage list
        api_response = api_instance.ezmaxpartnerproductstage_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_list_v1: %s\n" % e)
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

[**EzmaxpartnerproductstageGetListV1Response**](EzmaxpartnerproductstageGetListV1Response.md)

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

# **ezmaxpartnerproductstage_get_object_v2**
> EzmaxpartnerproductstageGetObjectV2Response ezmaxpartnerproductstage_get_object_v2(pki_ezmaxpartnerproductstage_id)

Retrieve an existing Ezmaxpartnerproductstage



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartnerproductstage_get_object_v2_response import EzmaxpartnerproductstageGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerproductstageApi(api_client)
    pki_ezmaxpartnerproductstage_id = 56 # int | The unique ID of the Ezmaxpartnerproductstage

    try:
        # Retrieve an existing Ezmaxpartnerproductstage
        api_response = api_instance.ezmaxpartnerproductstage_get_object_v2(pki_ezmaxpartnerproductstage_id)
        print("The response of ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxpartnerproductstage_id** | **int**| The unique ID of the Ezmaxpartnerproductstage | 

### Return type

[**EzmaxpartnerproductstageGetObjectV2Response**](EzmaxpartnerproductstageGetObjectV2Response.md)

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

# **ezmaxpartnerproductstage_subscribe_v1**
> EzmaxpartnerproductstageSubscribeV1Response ezmaxpartnerproductstage_subscribe_v1(pki_ezmaxpartnerproductstage_id, body)

Subscribe to the Ezmaxpartnerproductstage

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartnerproductstage_subscribe_v1_response import EzmaxpartnerproductstageSubscribeV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerproductstageApi(api_client)
    pki_ezmaxpartnerproductstage_id = 56 # int | 
    body = None # object | 

    try:
        # Subscribe to the Ezmaxpartnerproductstage
        api_response = api_instance.ezmaxpartnerproductstage_subscribe_v1(pki_ezmaxpartnerproductstage_id, body)
        print("The response of ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxpartnerproductstage_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzmaxpartnerproductstageSubscribeV1Response**](EzmaxpartnerproductstageSubscribeV1Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezmaxpartnerproductstage_unsubscribe_v1**
> EzmaxpartnerproductstageUnsubscribeV1Response ezmaxpartnerproductstage_unsubscribe_v1(pki_ezmaxpartnerproductstage_id, body)

Unsubscribe to the Ezmaxpartnerproductstage

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartnerproductstage_unsubscribe_v1_response import EzmaxpartnerproductstageUnsubscribeV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerproductstageApi(api_client)
    pki_ezmaxpartnerproductstage_id = 56 # int | 
    body = None # object | 

    try:
        # Unsubscribe to the Ezmaxpartnerproductstage
        api_response = api_instance.ezmaxpartnerproductstage_unsubscribe_v1(pki_ezmaxpartnerproductstage_id, body)
        print("The response of ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_unsubscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerproductstageApi->ezmaxpartnerproductstage_unsubscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxpartnerproductstage_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzmaxpartnerproductstageUnsubscribeV1Response**](EzmaxpartnerproductstageUnsubscribeV1Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

