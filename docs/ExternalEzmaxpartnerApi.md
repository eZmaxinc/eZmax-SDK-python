# eZmaxApi.ExternalEzmaxpartnerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezmaxpartner_subscribe_v1**](ExternalEzmaxpartnerApi.md#ezmaxpartner_subscribe_v1) | **POST** /1/external/ezmaxpartner/subscribe | Subscribe to an Ezmaxparnerproductstage


# **ezmaxpartner_subscribe_v1**
> EzmaxpartnerSubscribeV1Response ezmaxpartner_subscribe_v1(ezmaxpartner_subscribe_v1_request)

Subscribe to an Ezmaxparnerproductstage

Subscribe to an Ezmaxparnerproductstage

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartner_subscribe_v1_request import EzmaxpartnerSubscribeV1Request
from eZmaxApi.models.ezmaxpartner_subscribe_v1_response import EzmaxpartnerSubscribeV1Response
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
    api_instance = eZmaxApi.ExternalEzmaxpartnerApi(api_client)
    ezmaxpartner_subscribe_v1_request = eZmaxApi.EzmaxpartnerSubscribeV1Request() # EzmaxpartnerSubscribeV1Request | 

    try:
        # Subscribe to an Ezmaxparnerproductstage
        api_response = api_instance.ezmaxpartner_subscribe_v1(ezmaxpartner_subscribe_v1_request)
        print("The response of ExternalEzmaxpartnerApi->ezmaxpartner_subscribe_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalEzmaxpartnerApi->ezmaxpartner_subscribe_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezmaxpartner_subscribe_v1_request** | [**EzmaxpartnerSubscribeV1Request**](EzmaxpartnerSubscribeV1Request.md)|  | 

### Return type

[**EzmaxpartnerSubscribeV1Response**](EzmaxpartnerSubscribeV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

