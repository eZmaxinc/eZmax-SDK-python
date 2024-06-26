# eZmaxApi.ObjectEzsigntemplatepackagesignerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatepackagesigner_create_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_create_object_v1) | **POST** /1/object/ezsigntemplatepackagesigner | Create a new Ezsigntemplatepackagesigner
[**ezsigntemplatepackagesigner_delete_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_delete_object_v1) | **DELETE** /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID} | Delete an existing Ezsigntemplatepackagesigner
[**ezsigntemplatepackagesigner_edit_object_v1**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_edit_object_v1) | **PUT** /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID} | Edit an existing Ezsigntemplatepackagesigner
[**ezsigntemplatepackagesigner_get_object_v2**](ObjectEzsigntemplatepackagesignerApi.md#ezsigntemplatepackagesigner_get_object_v2) | **GET** /2/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID} | Retrieve an existing Ezsigntemplatepackagesigner


# **ezsigntemplatepackagesigner_create_object_v1**
> EzsigntemplatepackagesignerCreateObjectV1Response ezsigntemplatepackagesigner_create_object_v1(ezsigntemplatepackagesigner_create_object_v1_request)

Create a new Ezsigntemplatepackagesigner

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v1_request import EzsigntemplatepackagesignerCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v1_response import EzsigntemplatepackagesignerCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagesignerApi(api_client)
    ezsigntemplatepackagesigner_create_object_v1_request = eZmaxApi.EzsigntemplatepackagesignerCreateObjectV1Request() # EzsigntemplatepackagesignerCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_create_object_v1(ezsigntemplatepackagesigner_create_object_v1_request)
        print("The response of ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagesigner_delete_object_v1_response import EzsigntemplatepackagesignerDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagesignerApi(api_client)
    pki_ezsigntemplatepackagesigner_id = 56 # int | 

    try:
        # Delete an existing Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_delete_object_v1(pki_ezsigntemplatepackagesigner_id)
        print("The response of ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplatepackagesigner_edit_object_v1**
> EzsigntemplatepackagesignerEditObjectV1Response ezsigntemplatepackagesigner_edit_object_v1(pki_ezsigntemplatepackagesigner_id, ezsigntemplatepackagesigner_edit_object_v1_request)

Edit an existing Ezsigntemplatepackagesigner



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagesigner_edit_object_v1_request import EzsigntemplatepackagesignerEditObjectV1Request
from eZmaxApi.models.ezsigntemplatepackagesigner_edit_object_v1_response import EzsigntemplatepackagesignerEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagesignerApi(api_client)
    pki_ezsigntemplatepackagesigner_id = 56 # int | 
    ezsigntemplatepackagesigner_edit_object_v1_request = eZmaxApi.EzsigntemplatepackagesignerEditObjectV1Request() # EzsigntemplatepackagesignerEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_edit_object_v1(pki_ezsigntemplatepackagesigner_id, ezsigntemplatepackagesigner_edit_object_v1_request)
        print("The response of ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplatepackagesigner_get_object_v2**
> EzsigntemplatepackagesignerGetObjectV2Response ezsigntemplatepackagesigner_get_object_v2(pki_ezsigntemplatepackagesigner_id)

Retrieve an existing Ezsigntemplatepackagesigner



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v2_response import EzsigntemplatepackagesignerGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagesignerApi(api_client)
    pki_ezsigntemplatepackagesigner_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatepackagesigner
        api_response = api_instance.ezsigntemplatepackagesigner_get_object_v2(pki_ezsigntemplatepackagesigner_id)
        print("The response of ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignerApi->ezsigntemplatepackagesigner_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagesigner_id** | **int**|  | 

### Return type

[**EzsigntemplatepackagesignerGetObjectV2Response**](EzsigntemplatepackagesignerGetObjectV2Response.md)

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

