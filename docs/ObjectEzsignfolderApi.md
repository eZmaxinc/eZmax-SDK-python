# eZmaxinc/eZmax-SDK-python.ObjectEzsignfolderApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignfolder_create_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_create_object_v1) | **POST** /1/object/ezsignfolder | Create a new Ezsignfolder
[**ezsignfolder_delete_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_delete_object_v1) | **DELETE** /1/object/ezsignfolder/{pkiEzsignfolderID} | Delete an existing Ezsignfolder
[**ezsignfolder_edit_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_edit_object_v1) | **PUT** /1/object/ezsignfolder/{pkiEzsignfolderID} | Modify an existing Ezsignfolder
[**ezsignfolder_get_object_get_children_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_object_get_children_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID}/getChildren | Retrieve an existing Ezsignfolder&#39;s children IDs
[**ezsignfolder_get_object_v1**](ObjectEzsignfolderApi.md#ezsignfolder_get_object_v1) | **GET** /1/object/ezsignfolder/{pkiEzsignfolderID} | Retrieve an existing Ezsignfolder
[**ezsignfolder_send_v1**](ObjectEzsignfolderApi.md#ezsignfolder_send_v1) | **POST** /1/object/ezsignfolder/{pkiEzsignfolderID}/send | Send the Ezsignfolder to the signatories for signature


# **ezsignfolder_create_object_v1**
> EzsignfolderCreateObjectV1Response ezsignfolder_create_object_v1(ezsignfolder_create_object_v1_request)

Create a new Ezsignfolder

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfolder_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_create_object_v1_response import EzsignfolderCreateObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_create_object_v1_request import EzsignfolderCreateObjectV1Request
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    ezsignfolder_create_object_v1_request = [
        EzsignfolderCreateObjectV1Request(
            obj_ezsignfolder=EzsignfolderRequest(
                fki_ezsignfoldertype_id=5,
                fki_ezsigntsarequirement_id=FieldPkiEzsigntsarequirementID(92),
                s_ezsignfolder_description="s_ezsignfolder_description_example",
                t_ezsignfolder_note="t_ezsignfolder_note_example",
                e_ezsignfolder_sendreminderfrequency=FieldEEzsignfolderSendreminderfrequency("None"),
            ),
            obj_ezsignfolder_compound=EzsignfolderRequestCompound(
                a_ezsignfoldersignerassociation=[
                    EzsignfoldersignerassociationRequest(
                        fki_user_id=1,
                        fki_ezsignfolder_id=1,
                    ),
                ],
            ),
        ),
    ] # [EzsignfolderCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignfolder
        api_response = api_instance.ezsignfolder_create_object_v1(ezsignfolder_create_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_create_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfolder_create_object_v1_request** | [**[EzsignfolderCreateObjectV1Request]**](EzsignfolderCreateObjectV1Request.md)|  |

### Return type

[**EzsignfolderCreateObjectV1Response**](EzsignfolderCreateObjectV1Response.md)

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

# **ezsignfolder_delete_object_v1**
> EzsignfolderDeleteObjectV1Response ezsignfolder_delete_object_v1(pki_ezsignfolder_id)

Delete an existing Ezsignfolder

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfolder_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_delete_object_v1_response import EzsignfolderDeleteObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = 1 # int | The unique ID of the Ezsignfolder

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsignfolder
        api_response = api_instance.ezsignfolder_delete_object_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_delete_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**| The unique ID of the Ezsignfolder |

### Return type

[**EzsignfolderDeleteObjectV1Response**](EzsignfolderDeleteObjectV1Response.md)

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
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfolder_edit_object_v1**
> EzsignfolderEditObjectV1Response ezsignfolder_edit_object_v1(pki_ezsignfolder_id, ezsignfolder_edit_object_v1_request)

Modify an existing Ezsignfolder

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfolder_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_edit_object_v1_response import EzsignfolderEditObjectV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_edit_object_v1_request import EzsignfolderEditObjectV1Request
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = 1 # int | The unique ID of the Ezsignfolder
    ezsignfolder_edit_object_v1_request = EzsignfolderEditObjectV1Request(
        obj_ezsignfolder=EzsignfolderRequest(
            fki_ezsignfoldertype_id=5,
            fki_ezsigntsarequirement_id=FieldPkiEzsigntsarequirementID(92),
            s_ezsignfolder_description="s_ezsignfolder_description_example",
            t_ezsignfolder_note="t_ezsignfolder_note_example",
            e_ezsignfolder_sendreminderfrequency=FieldEEzsignfolderSendreminderfrequency("None"),
        ),
    ) # EzsignfolderEditObjectV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Modify an existing Ezsignfolder
        api_response = api_instance.ezsignfolder_edit_object_v1(pki_ezsignfolder_id, ezsignfolder_edit_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_edit_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**| The unique ID of the Ezsignfolder |
 **ezsignfolder_edit_object_v1_request** | [**EzsignfolderEditObjectV1Request**](EzsignfolderEditObjectV1Request.md)|  |

### Return type

[**EzsignfolderEditObjectV1Response**](EzsignfolderEditObjectV1Response.md)

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

# **ezsignfolder_get_object_get_children_v1**
> ezsignfolder_get_object_get_children_v1(pki_ezsignfolder_id)

Retrieve an existing Ezsignfolder's children IDs

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfolder_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = 1 # int | The unique ID of the Ezsignfolder

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfolder's children IDs
        api_instance.ezsignfolder_get_object_get_children_v1(pki_ezsignfolder_id)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_object_get_children_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**| The unique ID of the Ezsignfolder |

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The element you are trying to work on does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfolder_get_object_v1**
> EzsignfolderGetObjectV1Response ezsignfolder_get_object_v1(pki_ezsignfolder_id)

Retrieve an existing Ezsignfolder

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfolder_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_get_object_v1_response import EzsignfolderGetObjectV1Response
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = 1 # int | The unique ID of the Ezsignfolder

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfolder
        api_response = api_instance.ezsignfolder_get_object_v1(pki_ezsignfolder_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_get_object_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**| The unique ID of the Ezsignfolder |

### Return type

[**EzsignfolderGetObjectV1Response**](EzsignfolderGetObjectV1Response.md)

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

# **ezsignfolder_send_v1**
> EzsignfolderSendV1Response ezsignfolder_send_v1(pki_ezsignfolder_id, ezsignfolder_send_v1_request)

Send the Ezsignfolder to the signatories for signature

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfolder_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_send_v1_response import EzsignfolderSendV1Response
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsignfolder_send_v1_request import EzsignfolderSendV1Request
from pprint import pprint
# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxinc/eZmax-SDK-python.Configuration(
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
with eZmaxinc/eZmax-SDK-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = object_ezsignfolder_api.ObjectEzsignfolderApi(api_client)
    pki_ezsignfolder_id = 1 # int | The unique ID of the Ezsignfolder
    ezsignfolder_send_v1_request = EzsignfolderSendV1Request(
        t_extra_message="t_extra_message_example",
    ) # EzsignfolderSendV1Request | 

    # example passing only required values which don't have defaults set
    try:
        # Send the Ezsignfolder to the signatories for signature
        api_response = api_instance.ezsignfolder_send_v1(pki_ezsignfolder_id, ezsignfolder_send_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfolderApi->ezsignfolder_send_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfolder_id** | **int**| The unique ID of the Ezsignfolder |
 **ezsignfolder_send_v1_request** | [**EzsignfolderSendV1Request**](EzsignfolderSendV1Request.md)|  |

### Return type

[**EzsignfolderSendV1Response**](EzsignfolderSendV1Response.md)

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
**422** | The syntax of the request is valid but the request cannot be completed. Look for detail in body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

