# EzsigndocumentEditEzsignformfieldgroupsV1Request

Request for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignformfieldgroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupRequestCompound]**](EzsignformfieldgroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_ezsignformfieldgroups_v1_request import EzsigndocumentEditEzsignformfieldgroupsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditEzsignformfieldgroupsV1Request from a JSON string
ezsigndocument_edit_ezsignformfieldgroups_v1_request_instance = EzsigndocumentEditEzsignformfieldgroupsV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditEzsignformfieldgroupsV1Request.to_json())

# convert the object into a dict
ezsigndocument_edit_ezsignformfieldgroups_v1_request_dict = ezsigndocument_edit_ezsignformfieldgroups_v1_request_instance.to_dict()
# create an instance of EzsigndocumentEditEzsignformfieldgroupsV1Request from a dict
ezsigndocument_edit_ezsignformfieldgroups_v1_request_form_dict = ezsigndocument_edit_ezsignformfieldgroups_v1_request.from_dict(ezsigndocument_edit_ezsignformfieldgroups_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


