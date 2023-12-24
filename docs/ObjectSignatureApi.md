# eZmaxApi.ObjectSignatureApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signature_create_object_v1**](ObjectSignatureApi.md#signature_create_object_v1) | **POST** /1/object/signature | Create a new Signature
[**signature_delete_object_v1**](ObjectSignatureApi.md#signature_delete_object_v1) | **DELETE** /1/object/signature/{pkiSignatureID} | Delete an existing Signature
[**signature_edit_object_v1**](ObjectSignatureApi.md#signature_edit_object_v1) | **PUT** /1/object/signature/{pkiSignatureID} | Edit an existing Signature
[**signature_get_object_v2**](ObjectSignatureApi.md#signature_get_object_v2) | **GET** /2/object/signature/{pkiSignatureID} | Retrieve an existing Signature


# **signature_create_object_v1**
> SignatureCreateObjectV1Response signature_create_object_v1(signature_create_object_v1_request)

Create a new Signature

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.signature_create_object_v1_request import SignatureCreateObjectV1Request
from eZmaxApi.models.signature_create_object_v1_response import SignatureCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectSignatureApi(api_client)
    signature_create_object_v1_request = eZmaxApi.SignatureCreateObjectV1Request() # SignatureCreateObjectV1Request | 

    try:
        # Create a new Signature
        api_response = api_instance.signature_create_object_v1(signature_create_object_v1_request)
        print("The response of ObjectSignatureApi->signature_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSignatureApi->signature_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_create_object_v1_request** | [**SignatureCreateObjectV1Request**](SignatureCreateObjectV1Request.md)|  | 

### Return type

[**SignatureCreateObjectV1Response**](SignatureCreateObjectV1Response.md)

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

# **signature_delete_object_v1**
> SignatureDeleteObjectV1Response signature_delete_object_v1(pki_signature_id)

Delete an existing Signature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.signature_delete_object_v1_response import SignatureDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectSignatureApi(api_client)
    pki_signature_id = 56 # int | The unique ID of the Signature

    try:
        # Delete an existing Signature
        api_response = api_instance.signature_delete_object_v1(pki_signature_id)
        print("The response of ObjectSignatureApi->signature_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSignatureApi->signature_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_signature_id** | **int**| The unique ID of the Signature | 

### Return type

[**SignatureDeleteObjectV1Response**](SignatureDeleteObjectV1Response.md)

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

# **signature_edit_object_v1**
> SignatureEditObjectV1Response signature_edit_object_v1(pki_signature_id, signature_edit_object_v1_request)

Edit an existing Signature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.signature_edit_object_v1_request import SignatureEditObjectV1Request
from eZmaxApi.models.signature_edit_object_v1_response import SignatureEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectSignatureApi(api_client)
    pki_signature_id = 56 # int | The unique ID of the Signature
    signature_edit_object_v1_request = eZmaxApi.SignatureEditObjectV1Request() # SignatureEditObjectV1Request | 

    try:
        # Edit an existing Signature
        api_response = api_instance.signature_edit_object_v1(pki_signature_id, signature_edit_object_v1_request)
        print("The response of ObjectSignatureApi->signature_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSignatureApi->signature_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_signature_id** | **int**| The unique ID of the Signature | 
 **signature_edit_object_v1_request** | [**SignatureEditObjectV1Request**](SignatureEditObjectV1Request.md)|  | 

### Return type

[**SignatureEditObjectV1Response**](SignatureEditObjectV1Response.md)

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

# **signature_get_object_v2**
> SignatureGetObjectV2Response signature_get_object_v2(pki_signature_id)

Retrieve an existing Signature



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.signature_get_object_v2_response import SignatureGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectSignatureApi(api_client)
    pki_signature_id = 56 # int | The unique ID of the Signature

    try:
        # Retrieve an existing Signature
        api_response = api_instance.signature_get_object_v2(pki_signature_id)
        print("The response of ObjectSignatureApi->signature_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectSignatureApi->signature_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_signature_id** | **int**| The unique ID of the Signature | 

### Return type

[**SignatureGetObjectV2Response**](SignatureGetObjectV2Response.md)

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

