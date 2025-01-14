# eZmaxApi.ObjectElectronicfundstransferApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**electronicfundstransfer_get_communication_count_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communication_count_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationCount | Retrieve Communication count
[**electronicfundstransfer_get_communication_list_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communication_list_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationList | Retrieve Communication list
[**electronicfundstransfer_get_communicationrecipients_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communicationrecipients_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationrecipients | Retrieve Electronicfundstransfer&#39;s Communicationrecipient
[**electronicfundstransfer_get_communicationsenders_v1**](ObjectElectronicfundstransferApi.md#electronicfundstransfer_get_communicationsenders_v1) | **GET** /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/getCommunicationsenders | Retrieve Electronicfundstransfer&#39;s Communicationsender


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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

