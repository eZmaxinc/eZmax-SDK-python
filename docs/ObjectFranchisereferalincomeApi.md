# eZmaxApi.ObjectFranchisereferalincomeApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchisereferalincome_create_object_v1**](ObjectFranchisereferalincomeApi.md#franchisereferalincome_create_object_v1) | **POST** /1/object/franchisereferalincome | Create a new Franchisereferalincome
[**franchisereferalincome_create_object_v2**](ObjectFranchisereferalincomeApi.md#franchisereferalincome_create_object_v2) | **POST** /2/object/franchisereferalincome | Create a new Franchisereferalincome


# **franchisereferalincome_create_object_v1**
> FranchisereferalincomeCreateObjectV1Response franchisereferalincome_create_object_v1(franchisereferalincome_create_object_v1_request)

Create a new Franchisereferalincome

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.franchisereferalincome_create_object_v1_request import FranchisereferalincomeCreateObjectV1Request
from eZmaxApi.models.franchisereferalincome_create_object_v1_response import FranchisereferalincomeCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectFranchisereferalincomeApi(api_client)
    franchisereferalincome_create_object_v1_request = [eZmaxApi.FranchisereferalincomeCreateObjectV1Request()] # List[FranchisereferalincomeCreateObjectV1Request] | 

    try:
        # Create a new Franchisereferalincome
        api_response = api_instance.franchisereferalincome_create_object_v1(franchisereferalincome_create_object_v1_request)
        print("The response of ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **franchisereferalincome_create_object_v1_request** | [**List[FranchisereferalincomeCreateObjectV1Request]**](FranchisereferalincomeCreateObjectV1Request.md)|  | 

### Return type

[**FranchisereferalincomeCreateObjectV1Response**](FranchisereferalincomeCreateObjectV1Response.md)

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

# **franchisereferalincome_create_object_v2**
> FranchisereferalincomeCreateObjectV2Response franchisereferalincome_create_object_v2(franchisereferalincome_create_object_v2_request)

Create a new Franchisereferalincome

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.franchisereferalincome_create_object_v2_request import FranchisereferalincomeCreateObjectV2Request
from eZmaxApi.models.franchisereferalincome_create_object_v2_response import FranchisereferalincomeCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectFranchisereferalincomeApi(api_client)
    franchisereferalincome_create_object_v2_request = eZmaxApi.FranchisereferalincomeCreateObjectV2Request() # FranchisereferalincomeCreateObjectV2Request | 

    try:
        # Create a new Franchisereferalincome
        api_response = api_instance.franchisereferalincome_create_object_v2(franchisereferalincome_create_object_v2_request)
        print("The response of ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **franchisereferalincome_create_object_v2_request** | [**FranchisereferalincomeCreateObjectV2Request**](FranchisereferalincomeCreateObjectV2Request.md)|  | 

### Return type

[**FranchisereferalincomeCreateObjectV2Response**](FranchisereferalincomeCreateObjectV2Response.md)

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

