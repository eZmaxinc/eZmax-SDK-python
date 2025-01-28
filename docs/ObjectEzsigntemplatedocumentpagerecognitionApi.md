# eZmaxApi.ObjectEzsigntemplatedocumentpagerecognitionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatedocumentpagerecognition_create_object_v1**](ObjectEzsigntemplatedocumentpagerecognitionApi.md#ezsigntemplatedocumentpagerecognition_create_object_v1) | **POST** /1/object/ezsigntemplatedocumentpagerecognition | Create a new Ezsigntemplatedocumentpagerecognition
[**ezsigntemplatedocumentpagerecognition_delete_object_v1**](ObjectEzsigntemplatedocumentpagerecognitionApi.md#ezsigntemplatedocumentpagerecognition_delete_object_v1) | **DELETE** /1/object/ezsigntemplatedocumentpagerecognition/{pkiEzsigntemplatedocumentpagerecognitionID} | Delete an existing Ezsigntemplatedocumentpagerecognition
[**ezsigntemplatedocumentpagerecognition_edit_object_v1**](ObjectEzsigntemplatedocumentpagerecognitionApi.md#ezsigntemplatedocumentpagerecognition_edit_object_v1) | **PUT** /1/object/ezsigntemplatedocumentpagerecognition/{pkiEzsigntemplatedocumentpagerecognitionID} | Edit an existing Ezsigntemplatedocumentpagerecognition
[**ezsigntemplatedocumentpagerecognition_get_object_v2**](ObjectEzsigntemplatedocumentpagerecognitionApi.md#ezsigntemplatedocumentpagerecognition_get_object_v2) | **GET** /2/object/ezsigntemplatedocumentpagerecognition/{pkiEzsigntemplatedocumentpagerecognitionID} | Retrieve an existing Ezsigntemplatedocumentpagerecognition


# **ezsigntemplatedocumentpagerecognition_create_object_v1**
> EzsigntemplatedocumentpagerecognitionCreateObjectV1Response ezsigntemplatedocumentpagerecognition_create_object_v1(ezsigntemplatedocumentpagerecognition_create_object_v1_request)

Create a new Ezsigntemplatedocumentpagerecognition

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_create_object_v1_request import EzsigntemplatedocumentpagerecognitionCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_create_object_v1_response import EzsigntemplatedocumentpagerecognitionCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentpagerecognitionApi(api_client)
    ezsigntemplatedocumentpagerecognition_create_object_v1_request = eZmaxApi.EzsigntemplatedocumentpagerecognitionCreateObjectV1Request() # EzsigntemplatedocumentpagerecognitionCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatedocumentpagerecognition
        api_response = api_instance.ezsigntemplatedocumentpagerecognition_create_object_v1(ezsigntemplatedocumentpagerecognition_create_object_v1_request)
        print("The response of ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatedocumentpagerecognition_create_object_v1_request** | [**EzsigntemplatedocumentpagerecognitionCreateObjectV1Request**](EzsigntemplatedocumentpagerecognitionCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatedocumentpagerecognitionCreateObjectV1Response**](EzsigntemplatedocumentpagerecognitionCreateObjectV1Response.md)

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

# **ezsigntemplatedocumentpagerecognition_delete_object_v1**
> EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response ezsigntemplatedocumentpagerecognition_delete_object_v1(pki_ezsigntemplatedocumentpagerecognition_id)

Delete an existing Ezsigntemplatedocumentpagerecognition



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_delete_object_v1_response import EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentpagerecognitionApi(api_client)
    pki_ezsigntemplatedocumentpagerecognition_id = 56 # int | The unique ID of the Ezsigntemplatedocumentpagerecognition

    try:
        # Delete an existing Ezsigntemplatedocumentpagerecognition
        api_response = api_instance.ezsigntemplatedocumentpagerecognition_delete_object_v1(pki_ezsigntemplatedocumentpagerecognition_id)
        print("The response of ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocumentpagerecognition_id** | **int**| The unique ID of the Ezsigntemplatedocumentpagerecognition | 

### Return type

[**EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response**](EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response.md)

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

# **ezsigntemplatedocumentpagerecognition_edit_object_v1**
> EzsigntemplatedocumentpagerecognitionEditObjectV1Response ezsigntemplatedocumentpagerecognition_edit_object_v1(pki_ezsigntemplatedocumentpagerecognition_id, ezsigntemplatedocumentpagerecognition_edit_object_v1_request)

Edit an existing Ezsigntemplatedocumentpagerecognition



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_edit_object_v1_request import EzsigntemplatedocumentpagerecognitionEditObjectV1Request
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_edit_object_v1_response import EzsigntemplatedocumentpagerecognitionEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentpagerecognitionApi(api_client)
    pki_ezsigntemplatedocumentpagerecognition_id = 56 # int | The unique ID of the Ezsigntemplatedocumentpagerecognition
    ezsigntemplatedocumentpagerecognition_edit_object_v1_request = eZmaxApi.EzsigntemplatedocumentpagerecognitionEditObjectV1Request() # EzsigntemplatedocumentpagerecognitionEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplatedocumentpagerecognition
        api_response = api_instance.ezsigntemplatedocumentpagerecognition_edit_object_v1(pki_ezsigntemplatedocumentpagerecognition_id, ezsigntemplatedocumentpagerecognition_edit_object_v1_request)
        print("The response of ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocumentpagerecognition_id** | **int**| The unique ID of the Ezsigntemplatedocumentpagerecognition | 
 **ezsigntemplatedocumentpagerecognition_edit_object_v1_request** | [**EzsigntemplatedocumentpagerecognitionEditObjectV1Request**](EzsigntemplatedocumentpagerecognitionEditObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatedocumentpagerecognitionEditObjectV1Response**](EzsigntemplatedocumentpagerecognitionEditObjectV1Response.md)

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

# **ezsigntemplatedocumentpagerecognition_get_object_v2**
> EzsigntemplatedocumentpagerecognitionGetObjectV2Response ezsigntemplatedocumentpagerecognition_get_object_v2(pki_ezsigntemplatedocumentpagerecognition_id)

Retrieve an existing Ezsigntemplatedocumentpagerecognition



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_get_object_v2_response import EzsigntemplatedocumentpagerecognitionGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentpagerecognitionApi(api_client)
    pki_ezsigntemplatedocumentpagerecognition_id = 56 # int | The unique ID of the Ezsigntemplatedocumentpagerecognition

    try:
        # Retrieve an existing Ezsigntemplatedocumentpagerecognition
        api_response = api_instance.ezsigntemplatedocumentpagerecognition_get_object_v2(pki_ezsigntemplatedocumentpagerecognition_id)
        print("The response of ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatedocumentpagerecognitionApi->ezsigntemplatedocumentpagerecognition_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocumentpagerecognition_id** | **int**| The unique ID of the Ezsigntemplatedocumentpagerecognition | 

### Return type

[**EzsigntemplatedocumentpagerecognitionGetObjectV2Response**](EzsigntemplatedocumentpagerecognitionGetObjectV2Response.md)

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

