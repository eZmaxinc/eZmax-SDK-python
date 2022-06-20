# eZmaxApi.ModuleEzsignApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsign_suggest_signers_v1**](ModuleEzsignApi.md#ezsign_suggest_signers_v1) | **GET** /1/module/ezsign/suggestSigners | Suggest signers
[**ezsign_suggest_templates_v1**](ModuleEzsignApi.md#ezsign_suggest_templates_v1) | **GET** /1/module/ezsign/suggestTemplates | Suggest templates


# **ezsign_suggest_signers_v1**
> EzsignSuggestSignersV1Response ezsign_suggest_signers_v1()

Suggest signers

Retrieve previously used Ezsignsigners and all users from the system

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import module_ezsign_api
from eZmaxApi.model.ezsign_suggest_signers_v1_response import EzsignSuggestSignersV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = module_ezsign_api.ModuleEzsignApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Suggest signers
        api_response = api_instance.ezsign_suggest_signers_v1()
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ModuleEzsignApi->ezsign_suggest_signers_v1: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EzsignSuggestSignersV1Response**](EzsignSuggestSignersV1Response.md)

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

# **ezsign_suggest_templates_v1**
> EzsignSuggestTemplatesV1Response ezsign_suggest_templates_v1()

Suggest templates

Retrieve Ezsigntemplates and Ezsigntemplatepackages that can be imported in a Ezsignfolder

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import module_ezsign_api
from eZmaxApi.model.ezsign_suggest_templates_v1_response import EzsignSuggestTemplatesV1Response
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
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = module_ezsign_api.ModuleEzsignApi(api_client)
    fki_ezsignfoldertype_id = FieldPkiEzsignfoldertypeID(5) # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Suggest templates
        api_response = api_instance.ezsign_suggest_templates_v1(fki_ezsignfoldertype_id=fki_ezsignfoldertype_id)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ModuleEzsignApi->ezsign_suggest_templates_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fki_ezsignfoldertype_id** | **int**|  | [optional]

### Return type

[**EzsignSuggestTemplatesV1Response**](EzsignSuggestTemplatesV1Response.md)

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

