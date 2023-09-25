# EzsignSuggestTemplatesV1Response

Response for GET /1/module/ezsign/suggestTemplates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignSuggestTemplatesV1ResponseMPayload**](EzsignSuggestTemplatesV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsign_suggest_templates_v1_response import EzsignSuggestTemplatesV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignSuggestTemplatesV1Response from a JSON string
ezsign_suggest_templates_v1_response_instance = EzsignSuggestTemplatesV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignSuggestTemplatesV1Response.to_json()

# convert the object into a dict
ezsign_suggest_templates_v1_response_dict = ezsign_suggest_templates_v1_response_instance.to_dict()
# create an instance of EzsignSuggestTemplatesV1Response from a dict
ezsign_suggest_templates_v1_response_form_dict = ezsign_suggest_templates_v1_response.from_dict(ezsign_suggest_templates_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


