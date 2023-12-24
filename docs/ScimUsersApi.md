# eZmaxApi.ScimUsersApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create_object_scim_v2**](ScimUsersApi.md#users_create_object_scim_v2) | **POST** /2/scim/Users | Create a new User
[**users_delete_object_scim_v2**](ScimUsersApi.md#users_delete_object_scim_v2) | **DELETE** /2/scim/Users/{userId} | Delete an existing User
[**users_edit_object_scim_v2**](ScimUsersApi.md#users_edit_object_scim_v2) | **PUT** /2/scim/Users/{userId} | Edit an existing User
[**users_get_list_scim_v2**](ScimUsersApi.md#users_get_list_scim_v2) | **GET** /2/scim/Users | Retrieve User list
[**users_get_object_scim_v2**](ScimUsersApi.md#users_get_object_scim_v2) | **GET** /2/scim/Users/{userId} | Retrieve an existing User


# **users_create_object_scim_v2**
> ScimUser users_create_object_scim_v2(scim_user)

Create a new User

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.scim_user import ScimUser
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
    api_instance = eZmaxApi.ScimUsersApi(api_client)
    scim_user = eZmaxApi.ScimUser() # ScimUser | 

    try:
        # Create a new User
        api_response = api_instance.users_create_object_scim_v2(scim_user)
        print("The response of ScimUsersApi->users_create_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimUsersApi->users_create_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_user** | [**ScimUser**](ScimUser.md)|  | 

### Return type

[**ScimUser**](ScimUser.md)

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

# **users_delete_object_scim_v2**
> users_delete_object_scim_v2(user_id)

Delete an existing User

### Example

* Bearer Authentication (Bearer):

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

# Configure Bearer authorization: Bearer
configuration = eZmaxApi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimUsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Delete an existing User
        api_instance.users_delete_object_scim_v2(user_id)
    except Exception as e:
        print("Exception when calling ScimUsersApi->users_delete_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **users_edit_object_scim_v2**
> ScimUser users_edit_object_scim_v2(user_id, scim_user)

Edit an existing User

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.scim_user import ScimUser
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
    api_instance = eZmaxApi.ScimUsersApi(api_client)
    user_id = 'user_id_example' # str | 
    scim_user = eZmaxApi.ScimUser() # ScimUser | 

    try:
        # Edit an existing User
        api_response = api_instance.users_edit_object_scim_v2(user_id, scim_user)
        print("The response of ScimUsersApi->users_edit_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimUsersApi->users_edit_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **scim_user** | [**ScimUser**](ScimUser.md)|  | 

### Return type

[**ScimUser**](ScimUser.md)

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

# **users_get_list_scim_v2**
> ScimUserList users_get_list_scim_v2(filter=filter)

Retrieve User list

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.scim_user_list import ScimUserList
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
    api_instance = eZmaxApi.ScimUsersApi(api_client)
    filter = 'filter_example' # str | Filter expression for searching users (optional)

    try:
        # Retrieve User list
        api_response = api_instance.users_get_list_scim_v2(filter=filter)
        print("The response of ScimUsersApi->users_get_list_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimUsersApi->users_get_list_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter expression for searching users | [optional] 

### Return type

[**ScimUserList**](ScimUserList.md)

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

# **users_get_object_scim_v2**
> ScimUser users_get_object_scim_v2(user_id)

Retrieve an existing User

### Example

* Bearer Authentication (Bearer):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.scim_user import ScimUser
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
    api_instance = eZmaxApi.ScimUsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Retrieve an existing User
        api_response = api_instance.users_get_object_scim_v2(user_id)
        print("The response of ScimUsersApi->users_get_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimUsersApi->users_get_object_scim_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ScimUser**](ScimUser.md)

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

