# eZmaxApi.ObjectDiscussionmembershipApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discussionmembership_create_object_v1**](ObjectDiscussionmembershipApi.md#discussionmembership_create_object_v1) | **POST** /1/object/discussionmembership | Create a new Discussionmembership
[**discussionmembership_delete_object_v1**](ObjectDiscussionmembershipApi.md#discussionmembership_delete_object_v1) | **DELETE** /1/object/discussionmembership/{pkiDiscussionmembershipID} | Delete an existing Discussionmembership


# **discussionmembership_create_object_v1**
> DiscussionmembershipCreateObjectV1Response discussionmembership_create_object_v1(discussionmembership_create_object_v1_request)

Create a new Discussionmembership

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.discussionmembership_create_object_v1_request import DiscussionmembershipCreateObjectV1Request
from eZmaxApi.models.discussionmembership_create_object_v1_response import DiscussionmembershipCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionmembershipApi(api_client)
    discussionmembership_create_object_v1_request = eZmaxApi.DiscussionmembershipCreateObjectV1Request() # DiscussionmembershipCreateObjectV1Request | 

    try:
        # Create a new Discussionmembership
        api_response = api_instance.discussionmembership_create_object_v1(discussionmembership_create_object_v1_request)
        print("The response of ObjectDiscussionmembershipApi->discussionmembership_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionmembershipApi->discussionmembership_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discussionmembership_create_object_v1_request** | [**DiscussionmembershipCreateObjectV1Request**](DiscussionmembershipCreateObjectV1Request.md)|  | 

### Return type

[**DiscussionmembershipCreateObjectV1Response**](DiscussionmembershipCreateObjectV1Response.md)

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

# **discussionmembership_delete_object_v1**
> DiscussionmembershipDeleteObjectV1Response discussionmembership_delete_object_v1(pki_discussionmembership_id)

Delete an existing Discussionmembership



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.discussionmembership_delete_object_v1_response import DiscussionmembershipDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectDiscussionmembershipApi(api_client)
    pki_discussionmembership_id = 56 # int | The unique ID of the Discussionmembership

    try:
        # Delete an existing Discussionmembership
        api_response = api_instance.discussionmembership_delete_object_v1(pki_discussionmembership_id)
        print("The response of ObjectDiscussionmembershipApi->discussionmembership_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectDiscussionmembershipApi->discussionmembership_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_discussionmembership_id** | **int**| The unique ID of the Discussionmembership | 

### Return type

[**DiscussionmembershipDeleteObjectV1Response**](DiscussionmembershipDeleteObjectV1Response.md)

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

