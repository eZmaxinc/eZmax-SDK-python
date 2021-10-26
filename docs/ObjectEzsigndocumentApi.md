# eZmaxApi.ObjectEzsigndocumentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigndocument_apply_ezsigntemplate_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_apply_ezsigntemplate_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate | Apply an Ezsign Template to the Ezsigndocument.
[**ezsigndocument_apply_ezsigntemplate_v2**](ObjectEzsigndocumentApi.md#ezsigndocument_apply_ezsigntemplate_v2) | **POST** /2/object/ezsigndocument/{pkiEzsigndocumentID}/applyEzsigntemplate | Apply an Ezsign Template to the Ezsigndocument.
[**ezsigndocument_create_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_create_object_v1) | **POST** /1/object/ezsigndocument | Create a new Ezsigndocument
[**ezsigndocument_delete_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_delete_object_v1) | **DELETE** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Delete an existing Ezsigndocument
[**ezsigndocument_get_children_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_children_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getChildren | Retrieve an existing Ezsigndocument&#39;s children IDs
[**ezsigndocument_get_download_url_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_download_url_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getDownloadUrl/{eDocumentType} | Retrieve a URL to download documents.
[**ezsigndocument_get_ezsignpages_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsignpages_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignpages | Retrieve an existing Ezsigndocument&#39;s Ezsignpages
[**ezsigndocument_get_form_data_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_form_data_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getFormData | Retrieve an existing Ezsigndocument&#39;s Form Data
[**ezsigndocument_get_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_object_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Retrieve an existing Ezsigndocument
[**ezsigndocument_get_words_positions_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_words_positions_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getWordsPositions | Retrieve positions X,Y of given words from a Ezsigndocument


# **ezsigndocument_apply_ezsigntemplate_v1**
> EzsigndocumentApplyEzsigntemplateV1Response ezsigndocument_apply_ezsigntemplate_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v1_request)

Apply an Ezsign Template to the Ezsigndocument.

This function is deprecated. Please use *applyEzsigntemplate* instead which is doing the same thing but with a capital \"E\" to normalize the nomenclature.  This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigndocument_apply_ezsigntemplate_v1_request import EzsigndocumentApplyEzsigntemplateV1Request
from eZmaxApi.model.ezsigndocument_apply_ezsigntemplate_v1_response import EzsigndocumentApplyEzsigntemplateV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 
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
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |
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

# **ezsigndocument_apply_ezsigntemplate_v2**
> EzsigndocumentApplyEzsigntemplateV2Response ezsigndocument_apply_ezsigntemplate_v2(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v2_request)

Apply an Ezsign Template to the Ezsigndocument.

This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.ezsigndocument_apply_ezsigntemplate_v2_request import EzsigndocumentApplyEzsigntemplateV2Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigndocument_apply_ezsigntemplate_v2_response import EzsigndocumentApplyEzsigntemplateV2Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 
    ezsigndocument_apply_ezsigntemplate_v2_request = EzsigndocumentApplyEzsigntemplateV2Request(
        fki_ezsigntemplate_id=36,
        a_s_ezsigntemplatesigner=[
            "John",
        ],
        a_pki_ezsignfoldersignerassociation_id=[
            20,
        ],
    ) # EzsigndocumentApplyEzsigntemplateV2Request | 

    # example passing only required values which don't have defaults set
    try:
        # Apply an Ezsign Template to the Ezsigndocument.
        api_response = api_instance.ezsigndocument_apply_ezsigntemplate_v2(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v2_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |
 **ezsigndocument_apply_ezsigntemplate_v2_request** | [**EzsigndocumentApplyEzsigntemplateV2Request**](EzsigndocumentApplyEzsigntemplateV2Request.md)|  |

### Return type

[**EzsigndocumentApplyEzsigntemplateV2Response**](EzsigndocumentApplyEzsigntemplateV2Response.md)

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
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.ezsigndocument_create_object_v1_request import EzsigndocumentCreateObjectV1Request
from eZmaxApi.model.ezsigndocument_create_object_v1_response import EzsigndocumentCreateObjectV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    ezsigndocument_create_object_v1_request = [
        EzsigndocumentCreateObjectV1Request(
            obj_ezsigndocument=EzsigndocumentRequest(
                e_ezsigndocument_source="Base64",
                e_ezsigndocument_format="Pdf",
                s_ezsigndocument_base64='YQ==',
                s_ezsigndocument_url="http://www.example.com/document.pdf",
                b_ezsigndocument_forcerepair=True,
                s_ezsigndocument_password="SecretPassword123",
                fki_ezsignfolder_id=33,
                dt_ezsigndocument_duedate="2020-12-31 23:59:59",
                fki_language_id=FieldPkiLanguageID(2),
                s_ezsigndocument_name="Contract #123",
            ),
            obj_ezsigndocument_compound=EzsigndocumentRequestCompound(),
        ),
    ] # [EzsigndocumentCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsigndocument
        api_response = api_instance.ezsigndocument_create_object_v1(ezsigndocument_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
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
**404** | The element you are trying to work on does not exist |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_delete_object_v1**
> EzsigndocumentDeleteObjectV1Response ezsigndocument_delete_object_v1(pki_ezsigndocument_id)

Delete an existing Ezsigndocument

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigndocument_delete_object_v1_response import EzsigndocumentDeleteObjectV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_delete_object_v1(pki_ezsigndocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |

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

# **ezsigndocument_get_children_v1**
> ezsigndocument_get_children_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's children IDs

## ⚠️EARLY ADOPTERS WARNING  ### This endpoint is not officially released. Its definition might still change and it might not be available in every environment and region.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigndocument's children IDs
        api_instance.ezsigndocument_get_children_v1(pki_ezsigndocument_id)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_children_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |

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

# **ezsigndocument_get_download_url_v1**
> EzsigndocumentGetDownloadUrlV1Response ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type)

Retrieve a URL to download documents.

This endpoint returns URLs to different files that can be downloaded during the signing process.  These links will expire after 5 minutes so the download of the file should be made soon after retrieving the link.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.ezsigndocument_get_download_url_v1_response import EzsigndocumentGetDownloadUrlV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 
    e_document_type = "Initial" # str | The type of document to retrieve.  1. **Initial** Is the initial document before any signature were applied. 2. **Signed** Is the final document once all signatures were applied. 3. **Proofdocument** Is the evidence report. 4. **Proof** Is the complete evidence archive including all of the above and more. 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a URL to download documents.
        api_response = api_instance.ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_download_url_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |
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

# **ezsigndocument_get_ezsignpages_v1**
> EzsigndocumentGetEzsignpagesV1Response ezsigndocument_get_ezsignpages_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Ezsignpages

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.ezsigndocument_get_ezsignpages_v1_response import EzsigndocumentGetEzsignpagesV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigndocument's Ezsignpages
        api_response = api_instance.ezsigndocument_get_ezsignpages_v1(pki_ezsigndocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsignpages_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |

### Return type

[**EzsigndocumentGetEzsignpagesV1Response**](EzsigndocumentGetEzsignpagesV1Response.md)

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

# **ezsigndocument_get_form_data_v1**
> EzsigndocumentGetFormDataV1Response ezsigndocument_get_form_data_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Form Data

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.ezsigndocument_get_form_data_v1_response import EzsigndocumentGetFormDataV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigndocument's Form Data
        api_response = api_instance.ezsigndocument_get_form_data_v1(pki_ezsigndocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_form_data_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |

### Return type

[**EzsigndocumentGetFormDataV1Response**](EzsigndocumentGetFormDataV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The element you are trying to work on does not exist |  -  |
**406** | One of the accept header is not defined or invalid. |  -  |
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_object_v1**
> EzsigndocumentGetObjectV1Response ezsigndocument_get_object_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument

## ⚠️EARLY ADOPTERS WARNING  ### This endpoint is not officially released. Its definition might still change and it might not be available in every environment and region.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigndocument_get_object_v1_response import EzsigndocumentGetObjectV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_get_object_v1(pki_ezsigndocument_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |

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

# **ezsigndocument_get_words_positions_v1**
> EzsigndocumentGetWordsPositionsV1Response ezsigndocument_get_words_positions_v1(pki_ezsigndocument_id, ezsigndocument_get_words_positions_v1_request)

Retrieve positions X,Y of given words from a Ezsigndocument

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigndocument_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigndocument_get_words_positions_v1_request import EzsigndocumentGetWordsPositionsV1Request
from eZmaxApi.model.ezsigndocument_get_words_positions_v1_response import EzsigndocumentGetWordsPositionsV1Response
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
    api_instance = object_ezsigndocument_api.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 97 # int | 
    ezsigndocument_get_words_positions_v1_request = EzsigndocumentGetWordsPositionsV1Request(
        e_get="All",
        b_word_case_sensitive=True,
        a_s_word=[
            "a_s_word_example",
        ],
    ) # EzsigndocumentGetWordsPositionsV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve positions X,Y of given words from a Ezsigndocument
        api_response = api_instance.ezsigndocument_get_words_positions_v1(pki_ezsigndocument_id, ezsigndocument_get_words_positions_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_words_positions_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  |
 **ezsigndocument_get_words_positions_v1_request** | [**EzsigndocumentGetWordsPositionsV1Request**](EzsigndocumentGetWordsPositionsV1Request.md)|  |

### Return type

[**EzsigndocumentGetWordsPositionsV1Response**](EzsigndocumentGetWordsPositionsV1Response.md)

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

