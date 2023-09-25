# eZmaxApi.ObjectEzsignsignergroupmembershipApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignsignergroupmembership_create_object_v1**](ObjectEzsignsignergroupmembershipApi.md#ezsignsignergroupmembership_create_object_v1) | **POST** /1/object/ezsignsignergroupmembership | Create a new Ezsignsignergroupmembership
[**ezsignsignergroupmembership_delete_object_v1**](ObjectEzsignsignergroupmembershipApi.md#ezsignsignergroupmembership_delete_object_v1) | **DELETE** /1/object/ezsignsignergroupmembership/{pkiEzsignsignergroupmembershipID} | Delete an existing Ezsignsignergroupmembership
[**ezsignsignergroupmembership_get_object_v2**](ObjectEzsignsignergroupmembershipApi.md#ezsignsignergroupmembership_get_object_v2) | **GET** /2/object/ezsignsignergroupmembership/{pkiEzsignsignergroupmembershipID} | Retrieve an existing Ezsignsignergroupmembership


# **ezsignsignergroupmembership_create_object_v1**
> EzsignsignergroupmembershipCreateObjectV1Response ezsignsignergroupmembership_create_object_v1(ezsignsignergroupmembership_create_object_v1_request)

Create a new Ezsignsignergroupmembership

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignergroupmembership_create_object_v1_request import EzsignsignergroupmembershipCreateObjectV1Request
from eZmaxApi.models.ezsignsignergroupmembership_create_object_v1_response import EzsignsignergroupmembershipCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupmembershipApi(api_client)
    ezsignsignergroupmembership_create_object_v1_request = eZmaxApi.EzsignsignergroupmembershipCreateObjectV1Request() # EzsignsignergroupmembershipCreateObjectV1Request | 

    try:
        # Create a new Ezsignsignergroupmembership
        api_response = api_instance.ezsignsignergroupmembership_create_object_v1(ezsignsignergroupmembership_create_object_v1_request)
        print("The response of ObjectEzsignsignergroupmembershipApi->ezsignsignergroupmembership_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupmembershipApi->ezsignsignergroupmembership_create_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignsignergroupmembership_create_object_v1_request** | [**EzsignsignergroupmembershipCreateObjectV1Request**](EzsignsignergroupmembershipCreateObjectV1Request.md)|  | 

### Return type

[**EzsignsignergroupmembershipCreateObjectV1Response**](EzsignsignergroupmembershipCreateObjectV1Response.md)

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

# **ezsignsignergroupmembership_delete_object_v1**
> EzsignsignergroupmembershipDeleteObjectV1Response ezsignsignergroupmembership_delete_object_v1(pki_ezsignsignergroupmembership_id)

Delete an existing Ezsignsignergroupmembership



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignergroupmembership_delete_object_v1_response import EzsignsignergroupmembershipDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupmembershipApi(api_client)
    pki_ezsignsignergroupmembership_id = 56 # int | The unique ID of the Ezsignsignergroupmembership

    try:
        # Delete an existing Ezsignsignergroupmembership
        api_response = api_instance.ezsignsignergroupmembership_delete_object_v1(pki_ezsignsignergroupmembership_id)
        print("The response of ObjectEzsignsignergroupmembershipApi->ezsignsignergroupmembership_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupmembershipApi->ezsignsignergroupmembership_delete_object_v1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroupmembership_id** | **int**| The unique ID of the Ezsignsignergroupmembership | 

### Return type

[**EzsignsignergroupmembershipDeleteObjectV1Response**](EzsignsignergroupmembershipDeleteObjectV1Response.md)

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

# **ezsignsignergroupmembership_get_object_v2**
> EzsignsignergroupmembershipGetObjectV2Response ezsignsignergroupmembership_get_object_v2(pki_ezsignsignergroupmembership_id)

Retrieve an existing Ezsignsignergroupmembership



### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignsignergroupmembership_get_object_v2_response import EzsignsignergroupmembershipGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupmembershipApi(api_client)
    pki_ezsignsignergroupmembership_id = 56 # int | The unique ID of the Ezsignsignergroupmembership

    try:
        # Retrieve an existing Ezsignsignergroupmembership
        api_response = api_instance.ezsignsignergroupmembership_get_object_v2(pki_ezsignsignergroupmembership_id)
        print("The response of ObjectEzsignsignergroupmembershipApi->ezsignsignergroupmembership_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupmembershipApi->ezsignsignergroupmembership_get_object_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroupmembership_id** | **int**| The unique ID of the Ezsignsignergroupmembership | 

### Return type

[**EzsignsignergroupmembershipGetObjectV2Response**](EzsignsignergroupmembershipGetObjectV2Response.md)

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

