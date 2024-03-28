# eZmaxApi.ObjectEzsigndocumentApi

All URIs are relative to *https://prod.api.appcluster01.ca-central-1.ezmax.com/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ezsigndocument_apply_ezsigntemplate_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_apply_ezsigntemplate_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyezsigntemplate | Apply an Ezsigntemplate to the Ezsigndocument.
[**ezsigndocument_apply_ezsigntemplate_v2**](ObjectEzsigndocumentApi.md#ezsigndocument_apply_ezsigntemplate_v2) | **POST** /2/object/ezsigndocument/{pkiEzsigndocumentID}/applyEzsigntemplate | Apply an Ezsigntemplate to the Ezsigndocument.
[**ezsigndocument_apply_ezsigntemplateglobal_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_apply_ezsigntemplateglobal_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyEzsigntemplateglobal | Apply an Ezsigntemplateglobal to the Ezsigndocument.
[**ezsigndocument_create_ezsignelements_positioned_by_word_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_create_ezsignelements_positioned_by_word_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/createEzsignelementsPositionedByWord | Create multiple Ezsignsignatures/Ezsignformfieldgroups
[**ezsigndocument_create_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_create_object_v1) | **POST** /1/object/ezsigndocument | Create a new Ezsigndocument
[**ezsigndocument_create_object_v2**](ObjectEzsigndocumentApi.md#ezsigndocument_create_object_v2) | **POST** /2/object/ezsigndocument | Create a new Ezsigndocument
[**ezsigndocument_decline_to_sign_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_decline_to_sign_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/declineToSign | Decline to sign
[**ezsigndocument_delete_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_delete_object_v1) | **DELETE** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Delete an existing Ezsigndocument
[**ezsigndocument_edit_ezsignformfieldgroups_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_edit_ezsignformfieldgroups_v1) | **PUT** /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignformfieldgroups | Edit multiple Ezsignformfieldgroups
[**ezsigndocument_edit_ezsignsignatures_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_edit_ezsignsignatures_v1) | **PUT** /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignsignatures | Edit multiple Ezsignsignatures
[**ezsigndocument_end_prematurely_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_end_prematurely_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/endPrematurely | End prematurely
[**ezsigndocument_flatten_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_flatten_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/flatten | Flatten
[**ezsigndocument_get_actionable_elements_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_actionable_elements_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getActionableElements | Retrieve actionable elements for the Ezsigndocument
[**ezsigndocument_get_attachments_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_attachments_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getAttachments | Retrieve Ezsigndocument&#39;s Attachments
[**ezsigndocument_get_completed_elements_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_completed_elements_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getCompletedElements | Retrieve completed elements for the Ezsigndocument
[**ezsigndocument_get_download_url_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_download_url_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getDownloadUrl/{eDocumentType} | Retrieve a URL to download documents.
[**ezsigndocument_get_ezsignannotations_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsignannotations_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignannotations | Retrieve an existing Ezsigndocument&#39;s Ezsignannotations
[**ezsigndocument_get_ezsigndiscussions_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsigndiscussions_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsigndiscussions | Retrieve an existing Ezsigndocument&#39;s Ezsigndiscussions
[**ezsigndocument_get_ezsignformfieldgroups_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsignformfieldgroups_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignformfieldgroups | Retrieve an existing Ezsigndocument&#39;s Ezsignformfieldgroups
[**ezsigndocument_get_ezsignpages_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsignpages_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignpages | Retrieve an existing Ezsigndocument&#39;s Ezsignpages
[**ezsigndocument_get_ezsignsignatures_automatic_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsignsignatures_automatic_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignsignaturesAutomatic | Retrieve an existing Ezsigndocument&#39;s automatic Ezsignsignatures
[**ezsigndocument_get_ezsignsignatures_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_ezsignsignatures_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getEzsignsignatures | Retrieve an existing Ezsigndocument&#39;s Ezsignsignatures
[**ezsigndocument_get_form_data_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_form_data_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getFormData | Retrieve an existing Ezsigndocument&#39;s Form Data
[**ezsigndocument_get_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_object_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Retrieve an existing Ezsigndocument
[**ezsigndocument_get_object_v2**](ObjectEzsigndocumentApi.md#ezsigndocument_get_object_v2) | **GET** /2/object/ezsigndocument/{pkiEzsigndocumentID} | Retrieve an existing Ezsigndocument
[**ezsigndocument_get_temporary_proof_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_temporary_proof_v1) | **GET** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getTemporaryProof | Retrieve the temporary proof
[**ezsigndocument_get_words_positions_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_get_words_positions_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/getWordsPositions | Retrieve positions X,Y of given words from a Ezsigndocument
[**ezsigndocument_patch_object_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_patch_object_v1) | **PATCH** /1/object/ezsigndocument/{pkiEzsigndocumentID} | Patch an existing Ezsigndocument
[**ezsigndocument_submit_ezsignform_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_submit_ezsignform_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/submitEzsignform | Submit the Ezsignform
[**ezsigndocument_unsend_v1**](ObjectEzsigndocumentApi.md#ezsigndocument_unsend_v1) | **POST** /1/object/ezsigndocument/{pkiEzsigndocumentID}/unsend | Unsend the Ezsigndocument


# **ezsigndocument_apply_ezsigntemplate_v1**
> EzsigndocumentApplyEzsigntemplateV1Response ezsigndocument_apply_ezsigntemplate_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v1_request)

Apply an Ezsigntemplate to the Ezsigndocument.

This function is deprecated. Please use *applyEzsigntemplate* instead which is doing the same thing but with a capital \"E\" to normalize the nomenclature.  This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v1_request import EzsigndocumentApplyEzsigntemplateV1Request
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v1_response import EzsigndocumentApplyEzsigntemplateV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_apply_ezsigntemplate_v1_request = eZmaxApi.EzsigndocumentApplyEzsigntemplateV1Request() # EzsigndocumentApplyEzsigntemplateV1Request | 

    try:
        # Apply an Ezsigntemplate to the Ezsigndocument.
        api_response = api_instance.ezsigndocument_apply_ezsigntemplate_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_apply_ezsigntemplate_v1_request** | [**EzsigndocumentApplyEzsigntemplateV1Request**](EzsigndocumentApplyEzsigntemplateV1Request.md)|  | 

### Return type

[**EzsigndocumentApplyEzsigntemplateV1Response**](EzsigndocumentApplyEzsigntemplateV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_apply_ezsigntemplate_v2**
> EzsigndocumentApplyEzsigntemplateV2Response ezsigndocument_apply_ezsigntemplate_v2(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v2_request)

Apply an Ezsigntemplate to the Ezsigndocument.

This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v2_request import EzsigndocumentApplyEzsigntemplateV2Request
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v2_response import EzsigndocumentApplyEzsigntemplateV2Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_apply_ezsigntemplate_v2_request = eZmaxApi.EzsigndocumentApplyEzsigntemplateV2Request() # EzsigndocumentApplyEzsigntemplateV2Request | 

    try:
        # Apply an Ezsigntemplate to the Ezsigndocument.
        api_response = api_instance.ezsigndocument_apply_ezsigntemplate_v2(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplate_v2_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplate_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_apply_ezsigntemplate_v2_request** | [**EzsigndocumentApplyEzsigntemplateV2Request**](EzsigndocumentApplyEzsigntemplateV2Request.md)|  | 

### Return type

[**EzsigndocumentApplyEzsigntemplateV2Response**](EzsigndocumentApplyEzsigntemplateV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_apply_ezsigntemplateglobal_v1**
> EzsigndocumentApplyEzsigntemplateglobalV1Response ezsigndocument_apply_ezsigntemplateglobal_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplateglobal_v1_request)

Apply an Ezsigntemplateglobal to the Ezsigndocument.

This endpoint applies a predefined template to the ezsign document. This allows to automatically apply all the form and signature fields on a document in a single step.  The document must not already have fields otherwise an error will be returned.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplateglobal_v1_request import EzsigndocumentApplyEzsigntemplateglobalV1Request
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplateglobal_v1_response import EzsigndocumentApplyEzsigntemplateglobalV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_apply_ezsigntemplateglobal_v1_request = eZmaxApi.EzsigndocumentApplyEzsigntemplateglobalV1Request() # EzsigndocumentApplyEzsigntemplateglobalV1Request | 

    try:
        # Apply an Ezsigntemplateglobal to the Ezsigndocument.
        api_response = api_instance.ezsigndocument_apply_ezsigntemplateglobal_v1(pki_ezsigndocument_id, ezsigndocument_apply_ezsigntemplateglobal_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplateglobal_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_apply_ezsigntemplateglobal_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_apply_ezsigntemplateglobal_v1_request** | [**EzsigndocumentApplyEzsigntemplateglobalV1Request**](EzsigndocumentApplyEzsigntemplateglobalV1Request.md)|  | 

### Return type

[**EzsigndocumentApplyEzsigntemplateglobalV1Response**](EzsigndocumentApplyEzsigntemplateglobalV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_create_ezsignelements_positioned_by_word_v1**
> EzsigndocumentCreateEzsignelementsPositionedByWordV1Response ezsigndocument_create_ezsignelements_positioned_by_word_v1(pki_ezsigndocument_id, ezsigndocument_create_ezsignelements_positioned_by_word_v1_request)

Create multiple Ezsignsignatures/Ezsignformfieldgroups

Using this endpoint, you can create multiple Ezsignsignatures/Ezsignformfieldgroups positioned by word at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v1_request import EzsigndocumentCreateEzsignelementsPositionedByWordV1Request
from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v1_response import EzsigndocumentCreateEzsignelementsPositionedByWordV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_create_ezsignelements_positioned_by_word_v1_request = eZmaxApi.EzsigndocumentCreateEzsignelementsPositionedByWordV1Request() # EzsigndocumentCreateEzsignelementsPositionedByWordV1Request | 

    try:
        # Create multiple Ezsignsignatures/Ezsignformfieldgroups
        api_response = api_instance.ezsigndocument_create_ezsignelements_positioned_by_word_v1(pki_ezsigndocument_id, ezsigndocument_create_ezsignelements_positioned_by_word_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_create_ezsignelements_positioned_by_word_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_create_ezsignelements_positioned_by_word_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_create_ezsignelements_positioned_by_word_v1_request** | [**EzsigndocumentCreateEzsignelementsPositionedByWordV1Request**](EzsigndocumentCreateEzsignelementsPositionedByWordV1Request.md)|  | 

### Return type

[**EzsigndocumentCreateEzsignelementsPositionedByWordV1Response**](EzsigndocumentCreateEzsignelementsPositionedByWordV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_create_object_v1**
> EzsigndocumentCreateObjectV1Response ezsigndocument_create_object_v1(ezsigndocument_create_object_v1_request)

Create a new Ezsigndocument

The endpoint allows to create one or many elements at once.  The array can contain simple (Just the object) or compound (The object and its child) objects.  Creating compound elements allows to reduce the multiple requests to create all child objects.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_create_object_v1_request import EzsigndocumentCreateObjectV1Request
from eZmaxApi.models.ezsigndocument_create_object_v1_response import EzsigndocumentCreateObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    ezsigndocument_create_object_v1_request = [eZmaxApi.EzsigndocumentCreateObjectV1Request()] # List[EzsigndocumentCreateObjectV1Request] | 

    try:
        # Create a new Ezsigndocument
        api_response = api_instance.ezsigndocument_create_object_v1(ezsigndocument_create_object_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_create_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_create_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigndocument_create_object_v1_request** | [**List[EzsigndocumentCreateObjectV1Request]**](EzsigndocumentCreateObjectV1Request.md)|  | 

### Return type

[**EzsigndocumentCreateObjectV1Response**](EzsigndocumentCreateObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**413** | The request was large. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. If the error is recoverable sTemporaryFileUrl will be set and you can use this url to try a new request without sending the file over again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_create_object_v2**
> EzsigndocumentCreateObjectV2Response ezsigndocument_create_object_v2(ezsigndocument_create_object_v2_request)

Create a new Ezsigndocument

The endpoint allows to create one or many elements at once.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_create_object_v2_request import EzsigndocumentCreateObjectV2Request
from eZmaxApi.models.ezsigndocument_create_object_v2_response import EzsigndocumentCreateObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    ezsigndocument_create_object_v2_request = eZmaxApi.EzsigndocumentCreateObjectV2Request() # EzsigndocumentCreateObjectV2Request | 

    try:
        # Create a new Ezsigndocument
        api_response = api_instance.ezsigndocument_create_object_v2(ezsigndocument_create_object_v2_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_create_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_create_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ezsigndocument_create_object_v2_request** | [**EzsigndocumentCreateObjectV2Request**](EzsigndocumentCreateObjectV2Request.md)|  | 

### Return type

[**EzsigndocumentCreateObjectV2Response**](EzsigndocumentCreateObjectV2Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. If the error is recoverable sTemporaryFileUrl will be set and you can use this url to try a new request without sending the file over again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_decline_to_sign_v1**
> EzsigndocumentDeclineToSignV1Response ezsigndocument_decline_to_sign_v1(pki_ezsigndocument_id, ezsigndocument_decline_to_sign_v1_request)

Decline to sign

Decline to sign

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_decline_to_sign_v1_request import EzsigndocumentDeclineToSignV1Request
from eZmaxApi.models.ezsigndocument_decline_to_sign_v1_response import EzsigndocumentDeclineToSignV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_decline_to_sign_v1_request = eZmaxApi.EzsigndocumentDeclineToSignV1Request() # EzsigndocumentDeclineToSignV1Request | 

    try:
        # Decline to sign
        api_response = api_instance.ezsigndocument_decline_to_sign_v1(pki_ezsigndocument_id, ezsigndocument_decline_to_sign_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_decline_to_sign_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_decline_to_sign_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_decline_to_sign_v1_request** | [**EzsigndocumentDeclineToSignV1Request**](EzsigndocumentDeclineToSignV1Request.md)|  | 

### Return type

[**EzsigndocumentDeclineToSignV1Response**](EzsigndocumentDeclineToSignV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_delete_object_v1**
> EzsigndocumentDeleteObjectV1Response ezsigndocument_delete_object_v1(pki_ezsigndocument_id)

Delete an existing Ezsigndocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_delete_object_v1_response import EzsigndocumentDeleteObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Delete an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_delete_object_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_delete_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_delete_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentDeleteObjectV1Response**](EzsigndocumentDeleteObjectV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_edit_ezsignformfieldgroups_v1**
> EzsigndocumentEditEzsignformfieldgroupsV1Response ezsigndocument_edit_ezsignformfieldgroups_v1(pki_ezsigndocument_id, ezsigndocument_edit_ezsignformfieldgroups_v1_request)

Edit multiple Ezsignformfieldgroups

Using this endpoint, you can edit multiple Ezsignformfieldgroups at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_edit_ezsignformfieldgroups_v1_request import EzsigndocumentEditEzsignformfieldgroupsV1Request
from eZmaxApi.models.ezsigndocument_edit_ezsignformfieldgroups_v1_response import EzsigndocumentEditEzsignformfieldgroupsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_edit_ezsignformfieldgroups_v1_request = eZmaxApi.EzsigndocumentEditEzsignformfieldgroupsV1Request() # EzsigndocumentEditEzsignformfieldgroupsV1Request | 

    try:
        # Edit multiple Ezsignformfieldgroups
        api_response = api_instance.ezsigndocument_edit_ezsignformfieldgroups_v1(pki_ezsigndocument_id, ezsigndocument_edit_ezsignformfieldgroups_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_edit_ezsignformfieldgroups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_edit_ezsignformfieldgroups_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_edit_ezsignformfieldgroups_v1_request** | [**EzsigndocumentEditEzsignformfieldgroupsV1Request**](EzsigndocumentEditEzsignformfieldgroupsV1Request.md)|  | 

### Return type

[**EzsigndocumentEditEzsignformfieldgroupsV1Response**](EzsigndocumentEditEzsignformfieldgroupsV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_edit_ezsignsignatures_v1**
> EzsigndocumentEditEzsignsignaturesV1Response ezsigndocument_edit_ezsignsignatures_v1(pki_ezsigndocument_id, ezsigndocument_edit_ezsignsignatures_v1_request)

Edit multiple Ezsignsignatures

Using this endpoint, you can edit multiple Ezsignsignatures at the same time.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_edit_ezsignsignatures_v1_request import EzsigndocumentEditEzsignsignaturesV1Request
from eZmaxApi.models.ezsigndocument_edit_ezsignsignatures_v1_response import EzsigndocumentEditEzsignsignaturesV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_edit_ezsignsignatures_v1_request = eZmaxApi.EzsigndocumentEditEzsignsignaturesV1Request() # EzsigndocumentEditEzsignsignaturesV1Request | 

    try:
        # Edit multiple Ezsignsignatures
        api_response = api_instance.ezsigndocument_edit_ezsignsignatures_v1(pki_ezsigndocument_id, ezsigndocument_edit_ezsignsignatures_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_edit_ezsignsignatures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_edit_ezsignsignatures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_edit_ezsignsignatures_v1_request** | [**EzsigndocumentEditEzsignsignaturesV1Request**](EzsigndocumentEditEzsignsignaturesV1Request.md)|  | 

### Return type

[**EzsigndocumentEditEzsignsignaturesV1Response**](EzsigndocumentEditEzsignsignaturesV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_end_prematurely_v1**
> EzsigndocumentEndPrematurelyV1Response ezsigndocument_end_prematurely_v1(pki_ezsigndocument_id, body)

End prematurely

End prematurely an Ezsigndocument when some signatures are still required

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_end_prematurely_v1_response import EzsigndocumentEndPrematurelyV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    body = None # object | 

    try:
        # End prematurely
        api_response = api_instance.ezsigndocument_end_prematurely_v1(pki_ezsigndocument_id, body)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_end_prematurely_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_end_prematurely_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzsigndocumentEndPrematurelyV1Response**](EzsigndocumentEndPrematurelyV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_flatten_v1**
> EzsigndocumentFlattenV1Response ezsigndocument_flatten_v1(pki_ezsigndocument_id, body)

Flatten

Flatten an Ezsigndocument signatures, forms and annotations. This process finalizes the PDF so that the forms and annotations become part of the document content and cannot be edited.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_flatten_v1_response import EzsigndocumentFlattenV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    body = None # object | 

    try:
        # Flatten
        api_response = api_instance.ezsigndocument_flatten_v1(pki_ezsigndocument_id, body)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_flatten_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_flatten_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzsigndocumentFlattenV1Response**](EzsigndocumentFlattenV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_actionable_elements_v1**
> EzsigndocumentGetActionableElementsV1Response ezsigndocument_get_actionable_elements_v1(pki_ezsigndocument_id)

Retrieve actionable elements for the Ezsigndocument

Return the Ezsignsignatures that can be signed and Ezsignformfieldgroups that can be filled by the current user at the current step in the process

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_actionable_elements_v1_response import EzsigndocumentGetActionableElementsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve actionable elements for the Ezsigndocument
        api_response = api_instance.ezsigndocument_get_actionable_elements_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_actionable_elements_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_actionable_elements_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetActionableElementsV1Response**](EzsigndocumentGetActionableElementsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_attachments_v1**
> EzsigndocumentGetAttachmentsV1Response ezsigndocument_get_attachments_v1(pki_ezsigndocument_id)

Retrieve Ezsigndocument's Attachments



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_attachments_v1_response import EzsigndocumentGetAttachmentsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve Ezsigndocument's Attachments
        api_response = api_instance.ezsigndocument_get_attachments_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_attachments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_attachments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetAttachmentsV1Response**](EzsigndocumentGetAttachmentsV1Response.md)

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

# **ezsigndocument_get_completed_elements_v1**
> EzsigndocumentGetCompletedElementsV1Response ezsigndocument_get_completed_elements_v1(pki_ezsigndocument_id)

Retrieve completed elements for the Ezsigndocument

Return the completed Ezsignsignatures, Ezsignformfieldgroups and Ezsignannotations at the current step in the process

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_completed_elements_v1_response import EzsigndocumentGetCompletedElementsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve completed elements for the Ezsigndocument
        api_response = api_instance.ezsigndocument_get_completed_elements_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_completed_elements_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_completed_elements_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetCompletedElementsV1Response**](EzsigndocumentGetCompletedElementsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_download_url_v1**
> EzsigndocumentGetDownloadUrlV1Response ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type)

Retrieve a URL to download documents.

This endpoint returns URLs to different files that can be downloaded during the signing process.  These links will expire after 5 minutes so the download of the file should be made soon after retrieving the link.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_download_url_v1_response import EzsigndocumentGetDownloadUrlV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    e_document_type = 'e_document_type_example' # str | The type of document to retrieve.  1. **Initial** Is the initial document before any signature were applied. 2. **SignatureReady** Is the version containing the annotations/form to show the signer. 3. **Signed** Is the final document once all signatures were applied in current document if eEzsignfolderCompletion is PerEzsigndocument.<br>     Is the final document once all signatures were applied in all documents if eEzsignfolderCompletion is PerEzsignfolder. 4. **Proofdocument** Is the evidence report. 5. **Proof** Is the complete evidence archive including all of the above and more. 

    try:
        # Retrieve a URL to download documents.
        api_response = api_instance.ezsigndocument_get_download_url_v1(pki_ezsigndocument_id, e_document_type)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_download_url_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_download_url_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **e_document_type** | **str**| The type of document to retrieve.  1. **Initial** Is the initial document before any signature were applied. 2. **SignatureReady** Is the version containing the annotations/form to show the signer. 3. **Signed** Is the final document once all signatures were applied in current document if eEzsignfolderCompletion is PerEzsigndocument.&lt;br&gt;     Is the final document once all signatures were applied in all documents if eEzsignfolderCompletion is PerEzsignfolder. 4. **Proofdocument** Is the evidence report. 5. **Proof** Is the complete evidence archive including all of the above and more.  | 

### Return type

[**EzsigndocumentGetDownloadUrlV1Response**](EzsigndocumentGetDownloadUrlV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_ezsignannotations_v1**
> EzsigndocumentGetEzsignannotationsV1Response ezsigndocument_get_ezsignannotations_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Ezsignannotations



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_ezsignannotations_v1_response import EzsigndocumentGetEzsignannotationsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's Ezsignannotations
        api_response = api_instance.ezsigndocument_get_ezsignannotations_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_ezsignannotations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsignannotations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetEzsignannotationsV1Response**](EzsigndocumentGetEzsignannotationsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_ezsigndiscussions_v1**
> EzsigndocumentGetEzsigndiscussionsV1Response ezsigndocument_get_ezsigndiscussions_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Ezsigndiscussions



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_ezsigndiscussions_v1_response import EzsigndocumentGetEzsigndiscussionsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's Ezsigndiscussions
        api_response = api_instance.ezsigndocument_get_ezsigndiscussions_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_ezsigndiscussions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsigndiscussions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetEzsigndiscussionsV1Response**](EzsigndocumentGetEzsigndiscussionsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_ezsignformfieldgroups_v1**
> EzsigndocumentGetEzsignformfieldgroupsV1Response ezsigndocument_get_ezsignformfieldgroups_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Ezsignformfieldgroups



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_ezsignformfieldgroups_v1_response import EzsigndocumentGetEzsignformfieldgroupsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's Ezsignformfieldgroups
        api_response = api_instance.ezsigndocument_get_ezsignformfieldgroups_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_ezsignformfieldgroups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsignformfieldgroups_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetEzsignformfieldgroupsV1Response**](EzsigndocumentGetEzsignformfieldgroupsV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_ezsignpages_v1**
> EzsigndocumentGetEzsignpagesV1Response ezsigndocument_get_ezsignpages_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Ezsignpages



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_ezsignpages_v1_response import EzsigndocumentGetEzsignpagesV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's Ezsignpages
        api_response = api_instance.ezsigndocument_get_ezsignpages_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_ezsignpages_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsignpages_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetEzsignpagesV1Response**](EzsigndocumentGetEzsignpagesV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_ezsignsignatures_automatic_v1**
> EzsigndocumentGetEzsignsignaturesAutomaticV1Response ezsigndocument_get_ezsignsignatures_automatic_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's automatic Ezsignsignatures

Return the Ezsignsignatures that can be signed by the current user at the current step in the process

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_ezsignsignatures_automatic_v1_response import EzsigndocumentGetEzsignsignaturesAutomaticV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's automatic Ezsignsignatures
        api_response = api_instance.ezsigndocument_get_ezsignsignatures_automatic_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_ezsignsignatures_automatic_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsignsignatures_automatic_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetEzsignsignaturesAutomaticV1Response**](EzsigndocumentGetEzsignsignaturesAutomaticV1Response.md)

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

# **ezsigndocument_get_ezsignsignatures_v1**
> EzsigndocumentGetEzsignsignaturesV1Response ezsigndocument_get_ezsignsignatures_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Ezsignsignatures



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_ezsignsignatures_v1_response import EzsigndocumentGetEzsignsignaturesV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's Ezsignsignatures
        api_response = api_instance.ezsigndocument_get_ezsignsignatures_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_ezsignsignatures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_ezsignsignatures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetEzsignsignaturesV1Response**](EzsigndocumentGetEzsignsignaturesV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_form_data_v1**
> EzsigndocumentGetFormDataV1Response ezsigndocument_get_form_data_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument's Form Data



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_form_data_v1_response import EzsigndocumentGetFormDataV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument's Form Data
        api_response = api_instance.ezsigndocument_get_form_data_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_form_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_form_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetFormDataV1Response**](EzsigndocumentGetFormDataV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**406** | The URL is valid, but one of the Accept header is not defined or invalid. For example, you set the header \&quot;Accept: application/json\&quot; but the function can only return \&quot;Content-type: image/png\&quot; |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_object_v1**
> EzsigndocumentGetObjectV1Response ezsigndocument_get_object_v1(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_object_v1_response import EzsigndocumentGetObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_get_object_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetObjectV1Response**](EzsigndocumentGetObjectV1Response.md)

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

# **ezsigndocument_get_object_v2**
> EzsigndocumentGetObjectV2Response ezsigndocument_get_object_v2(pki_ezsigndocument_id)

Retrieve an existing Ezsigndocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_object_v2_response import EzsigndocumentGetObjectV2Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_get_object_v2(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_object_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_object_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetObjectV2Response**](EzsigndocumentGetObjectV2Response.md)

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

# **ezsigndocument_get_temporary_proof_v1**
> EzsigndocumentGetTemporaryProofV1Response ezsigndocument_get_temporary_proof_v1(pki_ezsigndocument_id)

Retrieve the temporary proof

Retrieve the temporary proof while the Ezsigndocument is being processed since the proof isn't available until the Ezsigndocument is completed

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_temporary_proof_v1_response import EzsigndocumentGetTemporaryProofV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 

    try:
        # Retrieve the temporary proof
        api_response = api_instance.ezsigndocument_get_temporary_proof_v1(pki_ezsigndocument_id)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_temporary_proof_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_temporary_proof_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 

### Return type

[**EzsigndocumentGetTemporaryProofV1Response**](EzsigndocumentGetTemporaryProofV1Response.md)

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
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_get_words_positions_v1**
> EzsigndocumentGetWordsPositionsV1Response ezsigndocument_get_words_positions_v1(pki_ezsigndocument_id, ezsigndocument_get_words_positions_v1_request)

Retrieve positions X,Y of given words from a Ezsigndocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_get_words_positions_v1_request import EzsigndocumentGetWordsPositionsV1Request
from eZmaxApi.models.ezsigndocument_get_words_positions_v1_response import EzsigndocumentGetWordsPositionsV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_get_words_positions_v1_request = eZmaxApi.EzsigndocumentGetWordsPositionsV1Request() # EzsigndocumentGetWordsPositionsV1Request | 

    try:
        # Retrieve positions X,Y of given words from a Ezsigndocument
        api_response = api_instance.ezsigndocument_get_words_positions_v1(pki_ezsigndocument_id, ezsigndocument_get_words_positions_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_get_words_positions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_get_words_positions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_get_words_positions_v1_request** | [**EzsigndocumentGetWordsPositionsV1Request**](EzsigndocumentGetWordsPositionsV1Request.md)|  | 

### Return type

[**EzsigndocumentGetWordsPositionsV1Response**](EzsigndocumentGetWordsPositionsV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_patch_object_v1**
> EzsigndocumentPatchObjectV1Response ezsigndocument_patch_object_v1(pki_ezsigndocument_id, ezsigndocument_patch_object_v1_request)

Patch an existing Ezsigndocument



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_patch_object_v1_request import EzsigndocumentPatchObjectV1Request
from eZmaxApi.models.ezsigndocument_patch_object_v1_response import EzsigndocumentPatchObjectV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_patch_object_v1_request = eZmaxApi.EzsigndocumentPatchObjectV1Request() # EzsigndocumentPatchObjectV1Request | 

    try:
        # Patch an existing Ezsigndocument
        api_response = api_instance.ezsigndocument_patch_object_v1(pki_ezsigndocument_id, ezsigndocument_patch_object_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_patch_object_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_patch_object_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_patch_object_v1_request** | [**EzsigndocumentPatchObjectV1Request**](EzsigndocumentPatchObjectV1Request.md)|  | 

### Return type

[**EzsigndocumentPatchObjectV1Response**](EzsigndocumentPatchObjectV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_submit_ezsignform_v1**
> EzsigndocumentSubmitEzsignformV1Response ezsigndocument_submit_ezsignform_v1(pki_ezsigndocument_id, ezsigndocument_submit_ezsignform_v1_request)

Submit the Ezsignform



### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_submit_ezsignform_v1_request import EzsigndocumentSubmitEzsignformV1Request
from eZmaxApi.models.ezsigndocument_submit_ezsignform_v1_response import EzsigndocumentSubmitEzsignformV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    ezsigndocument_submit_ezsignform_v1_request = eZmaxApi.EzsigndocumentSubmitEzsignformV1Request() # EzsigndocumentSubmitEzsignformV1Request | 

    try:
        # Submit the Ezsignform
        api_response = api_instance.ezsigndocument_submit_ezsignform_v1(pki_ezsigndocument_id, ezsigndocument_submit_ezsignform_v1_request)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_submit_ezsignform_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_submit_ezsignform_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **ezsigndocument_submit_ezsignform_v1_request** | [**EzsigndocumentSubmitEzsignformV1Request**](EzsigndocumentSubmitEzsignformV1Request.md)|  | 

### Return type

[**EzsigndocumentSubmitEzsignformV1Response**](EzsigndocumentSubmitEzsignformV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ezsigndocument_unsend_v1**
> EzsigndocumentUnsendV1Response ezsigndocument_unsend_v1(pki_ezsigndocument_id, body)

Unsend the Ezsigndocument

Once an Ezsigndocument has been sent to signatories, it cannot be modified.  Using this endpoint, you can unsend the Ezsigndocument and make it modifiable again.  Signatories will receive an email informing them the signature process was aborted and they might receive a new invitation to sign.  ⚠️ Warning: Any signature previously made by signatories on this Ezsigndocumentswill be lost.

### Example

* Api Key Authentication (Authorization):

```python
import eZmaxApi
from eZmaxApi.models.ezsigndocument_unsend_v1_response import EzsigndocumentUnsendV1Response
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
    api_instance = eZmaxApi.ObjectEzsigndocumentApi(api_client)
    pki_ezsigndocument_id = 56 # int | 
    body = None # object | 

    try:
        # Unsend the Ezsigndocument
        api_response = api_instance.ezsigndocument_unsend_v1(pki_ezsigndocument_id, body)
        print("The response of ObjectEzsigndocumentApi->ezsigndocument_unsend_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectEzsigndocumentApi->ezsigndocument_unsend_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pki_ezsigndocument_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**EzsigndocumentUnsendV1Response**](EzsigndocumentUnsendV1Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | The request failed. The element on which you were trying to work does not exists. Look for detail about the error in the body |  -  |
**422** | The request was syntactically valid but failed because of an interdependance condition. Look for detail about the error in the body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

