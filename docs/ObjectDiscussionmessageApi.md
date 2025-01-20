# eZmaxApi.ObjectDiscussionmessageApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discussionmessage_create_object_v1**](ObjectDiscussionmessageApi.md#discussionmessage_create_object_v1) | **POST** /1/object/discussionmessage | Create a new Discussionmessage
[**discussionmessage_delete_object_v1**](ObjectDiscussionmessageApi.md#discussionmessage_delete_object_v1) | **DELETE** /1/object/discussionmessage/{pkiDiscussionmessageID} | Delete an existing Discussionmessage
[**discussionmessage_patch_object_v1**](ObjectDiscussionmessageApi.md#discussionmessage_patch_object_v1) | **PATCH** /1/object/discussionmessage/{pkiDiscussionmessageID} | Patch an existing Discussionmessage


# **discussionmessage_create_object_v1**
> DiscussionmessageCreateObjectV1Response discussionmessage_create_object_v1(discussionmessage_create_object_v1_request)

Create a new Discussionmessage

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.discussionmessage_create_object_v1_request import DiscussionmessageCreateObjectV1Request
from eZmaxApi.models.discussionmessage_create_object_v1_response import DiscussionmessageCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionmessageApi(api_client)
    discussionmessage_create_object_v1_request = eZmaxApi.DiscussionmessageCreateObjectV1Request() # DiscussionmessageCreateObjectV1Request | 

    try:
        # Create a new Discussionmessage
        api_response = api_instance.discussionmessage_create_object_v1(discussionmessage_create_object_v1_request)
        print("The response of ObjectDiscussionmessageApi->discussionmessage_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionmessageApi->discussionmessage_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussionmessage_create_object_v1_request** | [**DiscussionmessageCreateObjectV1Request**](DiscussionmessageCreateObjectV1Request.md)|  | 

### Return type

[**DiscussionmessageCreateObjectV1Response**](DiscussionmessageCreateObjectV1Response.md)

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

# **discussionmessage_delete_object_v1**
> CommonResponse discussionmessage_delete_object_v1(pki_discussionmessage_id)

Delete an existing Discussionmessage



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
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
    api_instance = eZmaxApi.ObjectDiscussionmessageApi(api_client)
    pki_discussionmessage_id = 56 # int | The unique ID of the Discussionmessage

    try:
        # Delete an existing Discussionmessage
        api_response = api_instance.discussionmessage_delete_object_v1(pki_discussionmessage_id)
        print("The response of ObjectDiscussionmessageApi->discussionmessage_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionmessageApi->discussionmessage_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussionmessage_id** | **int**| The unique ID of the Discussionmessage | 

### Return type

[**CommonResponse**](CommonResponse.md)

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

# **discussionmessage_patch_object_v1**
> CommonResponse discussionmessage_patch_object_v1(pki_discussionmessage_id, discussionmessage_patch_object_v1_request)

Patch an existing Discussionmessage



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.common_response import CommonResponse
from eZmaxApi.models.discussionmessage_patch_object_v1_request import DiscussionmessagePatchObjectV1Request
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
    api_instance = eZmaxApi.ObjectDiscussionmessageApi(api_client)
    pki_discussionmessage_id = 56 # int | The unique ID of the Discussionmessage
    discussionmessage_patch_object_v1_request = eZmaxApi.DiscussionmessagePatchObjectV1Request() # DiscussionmessagePatchObjectV1Request | 

    try:
        # Patch an existing Discussionmessage
        api_response = api_instance.discussionmessage_patch_object_v1(pki_discussionmessage_id, discussionmessage_patch_object_v1_request)
        print("The response of ObjectDiscussionmessageApi->discussionmessage_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionmessageApi->discussionmessage_patch_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussionmessage_id** | **int**| The unique ID of the Discussionmessage | 
 **discussionmessage_patch_object_v1_request** | [**DiscussionmessagePatchObjectV1Request**](DiscussionmessagePatchObjectV1Request.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

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

