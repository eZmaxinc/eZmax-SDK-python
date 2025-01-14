# eZmaxApi.ObjectRejectedoffertopurchaseApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rejectedoffertopurchase_get_communication_count_v1**](ObjectRejectedoffertopurchaseApi.md#rejectedoffertopurchase_get_communication_count_v1) | **GET** /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationCount | Retrieve Communication count
[**rejectedoffertopurchase_get_communication_list_v1**](ObjectRejectedoffertopurchaseApi.md#rejectedoffertopurchase_get_communication_list_v1) | **GET** /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationList | Retrieve Communication list
[**rejectedoffertopurchase_get_communicationrecipients_v1**](ObjectRejectedoffertopurchaseApi.md#rejectedoffertopurchase_get_communicationrecipients_v1) | **GET** /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationrecipients | Retrieve Rejectedoffertopurchase&#39;s Communicationrecipient
[**rejectedoffertopurchase_get_communicationsenders_v1**](ObjectRejectedoffertopurchaseApi.md#rejectedoffertopurchase_get_communicationsenders_v1) | **GET** /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationsenders | Retrieve Rejectedoffertopurchase&#39;s Communicationsender


# **rejectedoffertopurchase_get_communication_count_v1**
> RejectedoffertopurchaseGetCommunicationCountV1Response rejectedoffertopurchase_get_communication_count_v1(pki_rejectedoffertopurchase_id)

Retrieve Communication count



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.rejectedoffertopurchase_get_communication_count_v1_response import RejectedoffertopurchaseGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectRejectedoffertopurchaseApi(api_client)
    pki_rejectedoffertopurchase_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.rejectedoffertopurchase_get_communication_count_v1(pki_rejectedoffertopurchase_id)
        print("The response of ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_rejectedoffertopurchase_id** | **int**|  | 

### Return type

[**RejectedoffertopurchaseGetCommunicationCountV1Response**](RejectedoffertopurchaseGetCommunicationCountV1Response.md)

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

# **rejectedoffertopurchase_get_communication_list_v1**
> RejectedoffertopurchaseGetCommunicationListV1Response rejectedoffertopurchase_get_communication_list_v1(pki_rejectedoffertopurchase_id)

Retrieve Communication list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.rejectedoffertopurchase_get_communication_list_v1_response import RejectedoffertopurchaseGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectRejectedoffertopurchaseApi(api_client)
    pki_rejectedoffertopurchase_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.rejectedoffertopurchase_get_communication_list_v1(pki_rejectedoffertopurchase_id)
        print("The response of ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_rejectedoffertopurchase_id** | **int**|  | 

### Return type

[**RejectedoffertopurchaseGetCommunicationListV1Response**](RejectedoffertopurchaseGetCommunicationListV1Response.md)

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

# **rejectedoffertopurchase_get_communicationrecipients_v1**
> RejectedoffertopurchaseGetCommunicationrecipientsV1Response rejectedoffertopurchase_get_communicationrecipients_v1(pki_rejectedoffertopurchase_id)

Retrieve Rejectedoffertopurchase's Communicationrecipient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.rejectedoffertopurchase_get_communicationrecipients_v1_response import RejectedoffertopurchaseGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectRejectedoffertopurchaseApi(api_client)
    pki_rejectedoffertopurchase_id = 56 # int | 

    try:
        # Retrieve Rejectedoffertopurchase's Communicationrecipient
        api_response = api_instance.rejectedoffertopurchase_get_communicationrecipients_v1(pki_rejectedoffertopurchase_id)
        print("The response of ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_rejectedoffertopurchase_id** | **int**|  | 

### Return type

[**RejectedoffertopurchaseGetCommunicationrecipientsV1Response**](RejectedoffertopurchaseGetCommunicationrecipientsV1Response.md)

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

# **rejectedoffertopurchase_get_communicationsenders_v1**
> RejectedoffertopurchaseGetCommunicationsendersV1Response rejectedoffertopurchase_get_communicationsenders_v1(pki_rejectedoffertopurchase_id)

Retrieve Rejectedoffertopurchase's Communicationsender



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.rejectedoffertopurchase_get_communicationsenders_v1_response import RejectedoffertopurchaseGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectRejectedoffertopurchaseApi(api_client)
    pki_rejectedoffertopurchase_id = 56 # int | 

    try:
        # Retrieve Rejectedoffertopurchase's Communicationsender
        api_response = api_instance.rejectedoffertopurchase_get_communicationsenders_v1(pki_rejectedoffertopurchase_id)
        print("The response of ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectRejectedoffertopurchaseApi->rejectedoffertopurchase_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_rejectedoffertopurchase_id** | **int**|  | 

### Return type

[**RejectedoffertopurchaseGetCommunicationsendersV1Response**](RejectedoffertopurchaseGetCommunicationsendersV1Response.md)

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

