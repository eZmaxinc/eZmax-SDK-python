# EzsigntemplateGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompound**](EzsigntemplateResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_object_v2_response_m_payload import EzsigntemplateGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetObjectV2ResponseMPayload from a JSON string
ezsigntemplate_get_object_v2_response_m_payload_instance = EzsigntemplateGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplate_get_object_v2_response_m_payload_dict = ezsigntemplate_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateGetObjectV2ResponseMPayload from a dict
ezsigntemplate_get_object_v2_response_m_payload_form_dict = ezsigntemplate_get_object_v2_response_m_payload.from_dict(ezsigntemplate_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


