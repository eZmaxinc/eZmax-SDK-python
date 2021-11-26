# eZmaxApi.ObjectEzsigntemplatepackageApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigntemplatepackage_get_list_v1**](ObjectEzsigntemplatepackageApi.md#ezsigntemplatepackage_get_list_v1) | **GET** /1/object/ezsigntemplatepackage/getList | Retrieve Ezsigntemplatepackage list


# **ezsigntemplatepackage_get_list_v1**
> EzsigntemplatepackageGetListV1Response ezsigntemplatepackage_get_list_v1()

Retrieve Ezsigntemplatepackage list

Enum values that can be filtered in query parameter *sFilter*:  | Variable | Valid values | |---|---| | eEzsigntemplatepackageType | Company<br>Department<br>Team<br>User<br>Usergroup |

### Example

* Api Key Authentication (Authorization):

```python
import time
import eZmaxApi
from eZmaxApi.api import object_ezsigntemplatepackage_api
from eZmaxApi.model.common_response_error import CommonResponseError
from eZmaxApi.model.ezsigntemplatepackage_get_list_v1_response import EzsigntemplatepackageGetListV1Response
from eZmaxApi.model.header_accept_language import HeaderAcceptLanguage
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
    api_instance = object_ezsigntemplatepackage_api.ObjectEzsigntemplatepackageApi(api_client)
    e_order_by = "pkiEzsigntemplatepackageID_ASC" # str | Specify how you want the results to be sorted (optional)
    i_row_max = 100 # int |  (optional)
    i_row_offset = 0 # int |  (optional)
    accept_language = HeaderAcceptLanguage("*") # HeaderAcceptLanguage |  (optional)
    s_filter = "bField1 eq true and iField2 gte 0 and iField2 lte 1000 and sField3 eq 'Other' and eField4 eq 'Paid' and sField5 like '%needle%' and iField6 in '1,2,3' and dtField7 rg '=m,=3mm'" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Ezsigntemplatepackage list
        api_response = api_instance.ezsigntemplatepackage_get_list_v1(e_order_by=e_order_by, i_row_max=i_row_max, i_row_offset=i_row_offset, accept_language=accept_language, s_filter=s_filter)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectEzsigntemplatepackageApi->ezsigntemplatepackage_get_list_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_order_by** | **str**| Specify how you want the results to be sorted | [optional]
 **i_row_max** | **int**|  | [optional]
 **i_row_offset** | **int**|  | [optional]
 **accept_language** | **HeaderAcceptLanguage**|  | [optional]
 **s_filter** | **str**|  | [optional]

### Return type

[**EzsigntemplatepackageGetListV1Response**](EzsigntemplatepackageGetListV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**406** | One of the accept header is not defined or invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

