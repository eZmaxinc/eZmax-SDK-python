# EzsigntemplateglobalGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplateglobal/{pkiEzsigntemplateglobalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateglobal** | [**EzsigntemplateglobalResponseCompound**](EzsigntemplateglobalResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobal_get_object_v2_response_m_payload import EzsigntemplateglobalGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalGetObjectV2ResponseMPayload from a JSON string
ezsigntemplateglobal_get_object_v2_response_m_payload_instance = EzsigntemplateglobalGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplateglobal_get_object_v2_response_m_payload_dict = ezsigntemplateglobal_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateglobalGetObjectV2ResponseMPayload from a dict
ezsigntemplateglobal_get_object_v2_response_m_payload_from_dict = EzsigntemplateglobalGetObjectV2ResponseMPayload.from_dict(ezsigntemplateglobal_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


