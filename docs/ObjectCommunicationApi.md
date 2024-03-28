# eZmaxApi.ObjectCommunicationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communication_send_v1**](ObjectCommunicationApi.md#communication_send_v1) | **POST** /1/object/communication/send | Send a new Communication


# **communication_send_v1**
> CommunicationSendV1Response communication_send_v1(communication_send_v1_request)

Send a new Communication

The endpoint allows to send one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.communication_send_v1_request import CommunicationSendV1Request
from eZmaxApi.models.communication_send_v1_response import CommunicationSendV1Response
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
    api_instance = eZmaxApi.ObjectCommunicationApi(api_client)
    communication_send_v1_request = eZmaxApi.CommunicationSendV1Request() # CommunicationSendV1Request | 

    try:
        # Send a new Communication
        api_response = api_instance.communication_send_v1(communication_send_v1_request)
        print("The response of ObjectCommunicationApi->communication_send_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCommunicationApi->communication_send_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_send_v1_request** | [**CommunicationSendV1Request**](CommunicationSendV1Request.md)|  | 

### Return type

[**CommunicationSendV1Response**](CommunicationSendV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

