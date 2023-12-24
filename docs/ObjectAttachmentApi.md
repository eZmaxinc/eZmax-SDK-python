# eZmaxApi.ObjectAttachmentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachment_download_v1**](ObjectAttachmentApi.md#attachment_download_v1) | **GET** /1/object/attachment/{pkiAttachmentID}/download | Retrieve the content
[**attachment_get_attachmentlogs_v1**](ObjectAttachmentApi.md#attachment_get_attachmentlogs_v1) | **GET** /1/object/attachment/{pkiAttachmentID}/getAttachmentlogs | Retrieve the Attachmentlogs
[**attachment_get_download_url_v1**](ObjectAttachmentApi.md#attachment_get_download_url_v1) | **GET** /1/object/attachment/{pkiAttachmentID}/getDownloadUrl | Retrieve a URL to download attachments.


# **attachment_download_v1**
> attachment_download_v1(pki_attachment_id)

Retrieve the content

Using this endpoint, you can retrieve the content of an attachment.

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (Presigned):

```python
import time
import os
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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_get_attachmentlogs_v1**
> AttachmentGetAttachmentlogsV1Response attachment_get_attachmentlogs_v1(pki_attachment_id)

Retrieve the Attachmentlogs

Using this endpoint, you can retrieve the Attachmentlogs of an attachment.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment_get_download_url_v1**
> AttachmentGetDownloadUrlV1Response attachment_get_download_url_v1(pki_attachment_id)

Retrieve a URL to download attachments.

This endpoint returns an URL to download the attachment.  These links will expire after 5 minutes so the download of the file should be made soon after retrieving the link.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.attachment_get_download_url_v1_response import AttachmentGetDownloadUrlV1Response
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
        # Retrieve a URL to download attachments.
        api_response = api_instance.attachment_get_download_url_v1(pki_attachment_id)
        print("The response of ObjectAttachmentApi->attachment_get_download_url_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectAttachmentApi->attachment_get_download_url_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_attachment_id** | **int**|  | 

### Return type

[**AttachmentGetDownloadUrlV1Response**](AttachmentGetDownloadUrlV1Response.md)

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

