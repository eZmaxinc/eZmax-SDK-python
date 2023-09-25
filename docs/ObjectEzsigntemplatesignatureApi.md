# eZmaxApi.ObjectEzsigntemplatesignatureApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatesignature_create_object_v1**](ObjectEzsigntemplatesignatureApi.md#ezsigntemplatesignature_create_object_v1) | **POST** /1/object/ezsigntemplatesignature | Create a new Ezsigntemplatesignature
[**ezsigntemplatesignature_delete_object_v1**](ObjectEzsigntemplatesignatureApi.md#ezsigntemplatesignature_delete_object_v1) | **DELETE** /1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID} | Delete an existing Ezsigntemplatesignature
[**ezsigntemplatesignature_edit_object_v1**](ObjectEzsigntemplatesignatureApi.md#ezsigntemplatesignature_edit_object_v1) | **PUT** /1/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID} | Edit an existing Ezsigntemplatesignature
[**ezsigntemplatesignature_get_object_v2**](ObjectEzsigntemplatesignatureApi.md#ezsigntemplatesignature_get_object_v2) | **GET** /2/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID} | Retrieve an existing Ezsigntemplatesignature


# **ezsigntemplatesignature_create_object_v1**
> EzsigntemplatesignatureCreateObjectV1Response ezsigntemplatesignature_create_object_v1(ezsigntemplatesignature_create_object_v1_request)

Create a new Ezsigntemplatesignature

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesignature_create_object_v1_request import EzsigntemplatesignatureCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatesignature_create_object_v1_response import EzsigntemplatesignatureCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignatureApi(api_client)
    ezsigntemplatesignature_create_object_v1_request = eZmaxApi.EzsigntemplatesignatureCreateObjectV1Request() # EzsigntemplatesignatureCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatesignature
        api_response = api_instance.ezsigntemplatesignature_create_object_v1(ezsigntemplatesignature_create_object_v1_request)
        print("The response of ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_create_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatesignature_create_object_v1_request** | [**EzsigntemplatesignatureCreateObjectV1Request**](EzsigntemplatesignatureCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatesignatureCreateObjectV1Response**](EzsigntemplatesignatureCreateObjectV1Response.md)

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

# **ezsigntemplatesignature_delete_object_v1**
> EzsigntemplatesignatureDeleteObjectV1Response ezsigntemplatesignature_delete_object_v1(pki_ezsigntemplatesignature_id)

Delete an existing Ezsigntemplatesignature



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesignature_delete_object_v1_response import EzsigntemplatesignatureDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignatureApi(api_client)
    pki_ezsigntemplatesignature_id = 56 # int | 

    try:
        # Delete an existing Ezsigntemplatesignature
        api_response = api_instance.ezsigntemplatesignature_delete_object_v1(pki_ezsigntemplatesignature_id)
        print("The response of ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_delete_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesignature_id** | **int**|  | 

### Return type

[**EzsigntemplatesignatureDeleteObjectV1Response**](EzsigntemplatesignatureDeleteObjectV1Response.md)

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

# **ezsigntemplatesignature_edit_object_v1**
> EzsigntemplatesignatureEditObjectV1Response ezsigntemplatesignature_edit_object_v1(pki_ezsigntemplatesignature_id, ezsigntemplatesignature_edit_object_v1_request)

Edit an existing Ezsigntemplatesignature



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesignature_edit_object_v1_request import EzsigntemplatesignatureEditObjectV1Request
from eZmaxApi.models.ezsigntemplatesignature_edit_object_v1_response import EzsigntemplatesignatureEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignatureApi(api_client)
    pki_ezsigntemplatesignature_id = 56 # int | 
    ezsigntemplatesignature_edit_object_v1_request = eZmaxApi.EzsigntemplatesignatureEditObjectV1Request() # EzsigntemplatesignatureEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplatesignature
        api_response = api_instance.ezsigntemplatesignature_edit_object_v1(pki_ezsigntemplatesignature_id, ezsigntemplatesignature_edit_object_v1_request)
        print("The response of ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_edit_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesignature_id** | **int**|  | 
 **ezsigntemplatesignature_edit_object_v1_request** | [**EzsigntemplatesignatureEditObjectV1Request**](EzsigntemplatesignatureEditObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatesignatureEditObjectV1Response**](EzsigntemplatesignatureEditObjectV1Response.md)

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

# **ezsigntemplatesignature_get_object_v2**
> EzsigntemplatesignatureGetObjectV2Response ezsigntemplatesignature_get_object_v2(pki_ezsigntemplatesignature_id)

Retrieve an existing Ezsigntemplatesignature



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesignature_get_object_v2_response import EzsigntemplatesignatureGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignatureApi(api_client)
    pki_ezsigntemplatesignature_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatesignature
        api_response = api_instance.ezsigntemplatesignature_get_object_v2(pki_ezsigntemplatesignature_id)
        print("The response of ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignatureApi->ezsigntemplatesignature_get_object_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesignature_id** | **int**|  | 

### Return type

[**EzsigntemplatesignatureGetObjectV2Response**](EzsigntemplatesignatureGetObjectV2Response.md)

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

