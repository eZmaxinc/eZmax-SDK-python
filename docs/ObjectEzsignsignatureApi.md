# eZmaxinc/eZmax-SDK-python.ObjectEzsignsignatureApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignsignature_create_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_create_object_v1) | **POST** /1/object/ezsignsignature | Create a new Ezsignsignature
[**ezsignsignature_delete_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_delete_object_v1) | **DELETE** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Delete an existing Ezsignsignature
[**ezsignsignature_edit_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_edit_object_v1) | **PUT** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Modify an existing Ezsignsignature
[**ezsignsignature_get_children_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_get_children_v1) | **GET** /1/object/ezsignsignature/{pkiEzsignsignatureID}/getChildren | Retrieve an existing Ezsignsignature&#39;s children IDs
[**ezsignsignature_get_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_get_object_v1) | **GET** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Retrieve an existing Ezsignsignature


# **ezsignsignature_create_object_v1**
> EzsignsignatureCreateObjectV1Response ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request)

Create a new Ezsignsignature

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignsignature_api
from eZmaxinc/eZmax-SDK-python.model.ezsignsignature_create_object_v1_request import EzsignsignatureCreateObjectV1Request
from eZmaxinc/eZmax-SDK-python.model.ezsignsignature_create_object_v1_response import EzsignsignatureCreateObjectV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    ezsignsignature_create_object_v1_request = [
        EzsignsignatureCreateObjectV1Request(
            obj_ezsignsignature=EzsignsignatureRequest(
                fki_ezsignfoldersignerassociation_id=1,
                i_ezsignpage_pagenumber=1,
                i_ezsignsignature_x=1,
                i_ezsignsignature_y=1,
                i_ezsignsignature_step=1,
                e_ezsignsignature_type="Acknowledgement",
                fki_ezsigndocument_id=1,
            ),
            obj_ezsignsignature_compound=EzsignsignatureRequestCompound(),
        ),
    ] # [EzsignsignatureCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignsignature
        api_response = api_instance.ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
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
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignsignature_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsignsignature_delete_object_v1_response import EzsignsignatureDeleteObjectV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 1 # int | The unique ID of the Ezsignsignature

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_delete_object_v1(pki_ezsignsignature_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_delete_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**| The unique ID of the Ezsignsignature |

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

# **ezsignsignature_edit_object_v1**
> EzsignsignatureEditObjectV1Response ezsignsignature_edit_object_v1(pki_ezsignsignature_id, ezsignsignature_edit_object_v1_request)

Modify an existing Ezsignsignature

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignsignature_api
from eZmaxinc/eZmax-SDK-python.model.ezsignsignature_edit_object_v1_response import EzsignsignatureEditObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.ezsignsignature_edit_object_v1_request import EzsignsignatureEditObjectV1Request
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 1 # int | The unique ID of the Ezsignsignature
    ezsignsignature_edit_object_v1_request = EzsignsignatureEditObjectV1Request(
        obj_ezsignsignature=EzsignsignatureRequest(
            fki_ezsignfoldersignerassociation_id=1,
            i_ezsignpage_pagenumber=1,
            i_ezsignsignature_x=1,
            i_ezsignsignature_y=1,
            i_ezsignsignature_step=1,
            e_ezsignsignature_type="Acknowledgement",
            fki_ezsigndocument_id=1,
        ),
    ) # EzsignsignatureEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Modify an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_edit_object_v1(pki_ezsignsignature_id, ezsignsignature_edit_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_edit_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**| The unique ID of the Ezsignsignature |
 **ezsignsignature_edit_object_v1_request** | [**EzsignsignatureEditObjectV1Request**](EzsignsignatureEditObjectV1Request.md)|  |

### Return type

[**EzsignsignatureEditObjectV1Response**](EzsignsignatureEditObjectV1Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignsignature_get_children_v1**
> ezsignsignature_get_children_v1(pki_ezsignsignature_id)

Retrieve an existing Ezsignsignature's children IDs

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignsignature_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 1 # int | The unique ID of the Ezsignsignature

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignsignature's children IDs
        api_instance.ezsignsignature_get_children_v1(pki_ezsignsignature_id)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_get_children_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**| The unique ID of the Ezsignsignature |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The element you are trying to work on does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignsignature_get_object_v1**
> EzsignsignatureGetObjectV1Response ezsignsignature_get_object_v1(pki_ezsignsignature_id)

Retrieve an existing Ezsignsignature

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignsignature_api
from eZmaxinc/eZmax-SDK-python.model.ezsignsignature_get_object_v1_response import EzsignsignatureGetObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignsignature_api.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 1 # int | The unique ID of the Ezsignsignature

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_get_object_v1(pki_ezsignsignature_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_get_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**| The unique ID of the Ezsignsignature |

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

