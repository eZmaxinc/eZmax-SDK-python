# EzsignSuggestSignersV1Response

Response for GET /1/module/ezsign/suggestSigners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignSuggestSignersV1ResponseMPayload**](EzsignSuggestSignersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsign_suggest_signers_v1_response import EzsignSuggestSignersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignSuggestSignersV1Response from a JSON string
ezsign_suggest_signers_v1_response_instance = EzsignSuggestSignersV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignSuggestSignersV1Response.to_json()

# convert the object into a dict
ezsign_suggest_signers_v1_response_dict = ezsign_suggest_signers_v1_response_instance.to_dict()
# create an instance of EzsignSuggestSignersV1Response from a dict
ezsign_suggest_signers_v1_response_form_dict = ezsign_suggest_signers_v1_response.from_dict(ezsign_suggest_signers_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


