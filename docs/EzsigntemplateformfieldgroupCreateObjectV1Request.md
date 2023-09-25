# EzsigntemplateformfieldgroupCreateObjectV1Request

Request for POST /1/object/ezsigntemplateformfieldgroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplateformfieldgroup** | [**List[EzsigntemplateformfieldgroupRequestCompound]**](EzsigntemplateformfieldgroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_create_object_v1_request import EzsigntemplateformfieldgroupCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupCreateObjectV1Request from a JSON string
ezsigntemplateformfieldgroup_create_object_v1_request_instance = EzsigntemplateformfieldgroupCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupCreateObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroup_create_object_v1_request_dict = ezsigntemplateformfieldgroup_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupCreateObjectV1Request from a dict
ezsigntemplateformfieldgroup_create_object_v1_request_form_dict = ezsigntemplateformfieldgroup_create_object_v1_request.from_dict(ezsigntemplateformfieldgroup_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


