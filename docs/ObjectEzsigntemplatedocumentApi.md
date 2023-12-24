# eZmaxApi.ObjectEzsigntemplatedocumentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatedocument_create_object_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_create_object_v1) | **POST** /1/object/ezsigntemplatedocument | Create a new Ezsigntemplatedocument
[**ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1) | **PUT** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplateformfieldgroups | Edit multiple Ezsigntemplateformfieldgroups
[**ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1) | **PUT** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatesignatures | Edit multiple Ezsigntemplatesignatures
[**ezsigntemplatedocument_edit_object_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_edit_object_v1) | **PUT** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID} | Edit an existing Ezsigntemplatedocument
[**ezsigntemplatedocument_flatten_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_flatten_v1) | **POST** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/flatten | Flatten
[**ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatedocumentpages | Retrieve an existing Ezsigntemplatedocument&#39;s Ezsigntemplatedocumentpages
[**ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplateformfieldgroups | Retrieve an existing Ezsigntemplatedocument&#39;s Ezsigntemplateformfieldgroups
[**ezsigntemplatedocument_get_ezsigntemplatesignatures_v1**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_ezsigntemplatesignatures_v1) | **GET** /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatesignatures | Retrieve an existing Ezsigntemplatedocument&#39;s Ezsigntemplatesignatures
[**ezsigntemplatedocument_get_object_v2**](ObjectEzsigntemplatedocumentApi.md#ezsigntemplatedocument_get_object_v2) | **GET** /2/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID} | Retrieve an existing Ezsigntemplatedocument
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_create_object_v1_request import EzsigntemplatedocumentCreateObjectV1Request
from eZmaxApi.models.ezsigntemplatedocument_create_object_v1_response import EzsigntemplatedocumentCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    ezsigntemplatedocument_create_object_v1_request = eZmaxApi.EzsigntemplatedocumentCreateObjectV1Request() # EzsigntemplatedocumentCreateObjectV1Request | 

    try:
        # Create a new Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_create_object_v1(ezsigntemplatedocument_create_object_v1_request)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request import EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_response import EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 
    ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request = eZmaxApi.EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request() # EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request | 

    try:
        # Edit multiple Ezsigntemplateformfieldgroups
        api_response = api_instance.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request import EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response import EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 
    ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request = eZmaxApi.EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request() # EzsigntemplatedocumentEditEzsigntemplatesignaturesV1Request | 

    try:
        # Edit multiple Ezsigntemplatesignatures
        api_response = api_instance.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_request)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_edit_object_v1_request import EzsigntemplatedocumentEditObjectV1Request
from eZmaxApi.models.ezsigntemplatedocument_edit_object_v1_response import EzsigntemplatedocumentEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 
    ezsigntemplatedocument_edit_object_v1_request = eZmaxApi.EzsigntemplatedocumentEditObjectV1Request() # EzsigntemplatedocumentEditObjectV1Request | 

    try:
        # Edit an existing Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_edit_object_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_edit_object_v1_request)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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

# **ezsigntemplatedocument_flatten_v1**
> EzsigntemplatedocumentFlattenV1Response ezsigntemplatedocument_flatten_v1(pki_ezsigntemplatedocument_id, body)

Flatten

Flatten an Ezsigntemplatedocument signatures, forms and annotations. This process finalizes the PDF so that the forms and annotations become part of the document content and cannot be edited.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_flatten_v1_response import EzsigntemplatedocumentFlattenV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 
    body = None # object | 

    try:
        # Flatten
        api_response = api_instance.ezsigntemplatedocument_flatten_v1(pki_ezsigntemplatedocument_id, body)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_flatten_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_flatten_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzsigntemplatedocumentFlattenV1Response**](EzsigntemplatedocumentFlattenV1Response.md)

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

# **ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1**
> EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1(pki_ezsigntemplatedocument_id)

Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatedocumentpages



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response import EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatedocumentpages
        api_response = api_instance.ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1(pki_ezsigntemplatedocument_id)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response import EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatedocument's Ezsigntemplateformfieldgroups
        api_response = api_instance.ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1(pki_ezsigntemplatedocument_id)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatesignatures_v1_response import EzsigntemplatedocumentGetEzsigntemplatesignaturesV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatedocument's Ezsigntemplatesignatures
        api_response = api_instance.ezsigntemplatedocument_get_ezsigntemplatesignatures_v1(pki_ezsigntemplatedocument_id)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_ezsigntemplatesignatures_v1:\n")
        pprint(api_response)
    except Exception as e:
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

# **ezsigntemplatedocument_get_object_v2**
> EzsigntemplatedocumentGetObjectV2Response ezsigntemplatedocument_get_object_v2(pki_ezsigntemplatedocument_id)

Retrieve an existing Ezsigntemplatedocument



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_get_object_v2_response import EzsigntemplatedocumentGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_get_object_v2(pki_ezsigntemplatedocument_id)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigntemplatedocument_id** | **int**|  | 

### Return type

[**EzsigntemplatedocumentGetObjectV2Response**](EzsigntemplatedocumentGetObjectV2Response.md)

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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_get_words_positions_v1_request import EzsigntemplatedocumentGetWordsPositionsV1Request
from eZmaxApi.models.ezsigntemplatedocument_get_words_positions_v1_response import EzsigntemplatedocumentGetWordsPositionsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 
    ezsigntemplatedocument_get_words_positions_v1_request = eZmaxApi.EzsigntemplatedocumentGetWordsPositionsV1Request() # EzsigntemplatedocumentGetWordsPositionsV1Request | 

    try:
        # Retrieve positions X,Y of given words from a Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_get_words_positions_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_get_words_positions_v1_request)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_get_words_positions_v1:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import eZmaxApi
from eZmaxApi.models.ezsigntemplatedocument_patch_object_v1_request import EzsigntemplatedocumentPatchObjectV1Request
from eZmaxApi.models.ezsigntemplatedocument_patch_object_v1_response import EzsigntemplatedocumentPatchObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigntemplatedocumentApi(api_client)
    pki_ezsigntemplatedocument_id = 56 # int | 
    ezsigntemplatedocument_patch_object_v1_request = eZmaxApi.EzsigntemplatedocumentPatchObjectV1Request() # EzsigntemplatedocumentPatchObjectV1Request | 

    try:
        # Patch an existing Ezsigntemplatedocument
        api_response = api_instance.ezsigntemplatedocument_patch_object_v1(pki_ezsigntemplatedocument_id, ezsigntemplatedocument_patch_object_v1_request)
        print("The response of ObjectEzsigntemplatedocumentApi->ezsigntemplatedocument_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
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

