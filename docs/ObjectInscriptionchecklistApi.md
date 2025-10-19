# eZmaxApi.ObjectInscriptionchecklistApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inscriptionchecklist_get_autocomplete_v2**](ObjectInscriptionchecklistApi.md#inscriptionchecklist_get_autocomplete_v2) | **GET** /2/object/inscriptionchecklist/getAutocomplete/{sSelector} | Retrieve Inscriptionchecklists and IDs
[**inscriptionchecklist_get_autocomplete_v3**](ObjectInscriptionchecklistApi.md#inscriptionchecklist_get_autocomplete_v3) | **GET** /3/object/inscriptionchecklist/getAutocomplete/{sSelector} | Retrieve Inscriptionchecklists and IDs


# **inscriptionchecklist_get_autocomplete_v2**
> InscriptionchecklistGetAutocompleteV2Response inscriptionchecklist_get_autocomplete_v2(s_selector, fki_id=fki_id, e_type=e_type, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Inscriptionchecklists and IDs

Get the list of Inscriptionchecklist to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.inscriptionchecklist_get_autocomplete_v2_response import InscriptionchecklistGetAutocompleteV2Response
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
    api_instance = eZmaxApi.ObjectInscriptionchecklistApi(api_client)
    s_selector = 's_selector_example' # str | The type of Inscriptionchecklist to return
    fki_id = 'fki_id_example' # str | Specify which fkiID we want to display. (optional)
    e_type = 'e_type_example' # str | The type of Inscriptionchecklist (optional)
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Inscriptionchecklists and IDs
        api_response = api_instance.inscriptionchecklist_get_autocomplete_v2(s_selector, fki_id=fki_id, e_type=e_type, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectInscriptionchecklistApi->inscriptionchecklist_get_autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectInscriptionchecklistApi->inscriptionchecklist_get_autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Inscriptionchecklist to return | 
 **fki_id** | **str**| Specify which fkiID we want to display. | [optional] 
 **e_type** | **str**| The type of Inscriptionchecklist | [optional] 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**InscriptionchecklistGetAutocompleteV2Response**](InscriptionchecklistGetAutocompleteV2Response.md)

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

# **inscriptionchecklist_get_autocomplete_v3**
> InscriptionchecklistGetAutocompleteV3Response inscriptionchecklist_get_autocomplete_v3(s_selector, fki_buyercontract_id=fki_buyercontract_id, fki_inscription_id=fki_inscription_id, fki_inscriptionnotauthenticated_id=fki_inscriptionnotauthenticated_id, fki_inscriptiontemp_id=fki_inscriptiontemp_id, fki_agent_id=fki_agent_id, fki_broker_id=fki_broker_id, fki_otherincome_id=fki_otherincome_id, fki_rejectedoffertopurchase_id=fki_rejectedoffertopurchase_id, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)

Retrieve Inscriptionchecklists and IDs

Get the list of Inscriptionchecklist to be used in a dropdown or autocomplete control.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.header_accept_language import HeaderAcceptLanguage
from eZmaxApi.models.inscriptionchecklist_get_autocomplete_v3_response import InscriptionchecklistGetAutocompleteV3Response
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
    api_instance = eZmaxApi.ObjectInscriptionchecklistApi(api_client)
    s_selector = 's_selector_example' # str | The type of Inscriptionchecklist to return
    fki_buyercontract_id = 'fki_buyercontract_id_example' # str | Specify which Buyercontract we want to display. (optional)
    fki_inscription_id = 'fki_inscription_id_example' # str | Specify which Inscription we want to display. (optional)
    fki_inscriptionnotauthenticated_id = 'fki_inscriptionnotauthenticated_id_example' # str | Specify which Inscriptionnotauthenticated we want to display. (optional)
    fki_inscriptiontemp_id = 'fki_inscriptiontemp_id_example' # str | Specify which Inscriptiontemp we want to display. (optional)
    fki_agent_id = 'fki_agent_id_example' # str | Specify which Agent we want to display. (optional)
    fki_broker_id = 'fki_broker_id_example' # str | Specify which Broker we want to display. (optional)
    fki_otherincome_id = 'fki_otherincome_id_example' # str | Specify which Otherincome we want to display. (optional)
    fki_rejectedoffertopurchase_id = 'fki_rejectedoffertopurchase_id_example' # str | Specify which Rejectedoffertopurchase we want to display. (optional)
    e_filter_active = Active # str | Specify which results we want to display. (optional) (default to Active)
    s_query = 's_query_example' # str | Allow to filter the returned results (optional)
    accept_language = eZmaxApi.HeaderAcceptLanguage() # HeaderAcceptLanguage |  (optional)

    try:
        # Retrieve Inscriptionchecklists and IDs
        api_response = api_instance.inscriptionchecklist_get_autocomplete_v3(s_selector, fki_buyercontract_id=fki_buyercontract_id, fki_inscription_id=fki_inscription_id, fki_inscriptionnotauthenticated_id=fki_inscriptionnotauthenticated_id, fki_inscriptiontemp_id=fki_inscriptiontemp_id, fki_agent_id=fki_agent_id, fki_broker_id=fki_broker_id, fki_otherincome_id=fki_otherincome_id, fki_rejectedoffertopurchase_id=fki_rejectedoffertopurchase_id, e_filter_active=e_filter_active, s_query=s_query, accept_language=accept_language)
        print("The response of ObjectInscriptionchecklistApi->inscriptionchecklist_get_autocomplete_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectInscriptionchecklistApi->inscriptionchecklist_get_autocomplete_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s_selector** | **str**| The type of Inscriptionchecklist to return | 
 **fki_buyercontract_id** | **str**| Specify which Buyercontract we want to display. | [optional] 
 **fki_inscription_id** | **str**| Specify which Inscription we want to display. | [optional] 
 **fki_inscriptionnotauthenticated_id** | **str**| Specify which Inscriptionnotauthenticated we want to display. | [optional] 
 **fki_inscriptiontemp_id** | **str**| Specify which Inscriptiontemp we want to display. | [optional] 
 **fki_agent_id** | **str**| Specify which Agent we want to display. | [optional] 
 **fki_broker_id** | **str**| Specify which Broker we want to display. | [optional] 
 **fki_otherincome_id** | **str**| Specify which Otherincome we want to display. | [optional] 
 **fki_rejectedoffertopurchase_id** | **str**| Specify which Rejectedoffertopurchase we want to display. | [optional] 
 **e_filter_active** | **str**| Specify which results we want to display. | [optional] [default to Active]
 **s_query** | **str**| Allow to filter the returned results | [optional] 
 **accept_language** | [**HeaderAcceptLanguage**](.md)|  | [optional] 

### Return type

[**InscriptionchecklistGetAutocompleteV3Response**](InscriptionchecklistGetAutocompleteV3Response.md)

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

