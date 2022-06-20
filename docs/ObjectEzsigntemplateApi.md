# eZmaxApi.ObjectEzsigntemplateApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplate_create_object_v1**](ObjectEzsigntemplateApi.md#ezsigntemplate_create_object_v1) | **POST** /1/object/ezsigntemplate | Create a new Ezsigntemplate
[**ezsigntemplate_delete_object_v1**](ObjectEzsigntemplateApi.md#ezsigntemplate_delete_object_v1) | **DELETE** /1/object/ezsigntemplate/{pkiEzsigntemplateID} | Delete an existing Ezsigntemplate
[**ezsigntemplate_edit_object_v1**](ObjectEzsigntemplateApi.md#ezsigntemplate_edit_object_v1) | **PUT** /1/object/ezsigntemplate/{pkiEzsigntemplateID} | Edit an existing Ezsigntemplate
[**ezsigntemplate_get_autocomplete_v1**](ObjectEzsigntemplateApi.md#ezsigntemplate_get_autocomplete_v1) | **GET** /1/object/ezsigntemplate/getAutocomplete/{sSelector} | Retrieve Ezsigntemplate and IDs
[**ezsigntemplate_get_list_v1**](ObjectEzsigntemplateApi.md#ezsigntemplate_get_list_v1) | **GET** /1/object/ezsigntemplate/getList | Retrieve Ezsigntemplate list
[**ezsigntemplate_get_object_v1**](ObjectEzsigntemplateApi.md#ezsigntemplate_get_object_v1) | **GET** /1/object/ezsigntemplate/{pkiEzsigntemplateID} | Retrieve an existing Ezsigntemplate


# **ezsigntemplate_create_object_v1**
> EzsigntemplateCreateObjectV1Response ezsigntemplate_create_object_v1(ezsigntemplate_create_object_v1_request)

Create a new Ezsigntemplate

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplate_api
from eZmaxApi.model.ezsigntemplate_create_object_v1_request import EzsigntemplateCreateObjectV1Request
from eZmaxApi.model.ezsigntemplate_create_object_v1_response import EzsigntemplateCreateObjectV1Response
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
    api_instance = object_ezsigntemplate_api.ObjectEzsigntemplateApi(api_client)
    ezsigntemplate_create_object_v1_request = EzsigntemplateCreateObjectV1Request(
        a_obj_ezsigntemplate=[
            EzsigntemplateRequestCompound(),
        ],
    ) # EzsigntemplateCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigntemplate
        api_response = api_instance.ezsigntemplate_create_object_v1(ezsigntemplate_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplate_create_object_v1_request** | [**EzsigntemplateCreateObjectV1Request**](EzsigntemplateCreateObjectV1Request.md)|  |

### Return type

[**EzsigntemplateCreateObjectV1Response**](EzsigntemplateCreateObjectV1Response.md)

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

# **ezsigntemplate_delete_object_v1**
> EzsigntemplateDeleteObjectV1Response ezsigntemplate_delete_object_v1(pki_ezsigntemplate_id)

Delete an existing Ezsigntemplate



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplate_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplate_delete_object_v1_response import EzsigntemplateDeleteObjectV1Response
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
    api_instance = object_ezsigntemplate_api.ObjectEzsigntemplateApi(api_client)
    pki_ezsigntemplate_id = FieldPkiEzsigntemplateID(36) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsigntemplate
        api_response = api_instance.ezsigntemplate_delete_object_v1(pki_ezsigntemplate_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplate_id** | **int**|  |

### Return type

[**EzsigntemplateDeleteObjectV1Response**](EzsigntemplateDeleteObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplate_edit_object_v1**
> EzsigntemplateEditObjectV1Response ezsigntemplate_edit_object_v1(pki_ezsigntemplate_id, ezsigntemplate_edit_object_v1_request)

Edit an existing Ezsigntemplate



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplate_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplate_edit_object_v1_request import EzsigntemplateEditObjectV1Request
from eZmaxApi.model.ezsigntemplate_edit_object_v1_response import EzsigntemplateEditObjectV1Response
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
    api_instance = object_ezsigntemplate_api.ObjectEzsigntemplateApi(api_client)
    pki_ezsigntemplate_id = FieldPkiEzsigntemplateID(36) # int | 
    ezsigntemplate_edit_object_v1_request = EzsigntemplateEditObjectV1Request(
        obj_ezsigntemplate=EzsigntemplateRequestCompound(),
    ) # EzsigntemplateEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Ezsigntemplate
        api_response = api_instance.ezsigntemplate_edit_object_v1(pki_ezsigntemplate_id, ezsigntemplate_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplate_id** | **int**|  |
 **ezsigntemplate_edit_object_v1_request** | [**EzsigntemplateEditObjectV1Request**](EzsigntemplateEditObjectV1Request.md)|  |

### Return type

[**EzsigntemplateEditObjectV1Response**](EzsigntemplateEditObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplate_get_autocomplete_v1**
> CommonGetAutocompleteV1Response ezsigntemplate_get_autocomplete_v1()

Retrieve Ezsigntemplate and IDs

Get the list of Ezsigntemplate to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplate_api
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
    api_instance = object_ezsigntemplate_api.ObjectEzsigntemplateApi(api_client)
    s_query = "sQuery_example" # str | Allow to filter the returned results (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Ezsigntemplate and IDs
        api_response = api_instance.ezsigntemplate_get_autocomplete_v1()
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_get_autocomplete_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Ezsigntemplate and IDs
        api_response = api_instance.ezsigntemplate_get_autocomplete_v1(s_query=s_query, accept_language=accept_language)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_get_autocomplete_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Ezsigntemplate to return | defaults to "All"
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

# **ezsigntemplate_get_list_v1**
> EzsigntemplateGetListV1Response ezsigntemplate_get_list_v1()

Retrieve Ezsigntemplate list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsigntemplateType | Company<br>Team<br>User<br>Usergroup | 

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplate_api
from eZmaxApi.model.ezsigntemplate_get_list_v1_response import EzsigntemplateGetListV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
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
    api_instance = object_ezsigntemplate_api.ObjectEzsigntemplateApi(api_client)
    e_order_by = "pkiEzsigntemplateID_ASC" # str | Specify how you want the results to be sorted (optional)
    i_row_max = FieldIRowMax(100) # int |  (optional)
    i_row_offset = FieldIRowOffset(0) # int |  (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)
    s_filter = "bField1 eq true and iField2 gte 0 and iField2 lte 1000 and sField3 eq 'Other' and eField4 eq 'Paid' and sField5 like '%needle%' and iField6 in '1,2,3' and dtField7 rg '=m,=3mm'" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Ezsigntemplate list
        api_response = api_instance.ezsigntemplate_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_get_list_v1: %s\n" % e)
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

[**EzsigntemplateGetListV1Response**](EzsigntemplateGetListV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**406** | One of the accept header is not defined or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplate_get_object_v1**
> EzsigntemplateGetObjectV1Response ezsigntemplate_get_object_v1(pki_ezsigntemplate_id)

Retrieve an existing Ezsigntemplate



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplate_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplate_get_object_v1_response import EzsigntemplateGetObjectV1Response
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
    api_instance = object_ezsigntemplate_api.ObjectEzsigntemplateApi(api_client)
    pki_ezsigntemplate_id = FieldPkiEzsigntemplateID(36) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplate
        api_response = api_instance.ezsigntemplate_get_object_v1(pki_ezsigntemplate_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplateApi->ezsigntemplate_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplate_id** | **int**|  |

### Return type

[**EzsigntemplateGetObjectV1Response**](EzsigntemplateGetObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

