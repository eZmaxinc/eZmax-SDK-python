# EzsignsignergroupmembershipGetObjectV2Response

Response for GET /2/object/ezsignsignergroupmembership/{pkiEzsignsignergroupmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignsignergroupmembershipGetObjectV2ResponseMPayload**](EzsignsignergroupmembershipGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_get_object_v2_response import EzsignsignergroupmembershipGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipGetObjectV2Response from a JSON string
ezsignsignergroupmembership_get_object_v2_response_instance = EzsignsignergroupmembershipGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupmembershipGetObjectV2Response.to_json())

# convert the object into a dict
ezsignsignergroupmembership_get_object_v2_response_dict = ezsignsignergroupmembership_get_object_v2_response_instance.to_dict()
# create an instance of EzsignsignergroupmembershipGetObjectV2Response from a dict
ezsignsignergroupmembership_get_object_v2_response_from_dict = EzsignsignergroupmembershipGetObjectV2Response.from_dict(ezsignsignergroupmembership_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


