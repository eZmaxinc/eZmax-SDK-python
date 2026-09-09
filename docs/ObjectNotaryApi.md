# eZmaxApi.ObjectNotaryApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notary_batch_download_v1**](ObjectNotaryApi.md#notary_batch_download_v1) | **POST** /1/object/notary/{pkiNotaryID}/batchDownload | Download multiples attachments from a Notary
[**notary_get_attachments_v1**](ObjectNotaryApi.md#notary_get_attachments_v1) | **GET** /1/object/notary/{pkiNotaryID}/getAttachments | Retrieve Notary&#39;s attachments
[**notary_import_into_edmv1**](ObjectNotaryApi.md#notary_import_into_edmv1) | **POST** /1/object/notary/{pkiNotaryID}/importIntoEDM | Import attachments into the Notary


# **notary_batch_download_v1**
> bytes notary_batch_download_v1(pki_notary_id, notary_batch_download_v1_request)

Download multiples attachments from a Notary

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.notary_batch_download_v1_request import NotaryBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectNotaryApi(api_client)
    pki_notary_id = 56 # int | 
    notary_batch_download_v1_request = eZmaxApi.NotaryBatchDownloadV1Request() # NotaryBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Notary
        api_response = api_instance.notary_batch_download_v1(pki_notary_id, notary_batch_download_v1_request)
        print("The response of ObjectNotaryApi->notary_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectNotaryApi->notary_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_notary_id** | **int**|  | 
 **notary_batch_download_v1_request** | [**NotaryBatchDownloadV1Request**](NotaryBatchDownloadV1Request.md)|  | 

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

# **notary_get_attachments_v1**
> NotaryGetAttachmentsV1Response notary_get_attachments_v1(pki_notary_id)

Retrieve Notary's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.notary_get_attachments_v1_response import NotaryGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectNotaryApi(api_client)
    pki_notary_id = 56 # int | 

    try:
        # Retrieve Notary's attachments
        api_response = api_instance.notary_get_attachments_v1(pki_notary_id)
        print("The response of ObjectNotaryApi->notary_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectNotaryApi->notary_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_notary_id** | **int**|  | 

### Return type

[**NotaryGetAttachmentsV1Response**](NotaryGetAttachmentsV1Response.md)

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

# **notary_import_into_edmv1**
> NotaryImportIntoEDMV1Response notary_import_into_edmv1(pki_notary_id, notary_import_into_edmv1_request)

Import attachments into the Notary

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.notary_import_into_edmv1_request import NotaryImportIntoEDMV1Request
from eZmaxApi.models.notary_import_into_edmv1_response import NotaryImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectNotaryApi(api_client)
    pki_notary_id = 56 # int | 
    notary_import_into_edmv1_request = eZmaxApi.NotaryImportIntoEDMV1Request() # NotaryImportIntoEDMV1Request | 

    try:
        # Import attachments into the Notary
        api_response = api_instance.notary_import_into_edmv1(pki_notary_id, notary_import_into_edmv1_request)
        print("The response of ObjectNotaryApi->notary_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectNotaryApi->notary_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_notary_id** | **int**|  | 
 **notary_import_into_edmv1_request** | [**NotaryImportIntoEDMV1Request**](NotaryImportIntoEDMV1Request.md)|  | 

### Return type

[**NotaryImportIntoEDMV1Response**](NotaryImportIntoEDMV1Response.md)

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

