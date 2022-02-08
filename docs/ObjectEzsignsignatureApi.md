# eZmaxApi.ObjectEzsignsignatureApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignsignature_create_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_create_object_v1) | **POST** /1/object/ezsignsignature | Create a new Ezsignsignature
[**ezsignsignature_delete_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_delete_object_v1) | **DELETE** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Delete an existing Ezsignsignature
[**ezsignsignature_get_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_get_object_v1) | **GET** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Retrieve an existing Ezsignsignature


# **ezsignsignature_create_object_v1**
> EzsignsignatureCreateObjectV1Response ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request)

Create a new Ezsignsignature

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignsignature_api
from eZmaxApi.model.ezsignsignature_create_object_v1_response import EzsignsignatureCreateObjectV1Response
from eZmaxApi.model.ezsignsignature_create_object_v1_request import EzsignsignatureCreateObjectV1Request
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
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    ezsignsignature_create_object_v1_request = [
        EzsignsignatureCreateObjectV1Request(
            obj_ezsignsignature=EzsignsignatureRequest(
                pki_ezsignsignature_id=49,
                fki_ezsignfoldersignerassociation_id=20,
                i_ezsignpage_pagenumber=1,
                i_ezsignsignature_x=200,
                i_ezsignsignature_y=300,
                i_ezsignsignature_step=1,
                e_ezsignsignature_type=FieldEEzsignsignatureType("Name"),
                fki_ezsigndocument_id=97,
            ),
            obj_ezsignsignature_compound=EzsignsignatureRequestCompound(),
        ),
    ] # [EzsignsignatureCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignsignature
        api_response = api_instance.ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignsignature_create_object_v1_request** | [**[EzsignsignatureCreateObjectV1Request]**](EzsignsignatureCreateObjectV1Request.md)|  |

### Return type

[**EzsignsignatureCreateObjectV1Response**](EzsignsignatureCreateObjectV1Response.md)

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

# **ezsignsignature_delete_object_v1**
> EzsignsignatureDeleteObjectV1Response ezsignsignature_delete_object_v1(pki_ezsignsignature_id)

Delete an existing Ezsignsignature

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignsignature_api
from eZmaxApi.model.ezsignsignature_delete_object_v1_response import EzsignsignatureDeleteObjectV1Response
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
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 49 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_delete_object_v1(pki_ezsignsignature_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  |

### Return type

[**EzsignsignatureDeleteObjectV1Response**](EzsignsignatureDeleteObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignsignature_get_object_v1**
> EzsignsignatureGetObjectV1Response ezsignsignature_get_object_v1(pki_ezsignsignature_id)

Retrieve an existing Ezsignsignature

## ⚠️EARLY ADOPTERS WARNING  ### This endpoint is not officially released. Its definition might still change and it might not be available in every environment and region.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignsignature_api
from eZmaxApi.model.ezsignsignature_get_object_v1_response import EzsignsignatureGetObjectV1Response
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
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 49 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_get_object_v1(pki_ezsignsignature_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  |

### Return type

[**EzsignsignatureGetObjectV1Response**](EzsignsignatureGetObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

