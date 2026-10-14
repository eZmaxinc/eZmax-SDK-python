# eZmaxApi.ObjectPaymentpreparationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentpreparation_batch_download_v1**](ObjectPaymentpreparationApi.md#paymentpreparation_batch_download_v1) | **POST** /1/object/paymentpreparation/{pkiPaymentpreparationID}/batchDownload | Download multiples attachments from an Paymentpreparation
[**paymentpreparation_get_attachments_v1**](ObjectPaymentpreparationApi.md#paymentpreparation_get_attachments_v1) | **GET** /1/object/paymentpreparation/{pkiPaymentpreparationID}/getAttachments | Retrieve Paymentpreparation&#39;s attachments
[**paymentpreparation_get_communication_count_v1**](ObjectPaymentpreparationApi.md#paymentpreparation_get_communication_count_v1) | **GET** /1/object/paymentpreparation/{pkiPaymentpreparationID}/getCommunicationCount | Retrieve Communication count
[**paymentpreparation_get_communication_list_v1**](ObjectPaymentpreparationApi.md#paymentpreparation_get_communication_list_v1) | **GET** /1/object/paymentpreparation/{pkiPaymentpreparationID}/getCommunicationList | Retrieve Communication list
[**paymentpreparation_get_communicationrecipients_v1**](ObjectPaymentpreparationApi.md#paymentpreparation_get_communicationrecipients_v1) | **GET** /1/object/paymentpreparation/{pkiPaymentpreparationID}/getCommunicationrecipients | Retrieve Communication recipients
[**paymentpreparation_get_communicationsenders_v1**](ObjectPaymentpreparationApi.md#paymentpreparation_get_communicationsenders_v1) | **GET** /1/object/paymentpreparation/{pkiPaymentpreparationID}/getCommunicationsenders | Retrieve Communication senders
[**paymentpreparation_import_into_edmv1**](ObjectPaymentpreparationApi.md#paymentpreparation_import_into_edmv1) | **POST** /1/object/paymentpreparation/{pkiPaymentpreparationID}/importIntoEDM | Import attachments into the Paymentpreparation


# **paymentpreparation_batch_download_v1**
> bytes paymentpreparation_batch_download_v1(pki_paymentpreparation_id, paymentpreparation_batch_download_v1_request)

Download multiples attachments from an Paymentpreparation

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_batch_download_v1_request import PaymentpreparationBatchDownloadV1Request
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 
    paymentpreparation_batch_download_v1_request = eZmaxApi.PaymentpreparationBatchDownloadV1Request() # PaymentpreparationBatchDownloadV1Request | 

    try:
        # Download multiples attachments from an Paymentpreparation
        api_response = api_instance.paymentpreparation_batch_download_v1(pki_paymentpreparation_id, paymentpreparation_batch_download_v1_request)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_batch_download_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_batch_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 
 **paymentpreparation_batch_download_v1_request** | [**PaymentpreparationBatchDownloadV1Request**](PaymentpreparationBatchDownloadV1Request.md)|  | 

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

# **paymentpreparation_get_attachments_v1**
> PaymentpreparationGetAttachmentsV1Response paymentpreparation_get_attachments_v1(pki_paymentpreparation_id)

Retrieve Paymentpreparation's attachments

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_get_attachments_v1_response import PaymentpreparationGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 

    try:
        # Retrieve Paymentpreparation's attachments
        api_response = api_instance.paymentpreparation_get_attachments_v1(pki_paymentpreparation_id)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 

### Return type

[**PaymentpreparationGetAttachmentsV1Response**](PaymentpreparationGetAttachmentsV1Response.md)

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

# **paymentpreparation_get_communication_count_v1**
> PaymentpreparationGetCommunicationCountV1Response paymentpreparation_get_communication_count_v1(pki_paymentpreparation_id)

Retrieve Communication count

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_get_communication_count_v1_response import PaymentpreparationGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.paymentpreparation_get_communication_count_v1(pki_paymentpreparation_id)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 

### Return type

[**PaymentpreparationGetCommunicationCountV1Response**](PaymentpreparationGetCommunicationCountV1Response.md)

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

# **paymentpreparation_get_communication_list_v1**
> PaymentpreparationGetCommunicationListV1Response paymentpreparation_get_communication_list_v1(pki_paymentpreparation_id)

Retrieve Communication list

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_get_communication_list_v1_response import PaymentpreparationGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.paymentpreparation_get_communication_list_v1(pki_paymentpreparation_id)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 

### Return type

[**PaymentpreparationGetCommunicationListV1Response**](PaymentpreparationGetCommunicationListV1Response.md)

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

# **paymentpreparation_get_communicationrecipients_v1**
> PaymentpreparationGetCommunicationrecipientsV1Response paymentpreparation_get_communicationrecipients_v1(pki_paymentpreparation_id)

Retrieve Communication recipients

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_get_communicationrecipients_v1_response import PaymentpreparationGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 

    try:
        # Retrieve Communication recipients
        api_response = api_instance.paymentpreparation_get_communicationrecipients_v1(pki_paymentpreparation_id)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 

### Return type

[**PaymentpreparationGetCommunicationrecipientsV1Response**](PaymentpreparationGetCommunicationrecipientsV1Response.md)

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

# **paymentpreparation_get_communicationsenders_v1**
> PaymentpreparationGetCommunicationsendersV1Response paymentpreparation_get_communicationsenders_v1(pki_paymentpreparation_id)

Retrieve Communication senders

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_get_communicationsenders_v1_response import PaymentpreparationGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 

    try:
        # Retrieve Communication senders
        api_response = api_instance.paymentpreparation_get_communicationsenders_v1(pki_paymentpreparation_id)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 

### Return type

[**PaymentpreparationGetCommunicationsendersV1Response**](PaymentpreparationGetCommunicationsendersV1Response.md)

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

# **paymentpreparation_import_into_edmv1**
> PaymentpreparationImportIntoEDMV1Response paymentpreparation_import_into_edmv1(pki_paymentpreparation_id, paymentpreparation_import_into_edmv1_request)

Import attachments into the Paymentpreparation

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.paymentpreparation_import_into_edmv1_request import PaymentpreparationImportIntoEDMV1Request
from eZmaxApi.models.paymentpreparation_import_into_edmv1_response import PaymentpreparationImportIntoEDMV1Response
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
    api_instance = eZmaxApi.ObjectPaymentpreparationApi(api_client)
    pki_paymentpreparation_id = 56 # int | 
    paymentpreparation_import_into_edmv1_request = eZmaxApi.PaymentpreparationImportIntoEDMV1Request() # PaymentpreparationImportIntoEDMV1Request | 

    try:
        # Import attachments into the Paymentpreparation
        api_response = api_instance.paymentpreparation_import_into_edmv1(pki_paymentpreparation_id, paymentpreparation_import_into_edmv1_request)
        print("The response of ObjectPaymentpreparationApi->paymentpreparation_import_into_edmv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPaymentpreparationApi->paymentpreparation_import_into_edmv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_paymentpreparation_id** | **int**|  | 
 **paymentpreparation_import_into_edmv1_request** | [**PaymentpreparationImportIntoEDMV1Request**](PaymentpreparationImportIntoEDMV1Request.md)|  | 

### Return type

[**PaymentpreparationImportIntoEDMV1Response**](PaymentpreparationImportIntoEDMV1Response.md)

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

