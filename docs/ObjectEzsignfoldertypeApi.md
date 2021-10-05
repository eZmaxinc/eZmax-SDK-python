# eZmaxApi.ObjectEzsignfoldertypeApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignfoldertype_get_list_v1**](ObjectEzsignfoldertypeApi.md#ezsignfoldertype_get_list_v1) | **GET** /1/object/ezsignfoldertype/getList | Retrieve Ezsignfoldertype list


# **ezsignfoldertype_get_list_v1**
> EzsignfoldertypeGetListV1Response ezsignfoldertype_get_list_v1()

Retrieve Ezsignfoldertype list

## ⚠️EARLY ADOPTERS WARNING  ### This endpoint is not officially released. Its definition might still change and it might not be available in every environment and region.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfoldertype_api
from eZmaxApi.model.ezsignfoldertype_get_list_v1_response import EzsignfoldertypeGetListV1Response
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
    api_instance = object_ezsignfoldertype_api.ObjectEzsignfoldertypeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve Ezsignfoldertype list
        api_response = api_instance.ezsignfoldertype_get_list_v1()
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfoldertypeApi->ezsignfoldertype_get_list_v1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EzsignfoldertypeGetListV1Response**](EzsignfoldertypeGetListV1Response.md)

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

