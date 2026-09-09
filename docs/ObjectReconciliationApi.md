# eZmaxApi.ObjectReconciliationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reconciliation_batch_download_v1**](ObjectReconciliationApi.md#reconciliation_batch_download_v1) | **POST** /1/object/reconciliation/{pkiReconciliationID}/batchDownload | Download multiples attachments from a Reconciliation
[**reconciliation_get_attachments_v1**](ObjectReconciliationApi.md#reconciliation_get_attachments_v1) | **GET** /1/object/reconciliation/{pkiReconciliationID}/getAttachments | Retrieve Reconciliation&#39;s attachments
[**reconciliation_import_into_edmv1**](ObjectReconciliationApi.md#reconciliation_import_into_edmv1) | **POST** /1/object/reconciliation/{pkiReconciliationID}/importIntoEDM | Import attachments into the Reconciliation


# **reconciliation_batch_download_v1**
> bytes reconciliation_batch_download_v1(pki_reconciliation_id, reconciliation_batch_download_v1_request)

Download multiples attachments from a Reconciliation

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.reconciliation_batch_download_v1_request import ReconciliationBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectReconciliationApi(api_client)
    pki_reconciliation_id = 56 # int | 
    reconciliation_batch_download_v1_request = eZmaxApi.ReconciliationBatchDownloadV1Request() # ReconciliationBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Reconciliation
        api_response = api_instance.reconciliation_batch_download_v1(pki_reconciliation_id, reconciliation_batch_download_v1_request)
        print("The response of ObjectReconciliationApi->reconciliation_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectReconciliationApi->reconciliation_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_reconciliation_id** | **int**|  | 
 **reconciliation_batch_download_v1_request** | [**ReconciliationBatchDownloadV1Request**](ReconciliationBatchDownloadV1Request.md)|  | 

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

# **reconciliation_get_attachments_v1**
> ReconciliationGetAttachmentsV1Response reconciliation_get_attachments_v1(pki_reconciliation_id)

Retrieve Reconciliation's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.reconciliation_get_attachments_v1_response import ReconciliationGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectReconciliationApi(api_client)
    pki_reconciliation_id = 56 # int | 

    try:
        # Retrieve Reconciliation's attachments
        api_response = api_instance.reconciliation_get_attachments_v1(pki_reconciliation_id)
        print("The response of ObjectReconciliationApi->reconciliation_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectReconciliationApi->reconciliation_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_reconciliation_id** | **int**|  | 

### Return type

[**ReconciliationGetAttachmentsV1Response**](ReconciliationGetAttachmentsV1Response.md)

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

# **reconciliation_import_into_edmv1**
> ReconciliationImportIntoEDMV1Response reconciliation_import_into_edmv1(pki_reconciliation_id, reconciliation_import_into_edmv1_request)

Import attachments into the Reconciliation

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.reconciliation_import_into_edmv1_request import ReconciliationImportIntoEDMV1Request
from eZmaxApi.models.reconciliation_import_into_edmv1_response import ReconciliationImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectReconciliationApi(api_client)
    pki_reconciliation_id = 56 # int | 
    reconciliation_import_into_edmv1_request = eZmaxApi.ReconciliationImportIntoEDMV1Request() # ReconciliationImportIntoEDMV1Request | 

    try:
        # Import attachments into the Reconciliation
        api_response = api_instance.reconciliation_import_into_edmv1(pki_reconciliation_id, reconciliation_import_into_edmv1_request)
        print("The response of ObjectReconciliationApi->reconciliation_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectReconciliationApi->reconciliation_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_reconciliation_id** | **int**|  | 
 **reconciliation_import_into_edmv1_request** | [**ReconciliationImportIntoEDMV1Request**](ReconciliationImportIntoEDMV1Request.md)|  | 

### Return type

[**ReconciliationImportIntoEDMV1Response**](ReconciliationImportIntoEDMV1Response.md)

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

