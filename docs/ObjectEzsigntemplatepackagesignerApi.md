# eZmaxApi.ObjectEzsigntemplatepackagesignerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatepackagesigner_create_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_create_object_v1) | **POST** /1/object/ezsigntemplatepackagesigner | Create a new Ezsigntemplatepackagesigner
[**ezsigntemplatepackagesigner_delete_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_delete_object_v1) | **DELETE** /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID} | Delete an existing Ezsigntemplatepackagesigner
[**ezsigntemplatepackagesigner_edit_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_edit_object_v1) | **PUT** /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID} | Edit an existing Ezsigntemplatepackagesigner
[**ezsigntemplatepackagesigner_get_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_get_object_v1) | **GET** /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID} | Retrieve an existing Ezsigntemplatepackagesigner


# **ezsigntemplatepackagesigner_create_object_v1**
> EzsigntemplatepackagesignerCreateObjectV1Response ezsigntemplatepackagesigner_create_object_v1(ezsigntemplatepackagesigner_create_object_v1_request)

Create a new Ezsigntemplatepackagesigner

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesigner_api
from eZmaxApi.model.ezsigntemplatepackagesigner_create_object_v1_response import EzsigntemplatepackagesignerCreateObjectV1Response
from eZmaxApi.model.ezsigntemplatepackagesigner_create_object_v1_request import EzsigntemplatepackagesignerCreateObjectV1Request
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
    api_instance = object_ezsigntemplatepackagesigner_api.ObjectEzsigntemplatepackagesignerApi(api_client)
    ezsigntemplatepackagesigner_create_object_v1_request = EzsigntemplatepackagesignerCreateObjectV1Request(
        a_obj_ezsigntemplatepackagesigner=[
            EzsigntemplatepackagesignerRequestCompound(),
        ],
    ) # EzsigntemplatepackagesignerCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_create_object_v1(ezsigntemplatepackagesigner_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatepackagesigner_create_object_v1_request** | [**EzsigntemplatepackagesignerCreateObjectV1Request**](EzsigntemplatepackagesignerCreateObjectV1Request.md)|  |

### Return type

[**EzsigntemplatepackagesignerCreateObjectV1Response**](EzsigntemplatepackagesignerCreateObjectV1Response.md)

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

# **ezsigntemplatepackagesigner_delete_object_v1**
> EzsigntemplatepackagesignerDeleteObjectV1Response ezsigntemplatepackagesigner_delete_object_v1(pki_ezsigntemplatepackagesigner_id)

Delete an existing Ezsigntemplatepackagesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesigner_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatepackagesigner_delete_object_v1_response import EzsigntemplatepackagesignerDeleteObjectV1Response
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
    api_instance = object_ezsigntemplatepackagesigner_api.ObjectEzsigntemplatepackagesignerApi(api_client)
    pki_ezsigntemplatepackagesigner_id = 174 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_delete_object_v1(pki_ezsigntemplatepackagesigner_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagesigner_id** | **int**|  |

### Return type

[**EzsigntemplatepackagesignerDeleteObjectV1Response**](EzsigntemplatepackagesignerDeleteObjectV1Response.md)

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

# **ezsigntemplatepackagesigner_edit_object_v1**
> EzsigntemplatepackagesignerEditObjectV1Response ezsigntemplatepackagesigner_edit_object_v1(pki_ezsigntemplatepackagesigner_id, ezsigntemplatepackagesigner_edit_object_v1_request)

Edit an existing Ezsigntemplatepackagesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesigner_api
from eZmaxApi.model.ezsigntemplatepackagesigner_edit_object_v1_response import EzsigntemplatepackagesignerEditObjectV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatepackagesigner_edit_object_v1_request import EzsigntemplatepackagesignerEditObjectV1Request
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
    api_instance = object_ezsigntemplatepackagesigner_api.ObjectEzsigntemplatepackagesignerApi(api_client)
    pki_ezsigntemplatepackagesigner_id = 174 # int | 
    ezsigntemplatepackagesigner_edit_object_v1_request = EzsigntemplatepackagesignerEditObjectV1Request(
        obj_ezsigntemplatepackagesigner=EzsigntemplatepackagesignerRequestCompound(),
    ) # EzsigntemplatepackagesignerEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_edit_object_v1(pki_ezsigntemplatepackagesigner_id, ezsigntemplatepackagesigner_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagesigner_id** | **int**|  |
 **ezsigntemplatepackagesigner_edit_object_v1_request** | [**EzsigntemplatepackagesignerEditObjectV1Request**](EzsigntemplatepackagesignerEditObjectV1Request.md)|  |

### Return type

[**EzsigntemplatepackagesignerEditObjectV1Response**](EzsigntemplatepackagesignerEditObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplatepackagesigner_get_object_v1**
> EzsigntemplatepackagesignerGetObjectV1Response ezsigntemplatepackagesigner_get_object_v1(pki_ezsigntemplatepackagesigner_id)

Retrieve an existing Ezsigntemplatepackagesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesigner_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatepackagesigner_get_object_v1_response import EzsigntemplatepackagesignerGetObjectV1Response
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
    api_instance = object_ezsigntemplatepackagesigner_api.ObjectEzsigntemplatepackagesignerApi(api_client)
    pki_ezsigntemplatepackagesigner_id = 174 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_get_object_v1(pki_ezsigntemplatepackagesigner_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagesigner_id** | **int**|  |

### Return type

[**EzsigntemplatepackagesignerGetObjectV1Response**](EzsigntemplatepackagesignerGetObjectV1Response.md)

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

