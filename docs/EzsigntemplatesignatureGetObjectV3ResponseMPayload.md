# EzsigntemplatesignatureGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesignature** | [**EzsigntemplatesignatureResponseCompoundV3**](EzsigntemplatesignatureResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_get_object_v3_response_m_payload import EzsigntemplatesignatureGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureGetObjectV3ResponseMPayload from a JSON string
ezsigntemplatesignature_get_object_v3_response_m_payload_instance = EzsigntemplatesignatureGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatesignature_get_object_v3_response_m_payload_dict = ezsigntemplatesignature_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatesignatureGetObjectV3ResponseMPayload from a dict
ezsigntemplatesignature_get_object_v3_response_m_payload_from_dict = EzsigntemplatesignatureGetObjectV3ResponseMPayload.from_dict(ezsigntemplatesignature_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


