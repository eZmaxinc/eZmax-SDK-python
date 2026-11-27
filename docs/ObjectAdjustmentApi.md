# eZmaxApi.ObjectAdjustmentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjustment_batch_download_v1**](ObjectAdjustmentApi.md#adjustment_batch_download_v1) | **POST** /1/object/adjustment/{pkiAdjustmentID}/batchDownload | Download multiples attachments from an Adjustment
[**adjustment_get_attachments_v1**](ObjectAdjustmentApi.md#adjustment_get_attachments_v1) | **GET** /1/object/adjustment/{pkiAdjustmentID}/getAttachments | Retrieve Adjustment&#39;s attachments
[**adjustment_get_communication_count_v1**](ObjectAdjustmentApi.md#adjustment_get_communication_count_v1) | **GET** /1/object/adjustment/{pkiAdjustmentID}/getCommunicationCount | Retrieve Communication count
[**adjustment_get_communication_list_v1**](ObjectAdjustmentApi.md#adjustment_get_communication_list_v1) | **GET** /1/object/adjustment/{pkiAdjustmentID}/getCommunicationList | Retrieve Communication list
[**adjustment_get_communicationrecipients_v1**](ObjectAdjustmentApi.md#adjustment_get_communicationrecipients_v1) | **GET** /1/object/adjustment/{pkiAdjustmentID}/getCommunicationrecipients | Retrieve Communication recipients
[**adjustment_get_communicationsenders_v1**](ObjectAdjustmentApi.md#adjustment_get_communicationsenders_v1) | **GET** /1/object/adjustment/{pkiAdjustmentID}/getCommunicationsenders | Retrieve Communication senders
[**adjustment_get_list_v1**](ObjectAdjustmentApi.md#adjustment_get_list_v1) | **GET** /1/object/adjustment/getList | Retrieve Adjustment list
[**adjustment_import_into_edmv1**](ObjectAdjustmentApi.md#adjustment_import_into_edmv1) | **POST** /1/object/adjustment/{pkiAdjustmentID}/importIntoEDM | Import attachments into the Adjustment


# **adjustment_batch_download_v1**
> bytes adjustment_batch_download_v1(pki_adjustment_id, adjustment_batch_download_v1_request)

Download multiples attachments from an Adjustment

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_batch_download_v1_request import AdjustmentBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 
    adjustment_batch_download_v1_request = eZmaxApi.AdjustmentBatchDownloadV1Request() # AdjustmentBatchDownloadV1Request | 

    try:
        # Download multiples attachments from an Adjustment
        api_response = api_instance.adjustment_batch_download_v1(pki_adjustment_id, adjustment_batch_download_v1_request)
        print("The response of ObjectAdjustmentApi->adjustment_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 
 **adjustment_batch_download_v1_request** | [**AdjustmentBatchDownloadV1Request**](AdjustmentBatchDownloadV1Request.md)|  | 

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

# **adjustment_get_attachments_v1**
> AdjustmentGetAttachmentsV1Response adjustment_get_attachments_v1(pki_adjustment_id)

Retrieve Adjustment's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_get_attachments_v1_response import AdjustmentGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 

    try:
        # Retrieve Adjustment's attachments
        api_response = api_instance.adjustment_get_attachments_v1(pki_adjustment_id)
        print("The response of ObjectAdjustmentApi->adjustment_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 

### Return type

[**AdjustmentGetAttachmentsV1Response**](AdjustmentGetAttachmentsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjustment_get_communication_count_v1**
> AdjustmentGetCommunicationCountV1Response adjustment_get_communication_count_v1(pki_adjustment_id)

Retrieve Communication count

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_get_communication_count_v1_response import AdjustmentGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.adjustment_get_communication_count_v1(pki_adjustment_id)
        print("The response of ObjectAdjustmentApi->adjustment_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 

### Return type

[**AdjustmentGetCommunicationCountV1Response**](AdjustmentGetCommunicationCountV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjustment_get_communication_list_v1**
> AdjustmentGetCommunicationListV1Response adjustment_get_communication_list_v1(pki_adjustment_id)

Retrieve Communication list

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_get_communication_list_v1_response import AdjustmentGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.adjustment_get_communication_list_v1(pki_adjustment_id)
        print("The response of ObjectAdjustmentApi->adjustment_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 

### Return type

[**AdjustmentGetCommunicationListV1Response**](AdjustmentGetCommunicationListV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjustment_get_communicationrecipients_v1**
> AdjustmentGetCommunicationrecipientsV1Response adjustment_get_communicationrecipients_v1(pki_adjustment_id)

Retrieve Communication recipients

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_get_communicationrecipients_v1_response import AdjustmentGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 

    try:
        # Retrieve Communication recipients
        api_response = api_instance.adjustment_get_communicationrecipients_v1(pki_adjustment_id)
        print("The response of ObjectAdjustmentApi->adjustment_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 

### Return type

[**AdjustmentGetCommunicationrecipientsV1Response**](AdjustmentGetCommunicationrecipientsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjustment_get_communicationsenders_v1**
> AdjustmentGetCommunicationsendersV1Response adjustment_get_communicationsenders_v1(pki_adjustment_id)

Retrieve Communication senders

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_get_communicationsenders_v1_response import AdjustmentGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 

    try:
        # Retrieve Communication senders
        api_response = api_instance.adjustment_get_communicationsenders_v1(pki_adjustment_id)
        print("The response of ObjectAdjustmentApi->adjustment_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 

### Return type

[**AdjustmentGetCommunicationsendersV1Response**](AdjustmentGetCommunicationsendersV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjustment_get_list_v1**
> AdjustmentGetListV1Response adjustment_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Adjustment list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_get_list_v1_response import AdjustmentGetListV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Adjustment list
        api_response = api_instance.adjustment_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectAdjustmentApi->adjustment_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_get_list_v1: %s\n" % e)
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

[**AdjustmentGetListV1Response**](AdjustmentGetListV1Response.md)

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

# **adjustment_import_into_edmv1**
> AdjustmentImportIntoEDMV1Response adjustment_import_into_edmv1(pki_adjustment_id, adjustment_import_into_edmv1_request)

Import attachments into the Adjustment

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.adjustment_import_into_edmv1_request import AdjustmentImportIntoEDMV1Request
from eZmaxApi.models.adjustment_import_into_edmv1_response import AdjustmentImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectAdjustmentApi(api_client)
    pki_adjustment_id = 56 # int | 
    adjustment_import_into_edmv1_request = eZmaxApi.AdjustmentImportIntoEDMV1Request() # AdjustmentImportIntoEDMV1Request | 

    try:
        # Import attachments into the Adjustment
        api_response = api_instance.adjustment_import_into_edmv1(pki_adjustment_id, adjustment_import_into_edmv1_request)
        print("The response of ObjectAdjustmentApi->adjustment_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAdjustmentApi->adjustment_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_adjustment_id** | **int**|  | 
 **adjustment_import_into_edmv1_request** | [**AdjustmentImportIntoEDMV1Request**](AdjustmentImportIntoEDMV1Request.md)|  | 

### Return type

[**AdjustmentImportIntoEDMV1Response**](AdjustmentImportIntoEDMV1Response.md)

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

