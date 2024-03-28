# EzsignformfieldgroupCreateObjectV1Request

Request for POST /1/object/ezsignformfieldgroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupRequestCompound]**](EzsignformfieldgroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_create_object_v1_request import EzsignformfieldgroupCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupCreateObjectV1Request from a JSON string
ezsignformfieldgroup_create_object_v1_request_instance = EzsignformfieldgroupCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupCreateObjectV1Request.to_json())

# convert the object into a dict
ezsignformfieldgroup_create_object_v1_request_dict = ezsignformfieldgroup_create_object_v1_request_instance.to_dict()
# create an instance of EzsignformfieldgroupCreateObjectV1Request from a dict
ezsignformfieldgroup_create_object_v1_request_form_dict = ezsignformfieldgroup_create_object_v1_request.from_dict(ezsignformfieldgroup_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


