# eZmaxApi.GlobalEzmaxclientApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_ezmaxclient_version_v1**](GlobalEzmaxclientApi.md#global_ezmaxclient_version_v1) | **GET** /1/ezmaxclient/{pksEzmaxclientOs}/version | Retrieve the latest version of the Ezmaxclient


# **global_ezmaxclient_version_v1**
> GlobalEzmaxclientVersionV1Response global_ezmaxclient_version_v1(pks_ezmaxclient_os)

Retrieve the latest version of the Ezmaxclient

Retrieve the latest version of the Ezmaxclient that is available on the store.

### Example


```python
import time
import os
import eZmaxApi
from eZmaxApi.models.field_pks_ezmaxclient_os import FieldPksEzmaxclientOs
from eZmaxApi.models.global_ezmaxclient_version_v1_response import GlobalEzmaxclientVersionV1Response
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
    api_instance = eZmaxApi.GlobalEzmaxclientApi(api_client)
    pks_ezmaxclient_os = eZmaxApi.FieldPksEzmaxclientOs() # FieldPksEzmaxclientOs | 

    try:
        # Retrieve the latest version of the Ezmaxclient
        api_response = api_instance.global_ezmaxclient_version_v1(pks_ezmaxclient_os)
        print("The response of GlobalEzmaxclientApi->global_ezmaxclient_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalEzmaxclientApi->global_ezmaxclient_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pks_ezmaxclient_os** | [**FieldPksEzmaxclientOs**](.md)|  | 

### Return type

[**GlobalEzmaxclientVersionV1Response**](GlobalEzmaxclientVersionV1Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

