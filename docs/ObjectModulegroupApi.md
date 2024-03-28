# eZmaxApi.ObjectModulegroupApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modulegroup_get_all_v1**](ObjectModulegroupApi.md#modulegroup_get_all_v1) | **GET** /1/object/modulegroup/getAll/{eContext} | Retrieve all Modulegroups


# **modulegroup_get_all_v1**
> ModulegroupGetAllV1Response modulegroup_get_all_v1(e_context)

Retrieve all Modulegroups

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.modulegroup_get_all_v1_response import ModulegroupGetAllV1Response
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
    api_instance = eZmaxApi.ObjectModulegroupApi(api_client)
    e_context = 'e_context_example' # str | The context of the Modulegroup

    try:
        # Retrieve all Modulegroups
        api_response = api_instance.modulegroup_get_all_v1(e_context)
        print("The response of ObjectModulegroupApi->modulegroup_get_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectModulegroupApi->modulegroup_get_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_context** | **str**| The context of the Modulegroup | 

### Return type

[**ModulegroupGetAllV1Response**](ModulegroupGetAllV1Response.md)

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

