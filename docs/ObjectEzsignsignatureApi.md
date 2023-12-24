# eZmaxApi.ObjectEzsignsignatureApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignsignature_create_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_create_object_v1) | **POST** /1/object/ezsignsignature | Create a new Ezsignsignature
[**ezsignsignature_create_object_v2**](ObjectEzsignsignatureApi.md#ezsignsignature_create_object_v2) | **POST** /2/object/ezsignsignature | Create a new Ezsignsignature
[**ezsignsignature_delete_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_delete_object_v1) | **DELETE** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Delete an existing Ezsignsignature
[**ezsignsignature_edit_object_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_edit_object_v1) | **PUT** /1/object/ezsignsignature/{pkiEzsignsignatureID} | Edit an existing Ezsignsignature
[**ezsignsignature_get_ezsignsignatureattachment_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_get_ezsignsignatureattachment_v1) | **GET** /1/object/ezsignsignature/{pkiEzsignsignatureID}/getEzsignsignatureattachment | Retrieve an existing Ezsignsignature&#39;s Ezsignsignatureattachments
[**ezsignsignature_get_ezsignsignatures_automatic_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_get_ezsignsignatures_automatic_v1) | **GET** /1/object/ezsignsignature/getEzsignsignaturesAutomatic | Retrieve all automatic Ezsignsignatures
[**ezsignsignature_get_object_v2**](ObjectEzsignsignatureApi.md#ezsignsignature_get_object_v2) | **GET** /2/object/ezsignsignature/{pkiEzsignsignatureID} | Retrieve an existing Ezsignsignature
[**ezsignsignature_sign_v1**](ObjectEzsignsignatureApi.md#ezsignsignature_sign_v1) | **POST** /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign | Sign the Ezsignsignature


# **ezsignsignature_create_object_v1**
> EzsignsignatureCreateObjectV1Response ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request)

Create a new Ezsignsignature

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_create_object_v1_request import EzsignsignatureCreateObjectV1Request
from eZmaxApi.models.ezsignsignature_create_object_v1_response import EzsignsignatureCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    ezsignsignature_create_object_v1_request = [eZmaxApi.EzsignsignatureCreateObjectV1Request()] # List[EzsignsignatureCreateObjectV1Request] | 

    try:
        # Create a new Ezsignsignature
        api_response = api_instance.ezsignsignature_create_object_v1(ezsignsignature_create_object_v1_request)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignsignature_create_object_v1_request** | [**List[EzsignsignatureCreateObjectV1Request]**](EzsignsignatureCreateObjectV1Request.md)|  | 

### Return type

[**EzsignsignatureCreateObjectV1Response**](EzsignsignatureCreateObjectV1Response.md)

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

# **ezsignsignature_create_object_v2**
> EzsignsignatureCreateObjectV2Response ezsignsignature_create_object_v2(ezsignsignature_create_object_v2_request)

Create a new Ezsignsignature

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_create_object_v2_request import EzsignsignatureCreateObjectV2Request
from eZmaxApi.models.ezsignsignature_create_object_v2_response import EzsignsignatureCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    ezsignsignature_create_object_v2_request = eZmaxApi.EzsignsignatureCreateObjectV2Request() # EzsignsignatureCreateObjectV2Request | 

    try:
        # Create a new Ezsignsignature
        api_response = api_instance.ezsignsignature_create_object_v2(ezsignsignature_create_object_v2_request)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignsignature_create_object_v2_request** | [**EzsignsignatureCreateObjectV2Request**](EzsignsignatureCreateObjectV2Request.md)|  | 

### Return type

[**EzsignsignatureCreateObjectV2Response**](EzsignsignatureCreateObjectV2Response.md)

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

# **ezsignsignature_delete_object_v1**
> EzsignsignatureDeleteObjectV1Response ezsignsignature_delete_object_v1(pki_ezsignsignature_id)

Delete an existing Ezsignsignature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_delete_object_v1_response import EzsignsignatureDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 56 # int | 

    try:
        # Delete an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_delete_object_v1(pki_ezsignsignature_id)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  | 

### Return type

[**EzsignsignatureDeleteObjectV1Response**](EzsignsignatureDeleteObjectV1Response.md)

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

# **ezsignsignature_edit_object_v1**
> EzsignsignatureEditObjectV1Response ezsignsignature_edit_object_v1(pki_ezsignsignature_id, ezsignsignature_edit_object_v1_request)

Edit an existing Ezsignsignature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_edit_object_v1_request import EzsignsignatureEditObjectV1Request
from eZmaxApi.models.ezsignsignature_edit_object_v1_response import EzsignsignatureEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 56 # int | 
    ezsignsignature_edit_object_v1_request = eZmaxApi.EzsignsignatureEditObjectV1Request() # EzsignsignatureEditObjectV1Request | 

    try:
        # Edit an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_edit_object_v1(pki_ezsignsignature_id, ezsignsignature_edit_object_v1_request)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  | 
 **ezsignsignature_edit_object_v1_request** | [**EzsignsignatureEditObjectV1Request**](EzsignsignatureEditObjectV1Request.md)|  | 

### Return type

[**EzsignsignatureEditObjectV1Response**](EzsignsignatureEditObjectV1Response.md)

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

# **ezsignsignature_get_ezsignsignatureattachment_v1**
> EzsignsignatureGetEzsignsignatureattachmentV1Response ezsignsignature_get_ezsignsignatureattachment_v1(pki_ezsignsignature_id)

Retrieve an existing Ezsignsignature's Ezsignsignatureattachments

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_get_ezsignsignatureattachment_v1_response import EzsignsignatureGetEzsignsignatureattachmentV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignsignature's Ezsignsignatureattachments
        api_response = api_instance.ezsignsignature_get_ezsignsignatureattachment_v1(pki_ezsignsignature_id)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_get_ezsignsignatureattachment_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_get_ezsignsignatureattachment_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  | 

### Return type

[**EzsignsignatureGetEzsignsignatureattachmentV1Response**](EzsignsignatureGetEzsignsignatureattachmentV1Response.md)

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

# **ezsignsignature_get_ezsignsignatures_automatic_v1**
> EzsignsignatureGetEzsignsignaturesAutomaticV1Response ezsignsignature_get_ezsignsignatures_automatic_v1()

Retrieve all automatic Ezsignsignatures

Return all the Ezsignsignatures that can be signed by the current user

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_get_ezsignsignatures_automatic_v1_response import EzsignsignatureGetEzsignsignaturesAutomaticV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)

    try:
        # Retrieve all automatic Ezsignsignatures
        api_response = api_instance.ezsignsignature_get_ezsignsignatures_automatic_v1()
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_get_ezsignsignatures_automatic_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_get_ezsignsignatures_automatic_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EzsignsignatureGetEzsignsignaturesAutomaticV1Response**](EzsignsignatureGetEzsignsignaturesAutomaticV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignsignature_get_object_v2**
> EzsignsignatureGetObjectV2Response ezsignsignature_get_object_v2(pki_ezsignsignature_id)

Retrieve an existing Ezsignsignature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_get_object_v2_response import EzsignsignatureGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignsignature
        api_response = api_instance.ezsignsignature_get_object_v2(pki_ezsignsignature_id)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  | 

### Return type

[**EzsignsignatureGetObjectV2Response**](EzsignsignatureGetObjectV2Response.md)

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

# **ezsignsignature_sign_v1**
> EzsignsignatureSignV1Response ezsignsignature_sign_v1(pki_ezsignsignature_id, ezsignsignature_sign_v1_request)

Sign the Ezsignsignature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignature_sign_v1_request import EzsignsignatureSignV1Request
from eZmaxApi.models.ezsignsignature_sign_v1_response import EzsignsignatureSignV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignatureApi(api_client)
    pki_ezsignsignature_id = 56 # int | 
    ezsignsignature_sign_v1_request = eZmaxApi.EzsignsignatureSignV1Request() # EzsignsignatureSignV1Request | 

    try:
        # Sign the Ezsignsignature
        api_response = api_instance.ezsignsignature_sign_v1(pki_ezsignsignature_id, ezsignsignature_sign_v1_request)
        print("The response of ObjectEzsignsignatureApi->ezsignsignature_sign_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignatureApi->ezsignsignature_sign_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignature_id** | **int**|  | 
 **ezsignsignature_sign_v1_request** | [**EzsignsignatureSignV1Request**](EzsignsignatureSignV1Request.md)|  | 

### Return type

[**EzsignsignatureSignV1Response**](EzsignsignatureSignV1Response.md)

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

