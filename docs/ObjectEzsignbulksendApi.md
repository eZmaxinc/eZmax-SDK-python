# eZmaxApi.ObjectEzsignbulksendApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignbulksend_create_ezsignbulksendtransmission_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_create_ezsignbulksendtransmission_v1) | **POST** /1/object/ezsignbulksend/{pkiEzsignbulksendID}/createEzsignbulksendtransmission | Create a new Ezsignbulksendtransmission in the Ezsignbulksend
[**ezsignbulksend_create_object_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_create_object_v1) | **POST** /1/object/ezsignbulksend | Create a new Ezsignbulksend
[**ezsignbulksend_delete_object_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_delete_object_v1) | **DELETE** /1/object/ezsignbulksend/{pkiEzsignbulksendID} | Delete an existing Ezsignbulksend
[**ezsignbulksend_edit_object_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_edit_object_v1) | **PUT** /1/object/ezsignbulksend/{pkiEzsignbulksendID} | Edit an existing Ezsignbulksend
[**ezsignbulksend_get_csv_template_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_get_csv_template_v1) | **GET** /1/object/ezsignbulksend/{pkiEzsignbulksendID}/getCsvTemplate | Retrieve an existing Ezsignbulksend&#39;s empty Csv template
[**ezsignbulksend_get_ezsignbulksendtransmissions_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_get_ezsignbulksendtransmissions_v1) | **GET** /1/object/ezsignbulksend/{pkiEzsignbulksendID}/getEzsignbulksendtransmissions | Retrieve an existing Ezsignbulksend&#39;s Ezsignbulksendtransmissions
[**ezsignbulksend_get_ezsignsignatures_automatic_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_get_ezsignsignatures_automatic_v1) | **GET** /1/object/ezsignbulksend/{pkiEzsignbulksendID}/getEzsignsignaturesAutomatic | Retrieve an existing Ezsignbulksend&#39;s automatic Ezsignsignatures
[**ezsignbulksend_get_forms_data_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_get_forms_data_v1) | **GET** /1/object/ezsignbulksend/{pkiEzsignbulksendID}/getFormsData | Retrieve an existing Ezsignbulksend&#39;s forms data
[**ezsignbulksend_get_list_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_get_list_v1) | **GET** /1/object/ezsignbulksend/getList | Retrieve Ezsignbulksend list
[**ezsignbulksend_get_object_v2**](ObjectEzsignbulksendApi.md#ezsignbulksend_get_object_v2) | **GET** /2/object/ezsignbulksend/{pkiEzsignbulksendID} | Retrieve an existing Ezsignbulksend
[**ezsignbulksend_reorder_v1**](ObjectEzsignbulksendApi.md#ezsignbulksend_reorder_v1) | **POST** /1/object/ezsignbulksend/{pkiEzsignbulksendID}/reorder | Reorder Ezsignbulksenddocumentmappings in the Ezsignbulksend


# **ezsignbulksend_create_ezsignbulksendtransmission_v1**
> EzsignbulksendCreateEzsignbulksendtransmissionV1Response ezsignbulksend_create_ezsignbulksendtransmission_v1(pki_ezsignbulksend_id, ezsignbulksend_create_ezsignbulksendtransmission_v1_request)

Create a new Ezsignbulksendtransmission in the Ezsignbulksend

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v1_request import EzsignbulksendCreateEzsignbulksendtransmissionV1Request
from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v1_response import EzsignbulksendCreateEzsignbulksendtransmissionV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 
    ezsignbulksend_create_ezsignbulksendtransmission_v1_request = eZmaxApi.EzsignbulksendCreateEzsignbulksendtransmissionV1Request() # EzsignbulksendCreateEzsignbulksendtransmissionV1Request | 

    try:
        # Create a new Ezsignbulksendtransmission in the Ezsignbulksend
        api_response = api_instance.ezsignbulksend_create_ezsignbulksendtransmission_v1(pki_ezsignbulksend_id, ezsignbulksend_create_ezsignbulksendtransmission_v1_request)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_create_ezsignbulksendtransmission_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_create_ezsignbulksendtransmission_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 
 **ezsignbulksend_create_ezsignbulksendtransmission_v1_request** | [**EzsignbulksendCreateEzsignbulksendtransmissionV1Request**](EzsignbulksendCreateEzsignbulksendtransmissionV1Request.md)|  | 

### Return type

[**EzsignbulksendCreateEzsignbulksendtransmissionV1Response**](EzsignbulksendCreateEzsignbulksendtransmissionV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksend_create_object_v1**
> EzsignbulksendCreateObjectV1Response ezsignbulksend_create_object_v1(ezsignbulksend_create_object_v1_request)

Create a new Ezsignbulksend

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_create_object_v1_request import EzsignbulksendCreateObjectV1Request
from eZmaxApi.models.ezsignbulksend_create_object_v1_response import EzsignbulksendCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    ezsignbulksend_create_object_v1_request = eZmaxApi.EzsignbulksendCreateObjectV1Request() # EzsignbulksendCreateObjectV1Request | 

    try:
        # Create a new Ezsignbulksend
        api_response = api_instance.ezsignbulksend_create_object_v1(ezsignbulksend_create_object_v1_request)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignbulksend_create_object_v1_request** | [**EzsignbulksendCreateObjectV1Request**](EzsignbulksendCreateObjectV1Request.md)|  | 

### Return type

[**EzsignbulksendCreateObjectV1Response**](EzsignbulksendCreateObjectV1Response.md)

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

# **ezsignbulksend_delete_object_v1**
> EzsignbulksendDeleteObjectV1Response ezsignbulksend_delete_object_v1(pki_ezsignbulksend_id)

Delete an existing Ezsignbulksend



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_delete_object_v1_response import EzsignbulksendDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 

    try:
        # Delete an existing Ezsignbulksend
        api_response = api_instance.ezsignbulksend_delete_object_v1(pki_ezsignbulksend_id)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 

### Return type

[**EzsignbulksendDeleteObjectV1Response**](EzsignbulksendDeleteObjectV1Response.md)

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

# **ezsignbulksend_edit_object_v1**
> EzsignbulksendEditObjectV1Response ezsignbulksend_edit_object_v1(pki_ezsignbulksend_id, ezsignbulksend_edit_object_v1_request)

Edit an existing Ezsignbulksend



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_edit_object_v1_request import EzsignbulksendEditObjectV1Request
from eZmaxApi.models.ezsignbulksend_edit_object_v1_response import EzsignbulksendEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 
    ezsignbulksend_edit_object_v1_request = eZmaxApi.EzsignbulksendEditObjectV1Request() # EzsignbulksendEditObjectV1Request | 

    try:
        # Edit an existing Ezsignbulksend
        api_response = api_instance.ezsignbulksend_edit_object_v1(pki_ezsignbulksend_id, ezsignbulksend_edit_object_v1_request)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 
 **ezsignbulksend_edit_object_v1_request** | [**EzsignbulksendEditObjectV1Request**](EzsignbulksendEditObjectV1Request.md)|  | 

### Return type

[**EzsignbulksendEditObjectV1Response**](EzsignbulksendEditObjectV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksend_get_csv_template_v1**
> str ezsignbulksend_get_csv_template_v1(pki_ezsignbulksend_id, e_csv_separator)

Retrieve an existing Ezsignbulksend's empty Csv template



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 
    e_csv_separator = 'e_csv_separator_example' # str | Separator that will be used to separate fields

    try:
        # Retrieve an existing Ezsignbulksend's empty Csv template
        api_response = api_instance.ezsignbulksend_get_csv_template_v1(pki_ezsignbulksend_id, e_csv_separator)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_get_csv_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_get_csv_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 
 **e_csv_separator** | **str**| Separator that will be used to separate fields | 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksend_get_ezsignbulksendtransmissions_v1**
> EzsignbulksendGetEzsignbulksendtransmissionsV1Response ezsignbulksend_get_ezsignbulksendtransmissions_v1(pki_ezsignbulksend_id)

Retrieve an existing Ezsignbulksend's Ezsignbulksendtransmissions



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_get_ezsignbulksendtransmissions_v1_response import EzsignbulksendGetEzsignbulksendtransmissionsV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksend's Ezsignbulksendtransmissions
        api_response = api_instance.ezsignbulksend_get_ezsignbulksendtransmissions_v1(pki_ezsignbulksend_id)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_get_ezsignbulksendtransmissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_get_ezsignbulksendtransmissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 

### Return type

[**EzsignbulksendGetEzsignbulksendtransmissionsV1Response**](EzsignbulksendGetEzsignbulksendtransmissionsV1Response.md)

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

# **ezsignbulksend_get_ezsignsignatures_automatic_v1**
> EzsignbulksendGetEzsignsignaturesAutomaticV1Response ezsignbulksend_get_ezsignsignatures_automatic_v1(pki_ezsignbulksend_id)

Retrieve an existing Ezsignbulksend's automatic Ezsignsignatures

Return the Ezsignsignatures that can be signed by the current user at the current step in the process

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_get_ezsignsignatures_automatic_v1_response import EzsignbulksendGetEzsignsignaturesAutomaticV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksend's automatic Ezsignsignatures
        api_response = api_instance.ezsignbulksend_get_ezsignsignatures_automatic_v1(pki_ezsignbulksend_id)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_get_ezsignsignatures_automatic_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_get_ezsignsignatures_automatic_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 

### Return type

[**EzsignbulksendGetEzsignsignaturesAutomaticV1Response**](EzsignbulksendGetEzsignsignaturesAutomaticV1Response.md)

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

# **ezsignbulksend_get_forms_data_v1**
> EzsignbulksendGetFormsDataV1Response ezsignbulksend_get_forms_data_v1(pki_ezsignbulksend_id)

Retrieve an existing Ezsignbulksend's forms data



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_get_forms_data_v1_response import EzsignbulksendGetFormsDataV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksend's forms data
        api_response = api_instance.ezsignbulksend_get_forms_data_v1(pki_ezsignbulksend_id)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_get_forms_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_get_forms_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 

### Return type

[**EzsignbulksendGetFormsDataV1Response**](EzsignbulksendGetFormsDataV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksend_get_list_v1**
> EzsignbulksendGetListV1Response ezsignbulksend_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Ezsignbulksend list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsignfoldertypePrivacylevel | User<br>Usergroup |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_get_list_v1_response import EzsignbulksendGetListV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Ezsignbulksend list
        api_response = api_instance.ezsignbulksend_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_get_list_v1: %s\n" % e)
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

[**EzsignbulksendGetListV1Response**](EzsignbulksendGetListV1Response.md)

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

# **ezsignbulksend_get_object_v2**
> EzsignbulksendGetObjectV2Response ezsignbulksend_get_object_v2(pki_ezsignbulksend_id)

Retrieve an existing Ezsignbulksend



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_get_object_v2_response import EzsignbulksendGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksend
        api_response = api_instance.ezsignbulksend_get_object_v2(pki_ezsignbulksend_id)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 

### Return type

[**EzsignbulksendGetObjectV2Response**](EzsignbulksendGetObjectV2Response.md)

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

# **ezsignbulksend_reorder_v1**
> EzsignbulksendReorderV1Response ezsignbulksend_reorder_v1(pki_ezsignbulksend_id, ezsignbulksend_reorder_v1_request)

Reorder Ezsignbulksenddocumentmappings in the Ezsignbulksend

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignbulksend_reorder_v1_request import EzsignbulksendReorderV1Request
from eZmaxApi.models.ezsignbulksend_reorder_v1_response import EzsignbulksendReorderV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendApi(api_client)
    pki_ezsignbulksend_id = 56 # int | 
    ezsignbulksend_reorder_v1_request = eZmaxApi.EzsignbulksendReorderV1Request() # EzsignbulksendReorderV1Request | 

    try:
        # Reorder Ezsignbulksenddocumentmappings in the Ezsignbulksend
        api_response = api_instance.ezsignbulksend_reorder_v1(pki_ezsignbulksend_id, ezsignbulksend_reorder_v1_request)
        print("The response of ObjectEzsignbulksendApi->ezsignbulksend_reorder_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendApi->ezsignbulksend_reorder_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksend_id** | **int**|  | 
 **ezsignbulksend_reorder_v1_request** | [**EzsignbulksendReorderV1Request**](EzsignbulksendReorderV1Request.md)|  | 

### Return type

[**EzsignbulksendReorderV1Response**](EzsignbulksendReorderV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

