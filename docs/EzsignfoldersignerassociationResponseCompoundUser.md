# EzsignfoldersignerassociationResponseCompoundUser

A Ezsignfoldersignerassociation->User Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_user_id** | **int** | The unique ID of the User | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_response_compound_user import EzsignfoldersignerassociationResponseCompoundUser

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationResponseCompoundUser from a JSON string
ezsignfoldersignerassociation_response_compound_user_instance = EzsignfoldersignerassociationResponseCompoundUser.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationResponseCompoundUser.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_response_compound_user_dict = ezsignfoldersignerassociation_response_compound_user_instance.to_dict()
# create an instance of EzsignfoldersignerassociationResponseCompoundUser from a dict
ezsignfoldersignerassociation_response_compound_user_from_dict = EzsignfoldersignerassociationResponseCompoundUser.from_dict(ezsignfoldersignerassociation_response_compound_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


