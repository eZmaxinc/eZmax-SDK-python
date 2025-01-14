# EzsigntemplateGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompoundV3**](EzsigntemplateResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_object_v3_response_m_payload import EzsigntemplateGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetObjectV3ResponseMPayload from a JSON string
ezsigntemplate_get_object_v3_response_m_payload_instance = EzsigntemplateGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplate_get_object_v3_response_m_payload_dict = ezsigntemplate_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateGetObjectV3ResponseMPayload from a dict
ezsigntemplate_get_object_v3_response_m_payload_from_dict = EzsigntemplateGetObjectV3ResponseMPayload.from_dict(ezsigntemplate_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


