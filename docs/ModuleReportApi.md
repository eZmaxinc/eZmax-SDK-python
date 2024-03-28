# eZmaxApi.ModuleReportApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_get_report_from_cache_v1**](ModuleReportApi.md#report_get_report_from_cache_v1) | **GET** /1/module/report/getReportFromCache/{sReportgroupCacheID} | Retrieve report from cache


# **report_get_report_from_cache_v1**
> CommonGetReportV1Response report_get_report_from_cache_v1(s_reportgroup_cache_id)

Retrieve report from cache

Retrieve a report that was previously generated and cached

### Example

* Api Key Authentication (Authorization):
* Api Key Authentication (Presigned):

```python
import eZmaxApi
from eZmaxApi.models.common_get_report_v1_response import CommonGetReportV1Response
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

# Configure API key authorization: Presigned
configuration.api_key['Presigned'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Presigned'] = 'Bearer'

# Enter a context with an instance of the API client
with eZmaxApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eZmaxApi.ModuleReportApi(api_client)
    s_reportgroup_cache_id = 's_reportgroup_cache_id_example' # str | 

    try:
        # Retrieve report from cache
        api_response = api_instance.report_get_report_from_cache_v1(s_reportgroup_cache_id)
        print("The response of ModuleReportApi->report_get_report_from_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModuleReportApi->report_get_report_from_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_reportgroup_cache_id** | **str**|  | 

### Return type

[**CommonGetReportV1Response**](CommonGetReportV1Response.md)

### Authorization

[Authorization](../README.md#Authorization), [Presigned](../README.md#Presigned)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/zip, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

