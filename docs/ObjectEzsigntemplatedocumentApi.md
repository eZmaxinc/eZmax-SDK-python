# eZmaxApi.ObjectEzsigntemplatedocumentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatedocument_create_object_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_create_object_v1) | **POST** /1/object/ezsigntemplatedocument | Create a new Ezsigntemplatedocument
[**ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1) | **PUT** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplateformfieldgroups | Edit multiple Ezsigntemplateformfieldgroups
[**ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1) | **PUT** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatesignatures | Edit multiple Ezsigntemplatesignatures
[**ezsigntemplatedocument_edit_object_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_edit_object_v1) | **PUT** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID} | Edit an existing Ezsigntemplatedocument
[**ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatedocumentpages | Retrieve an existing Ezsigntemplatedocument&#39;s Ezsigntemplatedocumentpages
[**ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplateformfieldgroups | Retrieve an existing Ezsigntemplatedocument&#39;s Ezsigntemplateformfieldgroups
[**ezsigntemplatedocument_get_ezsigntemplatesignatures_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_ezsigntemplatesignatures_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatesignatures | Retrieve an existing Ezsigntemplatedocument&#39;s Ezsigntemplatesignatures
[**ezsigntemplatedocument_get_object_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_object_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID} | Retrieve an existing Ezsigntemplatedocument
[**ezsigntemplatedocument_get_words_positions_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_words_positions_v1) | **POST** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getWordsPositions | Retrieve positions X,Y of given words from a Ezsigntemplatedocument
[**ezsigntemplatedocument_patch_object_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_patch_object_v1) | **PATCH** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID} | Patch an existing Ezsigntemplatedocument


# **ezsigntemplatedocument_create_object_v1**
> EzsigntemplatedocumentCreateObjectV1Response ezsigntemplatedocument_create_object_v1(ezsigntemplatedocument_create_object_v1_request)

Create a new Ezsigntemplatedocument

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_create_object_v1_request import EzsigntemplatedocumentCreateObjectV1Request
from eZmaxApi.model.ezsigntemplatedocument_create_object_v1_response import EzsigntemplatedocumentCreateObjectV1Response
from eZmaxApi.model.common_response_error_s_temporary_file_url import CommonResponseErrorSTemporaryFileUrl
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    ezsigntemplatedocument_create_object_v1_request = EzsigntemplatedocumentCreateObjectV1Request(
        a_obj_ezsigntemplatedocument=[
            EzsigntemplatedocumentRequestCompound(),
        ],
    ) # EzsigntemplatedocumentCreateObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_create_object_v1(ezsigntemplatedocument_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigntemplatedocument_create_object_v1_request** | [**EzsigntemplatedocumentCreateObjectV1Request**](EzsigntemplatedocumentCreateObjectV1Request.md)|  |

### Return type

[**EzsigntemplatedocumentCreateObjectV1Response**](EzsigntemplatedocumentCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. If the error is recoverable sTemporaryFileUrl will be set and you can use this url to try a new request without sending the file over again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1**
> EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Response ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request)

Edit multiple Ezsigntemplateformfieldgroups

Using this endpoint, you can edit multiple Ezsigntemplateformfieldgroups at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_response import EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request import EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 
    ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request = EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request(
        a_obj_ezsigntemplateformfieldgroup=[
            EzsigntemplateformfieldgroupRequestCompound(),
        ],
    ) # EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit multiple Ezsigntemplateformfieldgroups
        api_response = api_instance.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |
 **ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request** | [**EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request**](EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request.md)|  |

### Return type

[**EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Response**](EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Response.md)

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

# **ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1**
> EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request)

Edit multiple Ezsigntemplatesignatures

Using this endpoint, you can edit multiple Ezsigntemplatesignatures at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response import EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request import EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 
    ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request = EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request(
        a_obj_ezsigntemplatesignature=[
            EzsigntemplatesignatureRequestCompound(),
        ],
    ) # EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit multiple Ezsigntemplatesignatures
        api_response = api_instance.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |
 **ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request** | [**EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request**](EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request.md)|  |

### Return type

[**EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response**](EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response.md)

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

# **ezsigntemplatedocument_edit_object_v1**
> EzsigntemplatedocumentEditObjectV1Response ezsigntemplatedocument_edit_object_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_object_v1_request)

Edit an existing Ezsigntemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_edit_object_v1_response import EzsigntemplatedocumentEditObjectV1Response
from eZmaxApi.model.ezsigntemplatedocument_edit_object_v1_request import EzsigntemplatedocumentEditObjectV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.common_response_error_s_temporary_file_url import CommonResponseErrorSTemporaryFileUrl
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 
    ezsigntemplatedocument_edit_object_v1_request = EzsigntemplatedocumentEditObjectV1Request(
        obj_ezsigntemplatedocument=EzsigntemplatedocumentRequestCompound(),
    ) # EzsigntemplatedocumentEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_edit_object_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |
 **ezsigntemplatedocument_edit_object_v1_request** | [**EzsigntemplatedocumentEditObjectV1Request**](EzsigntemplatedocumentEditObjectV1Request.md)|  |

### Return type

[**EzsigntemplatedocumentEditObjectV1Response**](EzsigntemplatedocumentEditObjectV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. If the error is recoverable sTemporaryFileUrl will be set and you can use this url to try a new request without sending the file over again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1**
> EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1(pki_ezsigntemplatedocument_id)

Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatedocumentpages



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response import EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatedocumentpages
        api_response = api_instance.ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1(pki_ezsigntemplatedocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |

### Return type

[**EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response**](EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response.md)

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

# **ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1**
> EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1(pki_ezsigntemplatedocument_id)

Retrieve an existing Ezsigntemplatedocument's Ezsigntemplateformfieldgroups



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response import EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatedocument's Ezsigntemplateformfieldgroups
        api_response = api_instance.ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1(pki_ezsigntemplatedocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |

### Return type

[**EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response**](EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response.md)

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

# **ezsigntemplatedocument_get_ezsigntemplatesignatures_v1**
> EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response ezsigntemplatedocument_get_ezsigntemplatesignatures_v1(pki_ezsigntemplatedocument_id)

Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatesignatures



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response import EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatesignatures
        api_response = api_instance.ezsigntemplatedocument_get_ezsigntemplatesignatures_v1(pki_ezsigntemplatedocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_ezsigntemplatesignatures_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |

### Return type

[**EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response**](EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response.md)

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

# **ezsigntemplatedocument_get_object_v1**
> EzsigntemplatedocumentGetObjectV1Response ezsigntemplatedocument_get_object_v1(pki_ezsigntemplatedocument_id)

Retrieve an existing Ezsigntemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_get_object_v1_response import EzsigntemplatedocumentGetObjectV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_get_object_v1(pki_ezsigntemplatedocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |

### Return type

[**EzsigntemplatedocumentGetObjectV1Response**](EzsigntemplatedocumentGetObjectV1Response.md)

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

# **ezsigntemplatedocument_get_words_positions_v1**
> EzsigntemplatedocumentGetWordsPositionsV1Response ezsigntemplatedocument_get_words_positions_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_get_words_positions_v1_request)

Retrieve positions X,Y of given words from a Ezsigntemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_get_words_positions_v1_request import EzsigntemplatedocumentGetWordsPositionsV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatedocument_get_words_positions_v1_response import EzsigntemplatedocumentGetWordsPositionsV1Response
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 
    ezsigntemplatedocument_get_words_positions_v1_request = EzsigntemplatedocumentGetWordsPositionsV1Request(
        e_get="All",
        b_word_case_sensitive=True,
        a_s_word=[
            "a_s_word_example",
        ],
    ) # EzsigntemplatedocumentGetWordsPositionsV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve positions X,Y of given words from a Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_get_words_positions_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_get_words_positions_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_words_positions_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |
 **ezsigntemplatedocument_get_words_positions_v1_request** | [**EzsigntemplatedocumentGetWordsPositionsV1Request**](EzsigntemplatedocumentGetWordsPositionsV1Request.md)|  |

### Return type

[**EzsigntemplatedocumentGetWordsPositionsV1Response**](EzsigntemplatedocumentGetWordsPositionsV1Response.md)

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

# **ezsigntemplatedocument_patch_object_v1**
> EzsigntemplatedocumentPatchObjectV1Response ezsigntemplatedocument_patch_object_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_patch_object_v1_request)

Patch an existing Ezsigntemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatedocument_api
from eZmaxApi.model.ezsigntemplatedocument_patch_object_v1_request import EzsigntemplatedocumentPatchObjectV1Request
from eZmaxApi.model.ezsigntemplatedocument_patch_object_v1_response import EzsigntemplatedocumentPatchObjectV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
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
    api_instance = object_ezsigntemplatedocument_api.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = FieldPkiEzsigntemplatedocumentID(133) # int | 
    ezsigntemplatedocument_patch_object_v1_request = EzsigntemplatedocumentPatchObjectV1Request(
        obj_ezsigntemplatedocument=EzsigntemplatedocumentRequestPatch(
            s_ezsigntemplatedocument_name="Standard Contract",
        ),
    ) # EzsigntemplatedocumentPatchObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Patch an existing Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_patch_object_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_patch_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_patch_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  |
 **ezsigntemplatedocument_patch_object_v1_request** | [**EzsigntemplatedocumentPatchObjectV1Request**](EzsigntemplatedocumentPatchObjectV1Request.md)|  |

### Return type

[**EzsigntemplatedocumentPatchObjectV1Response**](EzsigntemplatedocumentPatchObjectV1Response.md)

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

