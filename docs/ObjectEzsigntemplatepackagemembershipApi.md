# eZmaxApi.ObjectEzsigntemplatepackagemembershipApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatepackagemembership_create_object_v1**](ObjectEzsigntemplatepackagemembershipApi.md#ezsigntemplatepackagemembership_create_object_v1) | **POST** /1/object/ezsigntemplatepackagemembership | Create a new Ezsigntemplatepackagemembership
[**ezsigntemplatepackagemembership_delete_object_v1**](ObjectEzsigntemplatepackagemembershipApi.md#ezsigntemplatepackagemembership_delete_object_v1) | **DELETE** /1/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID} | Delete an existing Ezsigntemplatepackagemembership
[**ezsigntemplatepackagemembership_get_object_v2**](ObjectEzsigntemplatepackagemembershipApi.md#ezsigntemplatepackagemembership_get_object_v2) | **GET** /2/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID} | Retrieve an existing Ezsigntemplatepackagemembership


# **ezsigntemplatepackagemembership_create_object_v1**
> EzsigntemplatepackagemembershipCreateObjectV1Response ezsigntemplatepackagemembership_create_object_v1(ezsigntemplatepackagemembership_create_object_v1_request)

Create a new Ezsigntemplatepackagemembership

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_request import EzsigntemplatepackagemembershipCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_response import EzsigntemplatepackagemembershipCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagemembershipApi(api_client)
    ezsigntemplatepackagemembership_create_object_v1_request = eZmaxApi.EzsigntemplatepackagemembershipCreateObjectV1Request() # EzsigntemplatepackagemembershipCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatepackagemembership
        api_response = api_instance.ezsigntemplatepackagemembership_create_object_v1(ezsigntemplatepackagemembership_create_object_v1_request)
        print("The response of ObjectEzsigntemplatepackagemembershipApi->ezsigntemplatepackagemembership_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackagemembershipApi->ezsigntemplatepackagemembership_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatepackagemembership_create_object_v1_request** | [**EzsigntemplatepackagemembershipCreateObjectV1Request**](EzsigntemplatepackagemembershipCreateObjectV1Request.md)|  | 

### Return type

[**EzsigntemplatepackagemembershipCreateObjectV1Response**](EzsigntemplatepackagemembershipCreateObjectV1Response.md)

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

# **ezsigntemplatepackagemembership_delete_object_v1**
> EzsigntemplatepackagemembershipDeleteObjectV1Response ezsigntemplatepackagemembership_delete_object_v1(pki_ezsigntemplatepackagemembership_id)

Delete an existing Ezsigntemplatepackagemembership



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagemembership_delete_object_v1_response import EzsigntemplatepackagemembershipDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagemembershipApi(api_client)
    pki_ezsigntemplatepackagemembership_id = 56 # int | 

    try:
        # Delete an existing Ezsigntemplatepackagemembership
        api_response = api_instance.ezsigntemplatepackagemembership_delete_object_v1(pki_ezsigntemplatepackagemembership_id)
        print("The response of ObjectEzsigntemplatepackagemembershipApi->ezsigntemplatepackagemembership_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackagemembershipApi->ezsigntemplatepackagemembership_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagemembership_id** | **int**|  | 

### Return type

[**EzsigntemplatepackagemembershipDeleteObjectV1Response**](EzsigntemplatepackagemembershipDeleteObjectV1Response.md)

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

# **ezsigntemplatepackagemembership_get_object_v2**
> EzsigntemplatepackagemembershipGetObjectV2Response ezsigntemplatepackagemembership_get_object_v2(pki_ezsigntemplatepackagemembership_id)

Retrieve an existing Ezsigntemplatepackagemembership



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatepackagemembership_get_object_v2_response import EzsigntemplatepackagemembershipGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatepackagemembershipApi(api_client)
    pki_ezsigntemplatepackagemembership_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatepackagemembership
        api_response = api_instance.ezsigntemplatepackagemembership_get_object_v2(pki_ezsigntemplatepackagemembership_id)
        print("The response of ObjectEzsigntemplatepackagemembershipApi->ezsigntemplatepackagemembership_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatepackagemembershipApi->ezsigntemplatepackagemembership_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagemembership_id** | **int**|  | 

### Return type

[**EzsigntemplatepackagemembershipGetObjectV2Response**](EzsigntemplatepackagemembershipGetObjectV2Response.md)

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

