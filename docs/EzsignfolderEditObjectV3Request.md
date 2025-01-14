# EzsignfolderEditObjectV3Request

Request for PUT /3/object/ezsignfolder/{pkiEzsignfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfolder** | [**EzsignfolderRequestCompoundV3**](EzsignfolderRequestCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_edit_object_v3_request import EzsignfolderEditObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderEditObjectV3Request from a JSON string
ezsignfolder_edit_object_v3_request_instance = EzsignfolderEditObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderEditObjectV3Request.to_json())

# convert the object into a dict
ezsignfolder_edit_object_v3_request_dict = ezsignfolder_edit_object_v3_request_instance.to_dict()
# create an instance of EzsignfolderEditObjectV3Request from a dict
ezsignfolder_edit_object_v3_request_from_dict = EzsignfolderEditObjectV3Request.from_dict(ezsignfolder_edit_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


