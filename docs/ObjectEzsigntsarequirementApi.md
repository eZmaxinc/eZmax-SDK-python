# eZmaxApi.ObjectEzsigntsarequirementApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntsarequirement_get_autocomplete_v1**](ObjectEzsigntsarequirementApi.md#ezsigntsarequirement_get_autocomplete_v1) | **GET** /1/object/ezsigntsarequirement/getAutocomplete/{sSelector} | Retrieve Ezsigntsarequirements and IDs


# **ezsigntsarequirement_get_autocomplete_v1**
> CommonGetAutocompleteDisabledV1Response ezsigntsarequirement_get_autocomplete_v1(s_selector)

Retrieve Ezsigntsarequirements and IDs

Get the list of Ezsigntsarequirement to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntsarequirement_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.common_get_autocomplete_disabled_v1_response import CommonGetAutocompleteDisabledV1Response
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
    api_instance = object_ezsigntsarequirement_api.ObjectEzsigntsarequirementApi(api_client)
    s_selector = "User" # str | The type of Ezsigntsarequirements to return
    fki_ezsignfoldertype_id = FieldPkiEzsignfoldertypeID(5) # int |  (optional)
    s_query = "sQuery_example" # str | Allow to filter the returned results (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Ezsigntsarequirements and IDs
        api_response = api_instance.ezsigntsarequirement_get_autocomplete_v1(s_selector)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntsarequirementApi->ezsigntsarequirement_get_autocomplete_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Ezsigntsarequirements and IDs
        api_response = api_instance.ezsigntsarequirement_get_autocomplete_v1(s_selector, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id, s_query=s_query, accept_language=accept_language)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntsarequirementApi->ezsigntsarequirement_get_autocomplete_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezsigntsarequirements to return |
 **fki_ezsignfoldertype_id** | **int**|  | [optional]
 **s_query** | **str**| Allow to filter the returned results | [optional]
 **accept_language** | **HeaderAcceptLanguage**|  | [optional]

### Return type

[**CommonGetAutocompleteDisabledV1Response**](CommonGetAutocompleteDisabledV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

