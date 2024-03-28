# EzsignsignergroupmembershipDeleteObjectV1Response

Response for DELETE /1/object/ezsignsignergroupmembership/{pkiEzsignsignergroupmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_delete_object_v1_response import EzsignsignergroupmembershipDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipDeleteObjectV1Response from a JSON string
ezsignsignergroupmembership_delete_object_v1_response_instance = EzsignsignergroupmembershipDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupmembershipDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsignsignergroupmembership_delete_object_v1_response_dict = ezsignsignergroupmembership_delete_object_v1_response_instance.to_dict()
# create an instance of EzsignsignergroupmembershipDeleteObjectV1Response from a dict
ezsignsignergroupmembership_delete_object_v1_response_form_dict = ezsignsignergroupmembership_delete_object_v1_response.from_dict(ezsignsignergroupmembership_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


