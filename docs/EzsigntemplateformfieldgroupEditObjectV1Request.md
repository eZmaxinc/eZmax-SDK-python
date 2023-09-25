# EzsigntemplateformfieldgroupEditObjectV1Request

Request for PUT /1/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateformfieldgroup** | [**EzsigntemplateformfieldgroupRequestCompound**](EzsigntemplateformfieldgroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_edit_object_v1_request import EzsigntemplateformfieldgroupEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupEditObjectV1Request from a JSON string
ezsigntemplateformfieldgroup_edit_object_v1_request_instance = EzsigntemplateformfieldgroupEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupEditObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroup_edit_object_v1_request_dict = ezsigntemplateformfieldgroup_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupEditObjectV1Request from a dict
ezsigntemplateformfieldgroup_edit_object_v1_request_form_dict = ezsigntemplateformfieldgroup_edit_object_v1_request.from_dict(ezsigntemplateformfieldgroup_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


