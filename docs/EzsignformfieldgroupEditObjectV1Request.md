# EzsignformfieldgroupEditObjectV1Request

Request for PUT /1/object/ezsignformfieldgroup/{pkiEzsignfoldersignerassociationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignformfieldgroup** | [**EzsignformfieldgroupRequestCompound**](EzsignformfieldgroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_edit_object_v1_request import EzsignformfieldgroupEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupEditObjectV1Request from a JSON string
ezsignformfieldgroup_edit_object_v1_request_instance = EzsignformfieldgroupEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupEditObjectV1Request.to_json())

# convert the object into a dict
ezsignformfieldgroup_edit_object_v1_request_dict = ezsignformfieldgroup_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignformfieldgroupEditObjectV1Request from a dict
ezsignformfieldgroup_edit_object_v1_request_from_dict = EzsignformfieldgroupEditObjectV1Request.from_dict(ezsignformfieldgroup_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


