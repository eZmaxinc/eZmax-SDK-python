# EzsignfolderEditObjectV1Request

Request for PUT /1/object/ezsignfolder/{pkiEzsignfolderID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfolder** | [**EzsignfolderRequestCompound**](EzsignfolderRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_edit_object_v1_request import EzsignfolderEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderEditObjectV1Request from a JSON string
ezsignfolder_edit_object_v1_request_instance = EzsignfolderEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderEditObjectV1Request.to_json()

# convert the object into a dict
ezsignfolder_edit_object_v1_request_dict = ezsignfolder_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignfolderEditObjectV1Request from a dict
ezsignfolder_edit_object_v1_request_form_dict = ezsignfolder_edit_object_v1_request.from_dict(ezsignfolder_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


