# eZmaxApi.ObjectDeposittransitchequeApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposittransitcheque_batch_download_v1**](ObjectDeposittransitchequeApi.md#deposittransitcheque_batch_download_v1) | **POST** /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/batchDownload | Download multiples attachments from a Deposittransitcheque
[**deposittransitcheque_get_attachments_v1**](ObjectDeposittransitchequeApi.md#deposittransitcheque_get_attachments_v1) | **GET** /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/getAttachments | Retrieve Deposittransitcheque&#39;s attachments
[**deposittransitcheque_import_into_edmv1**](ObjectDeposittransitchequeApi.md#deposittransitcheque_import_into_edmv1) | **POST** /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/importIntoEDM | Import attachments into the Deposittransitcheque


# **deposittransitcheque_batch_download_v1**
> bytes deposittransitcheque_batch_download_v1(pki_deposittransitcheque_id, deposittransitcheque_batch_download_v1_request)

Download multiples attachments from a Deposittransitcheque

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.deposittransitcheque_batch_download_v1_request import DeposittransitchequeBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectDeposittransitchequeApi(api_client)
    pki_deposittransitcheque_id = 56 # int | 
    deposittransitcheque_batch_download_v1_request = eZmaxApi.DeposittransitchequeBatchDownloadV1Request() # DeposittransitchequeBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Deposittransitcheque
        api_response = api_instance.deposittransitcheque_batch_download_v1(pki_deposittransitcheque_id, deposittransitcheque_batch_download_v1_request)
        print("The response of ObjectDeposittransitchequeApi->deposittransitcheque_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDeposittransitchequeApi->deposittransitcheque_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_deposittransitcheque_id** | **int**|  | 
 **deposittransitcheque_batch_download_v1_request** | [**DeposittransitchequeBatchDownloadV1Request**](DeposittransitchequeBatchDownloadV1Request.md)|  | 

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

# **deposittransitcheque_get_attachments_v1**
> DeposittransitchequeGetAttachmentsV1Response deposittransitcheque_get_attachments_v1(pki_deposittransitcheque_id)

Retrieve Deposittransitcheque's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.deposittransitcheque_get_attachments_v1_response import DeposittransitchequeGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectDeposittransitchequeApi(api_client)
    pki_deposittransitcheque_id = 56 # int | 

    try:
        # Retrieve Deposittransitcheque's attachments
        api_response = api_instance.deposittransitcheque_get_attachments_v1(pki_deposittransitcheque_id)
        print("The response of ObjectDeposittransitchequeApi->deposittransitcheque_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDeposittransitchequeApi->deposittransitcheque_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_deposittransitcheque_id** | **int**|  | 

### Return type

[**DeposittransitchequeGetAttachmentsV1Response**](DeposittransitchequeGetAttachmentsV1Response.md)

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

# **deposittransitcheque_import_into_edmv1**
> DeposittransitchequeImportIntoEDMV1Response deposittransitcheque_import_into_edmv1(pki_deposittransitcheque_id, deposittransitcheque_import_into_edmv1_request)

Import attachments into the Deposittransitcheque

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.deposittransitcheque_import_into_edmv1_request import DeposittransitchequeImportIntoEDMV1Request
from eZmaxApi.models.deposittransitcheque_import_into_edmv1_response import DeposittransitchequeImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectDeposittransitchequeApi(api_client)
    pki_deposittransitcheque_id = 56 # int | 
    deposittransitcheque_import_into_edmv1_request = eZmaxApi.DeposittransitchequeImportIntoEDMV1Request() # DeposittransitchequeImportIntoEDMV1Request | 

    try:
        # Import attachments into the Deposittransitcheque
        api_response = api_instance.deposittransitcheque_import_into_edmv1(pki_deposittransitcheque_id, deposittransitcheque_import_into_edmv1_request)
        print("The response of ObjectDeposittransitchequeApi->deposittransitcheque_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDeposittransitchequeApi->deposittransitcheque_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_deposittransitcheque_id** | **int**|  | 
 **deposittransitcheque_import_into_edmv1_request** | [**DeposittransitchequeImportIntoEDMV1Request**](DeposittransitchequeImportIntoEDMV1Request.md)|  | 

### Return type

[**DeposittransitchequeImportIntoEDMV1Response**](DeposittransitchequeImportIntoEDMV1Response.md)

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

