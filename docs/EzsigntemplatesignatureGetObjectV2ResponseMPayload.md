# EzsigntemplatesignatureGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesignature** | [**EzsigntemplatesignatureResponseCompound**](EzsigntemplatesignatureResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_get_object_v2_response_m_payload import EzsigntemplatesignatureGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatesignature_get_object_v2_response_m_payload_instance = EzsigntemplatesignatureGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignatureGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplatesignature_get_object_v2_response_m_payload_dict = ezsigntemplatesignature_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignatureGetObjectV2ResponseMPayload from a dict
ezsigntemplatesignature_get_object_v2_response_m_payload_form_dict = ezsigntemplatesignature_get_object_v2_response_m_payload.from_dict(ezsigntemplatesignature_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


