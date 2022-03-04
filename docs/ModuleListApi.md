# eZmaxApi.ModuleListApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_get_listpresentation_v1**](ModuleListApi.md#list_get_listpresentation_v1) | **GET** /1/module/list/listpresentation/{sListName} | Get all Listpresentation for a specific list
[**list_save_listpresentation_v1**](ModuleListApi.md#list_save_listpresentation_v1) | **POST** /1/module/list/listpresentation/{sListName} | Save all Listpresentation for a specific list


# **list_get_listpresentation_v1**
> ListGetListpresentationV1Response list_get_listpresentation_v1(s_list_name)

Get all Listpresentation for a specific list

Retrive previously saved Listpresentation

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import module_list_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.list_get_listpresentation_v1_response import ListGetListpresentationV1Response
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
    api_instance = module_list_api.ModuleListApi(api_client)
    s_list_name = "sListName_example" # str | The list Name

    # example passing only required values which don't have defaults set
    try:
        # Get all Listpresentation for a specific list
        api_response = api_instance.list_get_listpresentation_v1(s_list_name)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ModuleListApi->list_get_listpresentation_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_list_name** | **str**| The list Name |

### Return type

[**ListGetListpresentationV1Response**](ListGetListpresentationV1Response.md)

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

# **list_save_listpresentation_v1**
> ListSaveListpresentationV1Response list_save_listpresentation_v1(s_list_name, list_save_listpresentation_v1_request)

Save all Listpresentation for a specific list

Users can create many Listpresentations for lists in the system. They can customize orber by, filters, numbers of rows, etc.

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import module_list_api
from eZmaxApi.model.list_save_listpresentation_v1_request import ListSaveListpresentationV1Request
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.list_save_listpresentation_v1_response import ListSaveListpresentationV1Response
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
    api_instance = module_list_api.ModuleListApi(api_client)
    s_list_name = "sListName_example" # str | The list Name
    list_save_listpresentation_v1_request = ListSaveListpresentationV1Request(
        a_obj_listpresentation=[
            ListpresentationRequestCompound(),
        ],
    ) # ListSaveListpresentationV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Save all Listpresentation for a specific list
        api_response = api_instance.list_save_listpresentation_v1(s_list_name, list_save_listpresentation_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ModuleListApi->list_save_listpresentation_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_list_name** | **str**| The list Name |
 **list_save_listpresentation_v1_request** | [**ListSaveListpresentationV1Request**](ListSaveListpresentationV1Request.md)|  |

### Return type

[**ListSaveListpresentationV1Response**](ListSaveListpresentationV1Response.md)

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

