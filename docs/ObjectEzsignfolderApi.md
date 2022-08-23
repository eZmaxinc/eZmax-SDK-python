# eZmaxApi.ObjectEzsignfolderApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignfolder_archive_v1**](ObjectEzsignfolderApi.md#ezsignfolder_archive_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/archive | Archive the Ezsignfolder
[**ezsignfolder_batch_download_v1**](ObjectEzsignfolderApi.md#ezsignfolder_batch_download_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/batchDownload | Download multiples files from an Ezsignfolder
[**ezsignfolder_create_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_create_object_v1) | **POST** /1/object/ezsignfolder | Create a new Ezsignfolder
[**ezsignfolder_create_object_v2**](ObjectEzsignfolderApi.md#ezsignfolder_create_object_v2) | **POST** /2/object/ezsignfolder | Create a new Ezsignfolder
[**ezsignfolder_delete_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_delete_object_v1) | **DELETE** /1/object/ezsignfolder/{pkiEzsignfolderID} | Delete an existing Ezsignfolder
[**ezsignfolder_dispose_ezsignfolders_v1**](ObjectEzsignfolderApi.md#ezsignfolder_dispose_ezsignfolders_v1) | **POST** /1/object/ezsignfolder/disposeEzsignfolders | Dispose Ezsignfolders
[**ezsignfolder_dispose_v1**](ObjectEzsignfolderApi.md#ezsignfolder_dispose_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/dispose | Dispose the Ezsignfolder
[**ezsignfolder_edit_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_edit_object_v1) | **PUT** /1/object/ezsignfolder/{pkiEzsignfolderID} | Edit an existing Ezsignfolder
[**ezsignfolder_get_actionable_elements_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_actionable_elements_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID}/getActionableElements | Retrieve actionable elements for the Ezsignfolder
[**ezsignfolder_get_ezsigndocuments_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_ezsigndocuments_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID}/getEzsigndocuments | Retrieve an existing Ezsignfolder&#39;s Ezsigndocuments
[**ezsignfolder_get_ezsignfoldersignerassociations_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_ezsignfoldersignerassociations_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID}/getEzsignfoldersignerassociations | Retrieve an existing Ezsignfolder&#39;s Ezsignfoldersignerassociations
[**ezsignfolder_get_forms_data_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_forms_data_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID}/getFormsData | Retrieve an existing Ezsignfolder&#39;s forms data
[**ezsignfolder_get_list_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_list_v1) | **GET** /1/object/ezsignfolder/getList | Retrieve Ezsignfolder list
[**ezsignfolder_get_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_object_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID} | Retrieve an existing Ezsignfolder
[**ezsignfolder_import_ezsignfoldersignerassociations_v1**](ObjectEzsignfolderApi.md#ezsignfolder_import_ezsignfoldersignerassociations_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsignfoldersignerassociations | Import an existing Ezsignfoldersignerassociation into this Ezsignfolder
[**ezsignfolder_import_ezsigntemplatepackage_v1**](ObjectEzsignfolderApi.md#ezsignfolder_import_ezsigntemplatepackage_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/importEzsigntemplatepackage | Import an Ezsigntemplatepackage in the Ezsignfolder.
[**ezsignfolder_reorder_v1**](ObjectEzsignfolderApi.md#ezsignfolder_reorder_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/reorder | Reorder Ezsigndocuments in the Ezsignfolder
[**ezsignfolder_send_v1**](ObjectEzsignfolderApi.md#ezsignfolder_send_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/send | Send the Ezsignfolder to the signatories for signature
[**ezsignfolder_send_v2**](ObjectEzsignfolderApi.md#ezsignfolder_send_v2) | **POST** /2/object/ezsignfolder/{pkiEzsignfolderID}/send | Send the Ezsignfolder to the signatories for signature
[**ezsignfolder_unsend_v1**](ObjectEzsignfolderApi.md#ezsignfolder_unsend_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/unsend | Unsend the Ezsignfolder


# **ezsignfolder_archive_v1**
> EzsignfolderArchiveV1Response ezsignfolder_archive_v1(pki_ezsignfolder_id, body)

Archive the Ezsignfolder



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_archive_v1_response import EzsignfolderArchiveV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Archive the Ezsignfolder
        api_response = api_instance.ezsignfolder_archive_v1(pki_ezsignfolder_id, body)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_archive_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**EzsignfolderArchiveV1Response**](EzsignfolderArchiveV1Response.md)

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

# **ezsignfolder_batch_download_v1**
> file_type ezsignfolder_batch_download_v1(pki_ezsignfolder_id, ezsignfolder_batch_download_v1_request)

Download multiples files from an Ezsignfolder

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_batch_download_v1_request import EzsignfolderBatchDownloadV1Request
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_batch_download_v1_request = EzsignfolderBatchDownloadV1Request(
        a_pki_ezsigndocument_id=[
            FieldPkiEzsigndocumentID(97),
        ],
        a_e_document_type=[
            "Signed",
        ],
    ) # EzsignfolderBatchDownloadV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Download multiples files from an Ezsignfolder
        api_response = api_instance.ezsignfolder_batch_download_v1(pki_ezsignfolder_id, ezsignfolder_batch_download_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_batch_download_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_batch_download_v1_request** | [**EzsignfolderBatchDownloadV1Request**](EzsignfolderBatchDownloadV1Request.md)|  |

### Return type

**file_type**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfolder_create_object_v1**
> EzsignfolderCreateObjectV1Response ezsignfolder_create_object_v1(ezsignfolder_create_object_v1_request)

Create a new Ezsignfolder

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_create_object_v1_response import EzsignfolderCreateObjectV1Response
from eZmaxApi.model.ezsignfolder_create_object_v1_request import EzsignfolderCreateObjectV1Request
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    ezsignfolder_create_object_v1_request = [
        EzsignfolderCreateObjectV1Request(
            obj_ezsignfolder=EzsignfolderRequest(
                pki_ezsignfolder_id=FieldPkiEzsignfolderID(33),
                fki_ezsignfoldertype_id=FieldPkiEzsignfoldertypeID(5),
                fki_ezsigntsarequirement_id=FieldPkiEzsigntsarequirementID(1),
                s_ezsignfolder_description="Test eZsign Folder",
                t_ezsignfolder_note="This is a note",
                e_ezsignfolder_sendreminderfrequency=FieldEEzsignfolderSendreminderfrequency("None"),
            ),
            obj_ezsignfolder_compound=EzsignfolderRequestCompound(),
        ),
    ] # [EzsignfolderCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignfolder
        api_response = api_instance.ezsignfolder_create_object_v1(ezsignfolder_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfolder_create_object_v1_request** | [**[EzsignfolderCreateObjectV1Request]**](EzsignfolderCreateObjectV1Request.md)|  |

### Return type

[**EzsignfolderCreateObjectV1Response**](EzsignfolderCreateObjectV1Response.md)

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

# **ezsignfolder_create_object_v2**
> EzsignfolderCreateObjectV2Response ezsignfolder_create_object_v2(ezsignfolder_create_object_v2_request)

Create a new Ezsignfolder

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_create_object_v2_request import EzsignfolderCreateObjectV2Request
from eZmaxApi.model.ezsignfolder_create_object_v2_response import EzsignfolderCreateObjectV2Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    ezsignfolder_create_object_v2_request = EzsignfolderCreateObjectV2Request(
        a_obj_ezsignfolder=[
            EzsignfolderRequestCompound(),
        ],
    ) # EzsignfolderCreateObjectV2Request | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignfolder
        api_response = api_instance.ezsignfolder_create_object_v2(ezsignfolder_create_object_v2_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_create_object_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfolder_create_object_v2_request** | [**EzsignfolderCreateObjectV2Request**](EzsignfolderCreateObjectV2Request.md)|  |

### Return type

[**EzsignfolderCreateObjectV2Response**](EzsignfolderCreateObjectV2Response.md)

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

# **ezsignfolder_delete_object_v1**
> EzsignfolderDeleteObjectV1Response ezsignfolder_delete_object_v1(pki_ezsignfolder_id)

Delete an existing Ezsignfolder

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_delete_object_v1_response import EzsignfolderDeleteObjectV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsignfolder
        api_response = api_instance.ezsignfolder_delete_object_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |

### Return type

[**EzsignfolderDeleteObjectV1Response**](EzsignfolderDeleteObjectV1Response.md)

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

# **ezsignfolder_dispose_ezsignfolders_v1**
> EzsignfolderDisposeEzsignfoldersV1Response ezsignfolder_dispose_ezsignfolders_v1(ezsignfolder_dispose_ezsignfolders_v1_request)

Dispose Ezsignfolders



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_dispose_ezsignfolders_v1_response import EzsignfolderDisposeEzsignfoldersV1Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_dispose_ezsignfolders_v1_request import EzsignfolderDisposeEzsignfoldersV1Request
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    ezsignfolder_dispose_ezsignfolders_v1_request = EzsignfolderDisposeEzsignfoldersV1Request(
        a_pki_ezsignfolder_id=[
            FieldPkiEzsignfolderID(33),
        ],
    ) # EzsignfolderDisposeEzsignfoldersV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Dispose Ezsignfolders
        api_response = api_instance.ezsignfolder_dispose_ezsignfolders_v1(ezsignfolder_dispose_ezsignfolders_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_dispose_ezsignfolders_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfolder_dispose_ezsignfolders_v1_request** | [**EzsignfolderDisposeEzsignfoldersV1Request**](EzsignfolderDisposeEzsignfoldersV1Request.md)|  |

### Return type

[**EzsignfolderDisposeEzsignfoldersV1Response**](EzsignfolderDisposeEzsignfoldersV1Response.md)

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

# **ezsignfolder_dispose_v1**
> EzsignfolderDisposeV1Response ezsignfolder_dispose_v1(pki_ezsignfolder_id, body)

Dispose the Ezsignfolder



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_dispose_v1_response import EzsignfolderDisposeV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Dispose the Ezsignfolder
        api_response = api_instance.ezsignfolder_dispose_v1(pki_ezsignfolder_id, body)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_dispose_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**EzsignfolderDisposeV1Response**](EzsignfolderDisposeV1Response.md)

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

# **ezsignfolder_edit_object_v1**
> EzsignfolderEditObjectV1Response ezsignfolder_edit_object_v1(pki_ezsignfolder_id, ezsignfolder_edit_object_v1_request)

Edit an existing Ezsignfolder



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_edit_object_v1_request import EzsignfolderEditObjectV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_edit_object_v1_response import EzsignfolderEditObjectV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_edit_object_v1_request = EzsignfolderEditObjectV1Request(
        obj_ezsignfolder=EzsignfolderRequestCompound(),
    ) # EzsignfolderEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an existing Ezsignfolder
        api_response = api_instance.ezsignfolder_edit_object_v1(pki_ezsignfolder_id, ezsignfolder_edit_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_edit_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_edit_object_v1_request** | [**EzsignfolderEditObjectV1Request**](EzsignfolderEditObjectV1Request.md)|  |

### Return type

[**EzsignfolderEditObjectV1Response**](EzsignfolderEditObjectV1Response.md)

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

# **ezsignfolder_get_actionable_elements_v1**
> EzsignfolderGetActionableElementsV1Response ezsignfolder_get_actionable_elements_v1(pki_ezsignfolder_id)

Retrieve actionable elements for the Ezsignfolder

Return the Ezsignsignatures that can be signed and Ezsignformfieldgroups that can be filled by the current user at the current step in the process

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_get_actionable_elements_v1_response import EzsignfolderGetActionableElementsV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve actionable elements for the Ezsignfolder
        api_response = api_instance.ezsignfolder_get_actionable_elements_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_actionable_elements_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |

### Return type

[**EzsignfolderGetActionableElementsV1Response**](EzsignfolderGetActionableElementsV1Response.md)

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

# **ezsignfolder_get_ezsigndocuments_v1**
> EzsignfolderGetEzsigndocumentsV1Response ezsignfolder_get_ezsigndocuments_v1(pki_ezsignfolder_id)

Retrieve an existing Ezsignfolder's Ezsigndocuments



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_get_ezsigndocuments_v1_response import EzsignfolderGetEzsigndocumentsV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfolder's Ezsigndocuments
        api_response = api_instance.ezsignfolder_get_ezsigndocuments_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_ezsigndocuments_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |

### Return type

[**EzsignfolderGetEzsigndocumentsV1Response**](EzsignfolderGetEzsigndocumentsV1Response.md)

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

# **ezsignfolder_get_ezsignfoldersignerassociations_v1**
> EzsignfolderGetEzsignfoldersignerassociationsV1Response ezsignfolder_get_ezsignfoldersignerassociations_v1(pki_ezsignfolder_id)

Retrieve an existing Ezsignfolder's Ezsignfoldersignerassociations



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_get_ezsignfoldersignerassociations_v1_response import EzsignfolderGetEzsignfoldersignerassociationsV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfolder's Ezsignfoldersignerassociations
        api_response = api_instance.ezsignfolder_get_ezsignfoldersignerassociations_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_ezsignfoldersignerassociations_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |

### Return type

[**EzsignfolderGetEzsignfoldersignerassociationsV1Response**](EzsignfolderGetEzsignfoldersignerassociationsV1Response.md)

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

# **ezsignfolder_get_forms_data_v1**
> EzsignfolderGetFormsDataV1Response ezsignfolder_get_forms_data_v1(pki_ezsignfolder_id)

Retrieve an existing Ezsignfolder's forms data



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_get_forms_data_v1_response import EzsignfolderGetFormsDataV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfolder's forms data
        api_response = api_instance.ezsignfolder_get_forms_data_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_forms_data_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |

### Return type

[**EzsignfolderGetFormsDataV1Response**](EzsignfolderGetFormsDataV1Response.md)

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

# **ezsignfolder_get_list_v1**
> EzsignfolderGetListV1Response ezsignfolder_get_list_v1()

Retrieve Ezsignfolder list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsignfolderStep | Unsent<br>Sent<br>PartiallySigned<br>Expired<br>Completed<br>Archived<br>Disposed| | eEzsignfoldertypePrivacylevel | User<br>Usergroup |

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_get_list_v1_response import EzsignfolderGetListV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    e_order_by = "pkiEzsignfolderID_ASC" # str | Specify how you want the results to be sorted (optional)
    i_row_max = FieldIRowMax(100) # int |  (optional)
    i_row_offset = FieldIRowOffset(0) # int |  (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)
    s_filter = "bField1 eq true and iField2 gte 0 and iField2 lte 1000 and sField3 eq 'Other' and eField4 eq 'Paid' and sField5 like '%needle%' and iField6 in '1,2,3' and dtField7 rg '=m,=3mm'" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Ezsignfolder list
        api_response = api_instance.ezsignfolder_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_list_v1: %s\n" % e)
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

[**EzsignfolderGetListV1Response**](EzsignfolderGetListV1Response.md)

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

# **ezsignfolder_get_object_v1**
> EzsignfolderGetObjectV1Response ezsignfolder_get_object_v1(pki_ezsignfolder_id)

Retrieve an existing Ezsignfolder

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_get_object_v1_response import EzsignfolderGetObjectV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfolder
        api_response = api_instance.ezsignfolder_get_object_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |

### Return type

[**EzsignfolderGetObjectV1Response**](EzsignfolderGetObjectV1Response.md)

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

# **ezsignfolder_import_ezsignfoldersignerassociations_v1**
> EzsignfolderImportEzsignfoldersignerassociationsV1Response ezsignfolder_import_ezsignfoldersignerassociations_v1(pki_ezsignfolder_id, ezsignfolder_import_ezsignfoldersignerassociations_v1_request)

Import an existing Ezsignfoldersignerassociation into this Ezsignfolder



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_import_ezsignfoldersignerassociations_v1_request import EzsignfolderImportEzsignfoldersignerassociationsV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_import_ezsignfoldersignerassociations_v1_response import EzsignfolderImportEzsignfoldersignerassociationsV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_import_ezsignfoldersignerassociations_v1_request = EzsignfolderImportEzsignfoldersignerassociationsV1Request(
        a_fki_ezsignfoldersignerassociation_id=[
            FieldPkiEzsignfoldersignerassociationID(20),
        ],
    ) # EzsignfolderImportEzsignfoldersignerassociationsV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Import an existing Ezsignfoldersignerassociation into this Ezsignfolder
        api_response = api_instance.ezsignfolder_import_ezsignfoldersignerassociations_v1(pki_ezsignfolder_id, ezsignfolder_import_ezsignfoldersignerassociations_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_import_ezsignfoldersignerassociations_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_import_ezsignfoldersignerassociations_v1_request** | [**EzsignfolderImportEzsignfoldersignerassociationsV1Request**](EzsignfolderImportEzsignfoldersignerassociationsV1Request.md)|  |

### Return type

[**EzsignfolderImportEzsignfoldersignerassociationsV1Response**](EzsignfolderImportEzsignfoldersignerassociationsV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfolder_import_ezsigntemplatepackage_v1**
> EzsignfolderImportEzsigntemplatepackageV1Response ezsignfolder_import_ezsigntemplatepackage_v1(pki_ezsignfolder_id, ezsignfolder_import_ezsigntemplatepackage_v1_request)

Import an Ezsigntemplatepackage in the Ezsignfolder.

This endpoint imports all of the Ezsigntemplates from the Ezsigntemplatepackage into the Ezsignfolder as Ezsigndocuments.  This allows to automatically apply all the Ezsigntemplateformfieldgroups and Ezsigntemplatesignatures on the newly created Ezsigndocuments in a single step.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_import_ezsigntemplatepackage_v1_request import EzsignfolderImportEzsigntemplatepackageV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_import_ezsigntemplatepackage_v1_response import EzsignfolderImportEzsigntemplatepackageV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_import_ezsigntemplatepackage_v1_request = EzsignfolderImportEzsigntemplatepackageV1Request(
        fki_ezsigntemplatepackage_id=FieldPkiEzsigntemplatepackageID(99),
        dt_ezsigndocument_duedate="2020-12-31 23:59:59",
        a_obj_import_ezsigntemplatepackage_relation=[
            CustomImportEzsigntemplatepackageRelationRequest(
                fki_ezsigntemplatepackagesigner_id=FieldPkiEzsigntemplatepackagesignerID(174),
                fki_ezsignfoldersignerassociation_id=FieldPkiEzsignfoldersignerassociationID(20),
                s_ezsigntemplatepackagesigner_description="Customer",
            ),
        ],
    ) # EzsignfolderImportEzsigntemplatepackageV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Import an Ezsigntemplatepackage in the Ezsignfolder.
        api_response = api_instance.ezsignfolder_import_ezsigntemplatepackage_v1(pki_ezsignfolder_id, ezsignfolder_import_ezsigntemplatepackage_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_import_ezsigntemplatepackage_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_import_ezsigntemplatepackage_v1_request** | [**EzsignfolderImportEzsigntemplatepackageV1Request**](EzsignfolderImportEzsigntemplatepackageV1Request.md)|  |

### Return type

[**EzsignfolderImportEzsigntemplatepackageV1Response**](EzsignfolderImportEzsigntemplatepackageV1Response.md)

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

# **ezsignfolder_reorder_v1**
> EzsignfolderReorderV1Response ezsignfolder_reorder_v1(pki_ezsignfolder_id, ezsignfolder_reorder_v1_request)

Reorder Ezsigndocuments in the Ezsignfolder

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_reorder_v1_request import EzsignfolderReorderV1Request
from eZmaxApi.model.ezsignfolder_reorder_v1_response import EzsignfolderReorderV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_reorder_v1_request = EzsignfolderReorderV1Request(
        a_pki_ezsigndocument_id=[
            FieldPkiEzsigndocumentID(97),
        ],
    ) # EzsignfolderReorderV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Reorder Ezsigndocuments in the Ezsignfolder
        api_response = api_instance.ezsignfolder_reorder_v1(pki_ezsignfolder_id, ezsignfolder_reorder_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_reorder_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_reorder_v1_request** | [**EzsignfolderReorderV1Request**](EzsignfolderReorderV1Request.md)|  |

### Return type

[**EzsignfolderReorderV1Response**](EzsignfolderReorderV1Response.md)

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

# **ezsignfolder_send_v1**
> EzsignfolderSendV1Response ezsignfolder_send_v1(pki_ezsignfolder_id, ezsignfolder_send_v1_request)

Send the Ezsignfolder to the signatories for signature



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_send_v1_request import EzsignfolderSendV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_send_v1_response import EzsignfolderSendV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_send_v1_request = EzsignfolderSendV1Request(
        t_extra_message='''Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary''',
    ) # EzsignfolderSendV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Send the Ezsignfolder to the signatories for signature
        api_response = api_instance.ezsignfolder_send_v1(pki_ezsignfolder_id, ezsignfolder_send_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_send_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_send_v1_request** | [**EzsignfolderSendV1Request**](EzsignfolderSendV1Request.md)|  |

### Return type

[**EzsignfolderSendV1Response**](EzsignfolderSendV1Response.md)

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

# **ezsignfolder_send_v2**
> EzsignfolderSendV2Response ezsignfolder_send_v2(pki_ezsignfolder_id, ezsignfolder_send_v2_request)

Send the Ezsignfolder to the signatories for signature



### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_send_v2_response import EzsignfolderSendV2Response
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsignfolder_send_v2_request import EzsignfolderSendV2Request
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    ezsignfolder_send_v2_request = EzsignfolderSendV2Request(
        t_ezsignfolder_message='''Hi everyone,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary''',
        a_fki_ezsignfoldersignerassociation_id=[
            FieldPkiEzsignfoldersignerassociationID(20),
        ],
        a_obj_ezsignfoldersignerassociationmessage=[
            CustomEzsignfoldersignerassociationmessageRequest(
                fki_ezsignfoldersignerassociation_id=FieldPkiEzsignfoldersignerassociationID(20),
                t_ezsignfoldersignerassociation_message='''Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary''',
            ),
        ],
    ) # EzsignfolderSendV2Request | 

    # example passing only required values which don't have defaults set
    try:
        # Send the Ezsignfolder to the signatories for signature
        api_response = api_instance.ezsignfolder_send_v2(pki_ezsignfolder_id, ezsignfolder_send_v2_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_send_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **ezsignfolder_send_v2_request** | [**EzsignfolderSendV2Request**](EzsignfolderSendV2Request.md)|  |

### Return type

[**EzsignfolderSendV2Response**](EzsignfolderSendV2Response.md)

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

# **ezsignfolder_unsend_v1**
> EzsignfolderUnsendV1Response ezsignfolder_unsend_v1(pki_ezsignfolder_id, body)

Unsend the Ezsignfolder

Once an Ezsignfolder has been sent to signatories, it cannot be modified.  Using this endpoint, you can unsend the Ezsignfolder and make it modifiable again.  Signatories will receive an email informing them the signature process was aborted and they might receive a new invitation to sign.  ⚠️ Warning: Any signature previously made by signatories on \"Non-completed\" Ezsigndocuments will be lost.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsignfolder_api
from eZmaxApi.model.ezsignfolder_unsend_v1_response import EzsignfolderUnsendV1Response
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
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = FieldPkiEzsignfolderID(33) # int | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Unsend the Ezsignfolder
        api_response = api_instance.ezsignfolder_unsend_v1(pki_ezsignfolder_id, body)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_unsend_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**EzsignfolderUnsendV1Response**](EzsignfolderUnsendV1Response.md)

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

