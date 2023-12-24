# EzsignSuggestSignersV1ResponseMPayload

Payload for GET /1/module/ezsign/suggestSigners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldersignerassociation** | [**List[EzsignfoldersignerassociationResponseCompound]**](EzsignfoldersignerassociationResponseCompound.md) |  | 
**a_obj_user_team** | [**List[CustomUserResponse]**](CustomUserResponse.md) |  | 
**a_obj_user** | [**List[CustomUserResponse]**](CustomUserResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsign_suggest_signers_v1_response_m_payload import EzsignSuggestSignersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignSuggestSignersV1ResponseMPayload from a JSON string
ezsign_suggest_signers_v1_response_m_payload_instance = EzsignSuggestSignersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignSuggestSignersV1ResponseMPayload.to_json()

# convert the object into a dict
ezsign_suggest_signers_v1_response_m_payload_dict = ezsign_suggest_signers_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignSuggestSignersV1ResponseMPayload from a dict
ezsign_suggest_signers_v1_response_m_payload_form_dict = ezsign_suggest_signers_v1_response_m_payload.from_dict(ezsign_suggest_signers_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


