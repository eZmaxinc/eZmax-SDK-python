# eZmaxApi.ObjectUsergroupApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroup_get_autocomplete_v1**](ObjectUsergroupApi.md#usergroup_get_autocomplete_v1) | **GET** /1/object/usergroup/getAutocomplete/{sSelector} | Retrieve Usergroups and IDs


# **usergroup_get_autocomplete_v1**
> CommonGetAutocompleteV1Response usergroup_get_autocomplete_v1()

Retrieve Usergroups and IDs

Get the list of Usergroup to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_usergroup_api
from eZmaxApi.model.common_get_autocomplete_v1_response import CommonGetAutocompleteV1Response
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage
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
    api_instance = object_usergroup_api.ObjectUsergroupApi(api_client)
    s_query = "sQuery_example" # str | Allow to filter the returned results (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Usergroups and IDs
        api_response = api_instance.usergroup_get_autocomplete_v1()
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_autocomplete_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Usergroups and IDs
        api_response = api_instance.usergroup_get_autocomplete_v1(s_query=s_query, accept_language=accept_language)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_autocomplete_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Usergroups to return | defaults to "All"
 **s_query** | **str**| Allow to filter the returned results | [optional]
 **accept_language** | **HeaderAcceptLanguage**|  | [optional]

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

