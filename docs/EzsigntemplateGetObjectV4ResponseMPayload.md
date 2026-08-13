# EzsigntemplateGetObjectV4ResponseMPayload

Payload for GET /4/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompoundV4**](EzsigntemplateResponseCompoundV4.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_object_v4_response_m_payload import EzsigntemplateGetObjectV4ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetObjectV4ResponseMPayload from a JSON string
ezsigntemplate_get_object_v4_response_m_payload_instance = EzsigntemplateGetObjectV4ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateGetObjectV4ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplate_get_object_v4_response_m_payload_dict = ezsigntemplate_get_object_v4_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateGetObjectV4ResponseMPayload from a dict
ezsigntemplate_get_object_v4_response_m_payload_from_dict = EzsigntemplateGetObjectV4ResponseMPayload.from_dict(ezsigntemplate_get_object_v4_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


