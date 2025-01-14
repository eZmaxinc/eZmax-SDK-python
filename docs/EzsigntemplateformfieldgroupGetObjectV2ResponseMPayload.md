# EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateformfieldgroup** | [**EzsigntemplateformfieldgroupResponseCompound**](EzsigntemplateformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_get_object_v2_response_m_payload import EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload from a JSON string
ezsigntemplateformfieldgroup_get_object_v2_response_m_payload_instance = EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplateformfieldgroup_get_object_v2_response_m_payload_dict = ezsigntemplateformfieldgroup_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload from a dict
ezsigntemplateformfieldgroup_get_object_v2_response_m_payload_from_dict = EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload.from_dict(ezsigntemplateformfieldgroup_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


