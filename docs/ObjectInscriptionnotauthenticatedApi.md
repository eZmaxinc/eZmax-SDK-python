# eZmaxApi.ObjectInscriptionnotauthenticatedApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inscriptionnotauthenticated_get_communication_count_v1**](ObjectInscriptionnotauthenticatedApi.md#inscriptionnotauthenticated_get_communication_count_v1) | **GET** /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationCount | Retrieve Communication count
[**inscriptionnotauthenticated_get_communication_list_v1**](ObjectInscriptionnotauthenticatedApi.md#inscriptionnotauthenticated_get_communication_list_v1) | **GET** /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationList | Retrieve Communication list
[**inscriptionnotauthenticated_get_communicationrecipients_v1**](ObjectInscriptionnotauthenticatedApi.md#inscriptionnotauthenticated_get_communicationrecipients_v1) | **GET** /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationrecipients | Retrieve Inscriptionnotauthenticated&#39;s Communicationrecipient
[**inscriptionnotauthenticated_get_communicationsenders_v1**](ObjectInscriptionnotauthenticatedApi.md#inscriptionnotauthenticated_get_communicationsenders_v1) | **GET** /1/object/inscriptionnotauthenticated/{pkiInscriptionnotauthenticatedID}/getCommunicationsenders | Retrieve Inscriptionnotauthenticated&#39;s Communicationsender


# **inscriptionnotauthenticated_get_communication_count_v1**
> InscriptionnotauthenticatedGetCommunicationCountV1Response inscriptionnotauthenticated_get_communication_count_v1(pki_inscriptionnotauthenticated_id)

Retrieve Communication count



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.inscriptionnotauthenticated_get_communication_count_v1_response import InscriptionnotauthenticatedGetCommunicationCountV1Response
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
    api_instance = eZmaxApi.ObjectInscriptionnotauthenticatedApi(api_client)
    pki_inscriptionnotauthenticated_id = 56 # int | 

    try:
        # Retrieve Communication count
        api_response = api_instance.inscriptionnotauthenticated_get_communication_count_v1(pki_inscriptionnotauthenticated_id)
        print("The response of ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communication_count_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communication_count_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_inscriptionnotauthenticated_id** | **int**|  | 

### Return type

[**InscriptionnotauthenticatedGetCommunicationCountV1Response**](InscriptionnotauthenticatedGetCommunicationCountV1Response.md)

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

# **inscriptionnotauthenticated_get_communication_list_v1**
> InscriptionnotauthenticatedGetCommunicationListV1Response inscriptionnotauthenticated_get_communication_list_v1(pki_inscriptionnotauthenticated_id)

Retrieve Communication list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.inscriptionnotauthenticated_get_communication_list_v1_response import InscriptionnotauthenticatedGetCommunicationListV1Response
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
    api_instance = eZmaxApi.ObjectInscriptionnotauthenticatedApi(api_client)
    pki_inscriptionnotauthenticated_id = 56 # int | 

    try:
        # Retrieve Communication list
        api_response = api_instance.inscriptionnotauthenticated_get_communication_list_v1(pki_inscriptionnotauthenticated_id)
        print("The response of ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communication_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communication_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_inscriptionnotauthenticated_id** | **int**|  | 

### Return type

[**InscriptionnotauthenticatedGetCommunicationListV1Response**](InscriptionnotauthenticatedGetCommunicationListV1Response.md)

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

# **inscriptionnotauthenticated_get_communicationrecipients_v1**
> InscriptionnotauthenticatedGetCommunicationrecipientsV1Response inscriptionnotauthenticated_get_communicationrecipients_v1(pki_inscriptionnotauthenticated_id)

Retrieve Inscriptionnotauthenticated's Communicationrecipient



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.inscriptionnotauthenticated_get_communicationrecipients_v1_response import InscriptionnotauthenticatedGetCommunicationrecipientsV1Response
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
    api_instance = eZmaxApi.ObjectInscriptionnotauthenticatedApi(api_client)
    pki_inscriptionnotauthenticated_id = 56 # int | 

    try:
        # Retrieve Inscriptionnotauthenticated's Communicationrecipient
        api_response = api_instance.inscriptionnotauthenticated_get_communicationrecipients_v1(pki_inscriptionnotauthenticated_id)
        print("The response of ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communicationrecipients_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communicationrecipients_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_inscriptionnotauthenticated_id** | **int**|  | 

### Return type

[**InscriptionnotauthenticatedGetCommunicationrecipientsV1Response**](InscriptionnotauthenticatedGetCommunicationrecipientsV1Response.md)

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

# **inscriptionnotauthenticated_get_communicationsenders_v1**
> InscriptionnotauthenticatedGetCommunicationsendersV1Response inscriptionnotauthenticated_get_communicationsenders_v1(pki_inscriptionnotauthenticated_id)

Retrieve Inscriptionnotauthenticated's Communicationsender



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.inscriptionnotauthenticated_get_communicationsenders_v1_response import InscriptionnotauthenticatedGetCommunicationsendersV1Response
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
    api_instance = eZmaxApi.ObjectInscriptionnotauthenticatedApi(api_client)
    pki_inscriptionnotauthenticated_id = 56 # int | 

    try:
        # Retrieve Inscriptionnotauthenticated's Communicationsender
        api_response = api_instance.inscriptionnotauthenticated_get_communicationsenders_v1(pki_inscriptionnotauthenticated_id)
        print("The response of ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communicationsenders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectInscriptionnotauthenticatedApi->inscriptionnotauthenticated_get_communicationsenders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_inscriptionnotauthenticated_id** | **int**|  | 

### Return type

[**InscriptionnotauthenticatedGetCommunicationsendersV1Response**](InscriptionnotauthenticatedGetCommunicationsendersV1Response.md)

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

