# eZmaxApi.ScimServiceProviderConfigApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_provider_config_get_object_scim_v2**](ScimServiceProviderConfigApi.md#service_provider_config_get_object_scim_v2) | **GET** /2/scim/ServiceProviderConfig | Get Service Provider Configuration


# **service_provider_config_get_object_scim_v2**
> ScimServiceProviderConfig service_provider_config_get_object_scim_v2()

Get Service Provider Configuration

### Example


```python
import time
import os
import eZmaxApi
from eZmaxApi.models.scim_service_provider_config import ScimServiceProviderConfig
from eZmaxApi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://prod.api.appcluster01.ca-central-1.ezmax.com/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = eZmaxApi.Configuration(
    host = "https://prod.api.appcluster01.ca-central-1.ezmax.com/rest"
)


# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ScimServiceProviderConfigApi(api_client)

    try:
        # Get Service Provider Configuration
        api_response = api_instance.service_provider_config_get_object_scim_v2()
        print("The response of ScimServiceProviderConfigApi->service_provider_config_get_object_scim_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScimServiceProviderConfigApi->service_provider_config_get_object_scim_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

