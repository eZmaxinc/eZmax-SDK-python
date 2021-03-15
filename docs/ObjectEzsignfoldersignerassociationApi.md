# eZmaxinc/eZmax-SDK-python.ObjectEzsignfoldersignerassociationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignfoldersignerassociation_create_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_create_object_v1) | **POST** /1/object/ezsignfoldersignerassociation | Create a new Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_delete_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_delete_object_v1) | **DELETE** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Delete an existing Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_get_children_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_get_children_v1) | **GET** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/getChildren | Retrieve an existing Ezsignfoldersignerassociation&#39;s children IDs
[**ezsignfoldersignerassociation_get_in_person_login_url_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_get_in_person_login_url_v1) | **GET** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/getInPersonLoginUrl | Retrieve a Login Url to allow In-Person signing
[**ezsignfoldersignerassociation_get_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_get_object_v1) | **GET** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Retrieve an existing Ezsignfoldersignerassociation


# **ezsignfoldersignerassociation_create_object_v1**
> EzsignfoldersignerassociationCreateObjectV1Response ezsignfoldersignerassociation_create_object_v1(ezsignfoldersignerassociation_create_object_v1_request)

Create a new Ezsignfoldersignerassociation

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfoldersignerassociation_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfoldersignerassociation_create_object_v1_request import EzsignfoldersignerassociationCreateObjectV1Request
from eZmaxinc/eZmax-SDK-python.model.ezsignfoldersignerassociation_create_object_v1_response import EzsignfoldersignerassociationCreateObjectV1Response
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
    api_instance = object_ezsignfoldersignerassociation_api.ObjectEzsignfoldersignerassociationApi(api_client)
    ezsignfoldersignerassociation_create_object_v1_request = [
        EzsignfoldersignerassociationCreateObjectV1Request(
            obj_ezsignfoldersignerassociation=EzsignfoldersignerassociationRequest(
                fki_user_id=1,
                fki_ezsignfolder_id=1,
            ),
            obj_ezsignfoldersignerassociation_compound=EzsignfoldersignerassociationRequestCompound(
                obj_ezsignsigner=EzsignsignerRequestCompound(
                    obj_contact=EzsignsignerRequestCompoundContact(
                        s_contact_firstname="s_contact_firstname_example",
                        s_contact_lastname="s_contact_lastname_example",
                        fki_language_id=FieldPkiLanguageID(2),
                        s_email_address="s_email_address_example",
                        s_phone_number="s_phone_number_example",
                        s_phone_number_cell="s_phone_number_cell_example",
                    ),
                ),
            ),
        ),
    ] # [EzsignfoldersignerassociationCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_create_object_v1(ezsignfoldersignerassociation_create_object_v1_request)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfoldersignerassociation_create_object_v1_request** | [**[EzsignfoldersignerassociationCreateObjectV1Request]**](EzsignfoldersignerassociationCreateObjectV1Request.md)|  |

### Return type

[**EzsignfoldersignerassociationCreateObjectV1Response**](EzsignfoldersignerassociationCreateObjectV1Response.md)

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

# **ezsignfoldersignerassociation_delete_object_v1**
> EzsignfoldersignerassociationDeleteObjectV1Response ezsignfoldersignerassociation_delete_object_v1(pki_ezsignfoldersignerassociation_id)

Delete an existing Ezsignfoldersignerassociation

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfoldersignerassociation_api
from eZmaxinc/eZmax-SDK-python.model.common_response_error import CommonResponseError
from eZmaxinc/eZmax-SDK-python.model.ezsignfoldersignerassociation_delete_object_v1_response import EzsignfoldersignerassociationDeleteObjectV1Response
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
    api_instance = object_ezsignfoldersignerassociation_api.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 1 # int | The unique ID of the Ezsignfoldersignerassociation

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_delete_object_v1(pki_ezsignfoldersignerassociation_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_delete_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**| The unique ID of the Ezsignfoldersignerassociation |

### Return type

[**EzsignfoldersignerassociationDeleteObjectV1Response**](EzsignfoldersignerassociationDeleteObjectV1Response.md)

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

# **ezsignfoldersignerassociation_get_children_v1**
> ezsignfoldersignerassociation_get_children_v1(pki_ezsignfoldersignerassociation_id)

Retrieve an existing Ezsignfoldersignerassociation's children IDs

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfoldersignerassociation_api
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
    api_instance = object_ezsignfoldersignerassociation_api.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 1 # int | The unique ID of the Ezsignfoldersignerassociation

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfoldersignerassociation's children IDs
        api_instance.ezsignfoldersignerassociation_get_children_v1(pki_ezsignfoldersignerassociation_id)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_children_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**| The unique ID of the Ezsignfoldersignerassociation |

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

# **ezsignfoldersignerassociation_get_in_person_login_url_v1**
> EzsignfoldersignerassociationGetInPersonLoginUrlV1Response ezsignfoldersignerassociation_get_in_person_login_url_v1(pki_ezsignfoldersignerassociation_id)

Retrieve a Login Url to allow In-Person signing

This endpoint returns a Login Url that can be used in a browser or embedded in an I-Frame to allow in person signing.  The signer Login type must be configured as In-Person.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfoldersignerassociation_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfoldersignerassociation_get_in_person_login_url_v1_response import EzsignfoldersignerassociationGetInPersonLoginUrlV1Response
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
    api_instance = object_ezsignfoldersignerassociation_api.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 1 # int | The unique ID of the Ezsignfoldersignerassociation

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Login Url to allow In-Person signing
        api_response = api_instance.ezsignfoldersignerassociation_get_in_person_login_url_v1(pki_ezsignfoldersignerassociation_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_in_person_login_url_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**| The unique ID of the Ezsignfoldersignerassociation |

### Return type

[**EzsignfoldersignerassociationGetInPersonLoginUrlV1Response**](EzsignfoldersignerassociationGetInPersonLoginUrlV1Response.md)

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

# **ezsignfoldersignerassociation_get_object_v1**
> EzsignfoldersignerassociationGetObjectV1Response ezsignfoldersignerassociation_get_object_v1(pki_ezsignfoldersignerassociation_id)

Retrieve an existing Ezsignfoldersignerassociation

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api import object_ezsignfoldersignerassociation_api
from eZmaxinc/eZmax-SDK-python.model.ezsignfoldersignerassociation_get_object_v1_response import EzsignfoldersignerassociationGetObjectV1Response
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
    api_instance = object_ezsignfoldersignerassociation_api.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 1 # int | The unique ID of the Ezsignfoldersignerassociation

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_get_object_v1(pki_ezsignfoldersignerassociation_id)
        pprint(api_response)
    except eZmaxinc/eZmax-SDK-python.ApiException as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**| The unique ID of the Ezsignfoldersignerassociation |

### Return type

[**EzsignfoldersignerassociationGetObjectV1Response**](EzsignfoldersignerassociationGetObjectV1Response.md)

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

