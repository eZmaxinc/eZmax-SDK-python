# EzsignsignergroupEditEzsignsignergroupmembershipsV1Request

Request for PUT /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}/editEzsignsignergroupmemberships

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignergroupmembership** | [**List[EzsignsignergroupmembershipRequestCompound]**](EzsignsignergroupmembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request import EzsignsignergroupEditEzsignsignergroupmembershipsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupEditEzsignsignergroupmembershipsV1Request from a JSON string
ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request_instance = EzsignsignergroupEditEzsignsignergroupmembershipsV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupEditEzsignsignergroupmembershipsV1Request.to_json()

# convert the object into a dict
ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request_dict = ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request_instance.to_dict()
# create an instance of EzsignsignergroupEditEzsignsignergroupmembershipsV1Request from a dict
ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request_form_dict = ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request.from_dict(ezsignsignergroup_edit_ezsignsignergroupmemberships_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


