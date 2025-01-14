# eZmaxApi.ObjectUsergroupApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroup_create_object_v1**](ObjectUsergroupApi.md#usergroup_create_object_v1) | **POST** /1/object/usergroup | Create a new Usergroup
[**usergroup_edit_object_v1**](ObjectUsergroupApi.md#usergroup_edit_object_v1) | **PUT** /1/object/usergroup/{pkiUsergroupID} | Edit an existing Usergroup
[**usergroup_edit_permissions_v1**](ObjectUsergroupApi.md#usergroup_edit_permissions_v1) | **PUT** /1/object/usergroup/{pkiUsergroupID}/editPermissions | Edit multiple Permissions
[**usergroup_edit_usergroupdelegations_v1**](ObjectUsergroupApi.md#usergroup_edit_usergroupdelegations_v1) | **PUT** /1/object/usergroup/{pkiUsergroupID}/editUsergroupdelegations | Edit multiple Usergroupdelegations
[**usergroup_edit_usergroupmemberships_v1**](ObjectUsergroupApi.md#usergroup_edit_usergroupmemberships_v1) | **PUT** /1/object/usergroup/{pkiUsergroupID}/editUsergroupmemberships | Edit multiple Usergroupmemberships
[**usergroup_get_autocomplete_v2**](ObjectUsergroupApi.md#usergroup_get_autocomplete_v2) | **GET** /2/object/usergroup/getAutocomplete/{sSelector} | Retrieve Usergroups and IDs
[**usergroup_get_list_v1**](ObjectUsergroupApi.md#usergroup_get_list_v1) | **GET** /1/object/usergroup/getList | Retrieve Usergroup list
[**usergroup_get_object_v2**](ObjectUsergroupApi.md#usergroup_get_object_v2) | **GET** /2/object/usergroup/{pkiUsergroupID} | Retrieve an existing Usergroup
[**usergroup_get_permissions_v1**](ObjectUsergroupApi.md#usergroup_get_permissions_v1) | **GET** /1/object/usergroup/{pkiUsergroupID}/getPermissions | Retrieve an existing Usergroup&#39;s Permissions
[**usergroup_get_usergroupdelegations_v1**](ObjectUsergroupApi.md#usergroup_get_usergroupdelegations_v1) | **GET** /1/object/usergroup/{pkiUsergroupID}/getUsergroupdelegations | Retrieve an existing Usergroup&#39;s Usergroupdelegations
[**usergroup_get_usergroupmemberships_v1**](ObjectUsergroupApi.md#usergroup_get_usergroupmemberships_v1) | **GET** /1/object/usergroup/{pkiUsergroupID}/getUsergroupmemberships | Retrieve an existing Usergroup&#39;s Usergroupmemberships


# **usergroup_create_object_v1**
> UsergroupCreateObjectV1Response usergroup_create_object_v1(usergroup_create_object_v1_request)

Create a new Usergroup

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_create_object_v1_request import UsergroupCreateObjectV1Request
from eZmaxApi.models.usergroup_create_object_v1_response import UsergroupCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    usergroup_create_object_v1_request = eZmaxApi.UsergroupCreateObjectV1Request() # UsergroupCreateObjectV1Request | 

    try:
        # Create a new Usergroup
        api_response = api_instance.usergroup_create_object_v1(usergroup_create_object_v1_request)
        print("The response of ObjectUsergroupApi->usergroup_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_create_object_v1_request** | [**UsergroupCreateObjectV1Request**](UsergroupCreateObjectV1Request.md)|  | 

### Return type

[**UsergroupCreateObjectV1Response**](UsergroupCreateObjectV1Response.md)

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

# **usergroup_edit_object_v1**
> UsergroupEditObjectV1Response usergroup_edit_object_v1(pki_usergroup_id, usergroup_edit_object_v1_request)

Edit an existing Usergroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_edit_object_v1_request import UsergroupEditObjectV1Request
from eZmaxApi.models.usergroup_edit_object_v1_response import UsergroupEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 
    usergroup_edit_object_v1_request = eZmaxApi.UsergroupEditObjectV1Request() # UsergroupEditObjectV1Request | 

    try:
        # Edit an existing Usergroup
        api_response = api_instance.usergroup_edit_object_v1(pki_usergroup_id, usergroup_edit_object_v1_request)
        print("The response of ObjectUsergroupApi->usergroup_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 
 **usergroup_edit_object_v1_request** | [**UsergroupEditObjectV1Request**](UsergroupEditObjectV1Request.md)|  | 

### Return type

[**UsergroupEditObjectV1Response**](UsergroupEditObjectV1Response.md)

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

# **usergroup_edit_permissions_v1**
> UsergroupEditPermissionsV1Response usergroup_edit_permissions_v1(pki_usergroup_id, usergroup_edit_permissions_v1_request)

Edit multiple Permissions

Using this endpoint, you can edit multiple Permissions at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_edit_permissions_v1_request import UsergroupEditPermissionsV1Request
from eZmaxApi.models.usergroup_edit_permissions_v1_response import UsergroupEditPermissionsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 
    usergroup_edit_permissions_v1_request = eZmaxApi.UsergroupEditPermissionsV1Request() # UsergroupEditPermissionsV1Request | 

    try:
        # Edit multiple Permissions
        api_response = api_instance.usergroup_edit_permissions_v1(pki_usergroup_id, usergroup_edit_permissions_v1_request)
        print("The response of ObjectUsergroupApi->usergroup_edit_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_edit_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 
 **usergroup_edit_permissions_v1_request** | [**UsergroupEditPermissionsV1Request**](UsergroupEditPermissionsV1Request.md)|  | 

### Return type

[**UsergroupEditPermissionsV1Response**](UsergroupEditPermissionsV1Response.md)

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

# **usergroup_edit_usergroupdelegations_v1**
> UsergroupEditUsergroupdelegationsV1Response usergroup_edit_usergroupdelegations_v1(pki_usergroup_id, usergroup_edit_usergroupdelegations_v1_request)

Edit multiple Usergroupdelegations

Edit multiple Usergroupdelegations

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_edit_usergroupdelegations_v1_request import UsergroupEditUsergroupdelegationsV1Request
from eZmaxApi.models.usergroup_edit_usergroupdelegations_v1_response import UsergroupEditUsergroupdelegationsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 
    usergroup_edit_usergroupdelegations_v1_request = eZmaxApi.UsergroupEditUsergroupdelegationsV1Request() # UsergroupEditUsergroupdelegationsV1Request | 

    try:
        # Edit multiple Usergroupdelegations
        api_response = api_instance.usergroup_edit_usergroupdelegations_v1(pki_usergroup_id, usergroup_edit_usergroupdelegations_v1_request)
        print("The response of ObjectUsergroupApi->usergroup_edit_usergroupdelegations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_edit_usergroupdelegations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 
 **usergroup_edit_usergroupdelegations_v1_request** | [**UsergroupEditUsergroupdelegationsV1Request**](UsergroupEditUsergroupdelegationsV1Request.md)|  | 

### Return type

[**UsergroupEditUsergroupdelegationsV1Response**](UsergroupEditUsergroupdelegationsV1Response.md)

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

# **usergroup_edit_usergroupmemberships_v1**
> UsergroupEditUsergroupmembershipsV1Response usergroup_edit_usergroupmemberships_v1(pki_usergroup_id, usergroup_edit_usergroupmemberships_v1_request)

Edit multiple Usergroupmemberships

Using this endpoint, you can edit multiple Usergroupmemberships at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_edit_usergroupmemberships_v1_request import UsergroupEditUsergroupmembershipsV1Request
from eZmaxApi.models.usergroup_edit_usergroupmemberships_v1_response import UsergroupEditUsergroupmembershipsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 
    usergroup_edit_usergroupmemberships_v1_request = eZmaxApi.UsergroupEditUsergroupmembershipsV1Request() # UsergroupEditUsergroupmembershipsV1Request | 

    try:
        # Edit multiple Usergroupmemberships
        api_response = api_instance.usergroup_edit_usergroupmemberships_v1(pki_usergroup_id, usergroup_edit_usergroupmemberships_v1_request)
        print("The response of ObjectUsergroupApi->usergroup_edit_usergroupmemberships_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_edit_usergroupmemberships_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 
 **usergroup_edit_usergroupmemberships_v1_request** | [**UsergroupEditUsergroupmembershipsV1Request**](UsergroupEditUsergroupmembershipsV1Request.md)|  | 

### Return type

[**UsergroupEditUsergroupmembershipsV1Response**](UsergroupEditUsergroupmembershipsV1Response.md)

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

# **usergroup_get_autocomplete_v2**
> UsergroupGetAutocompleteV2Response usergroup_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Usergroups and IDs

Get the list of Usergroup to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.usergroup_get_autocomplete_v2_response import UsergroupGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    s_selector = 's_selector_example' # str | The type of Usergroups to return
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Usergroups and IDs
        api_response = api_instance.usergroup_get_autocomplete_v2(s_selector, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectUsergroupApi->usergroup_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Usergroups to return | 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**UsergroupGetAutocompleteV2Response**](UsergroupGetAutocompleteV2Response.md)

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

# **usergroup_get_list_v1**
> UsergroupGetListV1Response usergroup_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)

Retrieve Usergroup list



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.usergroup_get_list_v1_response import UsergroupGetListV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    e_order_by = 'e_order_by_example' # str | Specify how you want the results to be sorted (optional)
    i_row_max = 56 # int |  (optional)
    i_row_offset = 0 # int |  (optional) (default to 0)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)
    s_filter = 's_filter_example' # str |  (optional)

    try:
        # Retrieve Usergroup list
        api_response = api_instance.usergroup_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        print("The response of ObjectUsergroupApi->usergroup_get_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_list_v1: %s\n" % e)
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

[**UsergroupGetListV1Response**](UsergroupGetListV1Response.md)

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

# **usergroup_get_object_v2**
> UsergroupGetObjectV2Response usergroup_get_object_v2(pki_usergroup_id)

Retrieve an existing Usergroup



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_get_object_v2_response import UsergroupGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 

    try:
        # Retrieve an existing Usergroup
        api_response = api_instance.usergroup_get_object_v2(pki_usergroup_id)
        print("The response of ObjectUsergroupApi->usergroup_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 

### Return type

[**UsergroupGetObjectV2Response**](UsergroupGetObjectV2Response.md)

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

# **usergroup_get_permissions_v1**
> UsergroupGetPermissionsV1Response usergroup_get_permissions_v1(pki_usergroup_id)

Retrieve an existing Usergroup's Permissions

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_get_permissions_v1_response import UsergroupGetPermissionsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 

    try:
        # Retrieve an existing Usergroup's Permissions
        api_response = api_instance.usergroup_get_permissions_v1(pki_usergroup_id)
        print("The response of ObjectUsergroupApi->usergroup_get_permissions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_permissions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 

### Return type

[**UsergroupGetPermissionsV1Response**](UsergroupGetPermissionsV1Response.md)

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

# **usergroup_get_usergroupdelegations_v1**
> UsergroupGetUsergroupdelegationsV1Response usergroup_get_usergroupdelegations_v1(pki_usergroup_id)

Retrieve an existing Usergroup's Usergroupdelegations

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_get_usergroupdelegations_v1_response import UsergroupGetUsergroupdelegationsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 

    try:
        # Retrieve an existing Usergroup's Usergroupdelegations
        api_response = api_instance.usergroup_get_usergroupdelegations_v1(pki_usergroup_id)
        print("The response of ObjectUsergroupApi->usergroup_get_usergroupdelegations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_usergroupdelegations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 

### Return type

[**UsergroupGetUsergroupdelegationsV1Response**](UsergroupGetUsergroupdelegationsV1Response.md)

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

# **usergroup_get_usergroupmemberships_v1**
> UsergroupGetUsergroupmembershipsV1Response usergroup_get_usergroupmemberships_v1(pki_usergroup_id)

Retrieve an existing Usergroup's Usergroupmemberships

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.usergroup_get_usergroupmemberships_v1_response import UsergroupGetUsergroupmembershipsV1Response
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
    api_instance = eZmaxApi.ObjectUsergroupApi(api_client)
    pki_usergroup_id = 56 # int | 

    try:
        # Retrieve an existing Usergroup's Usergroupmemberships
        api_response = api_instance.usergroup_get_usergroupmemberships_v1(pki_usergroup_id)
        print("The response of ObjectUsergroupApi->usergroup_get_usergroupmemberships_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectUsergroupApi->usergroup_get_usergroupmemberships_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_usergroup_id** | **int**|  | 

### Return type

[**UsergroupGetUsergroupmembershipsV1Response**](UsergroupGetUsergroupmembershipsV1Response.md)

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

