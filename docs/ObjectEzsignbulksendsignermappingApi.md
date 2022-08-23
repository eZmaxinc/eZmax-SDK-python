# eZmaxApi.ObjectEzsignbulksendsignermappingApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignbulksendsignermapping_create_object_v1**](ObjectEzsignbulksendsignermappingApi.md#ezsignbulksendsignermapping_create_object_v1) | **POST** /1/object/ezsignbulksendsignermapping | Create a new Ezsignbulksendsignermapping
[**ezsignbulksendsignermapping_delete_object_v1**](ObjectEzsignbulksendsignermappingApi.md#ezsignbulksendsignermapping_delete_object_v1) | **DELETE** /1/object/ezsignbulksendsignermapping/{pkiEzsignbulksendsignermappingID} | Delete an existing Ezsignbulksendsignermapping
[**ezsignbulksendsignermapping_get_object_v1**](ObjectEzsignbulksendsignermappingApi.md#ezsignbulksendsignermapping_get_object_v1) | **GET** /1/object/ezsignbulksendsignermapping/{pkiEzsignbulksendsignermappingID} | Retrieve an existing Ezsignbulksendsignermapping


# **ezsignbulksendsignermapping_create_object_v1**
> EzsignbulksendsignermappingCreateObjectV1Response ezsignbulksendsignermapping_create_object_v1(ezsignbulksendsignermapping_create_object_v1_request)

Create a new Ezsignbulksendsignermapping

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignbulksendsignermapping_api
from eZmaxApi.model.ezsignbulksendsignermapping_create_object_v1_response import EzsignbulksendsignermappingCreateObjectV1Response
from eZmaxApi.model.ezsignbulksendsignermapping_create_object_v1_request import EzsignbulksendsignermappingCreateObjectV1Request
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignbulksendsignermapping_api.ObjectEzsignbulksendsignermappingApi(api_client)
    ezsignbulksendsignermapping_create_object_v1_request = EzsignbulksendsignermappingCreateObjectV1Request(
        a_obj_ezsignbulksendsignermapping=[
            EzsignbulksendsignermappingRequestCompound(),
        ],
    ) # EzsignbulksendsignermappingCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignbulksendsignermapping
        api_response = api_instance.ezsignbulksendsignermapping_create_object_v1(ezsignbulksendsignermapping_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignbulksendsignermappingApi->ezsignbulksendsignermapping_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignbulksendsignermapping_create_object_v1_request** | [**EzsignbulksendsignermappingCreateObjectV1Request**](EzsignbulksendsignermappingCreateObjectV1Request.md)|  |

### Return type

[**EzsignbulksendsignermappingCreateObjectV1Response**](EzsignbulksendsignermappingCreateObjectV1Response.md)

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

# **ezsignbulksendsignermapping_delete_object_v1**
> EzsignbulksendsignermappingDeleteObjectV1Response ezsignbulksendsignermapping_delete_object_v1(pki_ezsignbulksendsignermapping_id)

Delete an existing Ezsignbulksendsignermapping



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignbulksendsignermapping_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignbulksendsignermapping_delete_object_v1_response import EzsignbulksendsignermappingDeleteObjectV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignbulksendsignermapping_api.ObjectEzsignbulksendsignermappingApi(api_client)
    pki_ezsignbulksendsignermapping_id = FieldPkiEzsignbulksendsignermappingID(57) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsignbulksendsignermapping
        api_response = api_instance.ezsignbulksendsignermapping_delete_object_v1(pki_ezsignbulksendsignermapping_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignbulksendsignermappingApi->ezsignbulksendsignermapping_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksendsignermapping_id** | **int**|  |

### Return type

[**EzsignbulksendsignermappingDeleteObjectV1Response**](EzsignbulksendsignermappingDeleteObjectV1Response.md)

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

# **ezsignbulksendsignermapping_get_object_v1**
> EzsignbulksendsignermappingGetObjectV1Response ezsignbulksendsignermapping_get_object_v1(pki_ezsignbulksendsignermapping_id)

Retrieve an existing Ezsignbulksendsignermapping



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignbulksendsignermapping_api
from eZmaxApi.model.ezsignbulksendsignermapping_get_object_v1_response import EzsignbulksendsignermappingGetObjectV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignbulksendsignermapping_api.ObjectEzsignbulksendsignermappingApi(api_client)
    pki_ezsignbulksendsignermapping_id = FieldPkiEzsignbulksendsignermappingID(57) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignbulksendsignermapping
        api_response = api_instance.ezsignbulksendsignermapping_get_object_v1(pki_ezsignbulksendsignermapping_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignbulksendsignermappingApi->ezsignbulksendsignermapping_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksendsignermapping_id** | **int**|  |

### Return type

[**EzsignbulksendsignermappingGetObjectV1Response**](EzsignbulksendsignermappingGetObjectV1Response.md)

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

