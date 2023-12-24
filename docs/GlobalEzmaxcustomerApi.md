# eZmaxApi.GlobalEzmaxcustomerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_ezmaxcustomer_get_configuration_v1**](GlobalEzmaxcustomerApi.md#global_ezmaxcustomer_get_configuration_v1) | **GET** /1/ezmaxcustomer/{pksEzmaxcustomerCode}/getConfiguration | Get ezmaxcustomer configuration


# **global_ezmaxcustomer_get_configuration_v1**
> GlobalEzmaxcustomerGetConfigurationV1Response global_ezmaxcustomer_get_configuration_v1(pks_ezmaxcustomer_code)

Get ezmaxcustomer configuration

Retrieve the ezmaxcustomer's specific configuration. This will help locate the proper region (ie: sInfrastructureregionCode) and the proper environment (ie: sInfrastructureenvironmenttypeDescription) where the customer's data is stored.

### Example


```python
import time
import os
import eZmaxApi
from eZmaxApi.models.global_ezmaxcustomer_get_configuration_v1_response import GlobalEzmaxcustomerGetConfigurationV1Response
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
    api_instance = eZmaxApi.GlobalEzmaxcustomerApi(api_client)
    pks_ezmaxcustomer_code = 'pks_ezmaxcustomer_code_example' # str | 

    try:
        # Get ezmaxcustomer configuration
        api_response = api_instance.global_ezmaxcustomer_get_configuration_v1(pks_ezmaxcustomer_code)
        print("The response of GlobalEzmaxcustomerApi->global_ezmaxcustomer_get_configuration_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalEzmaxcustomerApi->global_ezmaxcustomer_get_configuration_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pks_ezmaxcustomer_code** | **str**|  | 

### Return type

[**GlobalEzmaxcustomerGetConfigurationV1Response**](GlobalEzmaxcustomerGetConfigurationV1Response.md)

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

