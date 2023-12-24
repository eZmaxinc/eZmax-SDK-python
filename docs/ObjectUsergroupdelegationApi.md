# eZmaxApi.ObjectUsergroupdelegationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroupdelegation_create_object_v1**](ObjectUsergroupdelegationApi.md#usergroupdelegation_create_object_v1) | **POST** /1/object/usergroupdelegation | Create a new Usergroupdelegation
[**usergroupdelegation_delete_object_v1**](ObjectUsergroupdelegationApi.md#usergroupdelegation_delete_object_v1) | **DELETE** /1/object/usergroupdelegation/{pkiUsergroupdelegationID} | Delete an existing Usergroupdelegation
[**usergroupdelegation_edit_object_v1**](ObjectUsergroupdelegationApi.md#usergroupdelegation_edit_object_v1) | **PUT** /1/object/usergroupdelegation/{pkiUsergroupdelegationID} | Edit an existing Usergroupdelegation
[**usergroupdelegation_get_object_v2**](ObjectUsergroupdelegationApi.md#usergroupdelegation_get_object_v2) | **GET** /2/object/usergroupdelegation/{pkiUsergroupdelegationID} | Retrieve an existing Usergroupdelegation


# **usergroupdelegation_create_object_v1**
> UsergroupdelegationCreateObjectV1Response usergroupdelegation_create_object_v1(usergroupdelegation_create_object_v1_request)

Create a new Usergroupdelegation

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.usergroupdelegation_create_object_v1_request import UsergroupdelegationCreateObjectV1Request
from eZmaxApi.models.usergroupdelegation_create_object_v1_response import UsergroupdelegationCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupdelegationApi(api_client)
    usergroupdelegation_create_object_v1_request = eZmaxApi.UsergroupdelegationCreateObjectV1Request() # UsergroupdelegationCreateObjectV1Request | 

    try:
        # Create a new Usergroupdelegation
        api_response = api_instance.usergroupdelegation_create_object_v1(usergroupdelegation_create_object_v1_request)
        print("The response of ObjectUsergroupdelegationApi->usergroupdelegation_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupdelegationApi->usergroupdelegation_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupdelegation_create_object_v1_request** | [**UsergroupdelegationCreateObjectV1Request**](UsergroupdelegationCreateObjectV1Request.md)|  | 

### Return type

[**UsergroupdelegationCreateObjectV1Response**](UsergroupdelegationCreateObjectV1Response.md)

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

# **usergroupdelegation_delete_object_v1**
> UsergroupdelegationDeleteObjectV1Response usergroupdelegation_delete_object_v1(pki_usergroupdelegation_id)

Delete an existing Usergroupdelegation



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.usergroupdelegation_delete_object_v1_response import UsergroupdelegationDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupdelegationApi(api_client)
    pki_usergroupdelegation_id = 56 # int | The unique ID of the Usergroupdelegation

    try:
        # Delete an existing Usergroupdelegation
        api_response = api_instance.usergroupdelegation_delete_object_v1(pki_usergroupdelegation_id)
        print("The response of ObjectUsergroupdelegationApi->usergroupdelegation_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupdelegationApi->usergroupdelegation_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupdelegation_id** | **int**| The unique ID of the Usergroupdelegation | 

### Return type

[**UsergroupdelegationDeleteObjectV1Response**](UsergroupdelegationDeleteObjectV1Response.md)

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

# **usergroupdelegation_edit_object_v1**
> UsergroupdelegationEditObjectV1Response usergroupdelegation_edit_object_v1(pki_usergroupdelegation_id, usergroupdelegation_edit_object_v1_request)

Edit an existing Usergroupdelegation



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.usergroupdelegation_edit_object_v1_request import UsergroupdelegationEditObjectV1Request
from eZmaxApi.models.usergroupdelegation_edit_object_v1_response import UsergroupdelegationEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupdelegationApi(api_client)
    pki_usergroupdelegation_id = 56 # int | The unique ID of the Usergroupdelegation
    usergroupdelegation_edit_object_v1_request = eZmaxApi.UsergroupdelegationEditObjectV1Request() # UsergroupdelegationEditObjectV1Request | 

    try:
        # Edit an existing Usergroupdelegation
        api_response = api_instance.usergroupdelegation_edit_object_v1(pki_usergroupdelegation_id, usergroupdelegation_edit_object_v1_request)
        print("The response of ObjectUsergroupdelegationApi->usergroupdelegation_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupdelegationApi->usergroupdelegation_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupdelegation_id** | **int**| The unique ID of the Usergroupdelegation | 
 **usergroupdelegation_edit_object_v1_request** | [**UsergroupdelegationEditObjectV1Request**](UsergroupdelegationEditObjectV1Request.md)|  | 

### Return type

[**UsergroupdelegationEditObjectV1Response**](UsergroupdelegationEditObjectV1Response.md)

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

# **usergroupdelegation_get_object_v2**
> UsergroupdelegationGetObjectV2Response usergroupdelegation_get_object_v2(pki_usergroupdelegation_id)

Retrieve an existing Usergroupdelegation



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.usergroupdelegation_get_object_v2_response import UsergroupdelegationGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectUsergroupdelegationApi(api_client)
    pki_usergroupdelegation_id = 56 # int | The unique ID of the Usergroupdelegation

    try:
        # Retrieve an existing Usergroupdelegation
        api_response = api_instance.usergroupdelegation_get_object_v2(pki_usergroupdelegation_id)
        print("The response of ObjectUsergroupdelegationApi->usergroupdelegation_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupdelegationApi->usergroupdelegation_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupdelegation_id** | **int**| The unique ID of the Usergroupdelegation | 

### Return type

[**UsergroupdelegationGetObjectV2Response**](UsergroupdelegationGetObjectV2Response.md)

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

