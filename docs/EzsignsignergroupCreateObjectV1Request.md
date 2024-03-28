# EzsignsignergroupCreateObjectV1Request

Request for POST /1/object/ezsignsignergroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignergroup** | [**List[EzsignsignergroupRequestCompound]**](EzsignsignergroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_create_object_v1_request import EzsignsignergroupCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupCreateObjectV1Request from a JSON string
ezsignsignergroup_create_object_v1_request_instance = EzsignsignergroupCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupCreateObjectV1Request.to_json())

# convert the object into a dict
ezsignsignergroup_create_object_v1_request_dict = ezsignsignergroup_create_object_v1_request_instance.to_dict()
# create an instance of EzsignsignergroupCreateObjectV1Request from a dict
ezsignsignergroup_create_object_v1_request_form_dict = ezsignsignergroup_create_object_v1_request.from_dict(ezsignsignergroup_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


