# eZmaxApi.ObjectEzsigntemplateformfieldgroupApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplateformfieldgroup_create_object_v1**](ObjectEzsigntemplateformfieldgroupApi.md#ezsigntemplateformfieldgroup_create_object_v1) | **POST** /1/object/ezsigntemplateformfieldgroup | Create a new Ezsigntemplateformfieldgroup
[**ezsigntemplateformfieldgroup_delete_object_v1**](ObjectEzsigntemplateformfieldgroupApi.md#ezsigntemplateformfieldgroup_delete_object_v1) | **DELETE** /1/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID} | Delete an existing Ezsigntemplateformfieldgroup
[**ezsigntemplateformfieldgroup_edit_object_v1**](ObjectEzsigntemplateformfieldgroupApi.md#ezsigntemplateformfieldgroup_edit_object_v1) | **PUT** /1/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID} | Edit an existing Ezsigntemplateformfieldgroup
[**ezsigntemplateformfieldgroup_get_object_v2**](ObjectEzsigntemplateformfieldgroupApi.md#ezsigntemplateformfieldgroup_get_object_v2) | **GET** /2/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID} | Retrieve an existing Ezsigntemplateformfieldgroup


# **ezsigntemplateformfieldgroup_create_object_v1**
> EzsigntemplateformfieldgroupCreateObjectV1Response ezsigntemplateformfieldgroup_create_object_v1(ezsigntemplateformfieldgroup_create_object_v1_request)

Create a new Ezsigntemplateformfieldgroup

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplateformfieldgroup_create_object_v1_request import EzsigntemplateformfieldgroupCreateObjectV1Request
from eZmaxApi.models.ezsigntemplateformfieldgroup_create_object_v1_response import EzsigntemplateformfieldgroupCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplateformfieldgroupApi(api_client)
    ezsigntemplateformfieldgroup_create_object_v1_request = eZmaxApi.EzsigntemplateformfieldgroupCreateObjectV1Request() # EzsigntemplateformfieldgroupCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplateformfieldgroup
        api_response = api_instance.ezsigntemplateformfieldgroup_create_object_v1(ezsigntemplateformfieldgroup_create_object_v1_request)
        print("The response of ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplateformfieldgroup_create_object_v1_request** | [**EzsigntemplateformfieldgroupCreateObjectV1Request**](EzsigntemplateformfieldgroupCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplateformfieldgroupCreateObjectV1Response**](EzsigntemplateformfieldgroupCreateObjectV1Response.md)

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

# **ezsigntemplateformfieldgroup_delete_object_v1**
> CommonResponse ezsigntemplateformfieldgroup_delete_object_v1(pki_ezsigntemplateformfieldgroup_id)

Delete an existing Ezsigntemplateformfieldgroup



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
    api_instance = eZmaxApi.ObjectEzsigntemplateformfieldgroupApi(api_client)
    pki_ezsigntemplateformfieldgroup_id = 56 # int | 

    try:
        # Delete an existing Ezsigntemplateformfieldgroup
        api_response = api_instance.ezsigntemplateformfieldgroup_delete_object_v1(pki_ezsigntemplateformfieldgroup_id)
        print("The response of ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplateformfieldgroup_id** | **int**|  | 

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

# **ezsigntemplateformfieldgroup_edit_object_v1**
> CommonResponse ezsigntemplateformfieldgroup_edit_object_v1(pki_ezsigntemplateformfieldgroup_id, ezsigntemplateformfieldgroup_edit_object_v1_request)

Edit an existing Ezsigntemplateformfieldgroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.ezsigntemplateformfieldgroup_edit_object_v1_request import EzsigntemplateformfieldgroupEditObjectV1Request
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
    api_instance = eZmaxApi.ObjectEzsigntemplateformfieldgroupApi(api_client)
    pki_ezsigntemplateformfieldgroup_id = 56 # int | 
    ezsigntemplateformfieldgroup_edit_object_v1_request = eZmaxApi.EzsigntemplateformfieldgroupEditObjectV1Request() # EzsigntemplateformfieldgroupEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplateformfieldgroup
        api_response = api_instance.ezsigntemplateformfieldgroup_edit_object_v1(pki_ezsigntemplateformfieldgroup_id, ezsigntemplateformfieldgroup_edit_object_v1_request)
        print("The response of ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplateformfieldgroup_id** | **int**|  | 
 **ezsigntemplateformfieldgroup_edit_object_v1_request** | [**EzsigntemplateformfieldgroupEditObjectV1Request**](EzsigntemplateformfieldgroupEditObjectV1Request.md)|  | 

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

# **ezsigntemplateformfieldgroup_get_object_v2**
> EzsigntemplateformfieldgroupGetObjectV2Response ezsigntemplateformfieldgroup_get_object_v2(pki_ezsigntemplateformfieldgroup_id)

Retrieve an existing Ezsigntemplateformfieldgroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigntemplateformfieldgroup_get_object_v2_response import EzsigntemplateformfieldgroupGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplateformfieldgroupApi(api_client)
    pki_ezsigntemplateformfieldgroup_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplateformfieldgroup
        api_response = api_instance.ezsigntemplateformfieldgroup_get_object_v2(pki_ezsigntemplateformfieldgroup_id)
        print("The response of ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplateformfieldgroupApi->ezsigntemplateformfieldgroup_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplateformfieldgroup_id** | **int**|  | 

### Return type

[**EzsigntemplateformfieldgroupGetObjectV2Response**](EzsigntemplateformfieldgroupGetObjectV2Response.md)

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

