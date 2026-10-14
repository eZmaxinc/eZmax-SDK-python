# eZmaxApi.ObjectPurchaseApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_batch_download_v1**](ObjectPurchaseApi.md#purchase_batch_download_v1) | **POST** /1/object/purchase/{pkiPurchaseID}/batchDownload | Download multiples attachments from a Purchase
[**purchase_get_attachments_v1**](ObjectPurchaseApi.md#purchase_get_attachments_v1) | **GET** /1/object/purchase/{pkiPurchaseID}/getAttachments | Retrieve Purchase&#39;s attachments
[**purchase_get_communication_count_v1**](ObjectPurchaseApi.md#purchase_get_communication_count_v1) | **GET** /1/object/purchase/{pkiPurchaseID}/getCommunicationCount | Retrieve Communication count
[**purchase_get_communication_list_v1**](ObjectPurchaseApi.md#purchase_get_communication_list_v1) | **GET** /1/object/purchase/{pkiPurchaseID}/getCommunicationList | Retrieve Communication list
[**purchase_get_communicationrecipients_v1**](ObjectPurchaseApi.md#purchase_get_communicationrecipients_v1) | **GET** /1/object/purchase/{pkiPurchaseID}/getCommunicationrecipients | Retrieve Communication recipients
[**purchase_get_communicationsenders_v1**](ObjectPurchaseApi.md#purchase_get_communicationsenders_v1) | **GET** /1/object/purchase/{pkiPurchaseID}/getCommunicationsenders | Retrieve Communication senders
[**purchase_get_list_v1**](ObjectPurchaseApi.md#purchase_get_list_v1) | **GET** /1/object/purchase/getList | Retrieve Purchase list
[**purchase_import_into_edmv1**](ObjectPurchaseApi.md#purchase_import_into_edmv1) | **POST** /1/object/purchase/{pkiPurchaseID}/importIntoEDM | Import attachments into the Purchase


# **purchase_batch_download_v1**
> bytes purchase_batch_download_v1(pki_purchase_id, purchase_batch_download_v1_request)

Download multiples attachments from a Purchase

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_batch_download_v1_request import PurchaseBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 
    purchase_batch_download_v1_request = eZmaxApi.PurchaseBatchDownloadV1Request() # PurchaseBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Purchase
        api_response = api_instance.purchase_batch_download_v1(pki_purchase_id, purchase_batch_download_v1_request)
        print("The response of ObjectPurchaseApi->purchase_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 
 **purchase_batch_download_v1_request** | [**PurchaseBatchDownloadV1Request**](PurchaseBatchDownloadV1Request.md)|  | 

### Return type

**bytes**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, text/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_get_attachments_v1**
> PurchaseGetAttachmentsV1Response purchase_get_attachments_v1(pki_purchase_id)

Retrieve Purchase's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_get_attachments_v1_response import PurchaseGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 

    try:
        # Retrieve Purchase's attachments
        api_response = api_instance.purchase_get_attachments_v1(pki_purchase_id)
        print("The response of ObjectPurchaseApi->purchase_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 

### Return type

[**PurchaseGetAttachmentsV1Response**](PurchaseGetAttachmentsV1Response.md)

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

# **purchase_get_communication_count_v1**
> PurchaseGetCommunicationCountV1Response purchase_get_communication_count_v1(pki_purchase_id)

Retrieve Communication count

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_get_communication_count_v1_response import PurchaseGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.purchase_get_communication_count_v1(pki_purchase_id)
        print("The response of ObjectPurchaseApi->purchase_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 

### Return type

[**PurchaseGetCommunicationCountV1Response**](PurchaseGetCommunicationCountV1Response.md)

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

# **purchase_get_communication_list_v1**
> PurchaseGetCommunicationListV1Response purchase_get_communication_list_v1(pki_purchase_id)

Retrieve Communication list

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_get_communication_list_v1_response import PurchaseGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.purchase_get_communication_list_v1(pki_purchase_id)
        print("The response of ObjectPurchaseApi->purchase_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 

### Return type

[**PurchaseGetCommunicationListV1Response**](PurchaseGetCommunicationListV1Response.md)

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

# **purchase_get_communicationrecipients_v1**
> PurchaseGetCommunicationrecipientsV1Response purchase_get_communicationrecipients_v1(pki_purchase_id)

Retrieve Communication recipients

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_get_communicationrecipients_v1_response import PurchaseGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 

    try:
        # Retrieve Communication recipients
        api_response = api_instance.purchase_get_communicationrecipients_v1(pki_purchase_id)
        print("The response of ObjectPurchaseApi->purchase_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 

### Return type

[**PurchaseGetCommunicationrecipientsV1Response**](PurchaseGetCommunicationrecipientsV1Response.md)

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

# **purchase_get_communicationsenders_v1**
> PurchaseGetCommunicationsendersV1Response purchase_get_communicationsenders_v1(pki_purchase_id)

Retrieve Communication senders

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_get_communicationsenders_v1_response import PurchaseGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 

    try:
        # Retrieve Communication senders
        api_response = api_instance.purchase_get_communicationsenders_v1(pki_purchase_id)
        print("The response of ObjectPurchaseApi->purchase_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 

### Return type

[**PurchaseGetCommunicationsendersV1Response**](PurchaseGetCommunicationsendersV1Response.md)

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

# **purchase_get_list_v1**
> PurchaseGetListV1Response purchase_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Purchase list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.purchase_get_list_v1_response import PurchaseGetListV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Purchase list
        api_response = api_instance.purchase_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectPurchaseApi->purchase_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_get_list_v1: %s\n" % e)
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

[**PurchaseGetListV1Response**](PurchaseGetListV1Response.md)

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

# **purchase_import_into_edmv1**
> PurchaseImportIntoEDMV1Response purchase_import_into_edmv1(pki_purchase_id, purchase_import_into_edmv1_request)

Import attachments into the Purchase

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.purchase_import_into_edmv1_request import PurchaseImportIntoEDMV1Request
from eZmaxApi.models.purchase_import_into_edmv1_response import PurchaseImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectPurchaseApi(api_client)
    pki_purchase_id = 56 # int | 
    purchase_import_into_edmv1_request = eZmaxApi.PurchaseImportIntoEDMV1Request() # PurchaseImportIntoEDMV1Request | 

    try:
        # Import attachments into the Purchase
        api_response = api_instance.purchase_import_into_edmv1(pki_purchase_id, purchase_import_into_edmv1_request)
        print("The response of ObjectPurchaseApi->purchase_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPurchaseApi->purchase_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_purchase_id** | **int**|  | 
 **purchase_import_into_edmv1_request** | [**PurchaseImportIntoEDMV1Request**](PurchaseImportIntoEDMV1Request.md)|  | 

### Return type

[**PurchaseImportIntoEDMV1Response**](PurchaseImportIntoEDMV1Response.md)

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

