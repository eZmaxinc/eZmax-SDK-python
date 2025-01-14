# eZmaxApi.ObjectCustomerApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_create_object_v1**](ObjectCustomerApi.md#customer_create_object_v1) | **POST** /1/object/customer | Create a new Customer
[**customer_get_object_v2**](ObjectCustomerApi.md#customer_get_object_v2) | **GET** /2/object/customer/{pkiCustomerID} | Retrieve an existing Customer


# **customer_create_object_v1**
> CustomerCreateObjectV1Response customer_create_object_v1(customer_create_object_v1_request)

Create a new Customer

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.customer_create_object_v1_request import CustomerCreateObjectV1Request
from eZmaxApi.models.customer_create_object_v1_response import CustomerCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectCustomerApi(api_client)
    customer_create_object_v1_request = eZmaxApi.CustomerCreateObjectV1Request() # CustomerCreateObjectV1Request | 

    try:
        # Create a new Customer
        api_response = api_instance.customer_create_object_v1(customer_create_object_v1_request)
        print("The response of ObjectCustomerApi->customer_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCustomerApi->customer_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_create_object_v1_request** | [**CustomerCreateObjectV1Request**](CustomerCreateObjectV1Request.md)|  | 

### Return type

[**CustomerCreateObjectV1Response**](CustomerCreateObjectV1Response.md)

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

# **customer_get_object_v2**
> CustomerGetObjectV2Response customer_get_object_v2(pki_customer_id)

Retrieve an existing Customer



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.customer_get_object_v2_response import CustomerGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectCustomerApi(api_client)
    pki_customer_id = 56 # int | The unique ID of the Customer

    try:
        # Retrieve an existing Customer
        api_response = api_instance.customer_get_object_v2(pki_customer_id)
        print("The response of ObjectCustomerApi->customer_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectCustomerApi->customer_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_customer_id** | **int**| The unique ID of the Customer | 

### Return type

[**CustomerGetObjectV2Response**](CustomerGetObjectV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

