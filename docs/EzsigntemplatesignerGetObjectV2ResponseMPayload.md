# EzsigntemplatesignerGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesigner** | [**EzsigntemplatesignerResponseCompound**](EzsigntemplatesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_get_object_v2_response_m_payload import EzsigntemplatesignerGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatesigner_get_object_v2_response_m_payload_instance = EzsigntemplatesignerGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatesigner_get_object_v2_response_m_payload_dict = ezsigntemplatesigner_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignerGetObjectV2ResponseMPayload from a dict
ezsigntemplatesigner_get_object_v2_response_m_payload_from_dict = EzsigntemplatesignerGetObjectV2ResponseMPayload.from_dict(ezsigntemplatesigner_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


