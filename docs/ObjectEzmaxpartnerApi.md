# eZmaxApi.ObjectEzmaxpartnerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezmaxpartner_get_custom_developpers_v1**](ObjectEzmaxpartnerApi.md#ezmaxpartner_get_custom_developpers_v1) | **GET** /1/object/ezmaxpartner/getCustomDeveloppers | Retrieve Ezmaxpartner custom developpers list
[**ezmaxpartner_get_object_v2**](ObjectEzmaxpartnerApi.md#ezmaxpartner_get_object_v2) | **GET** /2/object/ezmaxpartner/{pkiEzmaxpartnerID} | Retrieve an existing Ezmaxpartner


# **ezmaxpartner_get_custom_developpers_v1**
> EzmaxpartnerGetCustomDeveloppersV1Response ezmaxpartner_get_custom_developpers_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Ezmaxpartner custom developpers list

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartner_get_custom_developpers_v1_response import EzmaxpartnerGetCustomDeveloppersV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Ezmaxpartner custom developpers list
        api_response = api_instance.ezmaxpartner_get_custom_developpers_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectEzmaxpartnerApi->ezmaxpartner_get_custom_developpers_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerApi->ezmaxpartner_get_custom_developpers_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional] 
 **i_row_max** | **int**|  | [optional] 
 **i_row_offset** | **int**|  | [optional] [default to 0]
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 
 **s_filter** | **str**|  | [optional] 

### Return type

[**EzmaxpartnerGetCustomDeveloppersV1Response**](EzmaxpartnerGetCustomDeveloppersV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezmaxpartner_get_object_v2**
> EzmaxpartnerGetObjectV2Response ezmaxpartner_get_object_v2(pki_ezmaxpartner_id)

Retrieve an existing Ezmaxpartner



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxpartner_get_object_v2_response import EzmaxpartnerGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzmaxpartnerApi(api_client)
    pki_ezmaxpartner_id = 56 # int | The unique ID of the Ezmaxpartner

    try:
        # Retrieve an existing Ezmaxpartner
        api_response = api_instance.ezmaxpartner_get_object_v2(pki_ezmaxpartner_id)
        print("The response of ObjectEzmaxpartnerApi->ezmaxpartner_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxpartnerApi->ezmaxpartner_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxpartner_id** | **int**| The unique ID of the Ezmaxpartner | 

### Return type

[**EzmaxpartnerGetObjectV2Response**](EzmaxpartnerGetObjectV2Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

