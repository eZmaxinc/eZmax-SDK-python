# eZmaxApi.ObjectEzsigntemplatesignerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatesigner_create_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_create_object_v1) | **POST** /1/object/ezsigntemplatesigner | Create a new Ezsigntemplatesigner
[**ezsigntemplatesigner_delete_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_delete_object_v1) | **DELETE** /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID} | Delete an existing Ezsigntemplatesigner
[**ezsigntemplatesigner_edit_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_edit_object_v1) | **PUT** /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID} | Edit an existing Ezsigntemplatesigner
[**ezsigntemplatesigner_get_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_get_object_v1) | **GET** /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID} | Retrieve an existing Ezsigntemplatesigner


# **ezsigntemplatesigner_create_object_v1**
> EzsigntemplatesignerCreateObjectV1Response ezsigntemplatesigner_create_object_v1(ezsigntemplatesigner_create_object_v1_request)

Create a new Ezsigntemplatesigner

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatesigner_api
from eZmaxApi.model.ezsigntemplatesigner_create_object_v1_request import EzsigntemplatesignerCreateObjectV1Request
from eZmaxApi.model.ezsigntemplatesigner_create_object_v1_response import EzsigntemplatesignerCreateObjectV1Response
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
    api_instance = object_ezsigntemplatesigner_api.ObjectEzsigntemplatesignerApi(api_client)
    ezsigntemplatesigner_create_object_v1_request = EzsigntemplatesignerCreateObjectV1Request(
        a_obj_ezsigntemplatesigner=[
            EzsigntemplatesignerRequestCompound(),
        ],
    ) # EzsigntemplatesignerCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_create_object_v1(ezsigntemplatesigner_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatesigner_create_object_v1_request** | [**EzsigntemplatesignerCreateObjectV1Request**](EzsigntemplatesignerCreateObjectV1Request.md)|  |

### Return type

[**EzsigntemplatesignerCreateObjectV1Response**](EzsigntemplatesignerCreateObjectV1Response.md)

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

# **ezsigntemplatesigner_delete_object_v1**
> EzsigntemplatesignerDeleteObjectV1Response ezsigntemplatesigner_delete_object_v1(pki_ezsigntemplatesigner_id)

Delete an existing Ezsigntemplatesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatesigner_api
from eZmaxApi.model.ezsigntemplatesigner_delete_object_v1_response import EzsigntemplatesignerDeleteObjectV1Response
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
    api_instance = object_ezsigntemplatesigner_api.ObjectEzsigntemplatesignerApi(api_client)
    pki_ezsigntemplatesigner_id = FieldPkiEzsigntemplatesignerID(9) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_delete_object_v1(pki_ezsigntemplatesigner_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesigner_id** | **int**|  |

### Return type

[**EzsigntemplatesignerDeleteObjectV1Response**](EzsigntemplatesignerDeleteObjectV1Response.md)

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

# **ezsigntemplatesigner_edit_object_v1**
> EzsigntemplatesignerEditObjectV1Response ezsigntemplatesigner_edit_object_v1(pki_ezsigntemplatesigner_id, ezsigntemplatesigner_edit_object_v1_request)

Edit an existing Ezsigntemplatesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatesigner_api
from eZmaxApi.model.ezsigntemplatesigner_edit_object_v1_request import EzsigntemplatesignerEditObjectV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatesigner_edit_object_v1_response import EzsigntemplatesignerEditObjectV1Response
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
    api_instance = object_ezsigntemplatesigner_api.ObjectEzsigntemplatesignerApi(api_client)
    pki_ezsigntemplatesigner_id = FieldPkiEzsigntemplatesignerID(9) # int | 
    ezsigntemplatesigner_edit_object_v1_request = EzsigntemplatesignerEditObjectV1Request(
        obj_ezsigntemplatesigner=EzsigntemplatesignerRequestCompound(),
    ) # EzsigntemplatesignerEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_edit_object_v1(pki_ezsigntemplatesigner_id, ezsigntemplatesigner_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesigner_id** | **int**|  |
 **ezsigntemplatesigner_edit_object_v1_request** | [**EzsigntemplatesignerEditObjectV1Request**](EzsigntemplatesignerEditObjectV1Request.md)|  |

### Return type

[**EzsigntemplatesignerEditObjectV1Response**](EzsigntemplatesignerEditObjectV1Response.md)

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

# **ezsigntemplatesigner_get_object_v1**
> EzsigntemplatesignerGetObjectV1Response ezsigntemplatesigner_get_object_v1(pki_ezsigntemplatesigner_id)

Retrieve an existing Ezsigntemplatesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatesigner_api
from eZmaxApi.model.ezsigntemplatesigner_get_object_v1_response import EzsigntemplatesignerGetObjectV1Response
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
    api_instance = object_ezsigntemplatesigner_api.ObjectEzsigntemplatesignerApi(api_client)
    pki_ezsigntemplatesigner_id = FieldPkiEzsigntemplatesignerID(9) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_get_object_v1(pki_ezsigntemplatesigner_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesigner_id** | **int**|  |

### Return type

[**EzsigntemplatesignerGetObjectV1Response**](EzsigntemplatesignerGetObjectV1Response.md)

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

