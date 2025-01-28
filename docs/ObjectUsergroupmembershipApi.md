# eZmaxApi.ObjectUsergroupmembershipApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroupmembership_create_object_v1**](ObjectUsergroupmembershipApi.md#usergroupmembership_create_object_v1) | **POST** /1/object/usergroupmembership | Create a new Usergroupmembership
[**usergroupmembership_delete_object_v1**](ObjectUsergroupmembershipApi.md#usergroupmembership_delete_object_v1) | **DELETE** /1/object/usergroupmembership/{pkiUsergroupmembershipID} | Delete an existing Usergroupmembership
[**usergroupmembership_edit_object_v1**](ObjectUsergroupmembershipApi.md#usergroupmembership_edit_object_v1) | **PUT** /1/object/usergroupmembership/{pkiUsergroupmembershipID} | Edit an existing Usergroupmembership
[**usergroupmembership_get_object_v2**](ObjectUsergroupmembershipApi.md#usergroupmembership_get_object_v2) | **GET** /2/object/usergroupmembership/{pkiUsergroupmembershipID} | Retrieve an existing Usergroupmembership


# **usergroupmembership_create_object_v1**
> UsergroupmembershipCreateObjectV1Response usergroupmembership_create_object_v1(usergroupmembership_create_object_v1_request)

Create a new Usergroupmembership

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupmembership_create_object_v1_request import UsergroupmembershipCreateObjectV1Request
from eZmaxApi.models.usergroupmembership_create_object_v1_response import UsergroupmembershipCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupmembershipApi(api_client)
    usergroupmembership_create_object_v1_request = eZmaxApi.UsergroupmembershipCreateObjectV1Request() # UsergroupmembershipCreateObjectV1Request | 

    try:
        # Create a new Usergroupmembership
        api_response = api_instance.usergroupmembership_create_object_v1(usergroupmembership_create_object_v1_request)
        print("The response of ObjectUsergroupmembershipApi->usergroupmembership_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupmembershipApi->usergroupmembership_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroupmembership_create_object_v1_request** | [**UsergroupmembershipCreateObjectV1Request**](UsergroupmembershipCreateObjectV1Request.md)|  | 

### Return type

[**UsergroupmembershipCreateObjectV1Response**](UsergroupmembershipCreateObjectV1Response.md)

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

# **usergroupmembership_delete_object_v1**
> UsergroupmembershipDeleteObjectV1Response usergroupmembership_delete_object_v1(pki_usergroupmembership_id)

Delete an existing Usergroupmembership



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupmembership_delete_object_v1_response import UsergroupmembershipDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupmembershipApi(api_client)
    pki_usergroupmembership_id = 56 # int | 

    try:
        # Delete an existing Usergroupmembership
        api_response = api_instance.usergroupmembership_delete_object_v1(pki_usergroupmembership_id)
        print("The response of ObjectUsergroupmembershipApi->usergroupmembership_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupmembershipApi->usergroupmembership_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupmembership_id** | **int**|  | 

### Return type

[**UsergroupmembershipDeleteObjectV1Response**](UsergroupmembershipDeleteObjectV1Response.md)

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

# **usergroupmembership_edit_object_v1**
> UsergroupmembershipEditObjectV1Response usergroupmembership_edit_object_v1(pki_usergroupmembership_id, usergroupmembership_edit_object_v1_request)

Edit an existing Usergroupmembership



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupmembership_edit_object_v1_request import UsergroupmembershipEditObjectV1Request
from eZmaxApi.models.usergroupmembership_edit_object_v1_response import UsergroupmembershipEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupmembershipApi(api_client)
    pki_usergroupmembership_id = 56 # int | 
    usergroupmembership_edit_object_v1_request = eZmaxApi.UsergroupmembershipEditObjectV1Request() # UsergroupmembershipEditObjectV1Request | 

    try:
        # Edit an existing Usergroupmembership
        api_response = api_instance.usergroupmembership_edit_object_v1(pki_usergroupmembership_id, usergroupmembership_edit_object_v1_request)
        print("The response of ObjectUsergroupmembershipApi->usergroupmembership_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupmembershipApi->usergroupmembership_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupmembership_id** | **int**|  | 
 **usergroupmembership_edit_object_v1_request** | [**UsergroupmembershipEditObjectV1Request**](UsergroupmembershipEditObjectV1Request.md)|  | 

### Return type

[**UsergroupmembershipEditObjectV1Response**](UsergroupmembershipEditObjectV1Response.md)

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

# **usergroupmembership_get_object_v2**
> UsergroupmembershipGetObjectV2Response usergroupmembership_get_object_v2(pki_usergroupmembership_id)

Retrieve an existing Usergroupmembership



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroupmembership_get_object_v2_response import UsergroupmembershipGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectUsergroupmembershipApi(api_client)
    pki_usergroupmembership_id = 56 # int | 

    try:
        # Retrieve an existing Usergroupmembership
        api_response = api_instance.usergroupmembership_get_object_v2(pki_usergroupmembership_id)
        print("The response of ObjectUsergroupmembershipApi->usergroupmembership_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupmembershipApi->usergroupmembership_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroupmembership_id** | **int**|  | 

### Return type

[**UsergroupmembershipGetObjectV2Response**](UsergroupmembershipGetObjectV2Response.md)

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

