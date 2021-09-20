# eZmaxApi.ObjectFranchiseofficeApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchiseoffice_get_autocomplete_v1**](ObjectFranchiseofficeApi.md#franchiseoffice_get_autocomplete_v1) | **GET** /1/object/franchiseoffice/getAutocomplete/{sSelector} | Retrieve Franchiseoffices and IDs


# **franchiseoffice_get_autocomplete_v1**
> CommonGetAutocompleteV1Response franchiseoffice_get_autocomplete_v1(s_selector)

Retrieve Franchiseoffices and IDs

Get the list of Franchiseoffices to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_franchiseoffice_api
from eZmaxApi.model.common_get_autocomplete_v1_response import CommonGetAutocompleteV1Response
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
    api_instance = object_franchiseoffice_api.ObjectFranchiseofficeApi(api_client)
    s_selector = "Active" # str | The type of Franchiseoffices to return
    s_query = "sQuery_example" # str | Allow to filter on the option value (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Franchiseoffices and IDs
        api_response = api_instance.franchiseoffice_get_autocomplete_v1(s_selector)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectFranchiseofficeApi->franchiseoffice_get_autocomplete_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Franchiseoffices and IDs
        api_response = api_instance.franchiseoffice_get_autocomplete_v1(s_selector, s_query=s_query)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectFranchiseofficeApi->franchiseoffice_get_autocomplete_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Franchiseoffices to return |
 **s_query** | **str**| Allow to filter on the option value | [optional]

### Return type

[**CommonGetAutocompleteV1Response**](CommonGetAutocompleteV1Response.md)

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

