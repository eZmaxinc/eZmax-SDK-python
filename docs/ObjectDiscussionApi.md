# eZmaxApi.ObjectDiscussionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discussion_create_object_v1**](ObjectDiscussionApi.md#discussion_create_object_v1) | **POST** /1/object/discussion | Create a new Discussion
[**discussion_delete_object_v1**](ObjectDiscussionApi.md#discussion_delete_object_v1) | **DELETE** /1/object/discussion/{pkiDiscussionID} | Delete an existing Discussion
[**discussion_get_object_v2**](ObjectDiscussionApi.md#discussion_get_object_v2) | **GET** /2/object/discussion/{pkiDiscussionID} | Retrieve an existing Discussion
[**discussion_patch_object_v1**](ObjectDiscussionApi.md#discussion_patch_object_v1) | **PATCH** /1/object/discussion/{pkiDiscussionID} | Patch an existing Discussion
[**discussion_update_discussionreadstatus_v1**](ObjectDiscussionApi.md#discussion_update_discussionreadstatus_v1) | **POST** /1/object/discussion/{pkiDiscussionID}/updateDiscussionreadstatus | Update the read status of the discussion


# **discussion_create_object_v1**
> DiscussionCreateObjectV1Response discussion_create_object_v1(discussion_create_object_v1_request)

Create a new Discussion

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.discussion_create_object_v1_request import DiscussionCreateObjectV1Request
from eZmaxApi.models.discussion_create_object_v1_response import DiscussionCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionApi(api_client)
    discussion_create_object_v1_request = eZmaxApi.DiscussionCreateObjectV1Request() # DiscussionCreateObjectV1Request | 

    try:
        # Create a new Discussion
        api_response = api_instance.discussion_create_object_v1(discussion_create_object_v1_request)
        print("The response of ObjectDiscussionApi->discussion_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionApi->discussion_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussion_create_object_v1_request** | [**DiscussionCreateObjectV1Request**](DiscussionCreateObjectV1Request.md)|  | 

### Return type

[**DiscussionCreateObjectV1Response**](DiscussionCreateObjectV1Response.md)

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

# **discussion_delete_object_v1**
> DiscussionDeleteObjectV1Response discussion_delete_object_v1(pki_discussion_id)

Delete an existing Discussion



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.discussion_delete_object_v1_response import DiscussionDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionApi(api_client)
    pki_discussion_id = 56 # int | The unique ID of the Discussion

    try:
        # Delete an existing Discussion
        api_response = api_instance.discussion_delete_object_v1(pki_discussion_id)
        print("The response of ObjectDiscussionApi->discussion_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionApi->discussion_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussion_id** | **int**| The unique ID of the Discussion | 

### Return type

[**DiscussionDeleteObjectV1Response**](DiscussionDeleteObjectV1Response.md)

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

# **discussion_get_object_v2**
> DiscussionGetObjectV2Response discussion_get_object_v2(pki_discussion_id)

Retrieve an existing Discussion



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.discussion_get_object_v2_response import DiscussionGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectDiscussionApi(api_client)
    pki_discussion_id = 56 # int | The unique ID of the Discussion

    try:
        # Retrieve an existing Discussion
        api_response = api_instance.discussion_get_object_v2(pki_discussion_id)
        print("The response of ObjectDiscussionApi->discussion_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionApi->discussion_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussion_id** | **int**| The unique ID of the Discussion | 

### Return type

[**DiscussionGetObjectV2Response**](DiscussionGetObjectV2Response.md)

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

# **discussion_patch_object_v1**
> DiscussionPatchObjectV1Response discussion_patch_object_v1(pki_discussion_id, discussion_patch_object_v1_request)

Patch an existing Discussion



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.discussion_patch_object_v1_request import DiscussionPatchObjectV1Request
from eZmaxApi.models.discussion_patch_object_v1_response import DiscussionPatchObjectV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionApi(api_client)
    pki_discussion_id = 56 # int | The unique ID of the Discussion
    discussion_patch_object_v1_request = eZmaxApi.DiscussionPatchObjectV1Request() # DiscussionPatchObjectV1Request | 

    try:
        # Patch an existing Discussion
        api_response = api_instance.discussion_patch_object_v1(pki_discussion_id, discussion_patch_object_v1_request)
        print("The response of ObjectDiscussionApi->discussion_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionApi->discussion_patch_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussion_id** | **int**| The unique ID of the Discussion | 
 **discussion_patch_object_v1_request** | [**DiscussionPatchObjectV1Request**](DiscussionPatchObjectV1Request.md)|  | 

### Return type

[**DiscussionPatchObjectV1Response**](DiscussionPatchObjectV1Response.md)

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

# **discussion_update_discussionreadstatus_v1**
> DiscussionUpdateDiscussionreadstatusV1Response discussion_update_discussionreadstatus_v1(pki_discussion_id, discussion_update_discussionreadstatus_v1_request)

Update the read status of the discussion

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.discussion_update_discussionreadstatus_v1_request import DiscussionUpdateDiscussionreadstatusV1Request
from eZmaxApi.models.discussion_update_discussionreadstatus_v1_response import DiscussionUpdateDiscussionreadstatusV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionApi(api_client)
    pki_discussion_id = 56 # int | 
    discussion_update_discussionreadstatus_v1_request = eZmaxApi.DiscussionUpdateDiscussionreadstatusV1Request() # DiscussionUpdateDiscussionreadstatusV1Request | 

    try:
        # Update the read status of the discussion
        api_response = api_instance.discussion_update_discussionreadstatus_v1(pki_discussion_id, discussion_update_discussionreadstatus_v1_request)
        print("The response of ObjectDiscussionApi->discussion_update_discussionreadstatus_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionApi->discussion_update_discussionreadstatus_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussion_id** | **int**|  | 
 **discussion_update_discussionreadstatus_v1_request** | [**DiscussionUpdateDiscussionreadstatusV1Request**](DiscussionUpdateDiscussionreadstatusV1Request.md)|  | 

### Return type

[**DiscussionUpdateDiscussionreadstatusV1Response**](DiscussionUpdateDiscussionreadstatusV1Response.md)

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

