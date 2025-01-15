# eZmaxApi.ObjectEzsignbulksenddocumentmappingApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignbulksenddocumentmapping_create_object_v1**](ObjectEzsignbulksenddocumentmappingApi.md#ezsignbulksenddocumentmapping_create_object_v1) | **POST** /1/object/ezsignbulksenddocumentmapping | Create a new Ezsignbulksenddocumentmapping
[**ezsignbulksenddocumentmapping_delete_object_v1**](ObjectEzsignbulksenddocumentmappingApi.md#ezsignbulksenddocumentmapping_delete_object_v1) | **DELETE** /1/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID} | Delete an existing Ezsignbulksenddocumentmapping
[**ezsignbulksenddocumentmapping_get_object_v2**](ObjectEzsignbulksenddocumentmappingApi.md#ezsignbulksenddocumentmapping_get_object_v2) | **GET** /2/object/ezsignbulksenddocumentmapping/{pkiEzsignbulksenddocumentmappingID} | Retrieve an existing Ezsignbulksenddocumentmapping


# **ezsignbulksenddocumentmapping_create_object_v1**
> EzsignbulksenddocumentmappingCreateObjectV1Response ezsignbulksenddocumentmapping_create_object_v1(ezsignbulksenddocumentmapping_create_object_v1_request)

Create a new Ezsignbulksenddocumentmapping

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksenddocumentmapping_create_object_v1_request import EzsignbulksenddocumentmappingCreateObjectV1Request
from eZmaxApi.models.ezsignbulksenddocumentmapping_create_object_v1_response import EzsignbulksenddocumentmappingCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksenddocumentmappingApi(api_client)
    ezsignbulksenddocumentmapping_create_object_v1_request = eZmaxApi.EzsignbulksenddocumentmappingCreateObjectV1Request() # EzsignbulksenddocumentmappingCreateObjectV1Request | 

    try:
        # Create a new Ezsignbulksenddocumentmapping
        api_response = api_instance.ezsignbulksenddocumentmapping_create_object_v1(ezsignbulksenddocumentmapping_create_object_v1_request)
        print("The response of ObjectEzsignbulksenddocumentmappingApi->ezsignbulksenddocumentmapping_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksenddocumentmappingApi->ezsignbulksenddocumentmapping_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignbulksenddocumentmapping_create_object_v1_request** | [**EzsignbulksenddocumentmappingCreateObjectV1Request**](EzsignbulksenddocumentmappingCreateObjectV1Request.md)|  | 

### Return type

[**EzsignbulksenddocumentmappingCreateObjectV1Response**](EzsignbulksenddocumentmappingCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksenddocumentmapping_delete_object_v1**
> CommonResponse ezsignbulksenddocumentmapping_delete_object_v1(pki_ezsignbulksenddocumentmapping_id)

Delete an existing Ezsignbulksenddocumentmapping



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
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
    api_instance = eZmaxApi.ObjectEzsignbulksenddocumentmappingApi(api_client)
    pki_ezsignbulksenddocumentmapping_id = 56 # int | 

    try:
        # Delete an existing Ezsignbulksenddocumentmapping
        api_response = api_instance.ezsignbulksenddocumentmapping_delete_object_v1(pki_ezsignbulksenddocumentmapping_id)
        print("The response of ObjectEzsignbulksenddocumentmappingApi->ezsignbulksenddocumentmapping_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksenddocumentmappingApi->ezsignbulksenddocumentmapping_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksenddocumentmapping_id** | **int**|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

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

# **ezsignbulksenddocumentmapping_get_object_v2**
> EzsignbulksenddocumentmappingGetObjectV2Response ezsignbulksenddocumentmapping_get_object_v2(pki_ezsignbulksenddocumentmapping_id)

Retrieve an existing Ezsignbulksenddocumentmapping



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksenddocumentmapping_get_object_v2_response import EzsignbulksenddocumentmappingGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksenddocumentmappingApi(api_client)
    pki_ezsignbulksenddocumentmapping_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksenddocumentmapping
        api_response = api_instance.ezsignbulksenddocumentmapping_get_object_v2(pki_ezsignbulksenddocumentmapping_id)
        print("The response of ObjectEzsignbulksenddocumentmappingApi->ezsignbulksenddocumentmapping_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksenddocumentmappingApi->ezsignbulksenddocumentmapping_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksenddocumentmapping_id** | **int**|  | 

### Return type

[**EzsignbulksenddocumentmappingGetObjectV2Response**](EzsignbulksenddocumentmappingGetObjectV2Response.md)

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

