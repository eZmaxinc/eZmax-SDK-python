# EzsignfolderCreateObjectV1Request

Request for POST /1/object/ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignfolder** | [**EzsignfolderRequest**](EzsignfolderRequest.md) |  | [optional] 
**obj_ezsignfolder_compound** | [**EzsignfolderRequestCompound**](EzsignfolderRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v1_request import EzsignfolderCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV1Request from a JSON string
ezsignfolder_create_object_v1_request_instance = EzsignfolderCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignfolder_create_object_v1_request_dict = ezsignfolder_create_object_v1_request_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV1Request from a dict
ezsignfolder_create_object_v1_request_form_dict = ezsignfolder_create_object_v1_request.from_dict(ezsignfolder_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


