# eZmaxApi.ObjectEzsignpageApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsignpage_consult_v1**](ObjectEzsignpageApi.md#ezsignpage_consult_v1) | **POST** /1/object/ezsignpage/{pkiEzsignpageID}/consult | Consult an Ezsignpage


# **ezsignpage_consult_v1**
> EzsignpageConsultV1Response ezsignpage_consult_v1(pki_ezsignpage_id, body)

Consult an Ezsignpage

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsignpage_consult_v1_response import EzsignpageConsultV1Response
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
    api_instance = eZmaxApi.ObjectEzsignpageApi(api_client)
    pki_ezsignpage_id = 56 # int | 
    body = None # object | 

    try:
        # Consult an Ezsignpage
        api_response = api_instance.ezsignpage_consult_v1(pki_ezsignpage_id, body)
        print("The response of ObjectEzsignpageApi->ezsignpage_consult_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsignpageApi->ezsignpage_consult_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsignpage_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzsignpageConsultV1Response**](EzsignpageConsultV1Response.md)

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

