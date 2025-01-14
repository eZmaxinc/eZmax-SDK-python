# CustomEzsigndocumentEzsignsignaturesAutomaticResponse

An Ezsigndocument Object in the context of an EzsignsignaturesAutomatic path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**a_obj_ezsignsignature** | [**List[CustomEzsignsignatureEzsignsignaturesAutomaticResponse]**](CustomEzsignsignatureEzsignsignaturesAutomaticResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezsigndocument_ezsignsignatures_automatic_response import CustomEzsigndocumentEzsignsignaturesAutomaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsigndocumentEzsignsignaturesAutomaticResponse from a JSON string
custom_ezsigndocument_ezsignsignatures_automatic_response_instance = CustomEzsigndocumentEzsignsignaturesAutomaticResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsigndocumentEzsignsignaturesAutomaticResponse.to_json())

# convert the object into a dict
custom_ezsigndocument_ezsignsignatures_automatic_response_dict = custom_ezsigndocument_ezsignsignatures_automatic_response_instance.to_dict()
# create an instance of CustomEzsigndocumentEzsignsignaturesAutomaticResponse from a dict
custom_ezsigndocument_ezsignsignatures_automatic_response_from_dict = CustomEzsigndocumentEzsignsignaturesAutomaticResponse.from_dict(custom_ezsigndocument_ezsignsignatures_automatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


