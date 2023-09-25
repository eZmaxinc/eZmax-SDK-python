# EzsignfolderCreateObjectV2Request

Request for POST /2/object/ezsignfolder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfolder** | [**List[EzsignfolderRequestCompound]**](EzsignfolderRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_create_object_v2_request import EzsignfolderCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderCreateObjectV2Request from a JSON string
ezsignfolder_create_object_v2_request_instance = EzsignfolderCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderCreateObjectV2Request.to_json()

# convert the object into a dict
ezsignfolder_create_object_v2_request_dict = ezsignfolder_create_object_v2_request_instance.to_dict()
# create an instance of EzsignfolderCreateObjectV2Request from a dict
ezsignfolder_create_object_v2_request_form_dict = ezsignfolder_create_object_v2_request.from_dict(ezsignfolder_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


