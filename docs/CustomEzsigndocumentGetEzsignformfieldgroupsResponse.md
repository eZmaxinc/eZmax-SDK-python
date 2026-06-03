# CustomEzsigndocumentGetEzsignformfieldgroupsResponse

An Ezsigndocument Object in the context of a getEzsignformfieldgroups path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupResponseCompound]**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezsigndocument_get_ezsignformfieldgroups_response import CustomEzsigndocumentGetEzsignformfieldgroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsigndocumentGetEzsignformfieldgroupsResponse from a JSON string
custom_ezsigndocument_get_ezsignformfieldgroups_response_instance = CustomEzsigndocumentGetEzsignformfieldgroupsResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsigndocumentGetEzsignformfieldgroupsResponse.to_json())

# convert the object into a dict
custom_ezsigndocument_get_ezsignformfieldgroups_response_dict = custom_ezsigndocument_get_ezsignformfieldgroups_response_instance.to_dict()
# create an instance of CustomEzsigndocumentGetEzsignformfieldgroupsResponse from a dict
custom_ezsigndocument_get_ezsignformfieldgroups_response_from_dict = CustomEzsigndocumentGetEzsignformfieldgroupsResponse.from_dict(custom_ezsigndocument_get_ezsignformfieldgroups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


