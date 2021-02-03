# eZmaxinc/eZmax-SDK-python.ObjectEzsigndocumentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigndocument_apply_ezsigntemplate_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_apply_ezsigntemplate_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate | Apply an Ezsign Template to the Ezsigndocument.
[**ezsigndocument_create_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_create_object_v1) | **POST** /1/object/ezsigndocument | Create a new Ezsigndocument
[**ezsigndocument_delete_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_delete_object_v1) | **DELETE** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Delete an existing Ezsigndocument
[**ezsigndocument_edit_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_edit_object_v1) | **PUT** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Modify an existing Ezsigndocument
[**ezsigndocument_get_download_url_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_download_url_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getDownloadUrl/{eDocumentType} | Retrieve a URL to download documents.
[**ezsigndocument_get_object_get_children_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_object_get_children_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getChildren | Retrieve an existing Ezsigndocument&#39;s children IDs
[**ezsigndocument_get_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_object_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Retrieve an existing Ezsigndocument


# **ezsigndocument_apply_ezsigntemplate_v1**
> EzsigndocumentApplyEzsigntemplateV1Response ezsigndocument_apply_ezsigntemplate_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v1_request)

Apply an Ezsign Template to the Ezsigndocument.

This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_apply_ezsigntemplate_v1_request import EzsigndocumentApplyEzsigntemplateV1Request
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_apply_ezsigntemplate_v1_response import EzsigndocumentApplyEzsigntemplateV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 1 # int | The unique ID of the Ezsigndocument
    ezsigndocument_apply_ezsigntemplate_v1_request = EzsigndocumentApplyEzsigntemplateV1Request(
        fki_ezsigntemplate_id=36,
        a_s_ezsigntemplatesigner=[
            "John",
        ],
        a_pki_ezsignfoldersignerassociation_id=[
            20,
        ],
    ) # EzsigndocumentApplyEzsigntemplateV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Apply an Ezsign Template to the Ezsigndocument.
        api_response = api_instance.ezsigndocument_apply_ezsigntemplate_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**| The unique ID of the Ezsigndocument |
 **ezsigndocument_apply_ezsigntemplate_v1_request** | [**EzsigndocumentApplyEzsigntemplateV1Request**](EzsigndocumentApplyEzsigntemplateV1Request.md)|  |

### Return type

[**EzsigndocumentApplyEzsigntemplateV1Response**](EzsigndocumentApplyEzsigntemplateV1Response.md)

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

# **ezsigndocument_create_object_v1**
> EzsigndocumentCreateObjectV1Response ezsigndocument_create_object_v1(ezsigndocument_create_object_v1_request)

Create a new Ezsigndocument

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_create_object_v1_request import EzsigndocumentCreateObjectV1Request
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_create_object_v1_response import EzsigndocumentCreateObjectV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    ezsigndocument_create_object_v1_request = [
        EzsigndocumentCreateObjectV1Request(
            obj_ezsigndocument=EzsigndocumentRequest(
                e_ezsigndocument_source="Base64",
                e_ezsigndocument_format="Pdf",
                s_ezsigndocument_base64='YQ==',
                fki_ezsignfolder_id=1,
                dt_ezsigndocument_duedate="2020-12-31 23:59:59",
                fki_language_id=FieldPkiLanguageID(2),
                s_ezsigndocument_filename="s_ezsigndocument_filename_example",
                s_ezsigndocument_name="s_ezsigndocument_name_example",
            ),
            obj_ezsigndocument_compound=EzsigndocumentRequestCompound(),
        ),
    ] # [EzsigndocumentCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigndocument
        api_response = api_instance.ezsigndocument_create_object_v1(ezsigndocument_create_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_create_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigndocument_create_object_v1_request** | [**[EzsigndocumentCreateObjectV1Request]**](EzsigndocumentCreateObjectV1Request.md)|  |

### Return type

[**EzsigndocumentCreateObjectV1Response**](EzsigndocumentCreateObjectV1Response.md)

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

# **ezsigndocument_delete_object_v1**
> EzsigndocumentDeleteObjectV1Response ezsigndocument_delete_object_v1(pki_ezsigndocument_id)

Delete an existing Ezsigndocument

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_delete_object_v1_response import EzsigndocumentDeleteObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 1 # int | The unique ID of the Ezsigndocument

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_delete_object_v1(pki_ezsigndocument_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_delete_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**| The unique ID of the Ezsigndocument |

### Return type

[**EzsigndocumentDeleteObjectV1Response**](EzsigndocumentDeleteObjectV1Response.md)

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
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_edit_object_v1**
> EzsigndocumentEditObjectV1Response ezsigndocument_edit_object_v1(pki_ezsigndocument_id, ezsigndocument_edit_object_v1_request)

Modify an existing Ezsigndocument

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_edit_object_v1_request import EzsigndocumentEditObjectV1Request
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_edit_object_v1_response import EzsigndocumentEditObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 1 # int | The unique ID of the Ezsigndocument
    ezsigndocument_edit_object_v1_request = EzsigndocumentEditObjectV1Request(
        obj_ezsigndocument=EzsigndocumentRequest(
            e_ezsigndocument_source="Base64",
            e_ezsigndocument_format="Pdf",
            s_ezsigndocument_base64='YQ==',
            fki_ezsignfolder_id=1,
            dt_ezsigndocument_duedate="2020-12-31 23:59:59",
            fki_language_id=FieldPkiLanguageID(2),
            s_ezsigndocument_filename="s_ezsigndocument_filename_example",
            s_ezsigndocument_name="s_ezsigndocument_name_example",
        ),
    ) # EzsigndocumentEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Modify an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_edit_object_v1(pki_ezsigndocument_id, ezsigndocument_edit_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_edit_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**| The unique ID of the Ezsigndocument |
 **ezsigndocument_edit_object_v1_request** | [**EzsigndocumentEditObjectV1Request**](EzsigndocumentEditObjectV1Request.md)|  |

### Return type

[**EzsigndocumentEditObjectV1Response**](EzsigndocumentEditObjectV1Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_download_url_v1**
> EzsigndocumentGetDownloadUrlV1Response ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type)

Retrieve a URL to download documents.

This endpoint returns URLs to different files that can be downloaded during the signing process.  These links will expire after 5 minutes so the download of the file should be made soon after retrieving the link.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_get_download_url_v1_response import EzsigndocumentGetDownloadUrlV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 1 # int | The unique ID of the Ezsigndocument
    e_document_type = "Initial" # str | The type of document to retrieve.  1. **Initial** Is the initial document before any signature were applied. 2. **Signed** Is the final document once all signatures were applied. 3. **Proofdocument** Is the evidence report. 4. **Proof** Is the complete evidence archive including all of the above and more. 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a URL to download documents.
        api_response = api_instance.ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_download_url_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**| The unique ID of the Ezsigndocument |
 **e_document_type** | **str**| The type of document to retrieve.  1. **Initial** Is the initial document before any signature were applied. 2. **Signed** Is the final document once all signatures were applied. 3. **Proofdocument** Is the evidence report. 4. **Proof** Is the complete evidence archive including all of the above and more.  |

### Return type

[**EzsigndocumentGetDownloadUrlV1Response**](EzsigndocumentGetDownloadUrlV1Response.md)

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
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_object_get_children_v1**
> ezsigndocument_get_object_get_children_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's children IDs

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 1 # int | The unique ID of the Ezsigndocument

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigndocument's children IDs
        api_instance.ezsigndocument_get_object_get_children_v1(pki_ezsigndocument_id)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_object_get_children_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**| The unique ID of the Ezsigndocument |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The element you are trying to work on does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_object_v1**
> EzsigndocumentGetObjectV1Response ezsigndocument_get_object_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsigndocument_api
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_get_object_v1_response import EzsigndocumentGetObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 1 # int | The unique ID of the Ezsigndocument

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_get_object_v1(pki_ezsigndocument_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**| The unique ID of the Ezsigndocument |

### Return type

[**EzsigndocumentGetObjectV1Response**](EzsigndocumentGetObjectV1Response.md)

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

