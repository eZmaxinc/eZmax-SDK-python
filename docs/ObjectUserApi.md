# eZmaxApi.ObjectUserApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create_object_v1**](ObjectUserApi.md#user_create_object_v1) | **POST** /1/object/user | Create a new User
[**user_create_object_v2**](ObjectUserApi.md#user_create_object_v2) | **POST** /2/object/user | Create a new User
[**user_edit_object_v1**](ObjectUserApi.md#user_edit_object_v1) | **PUT** /1/object/user/{pkiUserID} | Edit an existing User
[**user_edit_permissions_v1**](ObjectUserApi.md#user_edit_permissions_v1) | **PUT** /1/object/user/{pkiUserID}/editPermissions | Edit multiple Permissions
[**user_get_apikeys_v1**](ObjectUserApi.md#user_get_apikeys_v1) | **GET** /1/object/user/{pkiUserID}/getApikeys | Retrieve an existing User&#39;s Apikeys
[**user_get_autocomplete_v2**](ObjectUserApi.md#user_get_autocomplete_v2) | **GET** /2/object/user/getAutocomplete/{sSelector} | Retrieve Users and IDs
[**user_get_effective_permissions_v1**](ObjectUserApi.md#user_get_effective_permissions_v1) | **GET** /1/object/user/{pkiUserID}/getEffectivePermissions | Retrieve an existing User&#39;s Effective Permissions
[**user_get_list_v1**](ObjectUserApi.md#user_get_list_v1) | **GET** /1/object/user/getList | Retrieve User list
[**user_get_object_v2**](ObjectUserApi.md#user_get_object_v2) | **GET** /2/object/user/{pkiUserID} | Retrieve an existing User
[**user_get_permissions_v1**](ObjectUserApi.md#user_get_permissions_v1) | **GET** /1/object/user/{pkiUserID}/getPermissions | Retrieve an existing User&#39;s Permissions
[**user_get_subnets_v1**](ObjectUserApi.md#user_get_subnets_v1) | **GET** /1/object/user/{pkiUserID}/getSubnets | Retrieve an existing User&#39;s Subnets
[**user_get_usergroupexternals_v1**](ObjectUserApi.md#user_get_usergroupexternals_v1) | **GET** /1/object/user/{pkiUserID}/getUsergroupexternals | Get User&#39;s Usergroupexternals
[**user_get_usergroups_v1**](ObjectUserApi.md#user_get_usergroups_v1) | **GET** /1/object/user/{pkiUserID}/getUsergroups | Get User&#39;s Usergroups
[**user_send_password_reset_v1**](ObjectUserApi.md#user_send_password_reset_v1) | **POST** /1/object/user/{pkiUserID}/sendPasswordReset | Send password reset


# **user_create_object_v1**
> UserCreateObjectV1Response user_create_object_v1(user_create_object_v1_request)

Create a new User

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_create_object_v1_request import UserCreateObjectV1Request
from eZmaxApi.models.user_create_object_v1_response import UserCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    user_create_object_v1_request = eZmaxApi.UserCreateObjectV1Request() # UserCreateObjectV1Request | 

    try:
        # Create a new User
        api_response = api_instance.user_create_object_v1(user_create_object_v1_request)
        print("The response of ObjectUserApi->user_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_object_v1_request** | [**UserCreateObjectV1Request**](UserCreateObjectV1Request.md)|  | 

### Return type

[**UserCreateObjectV1Response**](UserCreateObjectV1Response.md)

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

# **user_create_object_v2**
> UserCreateObjectV2Response user_create_object_v2(user_create_object_v2_request)

Create a new User

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_create_object_v2_request import UserCreateObjectV2Request
from eZmaxApi.models.user_create_object_v2_response import UserCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    user_create_object_v2_request = eZmaxApi.UserCreateObjectV2Request() # UserCreateObjectV2Request | 

    try:
        # Create a new User
        api_response = api_instance.user_create_object_v2(user_create_object_v2_request)
        print("The response of ObjectUserApi->user_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_object_v2_request** | [**UserCreateObjectV2Request**](UserCreateObjectV2Request.md)|  | 

### Return type

[**UserCreateObjectV2Response**](UserCreateObjectV2Response.md)

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

# **user_edit_object_v1**
> UserEditObjectV1Response user_edit_object_v1(pki_user_id, user_edit_object_v1_request)

Edit an existing User



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_edit_object_v1_request import UserEditObjectV1Request
from eZmaxApi.models.user_edit_object_v1_response import UserEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | The unique ID of the User
    user_edit_object_v1_request = eZmaxApi.UserEditObjectV1Request() # UserEditObjectV1Request | 

    try:
        # Edit an existing User
        api_response = api_instance.user_edit_object_v1(pki_user_id, user_edit_object_v1_request)
        print("The response of ObjectUserApi->user_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**| The unique ID of the User | 
 **user_edit_object_v1_request** | [**UserEditObjectV1Request**](UserEditObjectV1Request.md)|  | 

### Return type

[**UserEditObjectV1Response**](UserEditObjectV1Response.md)

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

# **user_edit_permissions_v1**
> UserEditPermissionsV1Response user_edit_permissions_v1(pki_user_id, user_edit_permissions_v1_request)

Edit multiple Permissions

Using this endpoint, you can edit multiple Permissions at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_edit_permissions_v1_request import UserEditPermissionsV1Request
from eZmaxApi.models.user_edit_permissions_v1_response import UserEditPermissionsV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 
    user_edit_permissions_v1_request = eZmaxApi.UserEditPermissionsV1Request() # UserEditPermissionsV1Request | 

    try:
        # Edit multiple Permissions
        api_response = api_instance.user_edit_permissions_v1(pki_user_id, user_edit_permissions_v1_request)
        print("The response of ObjectUserApi->user_edit_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_edit_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 
 **user_edit_permissions_v1_request** | [**UserEditPermissionsV1Request**](UserEditPermissionsV1Request.md)|  | 

### Return type

[**UserEditPermissionsV1Response**](UserEditPermissionsV1Response.md)

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

# **user_get_apikeys_v1**
> UserGetApikeysV1Response user_get_apikeys_v1(pki_user_id)

Retrieve an existing User's Apikeys

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_apikeys_v1_response import UserGetApikeysV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 

    try:
        # Retrieve an existing User's Apikeys
        api_response = api_instance.user_get_apikeys_v1(pki_user_id)
        print("The response of ObjectUserApi->user_get_apikeys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_apikeys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 

### Return type

[**UserGetApikeysV1Response**](UserGetApikeysV1Response.md)

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

# **user_get_autocomplete_v2**
> UserGetAutocompleteV2Response user_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Users and IDs

Get the list of User to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.user_get_autocomplete_v2_response import UserGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    s_selector = 's_selector_example' # str | The type of Users to return
    e_filter_active = 'Active' # str | Specify which results we want to display. (optional) (default to 'Active')
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Users and IDs
        api_response = api_instance.user_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectUserApi->user_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Users to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to &#39;Active&#39;]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**UserGetAutocompleteV2Response**](UserGetAutocompleteV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_effective_permissions_v1**
> UserGetEffectivePermissionsV1Response user_get_effective_permissions_v1(pki_user_id)

Retrieve an existing User's Effective Permissions

Effective Permissions refers to the combination of Permissions held by a User and the Permissions associated with the Usergroups they belong to.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_effective_permissions_v1_response import UserGetEffectivePermissionsV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 

    try:
        # Retrieve an existing User's Effective Permissions
        api_response = api_instance.user_get_effective_permissions_v1(pki_user_id)
        print("The response of ObjectUserApi->user_get_effective_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_effective_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 

### Return type

[**UserGetEffectivePermissionsV1Response**](UserGetEffectivePermissionsV1Response.md)

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

# **user_get_list_v1**
> UserGetListV1Response user_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve User list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eUserType | AgentBroker<br>Assistant<br>Employee<br>EzsignUser<br>Normal | | eUserOrigin | BuiltIn<br>External | | eUserEzsignaccess | No<br>PaidByOffice<br>PerDocument<br>Prepaid |

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.user_get_list_v1_response import UserGetListV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve User list
        api_response = api_instance.user_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectUserApi->user_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional] 
 **i_row_max** | **int**|  | [optional] 
 **i_row_offset** | **int**|  | [optional] [default to 0]
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 
 **s_filter** | **str**|  | [optional] 

### Return type

[**UserGetListV1Response**](UserGetListV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_object_v2**
> UserGetObjectV2Response user_get_object_v2(pki_user_id)

Retrieve an existing User



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_object_v2_response import UserGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | The unique ID of the User

    try:
        # Retrieve an existing User
        api_response = api_instance.user_get_object_v2(pki_user_id)
        print("The response of ObjectUserApi->user_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**| The unique ID of the User | 

### Return type

[**UserGetObjectV2Response**](UserGetObjectV2Response.md)

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

# **user_get_permissions_v1**
> UserGetPermissionsV1Response user_get_permissions_v1(pki_user_id)

Retrieve an existing User's Permissions

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_permissions_v1_response import UserGetPermissionsV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 

    try:
        # Retrieve an existing User's Permissions
        api_response = api_instance.user_get_permissions_v1(pki_user_id)
        print("The response of ObjectUserApi->user_get_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 

### Return type

[**UserGetPermissionsV1Response**](UserGetPermissionsV1Response.md)

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

# **user_get_subnets_v1**
> UserGetSubnetsV1Response user_get_subnets_v1(pki_user_id)

Retrieve an existing User's Subnets

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_subnets_v1_response import UserGetSubnetsV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 

    try:
        # Retrieve an existing User's Subnets
        api_response = api_instance.user_get_subnets_v1(pki_user_id)
        print("The response of ObjectUserApi->user_get_subnets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_subnets_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 

### Return type

[**UserGetSubnetsV1Response**](UserGetSubnetsV1Response.md)

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

# **user_get_usergroupexternals_v1**
> UserGetUsergroupexternalsV1Response user_get_usergroupexternals_v1(pki_user_id)

Get User's Usergroupexternals

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_usergroupexternals_v1_response import UserGetUsergroupexternalsV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 

    try:
        # Get User's Usergroupexternals
        api_response = api_instance.user_get_usergroupexternals_v1(pki_user_id)
        print("The response of ObjectUserApi->user_get_usergroupexternals_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_usergroupexternals_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 

### Return type

[**UserGetUsergroupexternalsV1Response**](UserGetUsergroupexternalsV1Response.md)

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

# **user_get_usergroups_v1**
> UserGetUsergroupsV1Response user_get_usergroups_v1(pki_user_id)

Get User's Usergroups

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_get_usergroups_v1_response import UserGetUsergroupsV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 

    try:
        # Get User's Usergroups
        api_response = api_instance.user_get_usergroups_v1(pki_user_id)
        print("The response of ObjectUserApi->user_get_usergroups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_get_usergroups_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 

### Return type

[**UserGetUsergroupsV1Response**](UserGetUsergroupsV1Response.md)

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

# **user_send_password_reset_v1**
> UserSendPasswordResetV1Response user_send_password_reset_v1(pki_user_id, body)

Send password reset

Send the password reset email

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.user_send_password_reset_v1_response import UserSendPasswordResetV1Response
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
    api_instance = eZmaxApi.ObjectUserApi(api_client)
    pki_user_id = 56 # int | 
    body = None # object | 

    try:
        # Send password reset
        api_response = api_instance.user_send_password_reset_v1(pki_user_id, body)
        print("The response of ObjectUserApi->user_send_password_reset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUserApi->user_send_password_reset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_user_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**UserSendPasswordResetV1Response**](UserSendPasswordResetV1Response.md)

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

