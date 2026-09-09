# eZmaxApi.ObjectOfficetaxreportApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**officetaxreport_batch_download_v1**](ObjectOfficetaxreportApi.md#officetaxreport_batch_download_v1) | **POST** /1/object/officetaxreport/{pkiOfficetaxreportID}/batchDownload | Download multiples attachments from an Officetaxreport
[**officetaxreport_get_attachments_v1**](ObjectOfficetaxreportApi.md#officetaxreport_get_attachments_v1) | **GET** /1/object/officetaxreport/{pkiOfficetaxreportID}/getAttachments | Retrieve Officetaxreport&#39;s attachments
[**officetaxreport_import_into_edmv1**](ObjectOfficetaxreportApi.md#officetaxreport_import_into_edmv1) | **POST** /1/object/officetaxreport/{pkiOfficetaxreportID}/importIntoEDM | Import attachments into the Officetaxreport


# **officetaxreport_batch_download_v1**
> bytes officetaxreport_batch_download_v1(pki_officetaxreport_id, officetaxreport_batch_download_v1_request)

Download multiples attachments from an Officetaxreport

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.officetaxreport_batch_download_v1_request import OfficetaxreportBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectOfficetaxreportApi(api_client)
    pki_officetaxreport_id = 56 # int | 
    officetaxreport_batch_download_v1_request = eZmaxApi.OfficetaxreportBatchDownloadV1Request() # OfficetaxreportBatchDownloadV1Request | 

    try:
        # Download multiples attachments from an Officetaxreport
        api_response = api_instance.officetaxreport_batch_download_v1(pki_officetaxreport_id, officetaxreport_batch_download_v1_request)
        print("The response of ObjectOfficetaxreportApi->officetaxreport_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectOfficetaxreportApi->officetaxreport_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_officetaxreport_id** | **int**|  | 
 **officetaxreport_batch_download_v1_request** | [**OfficetaxreportBatchDownloadV1Request**](OfficetaxreportBatchDownloadV1Request.md)|  | 

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

# **officetaxreport_get_attachments_v1**
> OfficetaxreportGetAttachmentsV1Response officetaxreport_get_attachments_v1(pki_officetaxreport_id)

Retrieve Officetaxreport's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.officetaxreport_get_attachments_v1_response import OfficetaxreportGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectOfficetaxreportApi(api_client)
    pki_officetaxreport_id = 56 # int | 

    try:
        # Retrieve Officetaxreport's attachments
        api_response = api_instance.officetaxreport_get_attachments_v1(pki_officetaxreport_id)
        print("The response of ObjectOfficetaxreportApi->officetaxreport_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectOfficetaxreportApi->officetaxreport_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_officetaxreport_id** | **int**|  | 

### Return type

[**OfficetaxreportGetAttachmentsV1Response**](OfficetaxreportGetAttachmentsV1Response.md)

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

# **officetaxreport_import_into_edmv1**
> OfficetaxreportImportIntoEDMV1Response officetaxreport_import_into_edmv1(pki_officetaxreport_id, officetaxreport_import_into_edmv1_request)

Import attachments into the Officetaxreport

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.officetaxreport_import_into_edmv1_request import OfficetaxreportImportIntoEDMV1Request
from eZmaxApi.models.officetaxreport_import_into_edmv1_response import OfficetaxreportImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectOfficetaxreportApi(api_client)
    pki_officetaxreport_id = 56 # int | 
    officetaxreport_import_into_edmv1_request = eZmaxApi.OfficetaxreportImportIntoEDMV1Request() # OfficetaxreportImportIntoEDMV1Request | 

    try:
        # Import attachments into the Officetaxreport
        api_response = api_instance.officetaxreport_import_into_edmv1(pki_officetaxreport_id, officetaxreport_import_into_edmv1_request)
        print("The response of ObjectOfficetaxreportApi->officetaxreport_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectOfficetaxreportApi->officetaxreport_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_officetaxreport_id** | **int**|  | 
 **officetaxreport_import_into_edmv1_request** | [**OfficetaxreportImportIntoEDMV1Request**](OfficetaxreportImportIntoEDMV1Request.md)|  | 

### Return type

[**OfficetaxreportImportIntoEDMV1Response**](OfficetaxreportImportIntoEDMV1Response.md)

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

