# eZmaxApi.ObjectEzsigntemplateannotationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplateannotation_create_object_v1**](ObjectEzsigntemplateannotationApi.md#ezsigntemplateannotation_create_object_v1) | **POST** /1/object/ezsigntemplateannotation | Create a new Ezsigntemplateannotation
[**ezsigntemplateannotation_delete_object_v1**](ObjectEzsigntemplateannotationApi.md#ezsigntemplateannotation_delete_object_v1) | **DELETE** /1/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID} | Delete an existing Ezsigntemplateannotation
[**ezsigntemplateannotation_edit_object_v1**](ObjectEzsigntemplateannotationApi.md#ezsigntemplateannotation_edit_object_v1) | **PUT** /1/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID} | Edit an existing Ezsigntemplateannotation
[**ezsigntemplateannotation_get_object_v2**](ObjectEzsigntemplateannotationApi.md#ezsigntemplateannotation_get_object_v2) | **GET** /2/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID} | Retrieve an existing Ezsigntemplateannotation


# **ezsigntemplateannotation_create_object_v1**
> EzsigntemplateannotationCreateObjectV1Response ezsigntemplateannotation_create_object_v1(ezsigntemplateannotation_create_object_v1_request)

Create a new Ezsigntemplateannotation

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplateannotation_create_object_v1_request import EzsigntemplateannotationCreateObjectV1Request
from eZmaxApi.models.ezsigntemplateannotation_create_object_v1_response import EzsigntemplateannotationCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplateannotationApi(api_client)
    ezsigntemplateannotation_create_object_v1_request = eZmaxApi.EzsigntemplateannotationCreateObjectV1Request() # EzsigntemplateannotationCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplateannotation
        api_response = api_instance.ezsigntemplateannotation_create_object_v1(ezsigntemplateannotation_create_object_v1_request)
        print("The response of ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplateannotation_create_object_v1_request** | [**EzsigntemplateannotationCreateObjectV1Request**](EzsigntemplateannotationCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplateannotationCreateObjectV1Response**](EzsigntemplateannotationCreateObjectV1Response.md)

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

# **ezsigntemplateannotation_delete_object_v1**
> EzsigntemplateannotationDeleteObjectV1Response ezsigntemplateannotation_delete_object_v1(pki_ezsigntemplateannotation_id)

Delete an existing Ezsigntemplateannotation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplateannotation_delete_object_v1_response import EzsigntemplateannotationDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplateannotationApi(api_client)
    pki_ezsigntemplateannotation_id = 56 # int | The unique ID of the Ezsigntemplateannotation

    try:
        # Delete an existing Ezsigntemplateannotation
        api_response = api_instance.ezsigntemplateannotation_delete_object_v1(pki_ezsigntemplateannotation_id)
        print("The response of ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplateannotation_id** | **int**| The unique ID of the Ezsigntemplateannotation | 

### Return type

[**EzsigntemplateannotationDeleteObjectV1Response**](EzsigntemplateannotationDeleteObjectV1Response.md)

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

# **ezsigntemplateannotation_edit_object_v1**
> EzsigntemplateannotationEditObjectV1Response ezsigntemplateannotation_edit_object_v1(pki_ezsigntemplateannotation_id, ezsigntemplateannotation_edit_object_v1_request)

Edit an existing Ezsigntemplateannotation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplateannotation_edit_object_v1_request import EzsigntemplateannotationEditObjectV1Request
from eZmaxApi.models.ezsigntemplateannotation_edit_object_v1_response import EzsigntemplateannotationEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplateannotationApi(api_client)
    pki_ezsigntemplateannotation_id = 56 # int | The unique ID of the Ezsigntemplateannotation
    ezsigntemplateannotation_edit_object_v1_request = eZmaxApi.EzsigntemplateannotationEditObjectV1Request() # EzsigntemplateannotationEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplateannotation
        api_response = api_instance.ezsigntemplateannotation_edit_object_v1(pki_ezsigntemplateannotation_id, ezsigntemplateannotation_edit_object_v1_request)
        print("The response of ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplateannotation_id** | **int**| The unique ID of the Ezsigntemplateannotation | 
 **ezsigntemplateannotation_edit_object_v1_request** | [**EzsigntemplateannotationEditObjectV1Request**](EzsigntemplateannotationEditObjectV1Request.md)|  | 

### Return type

[**EzsigntemplateannotationEditObjectV1Response**](EzsigntemplateannotationEditObjectV1Response.md)

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

# **ezsigntemplateannotation_get_object_v2**
> EzsigntemplateannotationGetObjectV2Response ezsigntemplateannotation_get_object_v2(pki_ezsigntemplateannotation_id)

Retrieve an existing Ezsigntemplateannotation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplateannotation_get_object_v2_response import EzsigntemplateannotationGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplateannotationApi(api_client)
    pki_ezsigntemplateannotation_id = 56 # int | The unique ID of the Ezsigntemplateannotation

    try:
        # Retrieve an existing Ezsigntemplateannotation
        api_response = api_instance.ezsigntemplateannotation_get_object_v2(pki_ezsigntemplateannotation_id)
        print("The response of ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateannotationApi->ezsigntemplateannotation_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplateannotation_id** | **int**| The unique ID of the Ezsigntemplateannotation | 

### Return type

[**EzsigntemplateannotationGetObjectV2Response**](EzsigntemplateannotationGetObjectV2Response.md)

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

