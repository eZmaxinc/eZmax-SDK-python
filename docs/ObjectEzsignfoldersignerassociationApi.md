# eZmaxApi.ObjectEzsignfoldersignerassociationApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignfoldersignerassociation_create_embedded_url_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_create_embedded_url_v1) | **POST** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/createEmbeddedUrl | Creates an Url to allow embedded signing
[**ezsignfoldersignerassociation_create_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_create_object_v1) | **POST** /1/object/ezsignfoldersignerassociation | Create a new Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_create_object_v2**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_create_object_v2) | **POST** /2/object/ezsignfoldersignerassociation | Create a new Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_delete_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_delete_object_v1) | **DELETE** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Delete an existing Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_edit_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_edit_object_v1) | **PUT** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Edit an existing Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_force_disconnect_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_force_disconnect_v1) | **POST** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/forceDisconnect | Disconnects the Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_get_in_person_login_url_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_get_in_person_login_url_v1) | **GET** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}/getInPersonLoginUrl | Retrieve a Login Url to allow In-Person signing
[**ezsignfoldersignerassociation_get_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_get_object_v1) | **GET** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Retrieve an existing Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_get_object_v2**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_get_object_v2) | **GET** /2/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Retrieve an existing Ezsignfoldersignerassociation
[**ezsignfoldersignerassociation_patch_object_v1**](ObjectEzsignfoldersignerassociationApi.md#ezsignfoldersignerassociation_patch_object_v1) | **PATCH** /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID} | Patch an existing Ezsignfoldersignerassociation


# **ezsignfoldersignerassociation_create_embedded_url_v1**
> EzsignfoldersignerassociationCreateEmbeddedUrlV1Response ezsignfoldersignerassociation_create_embedded_url_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_create_embedded_url_v1_request)

Creates an Url to allow embedded signing

This endpoint creates an Url that can be used in a browser or embedded in an I-Frame to allow signing.  The signer Login type must be configured as Embedded.  There will be a list to retrieve informations after the signing happens in the embedded version. To do so, there is a list of parameter to add to your sReturnUrl.  In example: https://www.example.com/sReturl?sParameter1&sParameter2. The sParameter1 et sParameter2 will be replace when we will redirect on the url.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_create_embedded_url_v1_request import EzsignfoldersignerassociationCreateEmbeddedUrlV1Request
from eZmaxApi.models.ezsignfoldersignerassociation_create_embedded_url_v1_response import EzsignfoldersignerassociationCreateEmbeddedUrlV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 
    ezsignfoldersignerassociation_create_embedded_url_v1_request = eZmaxApi.EzsignfoldersignerassociationCreateEmbeddedUrlV1Request() # EzsignfoldersignerassociationCreateEmbeddedUrlV1Request | 

    try:
        # Creates an Url to allow embedded signing
        api_response = api_instance.ezsignfoldersignerassociation_create_embedded_url_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_create_embedded_url_v1_request)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_embedded_url_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_embedded_url_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 
 **ezsignfoldersignerassociation_create_embedded_url_v1_request** | [**EzsignfoldersignerassociationCreateEmbeddedUrlV1Request**](EzsignfoldersignerassociationCreateEmbeddedUrlV1Request.md)|  | 

### Return type

[**EzsignfoldersignerassociationCreateEmbeddedUrlV1Response**](EzsignfoldersignerassociationCreateEmbeddedUrlV1Response.md)

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

# **ezsignfoldersignerassociation_create_object_v1**
> EzsignfoldersignerassociationCreateObjectV1Response ezsignfoldersignerassociation_create_object_v1(ezsignfoldersignerassociation_create_object_v1_request)

Create a new Ezsignfoldersignerassociation

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v1_request import EzsignfoldersignerassociationCreateObjectV1Request
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v1_response import EzsignfoldersignerassociationCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    ezsignfoldersignerassociation_create_object_v1_request = [eZmaxApi.EzsignfoldersignerassociationCreateObjectV1Request()] # List[EzsignfoldersignerassociationCreateObjectV1Request] | 

    try:
        # Create a new Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_create_object_v1(ezsignfoldersignerassociation_create_object_v1_request)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfoldersignerassociation_create_object_v1_request** | [**List[EzsignfoldersignerassociationCreateObjectV1Request]**](EzsignfoldersignerassociationCreateObjectV1Request.md)|  | 

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

# **ezsignfoldersignerassociation_create_object_v2**
> EzsignfoldersignerassociationCreateObjectV2Response ezsignfoldersignerassociation_create_object_v2(ezsignfoldersignerassociation_create_object_v2_request)

Create a new Ezsignfoldersignerassociation

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v2_request import EzsignfoldersignerassociationCreateObjectV2Request
from eZmaxApi.models.ezsignfoldersignerassociation_create_object_v2_response import EzsignfoldersignerassociationCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    ezsignfoldersignerassociation_create_object_v2_request = eZmaxApi.EzsignfoldersignerassociationCreateObjectV2Request() # EzsignfoldersignerassociationCreateObjectV2Request | 

    try:
        # Create a new Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_create_object_v2(ezsignfoldersignerassociation_create_object_v2_request)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsignfoldersignerassociation_create_object_v2_request** | [**EzsignfoldersignerassociationCreateObjectV2Request**](EzsignfoldersignerassociationCreateObjectV2Request.md)|  | 

### Return type

[**EzsignfoldersignerassociationCreateObjectV2Response**](EzsignfoldersignerassociationCreateObjectV2Response.md)

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
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_delete_object_v1_response import EzsignfoldersignerassociationDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 

    try:
        # Delete an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_delete_object_v1(pki_ezsignfoldersignerassociation_id)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 

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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfoldersignerassociation_edit_object_v1**
> EzsignfoldersignerassociationEditObjectV1Response ezsignfoldersignerassociation_edit_object_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_edit_object_v1_request)

Edit an existing Ezsignfoldersignerassociation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_edit_object_v1_request import EzsignfoldersignerassociationEditObjectV1Request
from eZmaxApi.models.ezsignfoldersignerassociation_edit_object_v1_response import EzsignfoldersignerassociationEditObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 
    ezsignfoldersignerassociation_edit_object_v1_request = eZmaxApi.EzsignfoldersignerassociationEditObjectV1Request() # EzsignfoldersignerassociationEditObjectV1Request | 

    try:
        # Edit an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_edit_object_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_edit_object_v1_request)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_edit_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_edit_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 
 **ezsignfoldersignerassociation_edit_object_v1_request** | [**EzsignfoldersignerassociationEditObjectV1Request**](EzsignfoldersignerassociationEditObjectV1Request.md)|  | 

### Return type

[**EzsignfoldersignerassociationEditObjectV1Response**](EzsignfoldersignerassociationEditObjectV1Response.md)

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

# **ezsignfoldersignerassociation_force_disconnect_v1**
> EzsignfoldersignerassociationForceDisconnectV1Response ezsignfoldersignerassociation_force_disconnect_v1(pki_ezsignfoldersignerassociation_id, body)

Disconnects the Ezsignfoldersignerassociation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_force_disconnect_v1_response import EzsignfoldersignerassociationForceDisconnectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 
    body = None # object | 

    try:
        # Disconnects the Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_force_disconnect_v1(pki_ezsignfoldersignerassociation_id, body)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_force_disconnect_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_force_disconnect_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzsignfoldersignerassociationForceDisconnectV1Response**](EzsignfoldersignerassociationForceDisconnectV1Response.md)

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

# **ezsignfoldersignerassociation_get_in_person_login_url_v1**
> EzsignfoldersignerassociationGetInPersonLoginUrlV1Response ezsignfoldersignerassociation_get_in_person_login_url_v1(pki_ezsignfoldersignerassociation_id)

Retrieve a Login Url to allow In-Person signing

This endpoint returns a Login Url that can be used in a browser or embedded in an I-Frame to allow in person signing.  The signer Login type must be configured as In-Person.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_get_in_person_login_url_v1_response import EzsignfoldersignerassociationGetInPersonLoginUrlV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 

    try:
        # Retrieve a Login Url to allow In-Person signing
        api_response = api_instance.ezsignfoldersignerassociation_get_in_person_login_url_v1(pki_ezsignfoldersignerassociation_id)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_in_person_login_url_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_in_person_login_url_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 

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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfoldersignerassociation_get_object_v1**
> EzsignfoldersignerassociationGetObjectV1Response ezsignfoldersignerassociation_get_object_v1(pki_ezsignfoldersignerassociation_id)

Retrieve an existing Ezsignfoldersignerassociation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v1_response import EzsignfoldersignerassociationGetObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_get_object_v1(pki_ezsignfoldersignerassociation_id)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 

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
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignfoldersignerassociation_get_object_v2**
> EzsignfoldersignerassociationGetObjectV2Response ezsignfoldersignerassociation_get_object_v2(pki_ezsignfoldersignerassociation_id)

Retrieve an existing Ezsignfoldersignerassociation



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v2_response import EzsignfoldersignerassociationGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_get_object_v2(pki_ezsignfoldersignerassociation_id)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 

### Return type

[**EzsignfoldersignerassociationGetObjectV2Response**](EzsignfoldersignerassociationGetObjectV2Response.md)

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

# **ezsignfoldersignerassociation_patch_object_v1**
> EzsignfoldersignerassociationPatchObjectV1Response ezsignfoldersignerassociation_patch_object_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_patch_object_v1_request)

Patch an existing Ezsignfoldersignerassociation

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignfoldersignerassociation_patch_object_v1_request import EzsignfoldersignerassociationPatchObjectV1Request
from eZmaxApi.models.ezsignfoldersignerassociation_patch_object_v1_response import EzsignfoldersignerassociationPatchObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsignfoldersignerassociationApi(api_client)
    pki_ezsignfoldersignerassociation_id = 56 # int | 
    ezsignfoldersignerassociation_patch_object_v1_request = eZmaxApi.EzsignfoldersignerassociationPatchObjectV1Request() # EzsignfoldersignerassociationPatchObjectV1Request | 

    try:
        # Patch an existing Ezsignfoldersignerassociation
        api_response = api_instance.ezsignfoldersignerassociation_patch_object_v1(pki_ezsignfoldersignerassociation_id, ezsignfoldersignerassociation_patch_object_v1_request)
        print("The response of ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignfoldersignerassociationApi->ezsignfoldersignerassociation_patch_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignfoldersignerassociation_id** | **int**|  | 
 **ezsignfoldersignerassociation_patch_object_v1_request** | [**EzsignfoldersignerassociationPatchObjectV1Request**](EzsignfoldersignerassociationPatchObjectV1Request.md)|  | 

### Return type

[**EzsignfoldersignerassociationPatchObjectV1Response**](EzsignfoldersignerassociationPatchObjectV1Response.md)

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

