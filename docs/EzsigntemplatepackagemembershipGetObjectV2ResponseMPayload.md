# EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackagemembership** | [**EzsigntemplatepackagemembershipResponseCompound**](EzsigntemplatepackagemembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_get_object_v2_response_m_payload import EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload from a JSON string
ezsigntemplatepackagemembership_get_object_v2_response_m_payload_instance = EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplatepackagemembership_get_object_v2_response_m_payload_dict = ezsigntemplatepackagemembership_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload from a dict
ezsigntemplatepackagemembership_get_object_v2_response_m_payload_form_dict = ezsigntemplatepackagemembership_get_object_v2_response_m_payload.from_dict(ezsigntemplatepackagemembership_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


