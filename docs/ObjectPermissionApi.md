# eZmaxApi.ObjectPermissionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permission_create_object_v1**](ObjectPermissionApi.md#permission_create_object_v1) | **POST** /1/object/permission | Create a new Permission
[**permission_delete_object_v1**](ObjectPermissionApi.md#permission_delete_object_v1) | **DELETE** /1/object/permission/{pkiPermissionID} | Delete an existing Permission
[**permission_edit_object_v1**](ObjectPermissionApi.md#permission_edit_object_v1) | **PUT** /1/object/permission/{pkiPermissionID} | Edit an existing Permission
[**permission_get_object_v2**](ObjectPermissionApi.md#permission_get_object_v2) | **GET** /2/object/permission/{pkiPermissionID} | Retrieve an existing Permission


# **permission_create_object_v1**
> PermissionCreateObjectV1Response permission_create_object_v1(permission_create_object_v1_request)

Create a new Permission

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.permission_create_object_v1_request import PermissionCreateObjectV1Request
from eZmaxApi.models.permission_create_object_v1_response import PermissionCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectPermissionApi(api_client)
    permission_create_object_v1_request = eZmaxApi.PermissionCreateObjectV1Request() # PermissionCreateObjectV1Request | 

    try:
        # Create a new Permission
        api_response = api_instance.permission_create_object_v1(permission_create_object_v1_request)
        print("The response of ObjectPermissionApi->permission_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPermissionApi->permission_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_create_object_v1_request** | [**PermissionCreateObjectV1Request**](PermissionCreateObjectV1Request.md)|  | 

### Return type

[**PermissionCreateObjectV1Response**](PermissionCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_delete_object_v1**
> CommonResponse permission_delete_object_v1(pki_permission_id)

Delete an existing Permission



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
    api_instance = eZmaxApi.ObjectPermissionApi(api_client)
    pki_permission_id = 56 # int | The unique ID of the Permission

    try:
        # Delete an existing Permission
        api_response = api_instance.permission_delete_object_v1(pki_permission_id)
        print("The response of ObjectPermissionApi->permission_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPermissionApi->permission_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_permission_id** | **int**| The unique ID of the Permission | 

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

# **permission_edit_object_v1**
> CommonResponse permission_edit_object_v1(pki_permission_id, permission_edit_object_v1_request)

Edit an existing Permission



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.permission_edit_object_v1_request import PermissionEditObjectV1Request
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
    api_instance = eZmaxApi.ObjectPermissionApi(api_client)
    pki_permission_id = 56 # int | The unique ID of the Permission
    permission_edit_object_v1_request = eZmaxApi.PermissionEditObjectV1Request() # PermissionEditObjectV1Request | 

    try:
        # Edit an existing Permission
        api_response = api_instance.permission_edit_object_v1(pki_permission_id, permission_edit_object_v1_request)
        print("The response of ObjectPermissionApi->permission_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPermissionApi->permission_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_permission_id** | **int**| The unique ID of the Permission | 
 **permission_edit_object_v1_request** | [**PermissionEditObjectV1Request**](PermissionEditObjectV1Request.md)|  | 

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

# **permission_get_object_v2**
> PermissionGetObjectV2Response permission_get_object_v2(pki_permission_id)

Retrieve an existing Permission



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.permission_get_object_v2_response import PermissionGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectPermissionApi(api_client)
    pki_permission_id = 56 # int | The unique ID of the Permission

    try:
        # Retrieve an existing Permission
        api_response = api_instance.permission_get_object_v2(pki_permission_id)
        print("The response of ObjectPermissionApi->permission_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectPermissionApi->permission_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_permission_id** | **int**| The unique ID of the Permission | 

### Return type

[**PermissionGetObjectV2Response**](PermissionGetObjectV2Response.md)

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

