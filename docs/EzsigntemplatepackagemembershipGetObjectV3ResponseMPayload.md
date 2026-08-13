# EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackagemembership** | [**EzsigntemplatepackagemembershipResponseCompoundV3**](EzsigntemplatepackagemembershipResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_get_object_v3_response_m_payload import EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload from a JSON string
ezsigntemplatepackagemembership_get_object_v3_response_m_payload_instance = EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_get_object_v3_response_m_payload_dict = ezsigntemplatepackagemembership_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload from a dict
ezsigntemplatepackagemembership_get_object_v3_response_m_payload_from_dict = EzsigntemplatepackagemembershipGetObjectV3ResponseMPayload.from_dict(ezsigntemplatepackagemembership_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


