# EzsignsignatureEditObjectV1Request

Request for PUT /1/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignature** | [**EzsignsignatureRequestCompound**](EzsignsignatureRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_edit_object_v1_request import EzsignsignatureEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureEditObjectV1Request from a JSON string
ezsignsignature_edit_object_v1_request_instance = EzsignsignatureEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignsignatureEditObjectV1Request.to_json()

# convert the object into a dict
ezsignsignature_edit_object_v1_request_dict = ezsignsignature_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignsignatureEditObjectV1Request from a dict
ezsignsignature_edit_object_v1_request_form_dict = ezsignsignature_edit_object_v1_request.from_dict(ezsignsignature_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


