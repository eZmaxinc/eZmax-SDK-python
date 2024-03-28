# EzsignSuggestTemplatesV1ResponseMPayload

Payload for GET /1/module/ezsign/suggestTemplates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplate** | [**List[EzsigntemplateResponseCompound]**](EzsigntemplateResponseCompound.md) |  | 
**a_obj_ezsigntemplatepackage** | [**List[EzsigntemplatepackageResponseCompound]**](EzsigntemplatepackageResponseCompound.md) |  | 
**a_obj_ezsigntemplateglobal** | [**List[EzsigntemplateglobalResponseCompound]**](EzsigntemplateglobalResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsign_suggest_templates_v1_response_m_payload import EzsignSuggestTemplatesV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignSuggestTemplatesV1ResponseMPayload from a JSON string
ezsign_suggest_templates_v1_response_m_payload_instance = EzsignSuggestTemplatesV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignSuggestTemplatesV1ResponseMPayload.to_json())

# convert the object into a dict
ezsign_suggest_templates_v1_response_m_payload_dict = ezsign_suggest_templates_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignSuggestTemplatesV1ResponseMPayload from a dict
ezsign_suggest_templates_v1_response_m_payload_form_dict = ezsign_suggest_templates_v1_response_m_payload.from_dict(ezsign_suggest_templates_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


