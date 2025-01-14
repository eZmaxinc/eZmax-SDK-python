# eZmaxApi.ObjectTranqcontractApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tranqcontract_get_communication_count_v1**](ObjectTranqcontractApi.md#tranqcontract_get_communication_count_v1) | **GET** /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationCount | Retrieve Communication count
[**tranqcontract_get_communication_list_v1**](ObjectTranqcontractApi.md#tranqcontract_get_communication_list_v1) | **GET** /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationList | Retrieve Communication list
[**tranqcontract_get_communicationrecipients_v1**](ObjectTranqcontractApi.md#tranqcontract_get_communicationrecipients_v1) | **GET** /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationrecipients | Retrieve Tranqcontract&#39;s Communicationrecipient
[**tranqcontract_get_communicationsenders_v1**](ObjectTranqcontractApi.md#tranqcontract_get_communicationsenders_v1) | **GET** /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationsenders | Retrieve Tranqcontract&#39;s Communicationsender


# **tranqcontract_get_communication_count_v1**
> TranqcontractGetCommunicationCountV1Response tranqcontract_get_communication_count_v1(pki_tranqcontract_id)

Retrieve Communication count



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.tranqcontract_get_communication_count_v1_response import TranqcontractGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectTranqcontractApi(api_client)
    pki_tranqcontract_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.tranqcontract_get_communication_count_v1(pki_tranqcontract_id)
        print("The response of ObjectTranqcontractApi->tranqcontract_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectTranqcontractApi->tranqcontract_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_tranqcontract_id** | **int**|  | 

### Return type

[**TranqcontractGetCommunicationCountV1Response**](TranqcontractGetCommunicationCountV1Response.md)

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

# **tranqcontract_get_communication_list_v1**
> TranqcontractGetCommunicationListV1Response tranqcontract_get_communication_list_v1(pki_tranqcontract_id)

Retrieve Communication list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.tranqcontract_get_communication_list_v1_response import TranqcontractGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectTranqcontractApi(api_client)
    pki_tranqcontract_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.tranqcontract_get_communication_list_v1(pki_tranqcontract_id)
        print("The response of ObjectTranqcontractApi->tranqcontract_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectTranqcontractApi->tranqcontract_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_tranqcontract_id** | **int**|  | 

### Return type

[**TranqcontractGetCommunicationListV1Response**](TranqcontractGetCommunicationListV1Response.md)

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

# **tranqcontract_get_communicationrecipients_v1**
> TranqcontractGetCommunicationrecipientsV1Response tranqcontract_get_communicationrecipients_v1(pki_tranqcontract_id)

Retrieve Tranqcontract's Communicationrecipient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.tranqcontract_get_communicationrecipients_v1_response import TranqcontractGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectTranqcontractApi(api_client)
    pki_tranqcontract_id = 56 # int | 

    try:
        # Retrieve Tranqcontract's Communicationrecipient
        api_response = api_instance.tranqcontract_get_communicationrecipients_v1(pki_tranqcontract_id)
        print("The response of ObjectTranqcontractApi->tranqcontract_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectTranqcontractApi->tranqcontract_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_tranqcontract_id** | **int**|  | 

### Return type

[**TranqcontractGetCommunicationrecipientsV1Response**](TranqcontractGetCommunicationrecipientsV1Response.md)

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

# **tranqcontract_get_communicationsenders_v1**
> TranqcontractGetCommunicationsendersV1Response tranqcontract_get_communicationsenders_v1(pki_tranqcontract_id)

Retrieve Tranqcontract's Communicationsender



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.tranqcontract_get_communicationsenders_v1_response import TranqcontractGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectTranqcontractApi(api_client)
    pki_tranqcontract_id = 56 # int | 

    try:
        # Retrieve Tranqcontract's Communicationsender
        api_response = api_instance.tranqcontract_get_communicationsenders_v1(pki_tranqcontract_id)
        print("The response of ObjectTranqcontractApi->tranqcontract_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectTranqcontractApi->tranqcontract_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_tranqcontract_id** | **int**|  | 

### Return type

[**TranqcontractGetCommunicationsendersV1Response**](TranqcontractGetCommunicationsendersV1Response.md)

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

