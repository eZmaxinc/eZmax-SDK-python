# eZmaxApi.ObjectEzsigntsarequirementApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntsarequirement_get_autocomplete_v2**](ObjectEzsigntsarequirementApi.md#ezsigntsarequirement_get_autocomplete_v2) | **GET** /2/object/ezsigntsarequirement/getAutocomplete/{sSelector} | Retrieve Ezsigntsarequirements and IDs


# **ezsigntsarequirement_get_autocomplete_v2**
> EzsigntsarequirementGetAutocompleteV2Response ezsigntsarequirement_get_autocomplete_v2(s_selector, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Ezsigntsarequirements and IDs

Get the list of Ezsigntsarequirement to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):
```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntsarequirement_get_autocomplete_v2_response import EzsigntsarequirementGetAutocompleteV2Response
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
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
    api_instance = eZmaxApi.ObjectEzsigntsarequirementApi(api_client)
    s_selector = 's_selector_example' # str | The type of Ezsigntsarequirements to return
    fki_ezsignfoldertype_id = 56 # int |  (optional)
    e_filter_active = 'Active' # str | Specify which results we want to display. (optional) (default to 'Active')
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Ezsigntsarequirements and IDs
        api_response = api_instance.ezsigntsarequirement_get_autocomplete_v2(s_selector, fki_ezsignfoldertype_id=fki_ezsignfoldertype_id, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectEzsigntsarequirementApi->ezsigntsarequirement_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntsarequirementApi->ezsigntsarequirement_get_autocomplete_v2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezsigntsarequirements to return | 
 **fki_ezsignfoldertype_id** | **int**|  | [optional] 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to &#39;Active&#39;]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**EzsigntsarequirementGetAutocompleteV2Response**](EzsigntsarequirementGetAutocompleteV2Response.md)

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

