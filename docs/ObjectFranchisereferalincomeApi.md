# eZmaxApi.ObjectFranchisereferalincomeApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**franchisereferalincome_create_object_v1**](ObjectFranchisereferalincomeApi.md#franchisereferalincome_create_object_v1) | **POST** /1/object/franchisereferalincome | Create a new Franchisereferalincome


# **franchisereferalincome_create_object_v1**
> FranchisereferalincomeCreateObjectV1Response franchisereferalincome_create_object_v1(franchisereferalincome_create_object_v1_request)

Create a new Franchisereferalincome

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):
```python
import time
import eZmaxApi
from eZmaxApi.api import object_franchisereferalincome_api
from eZmaxApi.model.franchisereferalincome_create_object_v1_response import FranchisereferalincomeCreateObjectV1Response
from eZmaxApi.model.franchisereferalincome_create_object_v1_request import FranchisereferalincomeCreateObjectV1Request
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
    api_instance = object_franchisereferalincome_api.ObjectFranchisereferalincomeApi(api_client)
    franchisereferalincome_create_object_v1_request = [
        FranchisereferalincomeCreateObjectV1Request(
            obj_franchisereferalincome=FranchisereferalincomeRequest(
                fki_franchisebroker_id=61,
                fki_franchisereferalincomeprogram_id=51,
                fki_period_id=21,
                d_franchisereferalincome_loan="500275.62",
                d_franchisereferalincome_franchiseamount="275.00",
                d_franchisereferalincome_franchisoramount="385.00",
                d_franchisereferalincome_agentamount="800.00",
                dt_franchisereferalincome_disbursed="2020-12-31",
                t_franchisereferalincome_comment="This is a comment",
                fki_franchiseoffice_id=50,
                s_franchisereferalincome_remoteid="s_franchisereferalincome_remoteid_example",
            ),
            obj_franchisereferalincome_compound=FranchisereferalincomeRequestCompound(
                obj_address=AddressRequest(
                    fki_addresstype_id=1,
                    s_address_civic="2540",
                    s_address_street="Daniel-Johnson Blvd.",
                    s_address_suite="610",
                    s_address_city="Laval",
                    fki_province_id=11,
                    fki_country_id=1,
                    s_address_zip="H7T2S3",
                ),
                a_obj_contact=[
                    ContactRequestCompound(),
                ],
            ),
        ),
    ] # [FranchisereferalincomeCreateObjectV1Request] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Franchisereferalincome
        api_response = api_instance.franchisereferalincome_create_object_v1(franchisereferalincome_create_object_v1_request)
        pprint(api_response)
    except eZmaxApi.ApiException as e:
        print("Exception when calling ObjectFranchisereferalincomeApi->franchisereferalincome_create_object_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **franchisereferalincome_create_object_v1_request** | [**[FranchisereferalincomeCreateObjectV1Request]**](FranchisereferalincomeCreateObjectV1Request.md)|  |

### Return type

[**FranchisereferalincomeCreateObjectV1Response**](FranchisereferalincomeCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

