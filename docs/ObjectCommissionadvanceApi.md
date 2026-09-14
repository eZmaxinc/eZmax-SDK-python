# eZmaxApi.ObjectCommissionadvanceApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commissionadvance_batch_download_v1**](ObjectCommissionadvanceApi.md#commissionadvance_batch_download_v1) | **POST** /1/object/commissionadvance/{pkiCommissionadvanceID}/batchDownload | Download multiples attachments from a Commission advance
[**commissionadvance_get_attachments_v1**](ObjectCommissionadvanceApi.md#commissionadvance_get_attachments_v1) | **GET** /1/object/commissionadvance/{pkiCommissionadvanceID}/getAttachments | Retrieve Commissionadvance&#39;s attachments
[**commissionadvance_get_communication_count_v1**](ObjectCommissionadvanceApi.md#commissionadvance_get_communication_count_v1) | **GET** /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationCount | Retrieve Communication count
[**commissionadvance_get_communication_list_v1**](ObjectCommissionadvanceApi.md#commissionadvance_get_communication_list_v1) | **GET** /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationList | Retrieve Communication list
[**commissionadvance_get_communicationrecipients_v1**](ObjectCommissionadvanceApi.md#commissionadvance_get_communicationrecipients_v1) | **GET** /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationrecipients | Retrieve Communication recipients
[**commissionadvance_get_communicationsenders_v1**](ObjectCommissionadvanceApi.md#commissionadvance_get_communicationsenders_v1) | **GET** /1/object/commissionadvance/{pkiCommissionadvanceID}/getCommunicationsenders | Retrieve Communication senders
[**commissionadvance_import_into_edmv1**](ObjectCommissionadvanceApi.md#commissionadvance_import_into_edmv1) | **POST** /1/object/commissionadvance/{pkiCommissionadvanceID}/importIntoEDM | Import attachments into the Commissionadvance


# **commissionadvance_batch_download_v1**
> bytes commissionadvance_batch_download_v1(pki_commissionadvance_id, commissionadvance_batch_download_v1_request)

Download multiples attachments from a Commission advance

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_batch_download_v1_request import CommissionadvanceBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 
    commissionadvance_batch_download_v1_request = eZmaxApi.CommissionadvanceBatchDownloadV1Request() # CommissionadvanceBatchDownloadV1Request | 

    try:
        # Download multiples attachments from a Commission advance
        api_response = api_instance.commissionadvance_batch_download_v1(pki_commissionadvance_id, commissionadvance_batch_download_v1_request)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 
 **commissionadvance_batch_download_v1_request** | [**CommissionadvanceBatchDownloadV1Request**](CommissionadvanceBatchDownloadV1Request.md)|  | 

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

# **commissionadvance_get_attachments_v1**
> CommissionadvanceGetAttachmentsV1Response commissionadvance_get_attachments_v1(pki_commissionadvance_id)

Retrieve Commissionadvance's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_get_attachments_v1_response import CommissionadvanceGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 

    try:
        # Retrieve Commissionadvance's attachments
        api_response = api_instance.commissionadvance_get_attachments_v1(pki_commissionadvance_id)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 

### Return type

[**CommissionadvanceGetAttachmentsV1Response**](CommissionadvanceGetAttachmentsV1Response.md)

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

# **commissionadvance_get_communication_count_v1**
> CommissionadvanceGetCommunicationCountV1Response commissionadvance_get_communication_count_v1(pki_commissionadvance_id)

Retrieve Communication count

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_get_communication_count_v1_response import CommissionadvanceGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.commissionadvance_get_communication_count_v1(pki_commissionadvance_id)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 

### Return type

[**CommissionadvanceGetCommunicationCountV1Response**](CommissionadvanceGetCommunicationCountV1Response.md)

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

# **commissionadvance_get_communication_list_v1**
> CommissionadvanceGetCommunicationListV1Response commissionadvance_get_communication_list_v1(pki_commissionadvance_id)

Retrieve Communication list

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_get_communication_list_v1_response import CommissionadvanceGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.commissionadvance_get_communication_list_v1(pki_commissionadvance_id)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 

### Return type

[**CommissionadvanceGetCommunicationListV1Response**](CommissionadvanceGetCommunicationListV1Response.md)

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

# **commissionadvance_get_communicationrecipients_v1**
> CommissionadvanceGetCommunicationrecipientsV1Response commissionadvance_get_communicationrecipients_v1(pki_commissionadvance_id)

Retrieve Communication recipients

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_get_communicationrecipients_v1_response import CommissionadvanceGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 

    try:
        # Retrieve Communication recipients
        api_response = api_instance.commissionadvance_get_communicationrecipients_v1(pki_commissionadvance_id)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 

### Return type

[**CommissionadvanceGetCommunicationrecipientsV1Response**](CommissionadvanceGetCommunicationrecipientsV1Response.md)

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

# **commissionadvance_get_communicationsenders_v1**
> CommissionadvanceGetCommunicationsendersV1Response commissionadvance_get_communicationsenders_v1(pki_commissionadvance_id)

Retrieve Communication senders

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_get_communicationsenders_v1_response import CommissionadvanceGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 

    try:
        # Retrieve Communication senders
        api_response = api_instance.commissionadvance_get_communicationsenders_v1(pki_commissionadvance_id)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 

### Return type

[**CommissionadvanceGetCommunicationsendersV1Response**](CommissionadvanceGetCommunicationsendersV1Response.md)

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

# **commissionadvance_import_into_edmv1**
> CommissionadvanceImportIntoEDMV1Response commissionadvance_import_into_edmv1(pki_commissionadvance_id, commissionadvance_import_into_edmv1_request)

Import attachments into the Commissionadvance

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.commissionadvance_import_into_edmv1_request import CommissionadvanceImportIntoEDMV1Request
from eZmaxApi.models.commissionadvance_import_into_edmv1_response import CommissionadvanceImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectCommissionadvanceApi(api_client)
    pki_commissionadvance_id = 56 # int | 
    commissionadvance_import_into_edmv1_request = eZmaxApi.CommissionadvanceImportIntoEDMV1Request() # CommissionadvanceImportIntoEDMV1Request | 

    try:
        # Import attachments into the Commissionadvance
        api_response = api_instance.commissionadvance_import_into_edmv1(pki_commissionadvance_id, commissionadvance_import_into_edmv1_request)
        print("The response of ObjectCommissionadvanceApi->commissionadvance_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommissionadvanceApi->commissionadvance_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_commissionadvance_id** | **int**|  | 
 **commissionadvance_import_into_edmv1_request** | [**CommissionadvanceImportIntoEDMV1Request**](CommissionadvanceImportIntoEDMV1Request.md)|  | 

### Return type

[**CommissionadvanceImportIntoEDMV1Response**](CommissionadvanceImportIntoEDMV1Response.md)

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

