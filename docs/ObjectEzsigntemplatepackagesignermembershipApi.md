# eZmaxApi.ObjectEzsigntemplatepackagesignermembershipApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatepackagesignermembership_create_object_v1**](ObjectEzsigntemplatepackagesignermembershipApi.md#ezsigntemplatepackagesignermembership_create_object_v1) | **POST** /1/object/ezsigntemplatepackagesignermembership | Create a new Ezsigntemplatepackagesignermembership
[**ezsigntemplatepackagesignermembership_delete_object_v1**](ObjectEzsigntemplatepackagesignermembershipApi.md#ezsigntemplatepackagesignermembership_delete_object_v1) | **DELETE** /1/object/ezsigntemplatepackagesignermembership/{pkiEzsigntemplatepackagesignermembershipID} | Delete an existing Ezsigntemplatepackagesignermembership
[**ezsigntemplatepackagesignermembership_get_object_v1**](ObjectEzsigntemplatepackagesignermembershipApi.md#ezsigntemplatepackagesignermembership_get_object_v1) | **GET** /1/object/ezsigntemplatepackagesignermembership/{pkiEzsigntemplatepackagesignermembershipID} | Retrieve an existing Ezsigntemplatepackagesignermembership


# **ezsigntemplatepackagesignermembership_create_object_v1**
> EzsigntemplatepackagesignermembershipCreateObjectV1Response ezsigntemplatepackagesignermembership_create_object_v1(ezsigntemplatepackagesignermembership_create_object_v1_request)

Create a new Ezsigntemplatepackagesignermembership

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesignermembership_api
from eZmaxApi.model.ezsigntemplatepackagesignermembership_create_object_v1_response import EzsigntemplatepackagesignermembershipCreateObjectV1Response
from eZmaxApi.model.ezsigntemplatepackagesignermembership_create_object_v1_request import EzsigntemplatepackagesignermembershipCreateObjectV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigntemplatepackagesignermembership_api.ObjectEzsigntemplatepackagesignermembershipApi(api_client)
    ezsigntemplatepackagesignermembership_create_object_v1_request = EzsigntemplatepackagesignermembershipCreateObjectV1Request(
        a_obj_ezsigntemplatepackagesignermembership=[
            EzsigntemplatepackagesignermembershipRequestCompound(),
        ],
    ) # EzsigntemplatepackagesignermembershipCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigntemplatepackagesignermembership
        api_response = api_instance.ezsigntemplatepackagesignermembership_create_object_v1(ezsigntemplatepackagesignermembership_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignermembershipApi->ezsigntemplatepackagesignermembership_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatepackagesignermembership_create_object_v1_request** | [**EzsigntemplatepackagesignermembershipCreateObjectV1Request**](EzsigntemplatepackagesignermembershipCreateObjectV1Request.md)|  |

### Return type

[**EzsigntemplatepackagesignermembershipCreateObjectV1Response**](EzsigntemplatepackagesignermembershipCreateObjectV1Response.md)

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

# **ezsigntemplatepackagesignermembership_delete_object_v1**
> EzsigntemplatepackagesignermembershipDeleteObjectV1Response ezsigntemplatepackagesignermembership_delete_object_v1(pki_ezsigntemplatepackagesignermembership_id)

Delete an existing Ezsigntemplatepackagesignermembership



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesignermembership_api
from eZmaxApi.model.ezsigntemplatepackagesignermembership_delete_object_v1_response import EzsigntemplatepackagesignermembershipDeleteObjectV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigntemplatepackagesignermembership_api.ObjectEzsigntemplatepackagesignermembershipApi(api_client)
    pki_ezsigntemplatepackagesignermembership_id = FieldPkiEzsigntemplatepackagesignermembershipID(237) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsigntemplatepackagesignermembership
        api_response = api_instance.ezsigntemplatepackagesignermembership_delete_object_v1(pki_ezsigntemplatepackagesignermembership_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignermembershipApi->ezsigntemplatepackagesignermembership_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagesignermembership_id** | **int**|  |

### Return type

[**EzsigntemplatepackagesignermembershipDeleteObjectV1Response**](EzsigntemplatepackagesignermembershipDeleteObjectV1Response.md)

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

# **ezsigntemplatepackagesignermembership_get_object_v1**
> EzsigntemplatepackagesignermembershipGetObjectV1Response ezsigntemplatepackagesignermembership_get_object_v1(pki_ezsigntemplatepackagesignermembership_id)

Retrieve an existing Ezsigntemplatepackagesignermembership



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackagesignermembership_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatepackagesignermembership_get_object_v1_response import EzsigntemplatepackagesignermembershipGetObjectV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigntemplatepackagesignermembership_api.ObjectEzsigntemplatepackagesignermembershipApi(api_client)
    pki_ezsigntemplatepackagesignermembership_id = FieldPkiEzsigntemplatepackagesignermembershipID(237) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatepackagesignermembership
        api_response = api_instance.ezsigntemplatepackagesignermembership_get_object_v1(pki_ezsigntemplatepackagesignermembership_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackagesignermembershipApi->ezsigntemplatepackagesignermembership_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatepackagesignermembership_id** | **int**|  |

### Return type

[**EzsigntemplatepackagesignermembershipGetObjectV1Response**](EzsigntemplatepackagesignermembershipGetObjectV1Response.md)

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

