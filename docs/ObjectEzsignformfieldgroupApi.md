# eZmaxApi.ObjectEzsignformfieldgroupApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignformfieldgroup_create_object_v1**](ObjectEzsignformfieldgroupApi.md#ezsignformfieldgroup_create_object_v1) | **POST** /1/object/ezsignformfieldgroup | Create a new Ezsignformfieldgroup
[**ezsignformfieldgroup_delete_object_v1**](ObjectEzsignformfieldgroupApi.md#ezsignformfieldgroup_delete_object_v1) | **DELETE** /1/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID} | Delete an existing Ezsignformfieldgroup
[**ezsignformfieldgroup_edit_object_v1**](ObjectEzsignformfieldgroupApi.md#ezsignformfieldgroup_edit_object_v1) | **PUT** /1/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID} | Edit an existing Ezsignformfieldgroup
[**ezsignformfieldgroup_get_object_v2**](ObjectEzsignformfieldgroupApi.md#ezsignformfieldgroup_get_object_v2) | **GET** /2/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID} | Retrieve an existing Ezsignformfieldgroup


# **ezsignformfieldgroup_create_object_v1**
> EzsignformfieldgroupCreateObjectV1Response ezsignformfieldgroup_create_object_v1(ezsignformfieldgroup_create_object_v1_request)

Create a new Ezsignformfieldgroup

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignformfieldgroup_create_object_v1_request import EzsignformfieldgroupCreateObjectV1Request
from eZmaxApi.models.ezsignformfieldgroup_create_object_v1_response import EzsignformfieldgroupCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignformfieldgroupApi(api_client)
    ezsignformfieldgroup_create_object_v1_request = eZmaxApi.EzsignformfieldgroupCreateObjectV1Request() # EzsignformfieldgroupCreateObjectV1Request | 

    try:
        # Create a new Ezsignformfieldgroup
        api_response = api_instance.ezsignformfieldgroup_create_object_v1(ezsignformfieldgroup_create_object_v1_request)
        print("The response of ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignformfieldgroup_create_object_v1_request** | [**EzsignformfieldgroupCreateObjectV1Request**](EzsignformfieldgroupCreateObjectV1Request.md)|  | 

### Return type

[**EzsignformfieldgroupCreateObjectV1Response**](EzsignformfieldgroupCreateObjectV1Response.md)

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

# **ezsignformfieldgroup_delete_object_v1**
> EzsignformfieldgroupDeleteObjectV1Response ezsignformfieldgroup_delete_object_v1(pki_ezsignformfieldgroup_id)

Delete an existing Ezsignformfieldgroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignformfieldgroup_delete_object_v1_response import EzsignformfieldgroupDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignformfieldgroupApi(api_client)
    pki_ezsignformfieldgroup_id = 56 # int | 

    try:
        # Delete an existing Ezsignformfieldgroup
        api_response = api_instance.ezsignformfieldgroup_delete_object_v1(pki_ezsignformfieldgroup_id)
        print("The response of ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignformfieldgroup_id** | **int**|  | 

### Return type

[**EzsignformfieldgroupDeleteObjectV1Response**](EzsignformfieldgroupDeleteObjectV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignformfieldgroup_edit_object_v1**
> EzsignformfieldgroupEditObjectV1Response ezsignformfieldgroup_edit_object_v1(pki_ezsignformfieldgroup_id, ezsignformfieldgroup_edit_object_v1_request)

Edit an existing Ezsignformfieldgroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignformfieldgroup_edit_object_v1_request import EzsignformfieldgroupEditObjectV1Request
from eZmaxApi.models.ezsignformfieldgroup_edit_object_v1_response import EzsignformfieldgroupEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignformfieldgroupApi(api_client)
    pki_ezsignformfieldgroup_id = 56 # int | 
    ezsignformfieldgroup_edit_object_v1_request = eZmaxApi.EzsignformfieldgroupEditObjectV1Request() # EzsignformfieldgroupEditObjectV1Request | 

    try:
        # Edit an existing Ezsignformfieldgroup
        api_response = api_instance.ezsignformfieldgroup_edit_object_v1(pki_ezsignformfieldgroup_id, ezsignformfieldgroup_edit_object_v1_request)
        print("The response of ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignformfieldgroup_id** | **int**|  | 
 **ezsignformfieldgroup_edit_object_v1_request** | [**EzsignformfieldgroupEditObjectV1Request**](EzsignformfieldgroupEditObjectV1Request.md)|  | 

### Return type

[**EzsignformfieldgroupEditObjectV1Response**](EzsignformfieldgroupEditObjectV1Response.md)

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

# **ezsignformfieldgroup_get_object_v2**
> EzsignformfieldgroupGetObjectV2Response ezsignformfieldgroup_get_object_v2(pki_ezsignformfieldgroup_id)

Retrieve an existing Ezsignformfieldgroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignformfieldgroup_get_object_v2_response import EzsignformfieldgroupGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignformfieldgroupApi(api_client)
    pki_ezsignformfieldgroup_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignformfieldgroup
        api_response = api_instance.ezsignformfieldgroup_get_object_v2(pki_ezsignformfieldgroup_id)
        print("The response of ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignformfieldgroupApi->ezsignformfieldgroup_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignformfieldgroup_id** | **int**|  | 

### Return type

[**EzsignformfieldgroupGetObjectV2Response**](EzsignformfieldgroupGetObjectV2Response.md)

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

