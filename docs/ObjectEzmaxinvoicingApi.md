# eZmaxApi.ObjectEzmaxinvoicingApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezmaxinvoicing_get_autocomplete_v1**](ObjectEzmaxinvoicingApi.md#ezmaxinvoicing_get_autocomplete_v1) | **GET** /1/object/ezmaxinvoicing/getAutocomplete/{sSelector} | Retrieve Ezmaxinvoicings and IDs
[**ezmaxinvoicing_get_autocomplete_v2**](ObjectEzmaxinvoicingApi.md#ezmaxinvoicing_get_autocomplete_v2) | **GET** /2/object/ezmaxinvoicing/getAutocomplete/{sSelector} | Retrieve Ezmaxinvoicings and IDs
[**ezmaxinvoicing_get_object_v2**](ObjectEzmaxinvoicingApi.md#ezmaxinvoicing_get_object_v2) | **GET** /2/object/ezmaxinvoicing/{pkiEzmaxinvoicingID} | Retrieve an existing Ezmaxinvoicing
[**ezmaxinvoicing_get_provisional_v1**](ObjectEzmaxinvoicingApi.md#ezmaxinvoicing_get_provisional_v1) | **GET** /1/object/ezmaxinvoicing/getProvisional | Retrieve provisional Ezmaxinvoicing


# **ezmaxinvoicing_get_autocomplete_v1**
> CommonGetAutocompleteV1Response ezmaxinvoicing_get_autocomplete_v1(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Ezmaxinvoicings and IDs

Get the list of Ezmaxinvoicing to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.common_get_autocomplete_v1_response import CommonGetAutocompleteV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxinvoicingApi(api_client)
    s_selector = 's_selector_example' # str | The type of Ezmaxinvoicings to return
    e_filter_active = 'e_filter_active_example' # str | Specify which results we want to display. Active is the default value. (optional)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Ezmaxinvoicings and IDs
        api_response = api_instance.ezmaxinvoicing_get_autocomplete_v1(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_autocomplete_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_autocomplete_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezmaxinvoicings to return | 
 **e_filter_active** | **str**| Specify which results we want to display. Active is the default value. | [optional] 
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

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

# **ezmaxinvoicing_get_autocomplete_v2**
> EzmaxinvoicingGetAutocompleteV2Response ezmaxinvoicing_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Ezmaxinvoicings and IDs

Get the list of Ezmaxinvoicing to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezmaxinvoicing_get_autocomplete_v2_response import EzmaxinvoicingGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectEzmaxinvoicingApi(api_client)
    s_selector = 's_selector_example' # str | The type of Ezmaxinvoicings to return
    e_filter_active = 'Active' # str | Specify which results we want to display. (optional) (default to 'Active')
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Ezmaxinvoicings and IDs
        api_response = api_instance.ezmaxinvoicing_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezmaxinvoicings to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to &#39;Active&#39;]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**EzmaxinvoicingGetAutocompleteV2Response**](EzmaxinvoicingGetAutocompleteV2Response.md)

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

# **ezmaxinvoicing_get_object_v2**
> EzmaxinvoicingGetObjectV2Response ezmaxinvoicing_get_object_v2(pki_ezmaxinvoicing_id)

Retrieve an existing Ezmaxinvoicing



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezmaxinvoicing_get_object_v2_response import EzmaxinvoicingGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzmaxinvoicingApi(api_client)
    pki_ezmaxinvoicing_id = 56 # int | 

    try:
        # Retrieve an existing Ezmaxinvoicing
        api_response = api_instance.ezmaxinvoicing_get_object_v2(pki_ezmaxinvoicing_id)
        print("The response of ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxinvoicing_id** | **int**|  | 

### Return type

[**EzmaxinvoicingGetObjectV2Response**](EzmaxinvoicingGetObjectV2Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezmaxinvoicing_get_provisional_v1**
> EzmaxinvoicingGetProvisionalV1Response ezmaxinvoicing_get_provisional_v1()

Retrieve provisional Ezmaxinvoicing



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezmaxinvoicing_get_provisional_v1_response import EzmaxinvoicingGetProvisionalV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxinvoicingApi(api_client)

    try:
        # Retrieve provisional Ezmaxinvoicing
        api_response = api_instance.ezmaxinvoicing_get_provisional_v1()
        print("The response of ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_provisional_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxinvoicingApi->ezmaxinvoicing_get_provisional_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EzmaxinvoicingGetProvisionalV1Response**](EzmaxinvoicingGetProvisionalV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

