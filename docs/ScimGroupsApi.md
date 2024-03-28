# eZmaxApi.ScimGroupsApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_create_object_scim_v2**](ScimGroupsApi.md#groups_create_object_scim_v2) | **POST** /2/scim/Groups | Create a new Usergroup
[**groups_delete_object_scim_v2**](ScimGroupsApi.md#groups_delete_object_scim_v2) | **DELETE** /2/scim/Groups/{groupId} | Delete an existing Usergroup
[**groups_edit_object_scim_v2**](ScimGroupsApi.md#groups_edit_object_scim_v2) | **PUT** /2/scim/Groups/{groupId} | Edit an existing Usergroup
[**groups_get_list_scim_v2**](ScimGroupsApi.md#groups_get_list_scim_v2) | **GET** /2/scim/Groups | Retrieve Usergroup list
[**groups_get_object_scim_v2**](ScimGroupsApi.md#groups_get_object_scim_v2) | **GET** /2/scim/Groups/{groupId} | Retrieve an existing Usergroup


# **groups_create_object_scim_v2**
> ScimGroup groups_create_object_scim_v2(scim_group)

Create a new Usergroup

### Example

* Bearer Authentication (Bearer):

```python
import eZmaxApi
from eZmaxApi.models.scim_group import ScimGroup
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

# Configure Bearer authorization: Bearer
configuration = eZmaxApi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimGroupsApi(api_client)
    scim_group = eZmaxApi.ScimGroup() # ScimGroup | 

    try:
        # Create a new Usergroup
        api_response = api_instance.groups_create_object_scim_v2(scim_group)
        print("The response of ScimGroupsApi->groups_create_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimGroupsApi->groups_create_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_group** | [**ScimGroup**](ScimGroup.md)|  | 

### Return type

[**ScimGroup**](ScimGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_delete_object_scim_v2**
> groups_delete_object_scim_v2(group_id)

Delete an existing Usergroup

### Example

* Bearer Authentication (Bearer):

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

# Configure Bearer authorization: Bearer
configuration = eZmaxApi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimGroupsApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Delete an existing Usergroup
        api_instance.groups_delete_object_scim_v2(group_id)
    except Exception as e:
        print("Exception when calling ScimGroupsApi->groups_delete_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_edit_object_scim_v2**
> ScimGroup groups_edit_object_scim_v2(group_id, scim_group)

Edit an existing Usergroup

### Example

* Bearer Authentication (Bearer):

```python
import eZmaxApi
from eZmaxApi.models.scim_group import ScimGroup
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

# Configure Bearer authorization: Bearer
configuration = eZmaxApi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimGroupsApi(api_client)
    group_id = 'group_id_example' # str | 
    scim_group = eZmaxApi.ScimGroup() # ScimGroup | 

    try:
        # Edit an existing Usergroup
        api_response = api_instance.groups_edit_object_scim_v2(group_id, scim_group)
        print("The response of ScimGroupsApi->groups_edit_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimGroupsApi->groups_edit_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **scim_group** | [**ScimGroup**](ScimGroup.md)|  | 

### Return type

[**ScimGroup**](ScimGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_list_scim_v2**
> ScimGroup groups_get_list_scim_v2(filter=filter)

Retrieve Usergroup list

### Example

* Bearer Authentication (Bearer):

```python
import eZmaxApi
from eZmaxApi.models.scim_group import ScimGroup
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

# Configure Bearer authorization: Bearer
configuration = eZmaxApi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimGroupsApi(api_client)
    filter = 'filter_example' # str | Filter expression for searching groups (optional)

    try:
        # Retrieve Usergroup list
        api_response = api_instance.groups_get_list_scim_v2(filter=filter)
        print("The response of ScimGroupsApi->groups_get_list_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimGroupsApi->groups_get_list_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter expression for searching groups | [optional] 

### Return type

[**ScimGroup**](ScimGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_object_scim_v2**
> ScimGroup groups_get_object_scim_v2(group_id)

Retrieve an existing Usergroup

### Example

* Bearer Authentication (Bearer):

```python
import eZmaxApi
from eZmaxApi.models.scim_group import ScimGroup
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

# Configure Bearer authorization: Bearer
configuration = eZmaxApi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimGroupsApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Retrieve an existing Usergroup
        api_response = api_instance.groups_get_object_scim_v2(group_id)
        print("The response of ScimGroupsApi->groups_get_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimGroupsApi->groups_get_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**ScimGroup**](ScimGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

