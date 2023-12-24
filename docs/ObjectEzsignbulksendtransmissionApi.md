# eZmaxApi.ObjectEzsignbulksendtransmissionApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignbulksendtransmission_get_csv_errors_v1**](ObjectEzsignbulksendtransmissionApi.md#ezsignbulksendtransmission_get_csv_errors_v1) | **GET** /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getCsvErrors | Retrieve an existing Ezsignbulksendtransmission&#39;s Csv containing errors
[**ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1**](ObjectEzsignbulksendtransmissionApi.md#ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1) | **GET** /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getEzsignsignaturesAutomatic | Retrieve an existing Ezsignbulksendtransmission&#39;s automatic Ezsignsignatures
[**ezsignbulksendtransmission_get_forms_data_v1**](ObjectEzsignbulksendtransmissionApi.md#ezsignbulksendtransmission_get_forms_data_v1) | **GET** /1/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}/getFormsData | Retrieve an existing Ezsignbulksendtransmission&#39;s forms data
[**ezsignbulksendtransmission_get_object_v2**](ObjectEzsignbulksendtransmissionApi.md#ezsignbulksendtransmission_get_object_v2) | **GET** /2/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID} | Retrieve an existing Ezsignbulksendtransmission


# **ezsignbulksendtransmission_get_csv_errors_v1**
> str ezsignbulksendtransmission_get_csv_errors_v1(pki_ezsignbulksendtransmission_id)

Retrieve an existing Ezsignbulksendtransmission's Csv containing errors



### Example

* Api Key Authentication (Authorization):

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

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ObjectEzsignbulksendtransmissionApi(api_client)
    pki_ezsignbulksendtransmission_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksendtransmission's Csv containing errors
        api_response = api_instance.ezsignbulksendtransmission_get_csv_errors_v1(pki_ezsignbulksendtransmission_id)
        print("The response of ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_csv_errors_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_csv_errors_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksendtransmission_id** | **int**|  | 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1**
> EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1(pki_ezsignbulksendtransmission_id)

Retrieve an existing Ezsignbulksendtransmission's automatic Ezsignsignatures

Return the Ezsignsignatures that can be signed by the current user at the current step in the process

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1_response import EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendtransmissionApi(api_client)
    pki_ezsignbulksendtransmission_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksendtransmission's automatic Ezsignsignatures
        api_response = api_instance.ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1(pki_ezsignbulksendtransmission_id)
        print("The response of ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_ezsignsignatures_automatic_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksendtransmission_id** | **int**|  | 

### Return type

[**EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response**](EzsignbulksendtransmissionGetEzsignsignaturesAutomaticV1Response.md)

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

# **ezsignbulksendtransmission_get_forms_data_v1**
> EzsignbulksendtransmissionGetFormsDataV1Response ezsignbulksendtransmission_get_forms_data_v1(pki_ezsignbulksendtransmission_id)

Retrieve an existing Ezsignbulksendtransmission's forms data



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignbulksendtransmission_get_forms_data_v1_response import EzsignbulksendtransmissionGetFormsDataV1Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendtransmissionApi(api_client)
    pki_ezsignbulksendtransmission_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksendtransmission's forms data
        api_response = api_instance.ezsignbulksendtransmission_get_forms_data_v1(pki_ezsignbulksendtransmission_id)
        print("The response of ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_forms_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_forms_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksendtransmission_id** | **int**|  | 

### Return type

[**EzsignbulksendtransmissionGetFormsDataV1Response**](EzsignbulksendtransmissionGetFormsDataV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsignbulksendtransmission_get_object_v2**
> EzsignbulksendtransmissionGetObjectV2Response ezsignbulksendtransmission_get_object_v2(pki_ezsignbulksendtransmission_id)

Retrieve an existing Ezsignbulksendtransmission



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import eZmaxApi
from eZmaxApi.models.ezsignbulksendtransmission_get_object_v2_response import EzsignbulksendtransmissionGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsignbulksendtransmissionApi(api_client)
    pki_ezsignbulksendtransmission_id = 56 # int | 

    try:
        # Retrieve an existing Ezsignbulksendtransmission
        api_response = api_instance.ezsignbulksendtransmission_get_object_v2(pki_ezsignbulksendtransmission_id)
        print("The response of ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignbulksendtransmissionApi->ezsignbulksendtransmission_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignbulksendtransmission_id** | **int**|  | 

### Return type

[**EzsignbulksendtransmissionGetObjectV2Response**](EzsignbulksendtransmissionGetObjectV2Response.md)

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

