# EzsigntemplateglobalannotationGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplateglobalannotation/{pkiEzsigntemplateglobalannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateglobalannotation** | [**EzsigntemplateglobalannotationResponseCompound**](EzsigntemplateglobalannotationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobalannotation_get_object_v2_response_m_payload import EzsigntemplateglobalannotationGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalannotationGetObjectV2ResponseMPayload from a JSON string
ezsigntemplateglobalannotation_get_object_v2_response_m_payload_instance = EzsigntemplateglobalannotationGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalannotationGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplateglobalannotation_get_object_v2_response_m_payload_dict = ezsigntemplateglobalannotation_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateglobalannotationGetObjectV2ResponseMPayload from a dict
ezsigntemplateglobalannotation_get_object_v2_response_m_payload_from_dict = EzsigntemplateglobalannotationGetObjectV2ResponseMPayload.from_dict(ezsigntemplateglobalannotation_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


