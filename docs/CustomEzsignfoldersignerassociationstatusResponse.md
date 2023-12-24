# CustomEzsignfoldersignerassociationstatusResponse

A Ezsignfoldersignerassociationstatus Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**s_ezsignfoldersignerassociationstatus_lastname** | **str** | The last name of the Ezsignsigner | [optional] 
**s_ezsignfoldersignerassociationstatus_firstname** | **str** | The first name of the Ezsignsigner | [optional] 
**s_ezsignfoldersignerassociationstatus_description_x** | **str** | The description of the Ezsignsigner | [optional] 
**a_obj_ezsignsignaturestatus** | [**List[CustomEzsignsignaturestatusResponse]**](CustomEzsignsignaturestatusResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldersignerassociationstatus_response import CustomEzsignfoldersignerassociationstatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldersignerassociationstatusResponse from a JSON string
custom_ezsignfoldersignerassociationstatus_response_instance = CustomEzsignfoldersignerassociationstatusResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzsignfoldersignerassociationstatusResponse.to_json()

# convert the object into a dict
custom_ezsignfoldersignerassociationstatus_response_dict = custom_ezsignfoldersignerassociationstatus_response_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationstatusResponse from a dict
custom_ezsignfoldersignerassociationstatus_response_form_dict = custom_ezsignfoldersignerassociationstatus_response.from_dict(custom_ezsignfoldersignerassociationstatus_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


