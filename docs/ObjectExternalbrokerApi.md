# eZmaxApi.ObjectExternalbrokerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**externalbroker_batch_download_v1**](ObjectExternalbrokerApi.md#externalbroker_batch_download_v1) | **POST** /1/object/externalbroker/{pkiExternalbrokerID}/batchDownload | Download multiples attachments from an Externalbroker
[**externalbroker_get_attachments_v1**](ObjectExternalbrokerApi.md#externalbroker_get_attachments_v1) | **GET** /1/object/externalbroker/{pkiExternalbrokerID}/getAttachments | Retrieve Externalbroker&#39;s attachments
[**externalbroker_import_into_edmv1**](ObjectExternalbrokerApi.md#externalbroker_import_into_edmv1) | **POST** /1/object/externalbroker/{pkiExternalbrokerID}/importIntoEDM | Import attachments into the Externalbroker


# **externalbroker_batch_download_v1**
> bytes externalbroker_batch_download_v1(pki_externalbroker_id, externalbroker_batch_download_v1_request)

Download multiples attachments from an Externalbroker

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.externalbroker_batch_download_v1_request import ExternalbrokerBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectExternalbrokerApi(api_client)
    pki_externalbroker_id = 56 # int | 
    externalbroker_batch_download_v1_request = eZmaxApi.ExternalbrokerBatchDownloadV1Request() # ExternalbrokerBatchDownloadV1Request | 

    try:
        # Download multiples attachments from an Externalbroker
        api_response = api_instance.externalbroker_batch_download_v1(pki_externalbroker_id, externalbroker_batch_download_v1_request)
        print("The response of ObjectExternalbrokerApi->externalbroker_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectExternalbrokerApi->externalbroker_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_externalbroker_id** | **int**|  | 
 **externalbroker_batch_download_v1_request** | [**ExternalbrokerBatchDownloadV1Request**](ExternalbrokerBatchDownloadV1Request.md)|  | 

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

# **externalbroker_get_attachments_v1**
> ExternalbrokerGetAttachmentsV1Response externalbroker_get_attachments_v1(pki_externalbroker_id)

Retrieve Externalbroker's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.externalbroker_get_attachments_v1_response import ExternalbrokerGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectExternalbrokerApi(api_client)
    pki_externalbroker_id = 56 # int | 

    try:
        # Retrieve Externalbroker's attachments
        api_response = api_instance.externalbroker_get_attachments_v1(pki_externalbroker_id)
        print("The response of ObjectExternalbrokerApi->externalbroker_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectExternalbrokerApi->externalbroker_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_externalbroker_id** | **int**|  | 

### Return type

[**ExternalbrokerGetAttachmentsV1Response**](ExternalbrokerGetAttachmentsV1Response.md)

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

# **externalbroker_import_into_edmv1**
> ExternalbrokerImportIntoEDMV1Response externalbroker_import_into_edmv1(pki_externalbroker_id, externalbroker_import_into_edmv1_request)

Import attachments into the Externalbroker



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.externalbroker_import_into_edmv1_request import ExternalbrokerImportIntoEDMV1Request
from eZmaxApi.models.externalbroker_import_into_edmv1_response import ExternalbrokerImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectExternalbrokerApi(api_client)
    pki_externalbroker_id = 56 # int | 
    externalbroker_import_into_edmv1_request = eZmaxApi.ExternalbrokerImportIntoEDMV1Request() # ExternalbrokerImportIntoEDMV1Request | 

    try:
        # Import attachments into the Externalbroker
        api_response = api_instance.externalbroker_import_into_edmv1(pki_externalbroker_id, externalbroker_import_into_edmv1_request)
        print("The response of ObjectExternalbrokerApi->externalbroker_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectExternalbrokerApi->externalbroker_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_externalbroker_id** | **int**|  | 
 **externalbroker_import_into_edmv1_request** | [**ExternalbrokerImportIntoEDMV1Request**](ExternalbrokerImportIntoEDMV1Request.md)|  | 

### Return type

[**ExternalbrokerImportIntoEDMV1Response**](ExternalbrokerImportIntoEDMV1Response.md)

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

