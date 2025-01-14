# eZmaxApi.ObjectBuyercontractApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buyercontract_get_communication_count_v1**](ObjectBuyercontractApi.md#buyercontract_get_communication_count_v1) | **GET** /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationCount | Retrieve Communication count
[**buyercontract_get_communication_list_v1**](ObjectBuyercontractApi.md#buyercontract_get_communication_list_v1) | **GET** /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationList | Retrieve Communication list
[**buyercontract_get_communicationrecipients_v1**](ObjectBuyercontractApi.md#buyercontract_get_communicationrecipients_v1) | **GET** /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationrecipients | Retrieve Buyercontract&#39;s Communicationrecipient
[**buyercontract_get_communicationsenders_v1**](ObjectBuyercontractApi.md#buyercontract_get_communicationsenders_v1) | **GET** /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationsenders | Retrieve Buyercontract&#39;s Communicationsender


# **buyercontract_get_communication_count_v1**
> BuyercontractGetCommunicationCountV1Response buyercontract_get_communication_count_v1(pki_buyercontract_id)

Retrieve Communication count



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.buyercontract_get_communication_count_v1_response import BuyercontractGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectBuyercontractApi(api_client)
    pki_buyercontract_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.buyercontract_get_communication_count_v1(pki_buyercontract_id)
        print("The response of ObjectBuyercontractApi->buyercontract_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectBuyercontractApi->buyercontract_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_buyercontract_id** | **int**|  | 

### Return type

[**BuyercontractGetCommunicationCountV1Response**](BuyercontractGetCommunicationCountV1Response.md)

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

# **buyercontract_get_communication_list_v1**
> BuyercontractGetCommunicationListV1Response buyercontract_get_communication_list_v1(pki_buyercontract_id)

Retrieve Communication list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.buyercontract_get_communication_list_v1_response import BuyercontractGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectBuyercontractApi(api_client)
    pki_buyercontract_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.buyercontract_get_communication_list_v1(pki_buyercontract_id)
        print("The response of ObjectBuyercontractApi->buyercontract_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectBuyercontractApi->buyercontract_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_buyercontract_id** | **int**|  | 

### Return type

[**BuyercontractGetCommunicationListV1Response**](BuyercontractGetCommunicationListV1Response.md)

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

# **buyercontract_get_communicationrecipients_v1**
> BuyercontractGetCommunicationrecipientsV1Response buyercontract_get_communicationrecipients_v1(pki_buyercontract_id)

Retrieve Buyercontract's Communicationrecipient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.buyercontract_get_communicationrecipients_v1_response import BuyercontractGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectBuyercontractApi(api_client)
    pki_buyercontract_id = 56 # int | 

    try:
        # Retrieve Buyercontract's Communicationrecipient
        api_response = api_instance.buyercontract_get_communicationrecipients_v1(pki_buyercontract_id)
        print("The response of ObjectBuyercontractApi->buyercontract_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectBuyercontractApi->buyercontract_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_buyercontract_id** | **int**|  | 

### Return type

[**BuyercontractGetCommunicationrecipientsV1Response**](BuyercontractGetCommunicationrecipientsV1Response.md)

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

# **buyercontract_get_communicationsenders_v1**
> BuyercontractGetCommunicationsendersV1Response buyercontract_get_communicationsenders_v1(pki_buyercontract_id)

Retrieve Buyercontract's Communicationsender



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.buyercontract_get_communicationsenders_v1_response import BuyercontractGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectBuyercontractApi(api_client)
    pki_buyercontract_id = 56 # int | 

    try:
        # Retrieve Buyercontract's Communicationsender
        api_response = api_instance.buyercontract_get_communicationsenders_v1(pki_buyercontract_id)
        print("The response of ObjectBuyercontractApi->buyercontract_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectBuyercontractApi->buyercontract_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_buyercontract_id** | **int**|  | 

### Return type

[**BuyercontractGetCommunicationsendersV1Response**](BuyercontractGetCommunicationsendersV1Response.md)

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

