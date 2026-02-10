# EzsigntemplateannotationGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateannotation** | [**EzsigntemplateannotationResponseCompound**](EzsigntemplateannotationResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_get_object_v2_response_m_payload import EzsigntemplateannotationGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationGetObjectV2ResponseMPayload from a JSON string
ezsigntemplateannotation_get_object_v2_response_m_payload_instance = EzsigntemplateannotationGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplateannotation_get_object_v2_response_m_payload_dict = ezsigntemplateannotation_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateannotationGetObjectV2ResponseMPayload from a dict
ezsigntemplateannotation_get_object_v2_response_m_payload_from_dict = EzsigntemplateannotationGetObjectV2ResponseMPayload.from_dict(ezsigntemplateannotation_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


