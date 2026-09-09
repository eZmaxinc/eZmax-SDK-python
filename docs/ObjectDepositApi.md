# eZmaxApi.ObjectDepositApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposit_batch_download_v1**](ObjectDepositApi.md#deposit_batch_download_v1) | **POST** /1/object/deposit/{pkiDepositID}/batchDownload | Download multiples attachments from a Deposit
[**deposit_get_attachments_v1**](ObjectDepositApi.md#deposit_get_attachments_v1) | **GET** /1/object/deposit/{pkiDepositID}/getAttachments | Retrieve Deposit&#39;s attachments
[**deposit_import_into_edmv1**](ObjectDepositApi.md#deposit_import_into_edmv1) | **POST** /1/object/deposit/{pkiDepositID}/importIntoEDM | Import attachments into the Deposit


# **deposit_batch_download_v1**
> bytes deposit_batch_download_v1(pki_deposit_id, deposit_batch_download_v1_request)

Download multiples attachments from a Deposit

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.deposit_batch_download_v1_request import DepositBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectDepositApi(api_client)
    pki_deposit_id = 56 # int | 
    deposit_batch_download_v1_request = eZmaxApi.DepositBatchDownloadV1Request() # DepositBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Deposit
        api_response = api_instance.deposit_batch_download_v1(pki_deposit_id, deposit_batch_download_v1_request)
        print("The response of ObjectDepositApi->deposit_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDepositApi->deposit_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_deposit_id** | **int**|  | 
 **deposit_batch_download_v1_request** | [**DepositBatchDownloadV1Request**](DepositBatchDownloadV1Request.md)|  | 

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

# **deposit_get_attachments_v1**
> DepositGetAttachmentsV1Response deposit_get_attachments_v1(pki_deposit_id)

Retrieve Deposit's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.deposit_get_attachments_v1_response import DepositGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectDepositApi(api_client)
    pki_deposit_id = 56 # int | 

    try:
        # Retrieve Deposit's attachments
        api_response = api_instance.deposit_get_attachments_v1(pki_deposit_id)
        print("The response of ObjectDepositApi->deposit_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDepositApi->deposit_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_deposit_id** | **int**|  | 

### Return type

[**DepositGetAttachmentsV1Response**](DepositGetAttachmentsV1Response.md)

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

# **deposit_import_into_edmv1**
> DepositImportIntoEDMV1Response deposit_import_into_edmv1(pki_deposit_id, deposit_import_into_edmv1_request)

Import attachments into the Deposit

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.deposit_import_into_edmv1_request import DepositImportIntoEDMV1Request
from eZmaxApi.models.deposit_import_into_edmv1_response import DepositImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectDepositApi(api_client)
    pki_deposit_id = 56 # int | 
    deposit_import_into_edmv1_request = eZmaxApi.DepositImportIntoEDMV1Request() # DepositImportIntoEDMV1Request | 

    try:
        # Import attachments into the Deposit
        api_response = api_instance.deposit_import_into_edmv1(pki_deposit_id, deposit_import_into_edmv1_request)
        print("The response of ObjectDepositApi->deposit_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDepositApi->deposit_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_deposit_id** | **int**|  | 
 **deposit_import_into_edmv1_request** | [**DepositImportIntoEDMV1Request**](DepositImportIntoEDMV1Request.md)|  | 

### Return type

[**DepositImportIntoEDMV1Response**](DepositImportIntoEDMV1Response.md)

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

