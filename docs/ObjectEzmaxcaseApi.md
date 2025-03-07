# eZmaxApi.ObjectEzmaxcaseApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezmaxcase_patch_object_v1**](ObjectEzmaxcaseApi.md#ezmaxcase_patch_object_v1) | **PATCH** /1/object/ezmaxcase/{pkiEzmaxcaseID} | Patch an existing Ezmaxcase


# **ezmaxcase_patch_object_v1**
> EzmaxcasePatchObjectV1Response ezmaxcase_patch_object_v1(pki_ezmaxcase_id, ezmaxcase_patch_object_v1_request)

Patch an existing Ezmaxcase



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezmaxcase_patch_object_v1_request import EzmaxcasePatchObjectV1Request
from eZmaxApi.models.ezmaxcase_patch_object_v1_response import EzmaxcasePatchObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzmaxcaseApi(api_client)
    pki_ezmaxcase_id = 56 # int | The unique ID of the Ezmaxcase
    ezmaxcase_patch_object_v1_request = eZmaxApi.EzmaxcasePatchObjectV1Request() # EzmaxcasePatchObjectV1Request | 

    try:
        # Patch an existing Ezmaxcase
        api_response = api_instance.ezmaxcase_patch_object_v1(pki_ezmaxcase_id, ezmaxcase_patch_object_v1_request)
        print("The response of ObjectEzmaxcaseApi->ezmaxcase_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzmaxcaseApi->ezmaxcase_patch_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezmaxcase_id** | **int**| The unique ID of the Ezmaxcase | 
 **ezmaxcase_patch_object_v1_request** | [**EzmaxcasePatchObjectV1Request**](EzmaxcasePatchObjectV1Request.md)|  | 

### Return type

[**EzmaxcasePatchObjectV1Response**](EzmaxcasePatchObjectV1Response.md)

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

