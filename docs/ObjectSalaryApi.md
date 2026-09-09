# eZmaxApi.ObjectSalaryApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salary_batch_download_v1**](ObjectSalaryApi.md#salary_batch_download_v1) | **POST** /1/object/salary/{pkiSalaryID}/batchDownload | Download multiples attachments from a Reconciliation
[**salary_get_attachments_v1**](ObjectSalaryApi.md#salary_get_attachments_v1) | **GET** /1/object/salary/{pkiSalaryID}/getAttachments | Retrieve Salary&#39;s attachments
[**salary_import_into_edmv1**](ObjectSalaryApi.md#salary_import_into_edmv1) | **POST** /1/object/salary/{pkiSalaryID}/importIntoEDM | Import attachments into the Salary


# **salary_batch_download_v1**
> bytes salary_batch_download_v1(pki_salary_id, salary_batch_download_v1_request)

Download multiples attachments from a Reconciliation

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.salary_batch_download_v1_request import SalaryBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectSalaryApi(api_client)
    pki_salary_id = 56 # int | 
    salary_batch_download_v1_request = eZmaxApi.SalaryBatchDownloadV1Request() # SalaryBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Reconciliation
        api_response = api_instance.salary_batch_download_v1(pki_salary_id, salary_batch_download_v1_request)
        print("The response of ObjectSalaryApi->salary_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSalaryApi->salary_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_salary_id** | **int**|  | 
 **salary_batch_download_v1_request** | [**SalaryBatchDownloadV1Request**](SalaryBatchDownloadV1Request.md)|  | 

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

# **salary_get_attachments_v1**
> SalaryGetAttachmentsV1Response salary_get_attachments_v1(pki_salary_id)

Retrieve Salary's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.salary_get_attachments_v1_response import SalaryGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectSalaryApi(api_client)
    pki_salary_id = 56 # int | 

    try:
        # Retrieve Salary's attachments
        api_response = api_instance.salary_get_attachments_v1(pki_salary_id)
        print("The response of ObjectSalaryApi->salary_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSalaryApi->salary_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_salary_id** | **int**|  | 

### Return type

[**SalaryGetAttachmentsV1Response**](SalaryGetAttachmentsV1Response.md)

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

# **salary_import_into_edmv1**
> SalaryImportIntoEDMV1Response salary_import_into_edmv1(pki_salary_id, salary_import_into_edmv1_request)

Import attachments into the Salary

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.salary_import_into_edmv1_request import SalaryImportIntoEDMV1Request
from eZmaxApi.models.salary_import_into_edmv1_response import SalaryImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectSalaryApi(api_client)
    pki_salary_id = 56 # int | 
    salary_import_into_edmv1_request = eZmaxApi.SalaryImportIntoEDMV1Request() # SalaryImportIntoEDMV1Request | 

    try:
        # Import attachments into the Salary
        api_response = api_instance.salary_import_into_edmv1(pki_salary_id, salary_import_into_edmv1_request)
        print("The response of ObjectSalaryApi->salary_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSalaryApi->salary_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_salary_id** | **int**|  | 
 **salary_import_into_edmv1_request** | [**SalaryImportIntoEDMV1Request**](SalaryImportIntoEDMV1Request.md)|  | 

### Return type

[**SalaryImportIntoEDMV1Response**](SalaryImportIntoEDMV1Response.md)

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

