# eZmaxApi.ObjectBillingentityexternalApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingentityexternal_generate_federation_token_v1**](ObjectBillingentityexternalApi.md#billingentityexternal_generate_federation_token_v1) | **POST** /1/object/billingentityexternal/{pkiBillingentityexternalID}/generateFederationToken | Generate a federation token
[**billingentityexternal_get_autocomplete_v2**](ObjectBillingentityexternalApi.md#billingentityexternal_get_autocomplete_v2) | **GET** /2/object/billingentityexternal/getAutocomplete/{sSelector} | Retrieve Billingentityexternals and IDs


# **billingentityexternal_generate_federation_token_v1**
> BillingentityexternalGenerateFederationTokenV1Response billingentityexternal_generate_federation_token_v1(pki_billingentityexternal_id, billingentityexternal_generate_federation_token_v1_request)

Generate a federation token



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.billingentityexternal_generate_federation_token_v1_request import BillingentityexternalGenerateFederationTokenV1Request
from eZmaxApi.models.billingentityexternal_generate_federation_token_v1_response import BillingentityexternalGenerateFederationTokenV1Response
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
    api_instance = eZmaxApi.ObjectBillingentityexternalApi(api_client)
    pki_billingentityexternal_id = 56 # int | 
    billingentityexternal_generate_federation_token_v1_request = eZmaxApi.BillingentityexternalGenerateFederationTokenV1Request() # BillingentityexternalGenerateFederationTokenV1Request | 

    try:
        # Generate a federation token
        api_response = api_instance.billingentityexternal_generate_federation_token_v1(pki_billingentityexternal_id, billingentityexternal_generate_federation_token_v1_request)
        print("The response of ObjectBillingentityexternalApi->billingentityexternal_generate_federation_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectBillingentityexternalApi->billingentityexternal_generate_federation_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_billingentityexternal_id** | **int**|  | 
 **billingentityexternal_generate_federation_token_v1_request** | [**BillingentityexternalGenerateFederationTokenV1Request**](BillingentityexternalGenerateFederationTokenV1Request.md)|  | 

### Return type

[**BillingentityexternalGenerateFederationTokenV1Response**](BillingentityexternalGenerateFederationTokenV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billingentityexternal_get_autocomplete_v2**
> BillingentityexternalGetAutocompleteV2Response billingentityexternal_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Billingentityexternals and IDs

Get the list of Billingentityexternal to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response import BillingentityexternalGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectBillingentityexternalApi(api_client)
    s_selector = 's_selector_example' # str | The type of Billingentityexternals to return
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Billingentityexternals and IDs
        api_response = api_instance.billingentityexternal_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectBillingentityexternalApi->billingentityexternal_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectBillingentityexternalApi->billingentityexternal_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Billingentityexternals to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**BillingentityexternalGetAutocompleteV2Response**](BillingentityexternalGetAutocompleteV2Response.md)

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

