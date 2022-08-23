# eZmaxApi.ObjectBrandingApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branding_create_object_v1**](ObjectBrandingApi.md#branding_create_object_v1) | **POST** /1/object/branding | Create a new Branding
[**branding_edit_object_v1**](ObjectBrandingApi.md#branding_edit_object_v1) | **PUT** /1/object/branding/{pkiBrandingID} | Edit an existing Branding
[**branding_get_autocomplete_v1**](ObjectBrandingApi.md#branding_get_autocomplete_v1) | **GET** /1/object/branding/getAutocomplete/{sSelector} | Retrieve Brandings and IDs
[**branding_get_list_v1**](ObjectBrandingApi.md#branding_get_list_v1) | **GET** /1/object/branding/getList | Retrieve Branding list
[**branding_get_object_v1**](ObjectBrandingApi.md#branding_get_object_v1) | **GET** /1/object/branding/{pkiBrandingID} | Retrieve an existing Branding


# **branding_create_object_v1**
> BrandingCreateObjectV1Response branding_create_object_v1(branding_create_object_v1_request)

Create a new Branding

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_branding_api
from eZmaxApi.model.branding_create_object_v1_request import BrandingCreateObjectV1Request
from eZmaxApi.model.branding_create_object_v1_response import BrandingCreateObjectV1Response
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
    api_instance = object_branding_api.ObjectBrandingApi(api_client)
    branding_create_object_v1_request = BrandingCreateObjectV1Request(
        a_obj_branding=[
            BrandingRequestCompound(),
        ],
    ) # BrandingCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Branding
        api_response = api_instance.branding_create_object_v1(branding_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectBrandingApi->branding_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branding_create_object_v1_request** | [**BrandingCreateObjectV1Request**](BrandingCreateObjectV1Request.md)|  |

### Return type

[**BrandingCreateObjectV1Response**](BrandingCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branding_edit_object_v1**
> BrandingEditObjectV1Response branding_edit_object_v1(pki_branding_id, branding_edit_object_v1_request)

Edit an existing Branding



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_branding_api
from eZmaxApi.model.branding_edit_object_v1_request import BrandingEditObjectV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.branding_edit_object_v1_response import BrandingEditObjectV1Response
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
    api_instance = object_branding_api.ObjectBrandingApi(api_client)
    pki_branding_id = FieldPkiBrandingID(78) # int | 
    branding_edit_object_v1_request = BrandingEditObjectV1Request(
        obj_branding=BrandingRequestCompound(),
    ) # BrandingEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Branding
        api_response = api_instance.branding_edit_object_v1(pki_branding_id, branding_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectBrandingApi->branding_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_branding_id** | **int**|  |
 **branding_edit_object_v1_request** | [**BrandingEditObjectV1Request**](BrandingEditObjectV1Request.md)|  |

### Return type

[**BrandingEditObjectV1Response**](BrandingEditObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branding_get_autocomplete_v1**
> CommonGetAutocompleteV1Response branding_get_autocomplete_v1()

Retrieve Brandings and IDs

Get the list of Branding to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_branding_api
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
    api_instance = object_branding_api.ObjectBrandingApi(api_client)
    e_filter_active = "Active" # str | Specify which results we want to display. (optional) if omitted the server will use the default value of "Active"
    s_query = "sQuery_example" # str | Allow to filter the returned results (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Brandings and IDs
        api_response = api_instance.branding_get_autocomplete_v1()
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectBrandingApi->branding_get_autocomplete_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Brandings and IDs
        api_response = api_instance.branding_get_autocomplete_v1(e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectBrandingApi->branding_get_autocomplete_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Brandings to return | defaults to "All"
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] if omitted the server will use the default value of "Active"
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

# **branding_get_list_v1**
> BrandingGetListV1Response branding_get_list_v1()

Retrieve Branding list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eBrandingLogo | Default<br>JPEG<br>PNG |

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_branding_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.branding_get_list_v1_response import BrandingGetListV1Response
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
    api_instance = object_branding_api.ObjectBrandingApi(api_client)
    e_order_by = "pkiBrandingID_ASC" # str | Specify how you want the results to be sorted (optional)
    i_row_max = FieldIRowMax(100) # int |  (optional)
    i_row_offset = FieldIRowOffset(0) # int |  (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)
    s_filter = "bField1 eq true and iField2 gte 0 and iField2 lte 1000 and sField3 eq 'Other' and eField4 eq 'Paid' and sField5 like '%needle%' and iField6 in '1,2,3' and dtField7 rg '=m,=3mm'" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Branding list
        api_response = api_instance.branding_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectBrandingApi->branding_get_list_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional]
 **i_row_max** | **int**|  | [optional]
 **i_row_offset** | **int**|  | [optional]
 **accept_language** | **HeaderAcceptLanguage**|  | [optional]
 **s_filter** | **str**|  | [optional]

### Return type

[**BrandingGetListV1Response**](BrandingGetListV1Response.md)

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

# **branding_get_object_v1**
> BrandingGetObjectV1Response branding_get_object_v1(pki_branding_id)

Retrieve an existing Branding



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_branding_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.branding_get_object_v1_response import BrandingGetObjectV1Response
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
    api_instance = object_branding_api.ObjectBrandingApi(api_client)
    pki_branding_id = FieldPkiBrandingID(78) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Branding
        api_response = api_instance.branding_get_object_v1(pki_branding_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectBrandingApi->branding_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_branding_id** | **int**|  |

### Return type

[**BrandingGetObjectV1Response**](BrandingGetObjectV1Response.md)

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

