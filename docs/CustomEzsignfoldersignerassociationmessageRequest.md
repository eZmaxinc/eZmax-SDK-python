# CustomEzsignfoldersignerassociationmessageRequest

A custom message Object in the context of an Ezsignfolder's send function

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**t_ezsignfoldersignerassociation_message** | **str** | A custom text message that will be added to the email sent. | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldersignerassociationmessage_request import CustomEzsignfoldersignerassociationmessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldersignerassociationmessageRequest from a JSON string
custom_ezsignfoldersignerassociationmessage_request_instance = CustomEzsignfoldersignerassociationmessageRequest.from_json(json)
# print the JSON string representation of the object
print CustomEzsignfoldersignerassociationmessageRequest.to_json()

# convert the object into a dict
custom_ezsignfoldersignerassociationmessage_request_dict = custom_ezsignfoldersignerassociationmessage_request_instance.to_dict()
# create an instance of CustomEzsignfoldersignerassociationmessageRequest from a dict
custom_ezsignfoldersignerassociationmessage_request_form_dict = custom_ezsignfoldersignerassociationmessage_request.from_dict(custom_ezsignfoldersignerassociationmessage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


