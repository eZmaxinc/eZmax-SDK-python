# eZmaxApi.ObjectCorsApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cors_create_object_v1**](ObjectCorsApi.md#cors_create_object_v1) | **POST** /1/object/cors | Create a new Cors
[**cors_delete_object_v1**](ObjectCorsApi.md#cors_delete_object_v1) | **DELETE** /1/object/cors/{pkiCorsID} | Delete an existing Cors
[**cors_edit_object_v1**](ObjectCorsApi.md#cors_edit_object_v1) | **PUT** /1/object/cors/{pkiCorsID} | Edit an existing Cors
[**cors_get_object_v2**](ObjectCorsApi.md#cors_get_object_v2) | **GET** /2/object/cors/{pkiCorsID} | Retrieve an existing Cors


# **cors_create_object_v1**
> CorsCreateObjectV1Response cors_create_object_v1(cors_create_object_v1_request)

Create a new Cors

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.cors_create_object_v1_request import CorsCreateObjectV1Request
from eZmaxApi.models.cors_create_object_v1_response import CorsCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectCorsApi(api_client)
    cors_create_object_v1_request = eZmaxApi.CorsCreateObjectV1Request() # CorsCreateObjectV1Request | 

    try:
        # Create a new Cors
        api_response = api_instance.cors_create_object_v1(cors_create_object_v1_request)
        print("The response of ObjectCorsApi->cors_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCorsApi->cors_create_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cors_create_object_v1_request** | [**CorsCreateObjectV1Request**](CorsCreateObjectV1Request.md)|  | 

### Return type

[**CorsCreateObjectV1Response**](CorsCreateObjectV1Response.md)

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

# **cors_delete_object_v1**
> CorsDeleteObjectV1Response cors_delete_object_v1(pki_cors_id)

Delete an existing Cors



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.cors_delete_object_v1_response import CorsDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectCorsApi(api_client)
    pki_cors_id = 56 # int | The unique ID of the Cors

    try:
        # Delete an existing Cors
        api_response = api_instance.cors_delete_object_v1(pki_cors_id)
        print("The response of ObjectCorsApi->cors_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCorsApi->cors_delete_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_cors_id** | **int**| The unique ID of the Cors | 

### Return type

[**CorsDeleteObjectV1Response**](CorsDeleteObjectV1Response.md)

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

# **cors_edit_object_v1**
> CorsEditObjectV1Response cors_edit_object_v1(pki_cors_id, cors_edit_object_v1_request)

Edit an existing Cors



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.cors_edit_object_v1_request import CorsEditObjectV1Request
from eZmaxApi.models.cors_edit_object_v1_response import CorsEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectCorsApi(api_client)
    pki_cors_id = 56 # int | The unique ID of the Cors
    cors_edit_object_v1_request = eZmaxApi.CorsEditObjectV1Request() # CorsEditObjectV1Request | 

    try:
        # Edit an existing Cors
        api_response = api_instance.cors_edit_object_v1(pki_cors_id, cors_edit_object_v1_request)
        print("The response of ObjectCorsApi->cors_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCorsApi->cors_edit_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_cors_id** | **int**| The unique ID of the Cors | 
 **cors_edit_object_v1_request** | [**CorsEditObjectV1Request**](CorsEditObjectV1Request.md)|  | 

### Return type

[**CorsEditObjectV1Response**](CorsEditObjectV1Response.md)

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

# **cors_get_object_v2**
> CorsGetObjectV2Response cors_get_object_v2(pki_cors_id)

Retrieve an existing Cors



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.cors_get_object_v2_response import CorsGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectCorsApi(api_client)
    pki_cors_id = 56 # int | The unique ID of the Cors

    try:
        # Retrieve an existing Cors
        api_response = api_instance.cors_get_object_v2(pki_cors_id)
        print("The response of ObjectCorsApi->cors_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCorsApi->cors_get_object_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_cors_id** | **int**| The unique ID of the Cors | 

### Return type

[**CorsGetObjectV2Response**](CorsGetObjectV2Response.md)

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

