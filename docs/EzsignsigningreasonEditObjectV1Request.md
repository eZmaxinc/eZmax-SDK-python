# EzsignsigningreasonEditObjectV1Request

Request for PUT /1/object/ezsignsigningreason/{pkiEzsignsigningreasonID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsigningreason** | [**EzsignsigningreasonRequestCompound**](EzsignsigningreasonRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_edit_object_v1_request import EzsignsigningreasonEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonEditObjectV1Request from a JSON string
ezsignsigningreason_edit_object_v1_request_instance = EzsignsigningreasonEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonEditObjectV1Request.to_json())

# convert the object into a dict
ezsignsigningreason_edit_object_v1_request_dict = ezsignsigningreason_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignsigningreasonEditObjectV1Request from a dict
ezsignsigningreason_edit_object_v1_request_form_dict = ezsignsigningreason_edit_object_v1_request.from_dict(ezsignsigningreason_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


