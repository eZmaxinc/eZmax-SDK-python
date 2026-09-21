# eZmaxApi.ObjectAttachmentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachment_delete_v1**](ObjectAttachmentApi.md#attachment_delete_v1) | **POST** /1/object/attachment/{pkiAttachmentID}/delete | Delete an existing attachment
[**attachment_document_type_v1**](ObjectAttachmentApi.md#attachment_document_type_v1) | **POST** /1/object/attachment/{pkiAttachmentID}/documentType | Change attachment document type
[**attachment_download_v1**](ObjectAttachmentApi.md#attachment_download_v1) | **GET** /1/object/attachment/{pkiAttachmentID}/download | Retrieve the content
[**attachment_get_attachmentlogs_v1**](ObjectAttachmentApi.md#attachment_get_attachmentlogs_v1) | **GET** /1/object/attachment/{pkiAttachmentID}/getAttachmentlogs | Retrieve the Attachmentlogs
[**attachment_privacy_v1**](ObjectAttachmentApi.md#attachment_privacy_v1) | **POST** /1/object/attachment/{pkiAttachmentID}/privacy | Change the attachment privacy
[**attachment_rename_v1**](ObjectAttachmentApi.md#attachment_rename_v1) | **POST** /1/object/attachment/{pkiAttachmentID}/rename | Rename an attachment
[**attachment_restore_v1**](ObjectAttachmentApi.md#attachment_restore_v1) | **POST** /1/object/attachment/{pkiAttachmentID}/restore | Restore a deleted attachment
[**attachment_validate_v1**](ObjectAttachmentApi.md#attachment_validate_v1) | **POST** /1/object/attachment/{pkiAttachmentID}/validate | Validate an existing attachment


# **attachment_delete_v1**
> AttachmentDeleteV1Response attachment_delete_v1(pki_attachment_id, body)

Delete an existing attachment

Te endpoint allows to delete an attachment.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_delete_v1_response import AttachmentDeleteV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 
    body = None # object | 

    try:
        # Delete an existing attachment
        api_response = api_instance.attachment_delete_v1(pki_attachment_id, body)
        print("The response of ObjectAttachmentApi->attachment_delete_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_delete_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**AttachmentDeleteV1Response**](AttachmentDeleteV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body. |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_document_type_v1**
> AttachmentDocumentTypeV1Response attachment_document_type_v1(pki_attachment_id, attachment_document_type_v1_request)

Change attachment document type

The endpoint allows to change the checklist document type for an attachment.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_document_type_v1_request import AttachmentDocumentTypeV1Request
from eZmaxApi.models.attachment_document_type_v1_response import AttachmentDocumentTypeV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 
    attachment_document_type_v1_request = eZmaxApi.AttachmentDocumentTypeV1Request() # AttachmentDocumentTypeV1Request | 

    try:
        # Change attachment document type
        api_response = api_instance.attachment_document_type_v1(pki_attachment_id, attachment_document_type_v1_request)
        print("The response of ObjectAttachmentApi->attachment_document_type_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_document_type_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 
 **attachment_document_type_v1_request** | [**AttachmentDocumentTypeV1Request**](AttachmentDocumentTypeV1Request.md)|  | 

### Return type

[**AttachmentDocumentTypeV1Response**](AttachmentDocumentTypeV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body. |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_download_v1**
> attachment_download_v1(pki_attachment_id)

Retrieve the content

Using this endpoint, you can retrieve the content of an attachment.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (Presigned):

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

# Configure API key authorization: Presigned
configuration.api_key['Presigned'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Presigned'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 

    try:
        # Retrieve the content
        api_instance.attachment_download_v1(pki_attachment_id)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_download_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization), [Presigned](../README.md#Presigned)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | The user has been redirected |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_get_attachmentlogs_v1**
> AttachmentGetAttachmentlogsV1Response attachment_get_attachmentlogs_v1(pki_attachment_id)

Retrieve the Attachmentlogs

Using this endpoint, you can retrieve the Attachmentlogs of an attachment.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_get_attachmentlogs_v1_response import AttachmentGetAttachmentlogsV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 

    try:
        # Retrieve the Attachmentlogs
        api_response = api_instance.attachment_get_attachmentlogs_v1(pki_attachment_id)
        print("The response of ObjectAttachmentApi->attachment_get_attachmentlogs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_get_attachmentlogs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 

### Return type

[**AttachmentGetAttachmentlogsV1Response**](AttachmentGetAttachmentlogsV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_privacy_v1**
> AttachmentPrivacyV1Response attachment_privacy_v1(pki_attachment_id, attachment_privacy_v1_request)

Change the attachment privacy

The endpoint allows to change an attachment's access privacy.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_privacy_v1_request import AttachmentPrivacyV1Request
from eZmaxApi.models.attachment_privacy_v1_response import AttachmentPrivacyV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 
    attachment_privacy_v1_request = eZmaxApi.AttachmentPrivacyV1Request() # AttachmentPrivacyV1Request | 

    try:
        # Change the attachment privacy
        api_response = api_instance.attachment_privacy_v1(pki_attachment_id, attachment_privacy_v1_request)
        print("The response of ObjectAttachmentApi->attachment_privacy_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_privacy_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 
 **attachment_privacy_v1_request** | [**AttachmentPrivacyV1Request**](AttachmentPrivacyV1Request.md)|  | 

### Return type

[**AttachmentPrivacyV1Response**](AttachmentPrivacyV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body. |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_rename_v1**
> AttachmentRenameV1Response attachment_rename_v1(pki_attachment_id, attachment_rename_v1_request)

Rename an attachment

The endpoint allows to change the attachment's file name and category.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_rename_v1_request import AttachmentRenameV1Request
from eZmaxApi.models.attachment_rename_v1_response import AttachmentRenameV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 
    attachment_rename_v1_request = eZmaxApi.AttachmentRenameV1Request() # AttachmentRenameV1Request | 

    try:
        # Rename an attachment
        api_response = api_instance.attachment_rename_v1(pki_attachment_id, attachment_rename_v1_request)
        print("The response of ObjectAttachmentApi->attachment_rename_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_rename_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 
 **attachment_rename_v1_request** | [**AttachmentRenameV1Request**](AttachmentRenameV1Request.md)|  | 

### Return type

[**AttachmentRenameV1Response**](AttachmentRenameV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body. |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**409** | The request failed due to a conflict with the resource state. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_restore_v1**
> AttachmentRestoreV1Response attachment_restore_v1(pki_attachment_id, attachment_restore_v1_request)

Restore a deleted attachment

The endpoints allows to restore a previously deleted attachment.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_restore_v1_request import AttachmentRestoreV1Request
from eZmaxApi.models.attachment_restore_v1_response import AttachmentRestoreV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 
    attachment_restore_v1_request = eZmaxApi.AttachmentRestoreV1Request() # AttachmentRestoreV1Request | 

    try:
        # Restore a deleted attachment
        api_response = api_instance.attachment_restore_v1(pki_attachment_id, attachment_restore_v1_request)
        print("The response of ObjectAttachmentApi->attachment_restore_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_restore_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 
 **attachment_restore_v1_request** | [**AttachmentRestoreV1Request**](AttachmentRestoreV1Request.md)|  | 

### Return type

[**AttachmentRestoreV1Response**](AttachmentRestoreV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body. |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**409** | The request failed due to a conflict with the resource state. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_validate_v1**
> AttachmentValidateV1Response attachment_validate_v1(pki_attachment_id, attachment_validate_v1_request)

Validate an existing attachment

This endpoint allows to validate or reject an attachment.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.attachment_validate_v1_request import AttachmentValidateV1Request
from eZmaxApi.models.attachment_validate_v1_response import AttachmentValidateV1Response
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
    api_instance = eZmaxApi.ObjectAttachmentApi(api_client)
    pki_attachment_id = 56 # int | 
    attachment_validate_v1_request = eZmaxApi.AttachmentValidateV1Request() # AttachmentValidateV1Request | 

    try:
        # Validate an existing attachment
        api_response = api_instance.attachment_validate_v1(pki_attachment_id, attachment_validate_v1_request)
        print("The response of ObjectAttachmentApi->attachment_validate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_validate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 
 **attachment_validate_v1_request** | [**AttachmentValidateV1Request**](AttachmentValidateV1Request.md)|  | 

### Return type

[**AttachmentValidateV1Response**](AttachmentValidateV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | The request is not allowed to be executed. Look for detail about the error in the body. |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

