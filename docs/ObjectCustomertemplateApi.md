# eZmaxApi.ObjectCustomertemplateApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customertemplate_get_documenttypechecklist_v1**](ObjectCustomertemplateApi.md#customertemplate_get_documenttypechecklist_v1) | **GET** /1/object/customertemplate/{pkiCustomertemplateID}/getDocumenttypechecklist | Retrieve Document type checklist
[**customertemplate_sync_documenttypechecklist_v1**](ObjectCustomertemplateApi.md#customertemplate_sync_documenttypechecklist_v1) | **POST** /1/object/customertemplate/{pkiCustomertemplateID}/syncDocumenttypechecklist | Synchronize Document type checklist


# **customertemplate_get_documenttypechecklist_v1**
> CustomertemplateGetDocumenttypechecklistV1Response customertemplate_get_documenttypechecklist_v1(pki_customertemplate_id)

Retrieve Document type checklist

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.customertemplate_get_documenttypechecklist_v1_response import CustomertemplateGetDocumenttypechecklistV1Response
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
    api_instance = eZmaxApi.ObjectCustomertemplateApi(api_client)
    pki_customertemplate_id = 56 # int | 

    try:
        # Retrieve Document type checklist
        api_response = api_instance.customertemplate_get_documenttypechecklist_v1(pki_customertemplate_id)
        print("The response of ObjectCustomertemplateApi->customertemplate_get_documenttypechecklist_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCustomertemplateApi->customertemplate_get_documenttypechecklist_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_customertemplate_id** | **int**|  | 

### Return type

[**CustomertemplateGetDocumenttypechecklistV1Response**](CustomertemplateGetDocumenttypechecklistV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customertemplate_sync_documenttypechecklist_v1**
> CustomertemplateSyncDocumenttypechecklistV1Response customertemplate_sync_documenttypechecklist_v1(pki_customertemplate_id, body=body)

Synchronize Document type checklist

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.customertemplate_sync_documenttypechecklist_v1_response import CustomertemplateSyncDocumenttypechecklistV1Response
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
    api_instance = eZmaxApi.ObjectCustomertemplateApi(api_client)
    pki_customertemplate_id = 56 # int | 
    body = None # object |  (optional)

    try:
        # Synchronize Document type checklist
        api_response = api_instance.customertemplate_sync_documenttypechecklist_v1(pki_customertemplate_id, body=body)
        print("The response of ObjectCustomertemplateApi->customertemplate_sync_documenttypechecklist_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCustomertemplateApi->customertemplate_sync_documenttypechecklist_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_customertemplate_id** | **int**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**CustomertemplateSyncDocumenttypechecklistV1Response**](CustomertemplateSyncDocumenttypechecklistV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

