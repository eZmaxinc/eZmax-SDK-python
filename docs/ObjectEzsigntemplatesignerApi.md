# eZmaxApi.ObjectEzsigntemplatesignerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatesigner_create_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_create_object_v1) | **POST** /1/object/ezsigntemplatesigner | Create a new Ezsigntemplatesigner
[**ezsigntemplatesigner_delete_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_delete_object_v1) | **DELETE** /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID} | Delete an existing Ezsigntemplatesigner
[**ezsigntemplatesigner_edit_object_v1**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_edit_object_v1) | **PUT** /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID} | Edit an existing Ezsigntemplatesigner
[**ezsigntemplatesigner_get_object_v2**](ObjectEzsigntemplatesignerApi.md#ezsigntemplatesigner_get_object_v2) | **GET** /2/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID} | Retrieve an existing Ezsigntemplatesigner


# **ezsigntemplatesigner_create_object_v1**
> EzsigntemplatesignerCreateObjectV1Response ezsigntemplatesigner_create_object_v1(ezsigntemplatesigner_create_object_v1_request)

Create a new Ezsigntemplatesigner

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesigner_create_object_v1_request import EzsigntemplatesignerCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatesigner_create_object_v1_response import EzsigntemplatesignerCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignerApi(api_client)
    ezsigntemplatesigner_create_object_v1_request = eZmaxApi.EzsigntemplatesignerCreateObjectV1Request() # EzsigntemplatesignerCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_create_object_v1(ezsigntemplatesigner_create_object_v1_request)
        print("The response of ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatesigner_create_object_v1_request** | [**EzsigntemplatesignerCreateObjectV1Request**](EzsigntemplatesignerCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatesignerCreateObjectV1Response**](EzsigntemplatesignerCreateObjectV1Response.md)

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

# **ezsigntemplatesigner_delete_object_v1**
> EzsigntemplatesignerDeleteObjectV1Response ezsigntemplatesigner_delete_object_v1(pki_ezsigntemplatesigner_id)

Delete an existing Ezsigntemplatesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesigner_delete_object_v1_response import EzsigntemplatesignerDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignerApi(api_client)
    pki_ezsigntemplatesigner_id = 56 # int | 

    try:
        # Delete an existing Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_delete_object_v1(pki_ezsigntemplatesigner_id)
        print("The response of ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesigner_id** | **int**|  | 

### Return type

[**EzsigntemplatesignerDeleteObjectV1Response**](EzsigntemplatesignerDeleteObjectV1Response.md)

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

# **ezsigntemplatesigner_edit_object_v1**
> EzsigntemplatesignerEditObjectV1Response ezsigntemplatesigner_edit_object_v1(pki_ezsigntemplatesigner_id, ezsigntemplatesigner_edit_object_v1_request)

Edit an existing Ezsigntemplatesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesigner_edit_object_v1_request import EzsigntemplatesignerEditObjectV1Request
from eZmaxApi.models.ezsigntemplatesigner_edit_object_v1_response import EzsigntemplatesignerEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignerApi(api_client)
    pki_ezsigntemplatesigner_id = 56 # int | 
    ezsigntemplatesigner_edit_object_v1_request = eZmaxApi.EzsigntemplatesignerEditObjectV1Request() # EzsigntemplatesignerEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_edit_object_v1(pki_ezsigntemplatesigner_id, ezsigntemplatesigner_edit_object_v1_request)
        print("The response of ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesigner_id** | **int**|  | 
 **ezsigntemplatesigner_edit_object_v1_request** | [**EzsigntemplatesignerEditObjectV1Request**](EzsigntemplatesignerEditObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatesignerEditObjectV1Response**](EzsigntemplatesignerEditObjectV1Response.md)

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

# **ezsigntemplatesigner_get_object_v2**
> EzsigntemplatesignerGetObjectV2Response ezsigntemplatesigner_get_object_v2(pki_ezsigntemplatesigner_id)

Retrieve an existing Ezsigntemplatesigner



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatesigner_get_object_v2_response import EzsigntemplatesignerGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatesignerApi(api_client)
    pki_ezsigntemplatesigner_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatesigner
        api_response = api_instance.ezsigntemplatesigner_get_object_v2(pki_ezsigntemplatesigner_id)
        print("The response of ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatesignerApi->ezsigntemplatesigner_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatesigner_id** | **int**|  | 

### Return type

[**EzsigntemplatesignerGetObjectV2Response**](EzsigntemplatesignerGetObjectV2Response.md)

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

