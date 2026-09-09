# eZmaxApi.ObjectElectronicfundstransferApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**electronicfundstransfer_batch_download_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_batch_download_v1) | **POST** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/batchDownload | Download multiples attachments from an Electronicfundstransfer
[**electronicfundstransfer_get_attachments_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_attachments_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getAttachments | Retrieve Electronicfundstransfer&#39;s attachments
[**electronicfundstransfer_get_communication_count_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communication_count_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationCount | Retrieve Communication count
[**electronicfundstransfer_get_communication_list_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communication_list_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationList | Retrieve Communication list
[**electronicfundstransfer_get_communicationrecipients_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communicationrecipients_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationrecipients | Retrieve Electronicfundstransfer&#39;s Communicationrecipient
[**electronicfundstransfer_get_communicationsenders_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communicationsenders_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationsenders | Retrieve Electronicfundstransfer&#39;s Communicationsender
[**electronicfundstransfer_import_into_edmv1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_import_into_edmv1) | **POST** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/importIntoEDM | Import attachments into the Electronicfundstransfer


# **electronicfundstransfer_batch_download_v1**
> bytes electronicfundstransfer_batch_download_v1(pki_electronicfundstransfer_id, electronicfundstransfer_batch_download_v1_request)

Download multiples attachments from an Electronicfundstransfer

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_batch_download_v1_request import ElectronicfundstransferBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 
    electronicfundstransfer_batch_download_v1_request = eZmaxApi.ElectronicfundstransferBatchDownloadV1Request() # ElectronicfundstransferBatchDownloadV1Request | 

    try:
        # Download multiples attachments from an Electronicfundstransfer
        api_response = api_instance.electronicfundstransfer_batch_download_v1(pki_electronicfundstransfer_id, electronicfundstransfer_batch_download_v1_request)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 
 **electronicfundstransfer_batch_download_v1_request** | [**ElectronicfundstransferBatchDownloadV1Request**](ElectronicfundstransferBatchDownloadV1Request.md)|  | 

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

# **electronicfundstransfer_get_attachments_v1**
> ElectronicfundstransferGetAttachmentsV1Response electronicfundstransfer_get_attachments_v1(pki_electronicfundstransfer_id)

Retrieve Electronicfundstransfer's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_get_attachments_v1_response import ElectronicfundstransferGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 

    try:
        # Retrieve Electronicfundstransfer's attachments
        api_response = api_instance.electronicfundstransfer_get_attachments_v1(pki_electronicfundstransfer_id)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 

### Return type

[**ElectronicfundstransferGetAttachmentsV1Response**](ElectronicfundstransferGetAttachmentsV1Response.md)

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

# **electronicfundstransfer_get_communication_count_v1**
> ElectronicfundstransferGetCommunicationCountV1Response electronicfundstransfer_get_communication_count_v1(pki_electronicfundstransfer_id)

Retrieve Communication count



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_get_communication_count_v1_response import ElectronicfundstransferGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.electronicfundstransfer_get_communication_count_v1(pki_electronicfundstransfer_id)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 

### Return type

[**ElectronicfundstransferGetCommunicationCountV1Response**](ElectronicfundstransferGetCommunicationCountV1Response.md)

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

# **electronicfundstransfer_get_communication_list_v1**
> ElectronicfundstransferGetCommunicationListV1Response electronicfundstransfer_get_communication_list_v1(pki_electronicfundstransfer_id)

Retrieve Communication list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_get_communication_list_v1_response import ElectronicfundstransferGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.electronicfundstransfer_get_communication_list_v1(pki_electronicfundstransfer_id)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 

### Return type

[**ElectronicfundstransferGetCommunicationListV1Response**](ElectronicfundstransferGetCommunicationListV1Response.md)

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

# **electronicfundstransfer_get_communicationrecipients_v1**
> ElectronicfundstransferGetCommunicationrecipientsV1Response electronicfundstransfer_get_communicationrecipients_v1(pki_electronicfundstransfer_id)

Retrieve Electronicfundstransfer's Communicationrecipient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_get_communicationrecipients_v1_response import ElectronicfundstransferGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 

    try:
        # Retrieve Electronicfundstransfer's Communicationrecipient
        api_response = api_instance.electronicfundstransfer_get_communicationrecipients_v1(pki_electronicfundstransfer_id)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 

### Return type

[**ElectronicfundstransferGetCommunicationrecipientsV1Response**](ElectronicfundstransferGetCommunicationrecipientsV1Response.md)

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

# **electronicfundstransfer_get_communicationsenders_v1**
> ElectronicfundstransferGetCommunicationsendersV1Response electronicfundstransfer_get_communicationsenders_v1(pki_electronicfundstransfer_id)

Retrieve Electronicfundstransfer's Communicationsender



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_get_communicationsenders_v1_response import ElectronicfundstransferGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 

    try:
        # Retrieve Electronicfundstransfer's Communicationsender
        api_response = api_instance.electronicfundstransfer_get_communicationsenders_v1(pki_electronicfundstransfer_id)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 

### Return type

[**ElectronicfundstransferGetCommunicationsendersV1Response**](ElectronicfundstransferGetCommunicationsendersV1Response.md)

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

# **electronicfundstransfer_import_into_edmv1**
> ElectronicfundstransferImportIntoEDMV1Response electronicfundstransfer_import_into_edmv1(pki_electronicfundstransfer_id, electronicfundstransfer_import_into_edmv1_request)

Import attachments into the Electronicfundstransfer



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.electronicfundstransfer_import_into_edmv1_request import ElectronicfundstransferImportIntoEDMV1Request
from eZmaxApi.models.electronicfundstransfer_import_into_edmv1_response import ElectronicfundstransferImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectElectronicfundstransferApi(api_client)
    pki_electronicfundstransfer_id = 56 # int | 
    electronicfundstransfer_import_into_edmv1_request = eZmaxApi.ElectronicfundstransferImportIntoEDMV1Request() # ElectronicfundstransferImportIntoEDMV1Request | 

    try:
        # Import attachments into the Electronicfundstransfer
        api_response = api_instance.electronicfundstransfer_import_into_edmv1(pki_electronicfundstransfer_id, electronicfundstransfer_import_into_edmv1_request)
        print("The response of ObjectElectronicfundstransferApi->electronicfundstransfer_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectElectronicfundstransferApi->electronicfundstransfer_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_electronicfundstransfer_id** | **int**|  | 
 **electronicfundstransfer_import_into_edmv1_request** | [**ElectronicfundstransferImportIntoEDMV1Request**](ElectronicfundstransferImportIntoEDMV1Request.md)|  | 

### Return type

[**ElectronicfundstransferImportIntoEDMV1Response**](ElectronicfundstransferImportIntoEDMV1Response.md)

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

