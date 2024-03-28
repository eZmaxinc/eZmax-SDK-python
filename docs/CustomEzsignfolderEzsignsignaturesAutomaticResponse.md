# CustomEzsignfolderEzsignsignaturesAutomaticResponse

An Ezsignfolder Object in the context of an EzsignsignaturesAutomatic path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**a_obj_ezsigndocument** | [**List[CustomEzsigndocumentEzsignsignaturesAutomaticResponse]**](CustomEzsigndocumentEzsignsignaturesAutomaticResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezsignfolder_ezsignsignatures_automatic_response import CustomEzsignfolderEzsignsignaturesAutomaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfolderEzsignsignaturesAutomaticResponse from a JSON string
custom_ezsignfolder_ezsignsignatures_automatic_response_instance = CustomEzsignfolderEzsignsignaturesAutomaticResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfolderEzsignsignaturesAutomaticResponse.to_json())

# convert the object into a dict
custom_ezsignfolder_ezsignsignatures_automatic_response_dict = custom_ezsignfolder_ezsignsignatures_automatic_response_instance.to_dict()
# create an instance of CustomEzsignfolderEzsignsignaturesAutomaticResponse from a dict
custom_ezsignfolder_ezsignsignatures_automatic_response_form_dict = custom_ezsignfolder_ezsignsignatures_automatic_response.from_dict(custom_ezsignfolder_ezsignsignatures_automatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


