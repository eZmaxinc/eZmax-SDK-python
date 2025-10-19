# EzsignsignatureEditObjectV3Request

Request for PUT /3/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignature** | [**EzsignsignatureRequestCompoundV2**](EzsignsignatureRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_edit_object_v3_request import EzsignsignatureEditObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureEditObjectV3Request from a JSON string
ezsignsignature_edit_object_v3_request_instance = EzsignsignatureEditObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureEditObjectV3Request.to_json())

# convert the object into a dict
ezsignsignature_edit_object_v3_request_dict = ezsignsignature_edit_object_v3_request_instance.to_dict()
# create an instance of EzsignsignatureEditObjectV3Request from a dict
ezsignsignature_edit_object_v3_request_from_dict = EzsignsignatureEditObjectV3Request.from_dict(ezsignsignature_edit_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


