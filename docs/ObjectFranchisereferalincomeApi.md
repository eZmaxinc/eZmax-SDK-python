# eZmaxApi.ObjectFranchisereferalincomeApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchisereferalincome_create_object_v2**](ObjectFranchisereferalincomeApi.md#franchisereferalincome_create_object_v2) | **POST** /2/object/franchisereferalincome | Create a new Franchisereferalincome


# **franchisereferalincome_create_object_v2**
> FranchisereferalincomeCreateObjectV2Response franchisereferalincome_create_object_v2(franchisereferalincome_create_object_v2_request)

Create a new Franchisereferalincome

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.franchisereferalincome_create_object_v2_request import FranchisereferalincomeCreateObjectV2Request
from eZmaxApi.models.franchisereferalincome_create_object_v2_response import FranchisereferalincomeCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectFranchisereferalincomeApi(api_client)
    franchisereferalincome_create_object_v2_request = eZmaxApi.FranchisereferalincomeCreateObjectV2Request() # FranchisereferalincomeCreateObjectV2Request | 

    try:
        # Create a new Franchisereferalincome
        api_response = api_instance.franchisereferalincome_create_object_v2(franchisereferalincome_create_object_v2_request)
        print("The response of ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **franchisereferalincome_create_object_v2_request** | [**FranchisereferalincomeCreateObjectV2Request**](FranchisereferalincomeCreateObjectV2Request.md)|  | 

### Return type

[**FranchisereferalincomeCreateObjectV2Response**](FranchisereferalincomeCreateObjectV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of this Franchisebroker is not in this Franchiseoffice. fkiFranchiseofficeID contains the id of Franchiseoffice where the Franchisebroker is located on the dtFranchisereferalincomeDisbursed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

