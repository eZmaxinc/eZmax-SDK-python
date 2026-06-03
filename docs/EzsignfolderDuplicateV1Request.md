# EzsignfolderDuplicateV1Request



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**a_fki_ezsignfoldersignerassociation_id** | **List[int]** |  | 
**a_obj_ezsigndocument** | [**List[CustomEzsigndocumentDuplicateRequest]**](CustomEzsigndocumentDuplicateRequest.md) |  | 
**t_ezsignfolder_note** | **str** | Note about the Ezsignfolder | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_duplicate_v1_request import EzsignfolderDuplicateV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderDuplicateV1Request from a JSON string
ezsignfolder_duplicate_v1_request_instance = EzsignfolderDuplicateV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderDuplicateV1Request.to_json())

# convert the object into a dict
ezsignfolder_duplicate_v1_request_dict = ezsignfolder_duplicate_v1_request_instance.to_dict()
# create an instance of EzsignfolderDuplicateV1Request from a dict
ezsignfolder_duplicate_v1_request_from_dict = EzsignfolderDuplicateV1Request.from_dict(ezsignfolder_duplicate_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


