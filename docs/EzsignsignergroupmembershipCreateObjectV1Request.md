# EzsignsignergroupmembershipCreateObjectV1Request

Request for POST /1/object/ezsignsignergroupmembership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignergroupmembership** | [**List[EzsignsignergroupmembershipRequestCompound]**](EzsignsignergroupmembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_create_object_v1_request import EzsignsignergroupmembershipCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipCreateObjectV1Request from a JSON string
ezsignsignergroupmembership_create_object_v1_request_instance = EzsignsignergroupmembershipCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupmembershipCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignsignergroupmembership_create_object_v1_request_dict = ezsignsignergroupmembership_create_object_v1_request_instance.to_dict()
# create an instance of EzsignsignergroupmembershipCreateObjectV1Request from a dict
ezsignsignergroupmembership_create_object_v1_request_form_dict = ezsignsignergroupmembership_create_object_v1_request.from_dict(ezsignsignergroupmembership_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


