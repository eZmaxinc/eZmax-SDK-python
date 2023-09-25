# EzmaxinvoicingGetObjectV2ResponseMPayload

Payload for GET /2/object/ezmaxinvoicing/{pkiEzmaxinvoicingID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxinvoicing** | [**EzmaxinvoicingResponseCompound**](EzmaxinvoicingResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_get_object_v2_response_m_payload import EzmaxinvoicingGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingGetObjectV2ResponseMPayload from a JSON string
ezmaxinvoicing_get_object_v2_response_m_payload_instance = EzmaxinvoicingGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzmaxinvoicingGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezmaxinvoicing_get_object_v2_response_m_payload_dict = ezmaxinvoicing_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzmaxinvoicingGetObjectV2ResponseMPayload from a dict
ezmaxinvoicing_get_object_v2_response_m_payload_form_dict = ezmaxinvoicing_get_object_v2_response_m_payload.from_dict(ezmaxinvoicing_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


