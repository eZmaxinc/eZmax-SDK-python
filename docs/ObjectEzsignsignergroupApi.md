# eZmaxApi.ObjectEzsignsignergroupApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignsignergroup_create_object_v1**](ObjectEzsignsignergroupApi.md#ezsignsignergroup_create_object_v1) | **POST** /1/object/ezsignsignergroup | Create a new Ezsignsignergroup
[**ezsignsignergroup_delete_object_v1**](ObjectEzsignsignergroupApi.md#ezsignsignergroup_delete_object_v1) | **DELETE** /1/object/ezsignsignergroup/{pkiEzsignsignergroupID} | Delete an existing Ezsignsignergroup
[**ezsignsignergroup_edit_ezsignsignergroupmemberships_v1**](ObjectEzsignsignergroupApi.md#ezsignsignergroup_edit_ezsignsignergroupmemberships_v1) | **PUT** /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/editEzsignsignergroupmemberships | Edit multiple Ezsignsignergroupmemberships
[**ezsignsignergroup_edit_object_v1**](ObjectEzsignsignergroupApi.md#ezsignsignergroup_edit_object_v1) | **PUT** /1/object/ezsignsignergroup/{pkiEzsignsignergroupID} | Edit an existing Ezsignsignergroup
[**ezsignsignergroup_get_ezsignsignergroupmemberships_v1**](ObjectEzsignsignergroupApi.md#ezsignsignergroup_get_ezsignsignergroupmemberships_v1) | **GET** /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/getEzsignsignergroupmemberships | Retrieve an existing Ezsignsignergroup&#39;s Ezsignsignergroupmemberships
[**ezsignsignergroup_get_object_v2**](ObjectEzsignsignergroupApi.md#ezsignsignergroup_get_object_v2) | **GET** /2/object/ezsignsignergroup/{pkiEzsignsignergroupID} | Retrieve an existing Ezsignsignergroup


# **ezsignsignergroup_create_object_v1**
> EzsignsignergroupCreateObjectV1Response ezsignsignergroup_create_object_v1(ezsignsignergroup_create_object_v1_request)

Create a new Ezsignsignergroup

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignsignergroup_create_object_v1_request import EzsignsignergroupCreateObjectV1Request
from eZmaxApi.models.ezsignsignergroup_create_object_v1_response import EzsignsignergroupCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupApi(api_client)
    ezsignsignergroup_create_object_v1_request = eZmaxApi.EzsignsignergroupCreateObjectV1Request() # EzsignsignergroupCreateObjectV1Request | 

    try:
        # Create a new Ezsignsignergroup
        api_response = api_instance.ezsignsignergroup_create_object_v1(ezsignsignergroup_create_object_v1_request)
        print("The response of ObjectEzsignsignergroupApi->ezsignsignergroup_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupApi->ezsignsignergroup_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignsignergroup_create_object_v1_request** | [**EzsignsignergroupCreateObjectV1Request**](EzsignsignergroupCreateObjectV1Request.md)|  | 

### Return type

[**EzsignsignergroupCreateObjectV1Response**](EzsignsignergroupCreateObjectV1Response.md)

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

# **ezsignsignergroup_delete_object_v1**
> CommonResponse ezsignsignergroup_delete_object_v1(pki_ezsignsignergroup_id)

Delete an existing Ezsignsignergroup



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
    api_instance = eZmaxApi.ObjectEzsignsignergroupApi(api_client)
    pki_ezsignsignergroup_id = 56 # int | The unique ID of the Ezsignsignergroup

    try:
        # Delete an existing Ezsignsignergroup
        api_response = api_instance.ezsignsignergroup_delete_object_v1(pki_ezsignsignergroup_id)
        print("The response of ObjectEzsignsignergroupApi->ezsignsignergroup_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupApi->ezsignsignergroup_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroup_id** | **int**| The unique ID of the Ezsignsignergroup | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignsignergroup_edit_ezsignsignergroupmemberships_v1**
> EzsignsignergroupEditEzsignsignergroupmembershipsV1Response ezsignsignergroup_edit_ezsignsignergroupmemberships_v1(pki_ezsignsignergroup_id, ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request)

Edit multiple Ezsignsignergroupmemberships

Using this endpoint, you can edit multiple Ezsignsignergroupmemberships at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request import EzsignsignergroupEditEzsignsignergroupmembershipsV1Request
from eZmaxApi.models.ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_response import EzsignsignergroupEditEzsignsignergroupmembershipsV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupApi(api_client)
    pki_ezsignsignergroup_id = 56 # int | 
    ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request = eZmaxApi.EzsignsignergroupEditEzsignsignergroupmembershipsV1Request() # EzsignsignergroupEditEzsignsignergroupmembershipsV1Request | 

    try:
        # Edit multiple Ezsignsignergroupmemberships
        api_response = api_instance.ezsignsignergroup_edit_ezsignsignergroupmemberships_v1(pki_ezsignsignergroup_id, ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request)
        print("The response of ObjectEzsignsignergroupApi->ezsignsignergroup_edit_ezsignsignergroupmemberships_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupApi->ezsignsignergroup_edit_ezsignsignergroupmemberships_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroup_id** | **int**|  | 
 **ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request** | [**EzsignsignergroupEditEzsignsignergroupmembershipsV1Request**](EzsignsignergroupEditEzsignsignergroupmembershipsV1Request.md)|  | 

### Return type

[**EzsignsignergroupEditEzsignsignergroupmembershipsV1Response**](EzsignsignergroupEditEzsignsignergroupmembershipsV1Response.md)

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

# **ezsignsignergroup_edit_object_v1**
> CommonResponse ezsignsignergroup_edit_object_v1(pki_ezsignsignergroup_id, ezsignsignergroup_edit_object_v1_request)

Edit an existing Ezsignsignergroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.ezsignsignergroup_edit_object_v1_request import EzsignsignergroupEditObjectV1Request
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupApi(api_client)
    pki_ezsignsignergroup_id = 56 # int | The unique ID of the Ezsignsignergroup
    ezsignsignergroup_edit_object_v1_request = eZmaxApi.EzsignsignergroupEditObjectV1Request() # EzsignsignergroupEditObjectV1Request | 

    try:
        # Edit an existing Ezsignsignergroup
        api_response = api_instance.ezsignsignergroup_edit_object_v1(pki_ezsignsignergroup_id, ezsignsignergroup_edit_object_v1_request)
        print("The response of ObjectEzsignsignergroupApi->ezsignsignergroup_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupApi->ezsignsignergroup_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroup_id** | **int**| The unique ID of the Ezsignsignergroup | 
 **ezsignsignergroup_edit_object_v1_request** | [**EzsignsignergroupEditObjectV1Request**](EzsignsignergroupEditObjectV1Request.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignsignergroup_get_ezsignsignergroupmemberships_v1**
> EzsignsignergroupGetEzsignsignergroupmembershipsV1Response ezsignsignergroup_get_ezsignsignergroupmemberships_v1(pki_ezsignsignergroup_id)

Retrieve an existing Ezsignsignergroup's Ezsignsignergroupmemberships

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response import EzsignsignergroupGetEzsignsignergroupmembershipsV1Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupApi(api_client)
    pki_ezsignsignergroup_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignsignergroup's Ezsignsignergroupmemberships
        api_response = api_instance.ezsignsignergroup_get_ezsignsignergroupmemberships_v1(pki_ezsignsignergroup_id)
        print("The response of ObjectEzsignsignergroupApi->ezsignsignergroup_get_ezsignsignergroupmemberships_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupApi->ezsignsignergroup_get_ezsignsignergroupmemberships_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroup_id** | **int**|  | 

### Return type

[**EzsignsignergroupGetEzsignsignergroupmembershipsV1Response**](EzsignsignergroupGetEzsignsignergroupmembershipsV1Response.md)

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

# **ezsignsignergroup_get_object_v2**
> EzsignsignergroupGetObjectV2Response ezsignsignergroup_get_object_v2(pki_ezsignsignergroup_id)

Retrieve an existing Ezsignsignergroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignsignergroup_get_object_v2_response import EzsignsignergroupGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignsignergroupApi(api_client)
    pki_ezsignsignergroup_id = 56 # int | The unique ID of the Ezsignsignergroup

    try:
        # Retrieve an existing Ezsignsignergroup
        api_response = api_instance.ezsignsignergroup_get_object_v2(pki_ezsignsignergroup_id)
        print("The response of ObjectEzsignsignergroupApi->ezsignsignergroup_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignsignergroupApi->ezsignsignergroup_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignsignergroup_id** | **int**| The unique ID of the Ezsignsignergroup | 

### Return type

[**EzsignsignergroupGetObjectV2Response**](EzsignsignergroupGetObjectV2Response.md)

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

