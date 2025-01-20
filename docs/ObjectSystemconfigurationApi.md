# eZmaxApi.ObjectSystemconfigurationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systemconfiguration_edit_object_v1**](ObjectSystemconfigurationApi.md#systemconfiguration_edit_object_v1) | **PUT** /1/object/systemconfiguration/{pkiSystemconfigurationID} | Edit an existing Systemconfiguration
[**systemconfiguration_get_object_v2**](ObjectSystemconfigurationApi.md#systemconfiguration_get_object_v2) | **GET** /2/object/systemconfiguration/{pkiSystemconfigurationID} | Retrieve an existing Systemconfiguration


# **systemconfiguration_edit_object_v1**
> CommonResponse systemconfiguration_edit_object_v1(pki_systemconfiguration_id, systemconfiguration_edit_object_v1_request)

Edit an existing Systemconfiguration



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.systemconfiguration_edit_object_v1_request import SystemconfigurationEditObjectV1Request
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
    api_instance = eZmaxApi.ObjectSystemconfigurationApi(api_client)
    pki_systemconfiguration_id = 56 # int | The unique ID of the Systemconfiguration
    systemconfiguration_edit_object_v1_request = eZmaxApi.SystemconfigurationEditObjectV1Request() # SystemconfigurationEditObjectV1Request | 

    try:
        # Edit an existing Systemconfiguration
        api_response = api_instance.systemconfiguration_edit_object_v1(pki_systemconfiguration_id, systemconfiguration_edit_object_v1_request)
        print("The response of ObjectSystemconfigurationApi->systemconfiguration_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSystemconfigurationApi->systemconfiguration_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_systemconfiguration_id** | **int**| The unique ID of the Systemconfiguration | 
 **systemconfiguration_edit_object_v1_request** | [**SystemconfigurationEditObjectV1Request**](SystemconfigurationEditObjectV1Request.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemconfiguration_get_object_v2**
> SystemconfigurationGetObjectV2Response systemconfiguration_get_object_v2(pki_systemconfiguration_id)

Retrieve an existing Systemconfiguration



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.systemconfiguration_get_object_v2_response import SystemconfigurationGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectSystemconfigurationApi(api_client)
    pki_systemconfiguration_id = 56 # int | The unique ID of the Systemconfiguration

    try:
        # Retrieve an existing Systemconfiguration
        api_response = api_instance.systemconfiguration_get_object_v2(pki_systemconfiguration_id)
        print("The response of ObjectSystemconfigurationApi->systemconfiguration_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSystemconfigurationApi->systemconfiguration_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_systemconfiguration_id** | **int**| The unique ID of the Systemconfiguration | 

### Return type

[**SystemconfigurationGetObjectV2Response**](SystemconfigurationGetObjectV2Response.md)

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

