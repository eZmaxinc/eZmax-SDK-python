# eZmaxApi.ObjectContacttitleApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacttitle_get_autocomplete_v2**](ObjectContacttitleApi.md#contacttitle_get_autocomplete_v2) | **GET** /2/object/contacttitle/getAutocomplete/{sSelector} | Retrieve Contacttitles and IDs


# **contacttitle_get_autocomplete_v2**
> ContacttitleGetAutocompleteV2Response contacttitle_get_autocomplete_v2(s_selector, s_query=s_query, accept_language=accept_language)

Retrieve Contacttitles and IDs

Get the list of Contacttitle to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.contacttitle_get_autocomplete_v2_response import ContacttitleGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectContacttitleApi(api_client)
    s_selector = 's_selector_example' # str | The type of Contacttitles to return
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Contacttitles and IDs
        api_response = api_instance.contacttitle_get_autocomplete_v2(s_selector, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectContacttitleApi->contacttitle_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectContacttitleApi->contacttitle_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Contacttitles to return | 
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**ContacttitleGetAutocompleteV2Response**](ContacttitleGetAutocompleteV2Response.md)

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

