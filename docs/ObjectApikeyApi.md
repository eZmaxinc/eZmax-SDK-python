# eZmaxApi.ObjectApikeyApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apikey_create_object_v1**](ObjectApikeyApi.md#apikey_create_object_v1) | **POST** /1/object/apikey | Create a new Apikey
[**apikey_create_object_v2**](ObjectApikeyApi.md#apikey_create_object_v2) | **POST** /2/object/apikey | Create a new Apikey


# **apikey_create_object_v1**
> ApikeyCreateObjectV1Response apikey_create_object_v1(apikey_create_object_v1_request)

Create a new Apikey

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_apikey_api
from eZmaxApi.model.apikey_create_object_v1_request import ApikeyCreateObjectV1Request
from eZmaxApi.model.apikey_create_object_v1_response import ApikeyCreateObjectV1Response
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
    api_instance = object_apikey_api.ObjectApikeyApi(api_client)
    apikey_create_object_v1_request = [
        ApikeyCreateObjectV1Request(
            obj_apikey=ApikeyRequest(
                pki_apikey_id=FieldPkiApikeyID(99),
                fki_user_id=FieldPkiUserID(70),
                obj_apikey_description=MultilingualApikeyDescription(
                    s_apikey_description1="Projet X",
                    s_apikey_description2="Project X",
                ),
            ),
            obj_apikey_compound=ApikeyRequestCompound(),
        ),
    ] # [ApikeyCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Apikey
        api_response = api_instance.apikey_create_object_v1(apikey_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectApikeyApi->apikey_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_create_object_v1_request** | [**[ApikeyCreateObjectV1Request]**](ApikeyCreateObjectV1Request.md)|  |

### Return type

[**ApikeyCreateObjectV1Response**](ApikeyCreateObjectV1Response.md)

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

# **apikey_create_object_v2**
> ApikeyCreateObjectV2Response apikey_create_object_v2(apikey_create_object_v2_request)

Create a new Apikey

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_apikey_api
from eZmaxApi.model.apikey_create_object_v2_request import ApikeyCreateObjectV2Request
from eZmaxApi.model.apikey_create_object_v2_response import ApikeyCreateObjectV2Response
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
    api_instance = object_apikey_api.ObjectApikeyApi(api_client)
    apikey_create_object_v2_request = ApikeyCreateObjectV2Request(
        a_obj_apikey=[
            ApikeyRequestCompound(),
        ],
    ) # ApikeyCreateObjectV2Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Apikey
        api_response = api_instance.apikey_create_object_v2(apikey_create_object_v2_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectApikeyApi->apikey_create_object_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_create_object_v2_request** | [**ApikeyCreateObjectV2Request**](ApikeyCreateObjectV2Request.md)|  |

### Return type

[**ApikeyCreateObjectV2Response**](ApikeyCreateObjectV2Response.md)

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

