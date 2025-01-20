# eZmaxApi.ObjectSubnetApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subnet_create_object_v1**](ObjectSubnetApi.md#subnet_create_object_v1) | **POST** /1/object/subnet | Create a new Subnet
[**subnet_delete_object_v1**](ObjectSubnetApi.md#subnet_delete_object_v1) | **DELETE** /1/object/subnet/{pkiSubnetID} | Delete an existing Subnet
[**subnet_edit_object_v1**](ObjectSubnetApi.md#subnet_edit_object_v1) | **PUT** /1/object/subnet/{pkiSubnetID} | Edit an existing Subnet
[**subnet_get_object_v2**](ObjectSubnetApi.md#subnet_get_object_v2) | **GET** /2/object/subnet/{pkiSubnetID} | Retrieve an existing Subnet


# **subnet_create_object_v1**
> SubnetCreateObjectV1Response subnet_create_object_v1(subnet_create_object_v1_request)

Create a new Subnet

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.subnet_create_object_v1_request import SubnetCreateObjectV1Request
from eZmaxApi.models.subnet_create_object_v1_response import SubnetCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectSubnetApi(api_client)
    subnet_create_object_v1_request = eZmaxApi.SubnetCreateObjectV1Request() # SubnetCreateObjectV1Request | 

    try:
        # Create a new Subnet
        api_response = api_instance.subnet_create_object_v1(subnet_create_object_v1_request)
        print("The response of ObjectSubnetApi->subnet_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSubnetApi->subnet_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_create_object_v1_request** | [**SubnetCreateObjectV1Request**](SubnetCreateObjectV1Request.md)|  | 

### Return type

[**SubnetCreateObjectV1Response**](SubnetCreateObjectV1Response.md)

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

# **subnet_delete_object_v1**
> CommonResponse subnet_delete_object_v1(pki_subnet_id)

Delete an existing Subnet



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
    api_instance = eZmaxApi.ObjectSubnetApi(api_client)
    pki_subnet_id = 56 # int | The unique ID of the Subnet

    try:
        # Delete an existing Subnet
        api_response = api_instance.subnet_delete_object_v1(pki_subnet_id)
        print("The response of ObjectSubnetApi->subnet_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSubnetApi->subnet_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_subnet_id** | **int**| The unique ID of the Subnet | 

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subnet_edit_object_v1**
> CommonResponse subnet_edit_object_v1(pki_subnet_id, subnet_edit_object_v1_request)

Edit an existing Subnet



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.subnet_edit_object_v1_request import SubnetEditObjectV1Request
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
    api_instance = eZmaxApi.ObjectSubnetApi(api_client)
    pki_subnet_id = 56 # int | The unique ID of the Subnet
    subnet_edit_object_v1_request = eZmaxApi.SubnetEditObjectV1Request() # SubnetEditObjectV1Request | 

    try:
        # Edit an existing Subnet
        api_response = api_instance.subnet_edit_object_v1(pki_subnet_id, subnet_edit_object_v1_request)
        print("The response of ObjectSubnetApi->subnet_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSubnetApi->subnet_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_subnet_id** | **int**| The unique ID of the Subnet | 
 **subnet_edit_object_v1_request** | [**SubnetEditObjectV1Request**](SubnetEditObjectV1Request.md)|  | 

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

# **subnet_get_object_v2**
> SubnetGetObjectV2Response subnet_get_object_v2(pki_subnet_id)

Retrieve an existing Subnet



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.subnet_get_object_v2_response import SubnetGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectSubnetApi(api_client)
    pki_subnet_id = 56 # int | The unique ID of the Subnet

    try:
        # Retrieve an existing Subnet
        api_response = api_instance.subnet_get_object_v2(pki_subnet_id)
        print("The response of ObjectSubnetApi->subnet_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSubnetApi->subnet_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_subnet_id** | **int**| The unique ID of the Subnet | 

### Return type

[**SubnetGetObjectV2Response**](SubnetGetObjectV2Response.md)

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

