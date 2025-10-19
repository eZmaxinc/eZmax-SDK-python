# CustomEzsignfoldersignerassociationstatusResponseV3

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
from eZmaxApi.models.custom_ezsignfoldersignerassociationstatus_response_v3 import CustomEzsignfoldersignerassociationstatusResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldersignerassociationstatusResponseV3 from a JSON string
custom_ezsignfoldersignerassociationstatus_response_v3_instance = CustomEzsignfoldersignerassociationstatusResponseV3.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfoldersignerassociationstatusResponseV3.to_json())

# convert the object into a dict
custom_ezsignfoldersignerassociationstatus_response_v3_dict = custom_ezsignfoldersignerassociationstatus_response_v3_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationstatusResponseV3 from a dict
custom_ezsignfoldersignerassociationstatus_response_v3_from_dict = CustomEzsignfoldersignerassociationstatusResponseV3.from_dict(custom_ezsignfoldersignerassociationstatus_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


